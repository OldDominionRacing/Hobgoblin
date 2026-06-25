# Hobgoblin

> Cheap-first, batteries-included primitives for the work agents *usually* hand to
> deterministic tools — with the option to wake the wizard (an LLM) only when the
> goblin can't be trusted.

## The idea

LLM-driven systems constantly face a fork for every subtask:

- **Deterministic tool** (pytesseract, regex, a parser, spaCy) — cheap, fast,
  predictable, zero tokens, but brittle and "dumb." Good enough *most* of the time.
- **The model itself** ("big brain") — flexible, handles ambiguity, but expensive,
  slower, non-deterministic, and overkill for what a small function nails.

Today that fork is usually resolved at *build time* by a human wiring in the cheap
tool — so the system never notices the cases where the cheap path was the wrong call.

**Hobgoblin** is a library of "goblin-first" wrappers: cheap deterministic primitives
that do the grunt work by default, with a clean seam to *escalate* to an LLM only when
confidence is low. A hobgoblin is the household spirit that does the chores — but a
mischievous one that sometimes botches them, so you keep a wizard on call.

```
hobgoblin.extract(...)   # entity + context extraction  (this doc)
hobgoblin.ocr(...)       # future
hobgoblin.classify(...)  # future
```

The LLM-escalation layer is **deferred**. v1 of `extract()` is pure spaCy — no tokens,
no network.

---

## `hobgoblin.extract()` — entity & context extraction

A deterministic, spaCy-POS-driven extractor. It finds candidate entities by their
part-of-speech / dependency shape, then gathers the surrounding context (verb, count,
dates, modifiers) with exact character offsets so the source document can be
reconstructed and highlighted.

### Part 1 — find entities by POS shape, grab their context

Candidate entity patterns, anchored on a `NOUN`/`PROPN` head so we don't invent phrases:

| Pattern                         | Example               |
|---------------------------------|-----------------------|
| `ADJ + NOUN`                    | "red car"             |
| `ADJ+ ADJ + NOUN` (stacked)     | "big red car"         |
| `NOUN + NOUN` (compound)        | "coffee mug"          |
| `PROPN (+ PROPN)`               | "New York"            |
| `DET? (ADJ\|NOUN)* NOUN` (chunk)| "the old wooden table"|
| bare `NOUN` / `PROPN`           | "John", "rain"        |

> **Implementation note:** under the hood we lean on spaCy's **dependency parse**
> (`amod`, `compound`, `nsubj`, `dobj`, `pobj`) rather than raw POS-tag regex — it's
> far more robust at "which adjective modifies which noun" — but we expose it to the
> user *as if* it were the POS combos above.

For each entity, collect its sentence's **elements**, each with `[start_char, end_char]`:

