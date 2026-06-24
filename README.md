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

🚧 Early design. No installable package yet. See [`DESIGN.md`](DESIGN.md) for the full
design of the first primitive, `hobgoblin.extract()` (spaCy-based entity & context
extraction).

## Roadmap

- [ ] `hobgoblin.extract()` — entity + context extraction (spaCy POS/dependency)
- [ ] Wizard escalation — LLM fallback when the goblin's confidence is low
- [ ] More primitives: `ocr()`, `classify()`, …

## License

MIT
