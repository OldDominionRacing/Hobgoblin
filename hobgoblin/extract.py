"""``hobgoblin.extract`` — deterministic entity & context extraction via spaCy.

Finds candidate entities by their POS / dependency shape, then gathers the
surrounding context (governing verb, count, dates, modifiers) with exact
character offsets so the source document can be reconstructed and highlighted.

See ``DESIGN.md`` for the full specification.
"""

from __future__ import annotations

import re
from typing import Iterable, Optional

from ._model import DEFAULT_MODEL, load
from .anchors import apply_anchors
from .associate import relatedness, paragraphs as _paragraphs
from .items import detect as detect_items
from .military import annotate as annotate_units

# Lightweight word -> number map for count values. Unknown words keep value=None.
_NUM_WORDS = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
    "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
    "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100,
    "thousand": 1000, "million": 1000000,
    "couple": 2, "pair": 2, "dozen": 12,
}

# Quantity words that imply a count without a precise numeric value.
_QUANTITY_WORDS = {
    "several", "many", "few", "numerous", "various", "multiple",
    "some", "lot", "lots", "plenty", "handful",
}

# Multiplier shorthand: "3x cars", "3X", "3× cars", or suffix "cars x3".
_MULT_RE = re.compile(r"^(?:(\d[\d,]*)\s*[xX×]|[xX×](\d[\d,]*))$")
# Symbolic approximator on a number: "~3", "≈3", ">5", "<=10".
_APPROX_NUM_RE = re.compile(r"^(>=|<=|[~≈<>])\s*(\d[\d,]*(?:\.\d+)?)$")
# Inline numeric range in a single token: "3-5", "3–5".
_RANGE_RE = re.compile(r"^(\d[\d,]*(?:\.\d+)?)\s*[-–—]\s*(\d[\d,]*(?:\.\d+)?)$")
# Words that qualify a count as approximate ("about 3", "over 100", "at least 10").
_APPROX_WORDS = {
    "about", "approximately", "around", "roughly", "nearly", "almost", "circa",
    "approx", "over", "under", "above", "below", "least", "most", "more",
    "less", "fewer", "upwards",
}


def _multiplier_value(text: str) -> Optional[float]:
    """Parse a multiplier token ('3x', '3X', '3×', 'x3') to its number."""
    m = _MULT_RE.match(text.strip())
    if not m:
        return None
    return _to_value(m.group(1) or m.group(2))


def _detect_range(head, num):
    """Return ``[lo, hi]`` if ``num`` is part of a numeric range, else None."""
    # single-token range, e.g. "3-5"
    m = _RANGE_RE.match(num.text)
    if m:
        lo, hi = _to_value(m.group(1)), _to_value(m.group(2))
        if lo is not None and hi is not None:
            return [min(lo, hi), max(lo, hi)]
    # two numeric nummods on the head, e.g. "3 - 5 cars"
    vals = [
        _to_value(c.text) for c in head.children
        if c.dep_ == "nummod" and not _is_temporal(c) and _to_value(c.text) is not None
    ]
    if len(vals) >= 2:
        return [min(vals), max(vals)]
    # secondary number hanging off num as quantmod/conj, e.g. "3 to 5", "between 3 and 5"
    for c in num.children:
        if c.dep_ in ("quantmod", "conj", "nummod") and _to_value(c.text) is not None:
            a, b = _to_value(num.text), _to_value(c.text)
            return [min(a, b), max(a, b)]
    return None


def _detect_approx(num):
    """Return the qualifier text if ``num`` is approximate, else None."""
    quals = [c for c in num.children if c.lemma_.lower() in _APPROX_WORDS]
    if not quals:
        return None
    left = min(quals, key=lambda t: t.idx)
    text = num.doc.text[left.left_edge.idx:num.idx].strip()
    return text or left.text