- **verb** — the **governing verb** for *this* entity, resolved via the dependency
  parse (not necessarily the sentence's root verb).
- **count + helper** — broad matching, in priority order:
  1. **measure/container**: "three **boxes of** apples" (only when a numeral is
     present — a bare `of`-phrase like "division of the Army" is *not* a count).
  2. **multiplier shorthand**: "**3x** cars", "**3X** cars", "**3×** cars" → value 3,
     `form: "multiplier"`.
  3. **bare numeric**: "three apples", "12 boxes".
  4. **quantity words**: "a **dozen**", "**several**", "a **lot of**".
  Enrichment on the numeric forms:
  - **range** → `range: [lo, hi]` for "3-5 cars", "3 to 5 cars", "between 3 and 5".
  - **approximate** → `approx: true, qualifier: "..."` for "about 3", "~3", ">5",
    "more than 5", "over 100", "at least 10".
  - A numeral that is part of a `DATE`/`TIME` span is a **year, not a count**
    ("the 1903 Nobel Prize" → no count).
  - *Known gaps:* "million/billion" scaling ("3.5 million"), distributive counts
    ("two cars each"), and the suffix multiplier ("cars x3", which spaCy splits
    inconsistently) are not yet handled.
- **dates** — from spaCy's built-in NER `DATE` / `TIME` labels.
- **modifiers** — the adjectives/compounds decorating the head.
- **annotations** — per-token `lemma`, `pos`, `dep`.

### Part 2 — anchors

A second function lets the user feed in **anchor words** — the entities they care about.

- **Match rule:** **lemma, case-insensitive** (`apple` matches `apples`, `Apple`).
- **Multiple anchors:** OR logic; `anchors_matched` reports *which* anchors hit.
- **Mode:** `anchor_mode=` — `"flag"` (default; return all entities, tag matches) or
  `"filter"` (return only entities that matched an anchor).

---

## Output schema

`extract()` returns an **array of dicts**, one per entity. Every element carries char
spans, so the original document can be reconstructed/highlighted exactly.

### Worked example

Input: `"Last Tuesday, John bought three boxes of red apples."`

```python
[
  { "entity": "red apples", "head": "apples", "span": [44, 54],
    "pattern": "ADJ+NOUN",
    "tokens": [
      {"text": "red",    "pos": "ADJ",  "dep": "amod", "span": [44, 47]},
      {"text": "apples", "pos": "NOUN", "dep": "pobj", "span": [48, 54]}
    ],
    "modifiers": [{"text": "red", "span": [44, 47]}],
    "context": {
      "sentence": "Last Tuesday, John bought three boxes of red apples.",
      "sentence_span": [0, 52],
      "verb":    {"text": "bought", "lemma": "buy", "span": [19, 25]},
      "count":   {"text": "three", "value": 3, "span": [26, 31],
                  "measure": {"text": "boxes", "span": [32, 37]},
                  "helper":  {"text": "of", "span": [38, 40]}},
      "dates":   [{"text": "Last Tuesday", "label": "DATE", "span": [0, 12]}],
      "subject": {"text": "John", "span": [14, 18]}
    },
    "anchors_matched": ["apple"],
    "part_of": null
  }
  # ... plus entities for "John", "three boxes", etc.
]
```

### Field reference

| Field              | Meaning                                                        |
|--------------------|----------------------------------------------------------------|
| `entity`           | the matched surface text                                       |
| `head`             | head noun/propn of the phrase                                  |
| `span`             | `[start_char, end_char]` of the entity in the document         |
| `pattern`          | which POS rule matched (e.g. `ADJ+NOUN`)                       |
| `tokens[]`         | per-token `text` / `pos` / `dep` / `span`                      |
| `modifiers[]`      | adjectives/compounds decorating the head                       |
| `context.verb`     | governing verb (`text`, `lemma`, `span`)                       |
| `context.count`    | `text` / `value` / `span` + optional `measure` + `helper`      |
| `context.dates[]`  | `text` / `label` / `span` from NER                             |
| `context.subject`  | nsubj of the governing verb, if any                            |
| `anchors_matched[]`| which user anchors hit this entity (lemma match)              |
| `part_of`          | char-span link to a broader overlapping entity, or `null`     |

---

## Defaults (v1)

- **spaCy model:** `en_core_web_sm` — fast, CPU-only, no vectors. This is the whole
  "cheap goblin" ethos; bigger models / the LLM are reserved for escalation later.
- **Count breadth:** broad (measure words, bare numerics, quantity words).
- **Dates:** spaCy NER `DATE`/`TIME` only — no hand-rolled date parser in v1.
- **Overlapping entities:** keep both the inner ("red apples") and the broader chunk
  ("three boxes of red apples"); link them via `part_of` so nothing is lost.
- **Anchors:** OR logic, lemma + case-insensitive, default `anchor_mode="flag"`.

---

## Items of interest & relatedness

Beyond entities, `extract()` detects **items of interest** — phone, email, URL,
money, street address — and scores how strongly each relates to every entity, fully
deterministically.

### Detection (deterministic)

Types: `email`, `url`, `uuid`, `mac`, `ipv6`, `ipv4`, `coordinate`, `date`,
`credit_card`, `ssn`, `phone`, `address`, `money`, `percent`, `time`, `handle`,
`hashtag`, `file_path`, `zip`.

- **regex + spaCy token alignment** for most types, matched in **priority order**
  (precise patterns first) with a claimed-range pass so they don't overlap.
- **validators** keep false positives down: **Luhn checksum** for `credit_card`,
  **octet range** for `ipv4`.
- **address** — regex finds the span, then `usaddress` (a CRF tagger) validates and
  parses `components`. If `usaddress` is absent, regex-only with no `components`.
- **spaCy NER pass** adds `date` / `time` / `percent` that the regex didn't claim,
  guarded so bare digit-runs NER sometimes mislabels as dates are rejected.
- An entity whose **head token** sits inside an item is dropped — it *is* the item,
  not a separate entity (e.g. a noun-chunk over an email or a street name).

### Relatedness weight (0–1)
We already pay for a dependency parse, so we blend linear and syntactic distance
instead of using raw token distance alone:

```
proximity_lin = exp(-token_distance / 5)      # linear gap
proximity_dep = exp(-dep_distance   / 2)      # parse-tree hops (same sentence)

same sentence:  weight = 0.4*proximity_lin + 0.6*proximity_dep
cross sentence: weight = 0.3*proximity_lin
intervening entity (linearly between, closer):  weight *= 0.5
```

Weights `>= min_weight` (default `0.1`) attach to each entity as `associations`,
each carrying its raw `signals` (`token_distance`, `dep_distance`, `same_sentence`)
so the score is never a black box. The constants live in `associate.py` and are
tunable; they could later be calibrated by logistic regression on labeled data
without leaving determinism at inference.

### Two views
- **Per-entity** (default return): each entity's `associations`, weight-ranked.
- **Item-centric**: `hobgoblin.item_index(entities)` inverts it — each item with a
  weight-ranked `entities` list and a `best_entity`.

```python
ents  = extract(text)            # entities, each with .associations
items = item_index(ents)         # [{type, text, span, entities[], best_entity}, ...]
```

---

## Military unit designations

A deterministic recognizer (`military.py`, exposed as `hobgoblin.detect_units`) for
unit designations, which mix numbering systems:

| Form | Example | `designation` / `form` |
|---|---|---|
| cardinal | `3 Corps` | `3` / cardinal |
| Roman | `I Corps`, `XVIII Airborne Corps` | `1`, `18` / roman |
| ordinal | `1st Infantry Division`, `3rd Battalion` | `1`, `3` / ordinal |
| letter | `C Company` | `"C"` / letter |

**The trick:** anchor on a known **echelon** keyword (Corps/Division/Battalion/…).
A number/letter/Roman token is only a designator when an echelon immediately follows
(optionally through a branch like *Airborne*). That keeps `I Corps` (unit) distinct
from `I went home` (pronoun), and `World War II` is never mistaken for a unit.

- Roman numerals are validated by round-trip (`XVIII` ✓, `IIII`/`VV` ✗).
- **Ambiguity** resolved by echelon: a lone Roman letter before a *company-level*
  echelon is a letter designation (`C Company` → letter `C`, not Roman 100).
- **Known limitation:** non-Roman letter companies (`A Company`, `B Company`) are not
  matched, because a capitalized `A`/`B` before an echelon is ambiguous with the
  article "A". Only Roman-letter companies fall out naturally.

`extract()` annotates any entity whose head sits inside a detected unit with a
`mil_unit` field (`echelon`, `branch`, `designation`, `designation_text`,
`designation_form`); disable with `military=False`.

**Caveat — the echelon vocabulary is the whole engine.** Recognition is driven by a
fixed, English/US-NATO-army-centric list (`DEFAULT_ECHELONS`). It will miss naval
rates, foreign-language echelons, and any org chart that doesn't use these words.
This is a documented assumption, not a bug: override it with
`detect_units(text, echelons=[...])` or `extract(text, unit_echelons=[...])`.

---

## TypeScript parity (planned)

spaCy is Python-only, but the design ports to TS. The output schema above is plain
JSON and is meant to be **language-agnostic** — the same shape across both ports.

- **`compromise`** — match syntax *is* POS patterns (`doc.match('#Adjective+ #Noun')`);
  `compromise-dates` / `compromise-numbers` plugins cover dates and counts.
- **`wink-nlp`** (+ `wink-eng-lite-web-model`) — more spaCy-like: POS, lemmas, NER.

**Caveat:** neither JS lib has a true dependency parser, so the **governing verb** would
be approximated heuristically (nearest preceding verb / sentence root) rather than
resolved through a dep tree. Everything else ports cleanly.

---

## Deferred / future

- **Wizard escalation:** LLM fallback when POS/dep patterns are ambiguous or low
  confidence — the "option 4" fallback seam that makes the goblin trustworthy.
- **More primitives:** `hobgoblin.ocr()`, `hobgoblin.classify()`, etc.
- **Confidence scoring** on each entity to drive escalation decisions.
- **Non-English models.**

---

## Status

v1 of `extract()` implemented and tested (Python, spaCy `en_core_web_sm`). Repo:
public `OldDominionRacing/Hobgoblin`.
