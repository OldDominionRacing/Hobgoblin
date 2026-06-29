import sys
cols = ['ents', 'typed', 'drops', 'adds', 'mistypes', 'type_sugg']
path, label = sys.argv[1], sys.argv[2]
tot = {c: 0 for c in cols}
n = 0
for line in open(path):
    line = line.strip()
    if line.startswith('| ') and ' | ' in line and not line.startswith('| title') and not line.startswith('| ---'):
        vals = [p.strip() for p in line.strip('|').split('|')][1:]
        if len(vals) == len(cols):
            try:
                nums = [int(v) for v in vals]
            except ValueError:
                continue
            for c, v in zip(cols, nums):
                tot[c] += v
            n += 1
e, ty = tot['ents'], tot['typed']
s = f"""
---

## Totals — {label} ({n} pages, {e} entities, LLM-judged by wizard.fix)

| metric | value |
|---|---|
| entities | {e} (typed {ty}, {100*ty/e:.0f}%) |
| drops (false positives) | {tot['drops']} |
| adds (missed) | {tot['adds']} |
| mistypes (wrong type on typed entity) | {tot['mistypes']} |
| type_sugg (label for untyped — coverage) | {tot['type_sugg']} |
| **identification recall** | **{100*(e/(e+tot['adds'])):.0f}%** |
| **identification precision** | **{100*(1-tot['drops']/e):.0f}%** |
| **typing accuracy** | **{100*(1-tot['mistypes']/ty):.0f}%** |

Each eval is a fresh random sample, so cross-run deltas include sampling noise.
Typing accuracy is bottlenecked by spaCy NER mislabels (the wizard's job to fix);
precision is gated by generic-noun over-extraction (see `drop_generic`).
"""
open(path, 'a').write(s)
print(s)
