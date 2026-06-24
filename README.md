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
from hobgoblin import extract

ents = extract("Last Tuesday, John bought three boxes of red apples.",
               anchors=["apple"])
# -> list of entity dicts: head, char span, POS pattern, governing verb,
#    count (three boxes of), dates, modifiers, anchors_matched, ...
```

## Roadmap

- [x] `hobgoblin.extract()` — entity + context extraction (spaCy POS/dependency)
- [ ] Wizard escalation — LLM fallback when the goblin's confidence is low
- [ ] TypeScript port (`compromise` / `wink-nlp`; shared JSON schema)
- [ ] More primitives: `ocr()`, `classify()`, …

## License

MIT
