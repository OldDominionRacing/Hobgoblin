# Hobgoblin

> Cheap-first, batteries-included primitives for the work agents *usually* hand to
> deterministic tools — with the option to wake the wizard (an LLM) only when the
> goblin can't be trusted.

LLM systems constantly face a fork for every subtask: use a cheap deterministic tool
(regex, a parser, spaCy, pytesseract) or spend tokens on the model itself. The cheap
path is usually good enough — but it's wired in at build time, so the system never
notices the cases where it was the wrong call.

Hobgoblin packages **goblin-first** primitives: deterministic by default, with a clean
seam to escalate to an LLM only when confidence is low.

## Status

v1 of the first primitive, `hobgoblin.extract()`, works. See [`DESIGN.md`](DESIGN.md)
for the full spec and output schema.

## Install

```bash
pip install -e .
python -m spacy download en_core_web_sm
```

## Usage

```python
from hobgoblin import extract, item_index

ents = extract("Last Tuesday, John bought three boxes of red apples.",
               anchors=["apple"])
# -> list of entity dicts: head, char span, POS pattern, governing verb,
#    count (three boxes of), dates, modifiers, anchors_matched, ...

# Items of interest (phone/email/URL/money/address) get associated to entities
# with a deterministic relatedness weight:
ents  = extract("Call John Smith at 555-123-4567; his office is at 123 Main St.")
items = item_index(ents)   # item-centric view: each item -> best_entity + ranked list
```

For a full end-to-end walkthrough (typed entities, counts, military units, item
association), see [`examples/intel_report.py`](examples/intel_report.py):

```bash
python examples/intel_report.py
```

### Interactive viewer

A zero-dependency local web viewer draws a pill around every entity and item.
Hover for a tooltip (type + what it's associated to); click an entity for its full
element breakdown.

```bash
python examples/annotate_server.py            # open http://localhost:8421
python examples/annotate_server.py --port 9000  # or pick your own
```

It falls back to a free port automatically if the chosen one is taken (it prints
the actual URL on startup).

## Roadmap

- [x] `hobgoblin.extract()` — entity + context extraction (spaCy POS/dependency)
- [x] Items of interest + relatedness scoring (blended token/dependency distance)
- [x] Expanded item types: email, url, uuid, mac, ip, coordinate, date, time,
      credit_card (Luhn), ssn, phone, address, money, percent, handle, hashtag,
      file_path, zip
- [x] Military unit recognizer (`detect_units`): cardinal/Roman/ordinal/letter
      designations (`3 Corps`, `I Corps`, `1st Infantry Division`, `C Company`)
- [x] Smart anchors: fuzzy typo matching (`brigdae`→brigade), abbreviation
      aliases (`BDE`), categorized output (unit/facility/equipment/place),
      rule-based `NAME` + `PLACE` detectors, and a built-in `ANCHORS` pack
- [ ] Wizard escalation — LLM fallback when the goblin's confidence is low
- [ ] TypeScript port (`compromise` / `wink-nlp`; shared JSON schema)
- [ ] More primitives: `ocr()`, `classify()`, …

## License

MIT