def _should_normalize(text: str, mode) -> bool:
    """Whether to lowercase the text for spaCy. ``mode`` is True/False/"auto"."""
    if mode is True:
        return True
    if mode is False:
        return False
    letters = [c for c in text if c.isalpha()]
    if len(letters) < 8:
        return False
    return sum(c.isupper() for c in letters) / len(letters) >= 0.85


def _resurface(node, src: str) -> None:
    """Rewrite every surface string from ``src`` by its char span (recursively).

    Lets us parse a lowercased copy for better tagging while keeping the output's
    text faithful to the original casing — spans line up because lowercasing is
    length-preserving.
    """
    if isinstance(node, list):
        for x in node:
            _resurface(x, src)
    elif isinstance(node, dict):
        sp = node.get("span")
        if isinstance(sp, list) and len(sp) == 2:
            if "text" in node:
                node["text"] = src[sp[0]:sp[1]]
            if "entity" in node:
                node["entity"] = src[sp[0]:sp[1]]
        ssp = node.get("sentence_span")
        if isinstance(ssp, list) and len(ssp) == 2 and "sentence" in node:
            node["sentence"] = src[ssp[0]:ssp[1]]
        hs = node.get("_head_span")
        if isinstance(hs, list) and len(hs) == 2:
            node["head"] = src[hs[0]:hs[1]]
        for v in node.values():
            _resurface(v, src)


def _span(token) -> list[int]:
    """Character offsets ``[start, end]`` for a single token."""
    return [token.idx, token.idx + len(token.text)]


def _is_temporal(token) -> bool:
    """True if the token is part of a DATE/TIME entity (a year is not a count)."""
    return token.ent_type_ in ("DATE", "TIME")


def _to_value(text: str) -> Optional[float]:
    """Best-effort numeric value for a count token."""
    cleaned = text.replace(",", "").strip()
    try:
        f = float(cleaned)
        return int(f) if f.is_integer() else f
    except ValueError:
        return _NUM_WORDS.get(cleaned.lower())


def _governing_verb(head) -> Optional[dict]:
    """The verb that grammatically governs ``head`` (nearest VERB, else AUX)."""
    fallback = None
    for anc in head.ancestors:
        if anc.pos_ == "VERB":
            return {"text": anc.text, "lemma": anc.lemma_, "span": _span(anc)}
        if anc.pos_ == "AUX" and fallback is None:
            fallback = {"text": anc.text, "lemma": anc.lemma_, "span": _span(anc)}
    return fallback


def _subject_of(verb_span: Optional[dict], doc) -> Optional[dict]:
    """nsubj of the verb token at ``verb_span`` (if any)."""
    if not verb_span:
        return None
    start = verb_span["span"][0]
    for tok in doc:
        if tok.idx == start:
            for child in tok.children:
                if child.dep_ in ("nsubj", "nsubjpass"):
                    return {"text": child.text, "span": _span(child)}
    return None


