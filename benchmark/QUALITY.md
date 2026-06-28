# Hobgoblin quality eval — goblin error rates judged by an LLM (the wizard)

One row per page. The judge is `wizard.fix()` (LLM). Corrections are split by what
they target so typing error isn't conflated with coverage:
`drops` = false positives · `adds` = missed entities · `mistypes` = retype of an
entity the goblin had *typed* (a real typing error) · `type_sugg` = retype of an
*untyped* entity (the wizard suggesting a label — a coverage gain, not an error).
Total later: precision ~= 1-drops/ents · recall ~= ents/(ents+adds) ·
typing-accuracy ~= 1-mistypes/typed.

| title | ents | typed | drops | adds | mistypes | type_sugg |
| --- | --- | --- | --- | --- | --- | --- |
| Captain Corelli's Mandolin (film) | 20 | 10 | 7 | 1 | 2 | 4 |
| Bruiser (TV series) | 27 | 13 | 14 | 1 | 2 | 0 |
| Creamed eggs on toast | 69 | 8 | 32 | 4 | 6 | 1 |
| 2020–21 Phoenix Suns season | 45 | 15 | 18 | 4 | 3 | 5 |
| Birgit Bjørnvig | 22 | 11 | 11 | 1 | 3 | 2 |
| 2013–14 ABA League | 14 | 11 | 2 | 1 | 1 | 1 |
| Boulay-Moselle | 17 | 9 | 8 | 2 | 4 | 0 |
| 2009 World Judo Juniors Championships | 6 | 5 | 1 | 0 | 1 | 0 |
| Rod Harrington | 19 | 9 | 10 | 0 | 5 | 0 |
| Christine Craft | 9 | 3 | 0 | 2 | 2 | 6 |
| Betiscoides | 19 | 4 | 11 | 0 | 3 | 4 |
| Nuit 1 | 13 | 5 | 1 | 0 | 2 | 3 |
| Dealu Frumos | 20 | 13 | 3 | 0 | 6 | 0 |
| Luis Aldunate | 18 | 10 | 5 | 0 | 4 | 2 |
| Mansurabad, Seyyedan | 12 | 6 | 5 | 0 | 3 | 1 |
| Lisa Iwamoto | 17 | 9 | 7 | 1 | 0 | 1 |
| Wójcza | 10 | 5 | 3 | 1 | 2 | 3 |
| Socialthing | 9 | 2 | 6 | 2 | 1 | 1 |
| Charles Santley | 38 | 10 | 14 | 2 | 0 | 3 |
| Almaz Capital | 48 | 31 | 22 | 3 | 8 | 3 |
| Manfred Nowak | 38 | 26 | 6 | 0 | 4 | 3 |
| Tony Bennett | 93 | 41 | 6 | 5 | 8 | 2 |
| State University of Non-Ferrous Metals and Gold | 13 | 8 | 3 | 0 | 0 | 0 |
| Kreischa | 13 | 6 | 7 | 0 | 1 | 1 |
| John P. Woodall | 49 | 18 | 23 | 2 | 2 | 7 |
| Bože pravde | 24 | 9 | 8 | 2 | 2 | 3 |
| Jim Sinclair (footballer) | 15 | 7 | 6 | 0 | 4 | 2 |
| Wild Women (1970 film) | 16 | 8 | 8 | 2 | 6 | 1 |
| James Lisney | 46 | 26 | 27 | 4 | 6 | 2 |
| Nahar Khan | 18 | 7 | 8 | 0 | 7 | 2 |
| The Frog Prince (play) | 37 | 12 | 20 | 0 | 4 | 3 |
| Désiré-François Le Filleul Des Guerrots | 18 | 8 | 15 | 3 | 3 | 0 |
| Wilfred Broadhead | 28 | 13 | 12 | 1 | 5 | 1 |
| The Broken Crown | 14 | 9 | 5 | 0 | 1 | 2 |
| Tip-Off Girls | 14 | 11 | 1 | 0 | 3 | 2 |
| Blackberry Belle | 54 | 24 | 3 | 3 | 7 | 1 |
| Tina Shagufta Munir | 21 | 12 | 8 | 3 | 3 | 2 |
| David Sagiv | 80 | 26 | 45 | 0 | 8 | 2 |
| Freedom Party (Iceland) | 14 | 7 | 9 | 2 | 1 | 0 |
| Järvsö | 43 | 22 | 21 | 1 | 10 | 1 |
| Nantucket Cliff Range Lights | 17 | 6 | 10 | 1 | 2 | 0 |
| Trevor Aston | 14 | 9 | 6 | 0 | 1 | 0 |
| 2011 Poznań Porsche Open | 13 | 2 | 4 | 1 | 0 | 7 |
| Gaylord Powless | 182 | 119 | 30 | 7 | 69 | 5 |
| Richard Baker (Zen teacher) | 27 | 13 | 11 | 4 | 2 | 3 |
| 1856 Hutt by-election | 19 | 10 | 7 | 3 | 5 | 3 |
| Oleh Koverko | 11 | 7 | 4 | 2 | 1 | 2 |
| Bilecik YHT railway station | 37 | 18 | 19 | 1 | 3 | 4 |
| Krasnokamensk (urban locality) | 14 | 9 | 7 | 0 | 2 | 0 |
| Kosmos 107 | 37 | 7 | 20 | 3 | 5 | 4 |

---

## Totals — 50 pages, 1471 entities (LLM-judged by wizard.fix, expanded pack)

| metric | value |
|---|---|
| pages | 50 |
| entities | 1471 · typed 689 (47%) |
| drops (false positives) | 539 |
| adds (missed entities) | 75 |
| mistypes (wrong type on a typed entity) | 233 |
| type_sugg (label for an untyped entity — coverage, not error) | 105 |

### Error rates
- **identification recall ≈ 95%** — the goblin rarely *misses* a real entity (the ~75 misses are mostly multi-word entities spaCy split apart).
- **identification precision ≈ 63%** — it *over-extracts*: ~37% of returned entities are generic noun phrases ("the film", "actors", "the series"). Deterministically fixable (filter common-noun chunks).
- **typing accuracy ≈ 66%** — of typed entities, ~34% are mislabeled, from two causes: inherited spaCy NER errors (Olivia Colman→organization) and Hobgoblin's own fuzzy false-positives (butter→military_unit). The former is the wizard's job; the latter is tightenable in match.py.

Judged by  (Claude) via the Claude Code CLI under a Max subscription —
an LLM proxy for ground truth, not gospel. Sample = 50 random Wikipedia pages.