def _find_count(head) -> Optional[dict]:
    """Detect a count attached to ``head``.

    Handles three shapes, in priority order:
      1. measure + helper:  "three **boxes of** apples"  (head is pobj of "of")
      2. bare numeric:      "three apples"               (nummod on head)
      3. quantity word:     "several apples"             (value left as None)
    """
    # 1. measure-of construction: "three boxes of apples" (head is pobj of "of").
    # Only a count if the measure actually carries a numeral — a bare "of" phrase
    # ("division of the Army") is not a count.
    if head.dep_ == "pobj" and head.head.lemma_ == "of" and head.head.pos_ == "ADP":
        helper = head.head
        measure = helper.head
        for child in measure.children:
            if child.dep_ == "nummod" and not _is_temporal(child):
                return {
                    "text": child.text,
                    "value": _to_value(child.text),
                    "span": _span(child),
                    "measure": {"text": measure.text, "span": _span(measure)},
                    "helper": {"text": helper.text, "span": _span(helper)},
                }
        # no numeral -> fall through to other count shapes / None

    # 2. multiplier shorthand ("3x cars", "3X", "3× cars", "cars x3"). Checked
    # before bare nummod because spaCy may tag "3X" as a compound, not a number.
    for child in head.children:
        if _is_temporal(child):
            continue
        mv = _multiplier_value(child.text)
        if mv is not None:
            return {
                "text": child.text,
                "value": mv,
                "span": _span(child),
                "form": "multiplier",
            }

    # 2b. symbolic approximator number ("~3 cars", ">5 cars") — not a nummod.
    for child in head.children:
        if _is_temporal(child):
            continue
        m = _APPROX_NUM_RE.match(child.text)
        if m:
            return {
                "text": child.text,
                "value": _to_value(m.group(2)),
                "span": _span(child),
                "approx": True,
                "qualifier": m.group(1),
            }

    # 3. bare numeric modifier on the head (skip years/dates, e.g. "1903 Prize").
    for child in head.children:
        if child.dep_ == "nummod" and not _is_temporal(child):
            count = {
                "text": child.text,
                "value": _to_value(child.text),
                "span": _span(child),
            }
            rng = _detect_range(head, child)
            if rng:
                count["range"] = rng
            qualifier = _detect_approx(child)
            if qualifier:
                count["approx"] = True
                count["qualifier"] = qualifier
            return count

    # 4. quantity word.
    for child in head.children:
        if child.lemma_.lower() in _QUANTITY_WORDS:
            return {
                "text": child.text,
                "value": _to_value(child.text),
                "span": _span(child),
            }

    return None


def _modifiers(head) -> list[dict]:
    """Adjectives / compounds decorating ``head``, in surface order."""
    mods = [
        {"text": c.text, "span": _span(c)}
        for c in head.children
        if c.dep_ in ("amod", "compound") and c.pos_ in ("ADJ", "NOUN", "PROPN")
    ]
    return sorted(mods, key=lambda m: m["span"][0])


def _pattern_label(chunk) -> str:
    """POS-shape label for a chunk, e.g. ``ADJ+NOUN`` (determiners dropped)."""
    poss = [t.pos_ for t in chunk if t.pos_ != "DET"]
    return "+".join(poss) if poss else chunk.root.pos_


def extract(
    text: str,
    anchors=None,
    *,
    anchor_mode: str = "flag",
    fuzzy: bool = True,
    items: bool = True,
    min_weight: float = 0.1,
    military: bool = True,
    unit_echelons: Optional[Iterable[str]] = None,
    normalize_case="auto",
    drop_stops: bool = True,
    model: str = DEFAULT_MODEL,
) -> list[dict]:
    """Extract entities and their context from ``text``.

    Returns a list of entity dicts (see ``DESIGN.md`` for the schema). If
    ``anchors`` is given, each entity is tagged with ``anchors_matched`` and,
    when ``anchor_mode="filter"``, only matched entities are returned.

    When ``items=True`` (default), items of interest (phone, email, URL, money,
    address) are detected and attached to each entity as ``associations`` with a
    deterministic relatedness ``weight`` (>= ``min_weight``). Use
    :func:`hobgoblin.item_index` to get the inverted, item-centric view.

    ``normalize_case`` ("auto" by default) lowercases mostly-uppercase text before
    spaCy — all-caps badly degrades tagging/chunking — while surface strings in the
    output are sliced from the original, so casing is preserved. Pass True/False to
    force it on/off.
    """
    nlp = load(model)
    normalized = _should_normalize(text, normalize_case)
    src = text
    doc = nlp(text.lower() if normalized else text)

    # Per-sentence date cache (spaCy NER DATE / TIME).
    sent_dates: dict[int, list[dict]] = {}
    for sent in doc.sents:
        sent_dates[sent.start] = [
            {"text": e.text, "label": e.label_, "span": [e.start_char, e.end_char]}
            for e in sent.ents
            if e.label_ in ("DATE", "TIME")
        ]

    entities: list[dict] = []
    for chunk in doc.noun_chunks:
        head = chunk.root
        # Drop bare stopword/pronoun entities ("It", "this", "the") — they're never
        # what anyone anchors on. Multi-word and content entities are kept (untyped
        # ones are useful signal for a later LLM pass).
        if drop_stops and len(chunk) == 1 and (head.is_stop or head.pos_ in ("PRON", "DET")):
            continue
        sent = chunk.sent
        verb = _governing_verb(head)

        context = {
            "sentence": sent.text,
            "sentence_span": [sent.start_char, sent.end_char],
            "verb": verb,
            "count": _find_count(head),
            "dates": sent_dates.get(sent.start, []),
            "subject": _subject_of(verb, doc),
        }

        entities.append(
            {
                "entity": chunk.text,
                "head": head.text,
                "head_pos": head.pos_,
                "head_ent": head.ent_type_,
                "span": [chunk.start_char, chunk.end_char],
                "pattern": _pattern_label(chunk),
                "tokens": [
                    {
                        "text": t.text,
                        "pos": t.pos_,
                        "dep": t.dep_,
                        "lemma": t.lemma_,
                        "span": _span(t),
                    }
                    for t in chunk
                ],
                "modifiers": _modifiers(head),
                "context": context,
                "associations": [],
                "mil_unit": None,
                "anchors_matched": [],
                "part_of": None,
                # internal: token coordinates for scoring / resurfacing (stripped below)
                "_tok_start": chunk.start,
                "_tok_end": chunk.end,
                "_root_i": head.i,
                "_head_span": [head.idx, head.idx + len(head.text)],
            }
        )

    _link_overlaps(entities)

    if items:
        _attach_associations(doc, entities, min_weight, _paragraphs(src))

    if military:
        annotate_units(doc, entities, echelons=unit_echelons, text=src)

    if normalized:
        _resurface(entities, src)

    for ent in entities:
        del ent["_tok_start"], ent["_tok_end"], ent["_root_i"], ent["_head_span"]

    if anchors is not None:
        entities = apply_anchors(entities, anchors, mode=anchor_mode, fuzzy=fuzzy)

    return entities


def _attach_associations(doc, entities: list[dict], min_weight: float, paras=None) -> None:
    """Score every (entity, item) pair and attach those above ``min_weight``."""
    found = detect_items(doc)
    if not found:
        return

    # Drop "entities" whose head token sits inside an item (the entity *is* the
    # item, e.g. a noun-chunk over an email address or street name).
    def _head_in_item(e):
        h = doc[e["_root_i"]].idx
        return any(i["span"][0] <= h < i["span"][1] for i in found)

    entities[:] = [e for e in entities if not _head_in_item(e)]

    entity_spans = [e["span"] for e in entities]
    for ent in entities:
        e_s, e_e = ent["span"]
        assoc = []
        for item in found:
            i_s, i_e = item["span"]
            if i_s < e_e and e_s < i_e:
                continue  # entity overlaps the item itself — not an association
            weight, signals = relatedness(doc, ent, item, entity_spans, paras)
            if weight >= min_weight:
                rec = {
                    "type": item["type"],
                    "text": item["text"],
                    "span": item["span"],
                    "weight": round(weight, 3),
                    "signals": signals,
                }
                if "components" in item:
                    rec["components"] = item["components"]
                assoc.append(rec)
        assoc.sort(key=lambda a: -a["weight"])
        ent["associations"] = assoc


def _link_overlaps(entities: list[dict]) -> None:
    """Set ``part_of`` to the span of the smallest entity strictly containing each."""
    for ent in entities:
        s, e = ent["span"]
        smallest = None
        for other in entities:
            if other is ent:
                continue
            os, oe = other["span"]
            if os <= s and e <= oe and (os, oe) != (s, e):
                size = oe - os
                if smallest is None or size < smallest[0]:
                    smallest = (size, [os, oe])
        ent["part_of"] = smallest[1] if smallest else None
