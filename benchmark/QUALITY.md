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
| Ballymacward | 27 | 10 | 10 | 1 | 3 | 5 |
| Carlton Complex Fire | 20 | 9 | 7 | 2 | 5 | 5 |
| Bunkai | 13 | 2 | 9 | 0 | 1 | 3 |
| Walloon church | 32 | 12 | 6 | 2 | 2 | 5 |
| Vi vil leve | 15 | 7 | 7 | 1 | 1 | 1 |
| Michael J. Flaherty | 24 | 12 | 12 | 2 | 4 | 0 |
| Statues of the National Statuary Hall Collection | 62 | 18 | 9 | 2 | 5 | 0 |
| Monstera tenuis | 31 | 8 | 24 | 1 | 2 | 2 |
| Pilica River Skansen | 10 | 3 | 3 | 0 | 2 | 2 |
| James P. Bassett | 8 | 4 | 2 | 3 | 1 | 2 |
| Antonio Salieri | 91 | 29 | 57 | 0 | 3 | 6 |
| A Stranger in Town (1943 film) | 15 | 8 | 7 | 1 | 7 | 1 |
| Elachyophtalma cotanoides | 17 | 2 | 12 | 0 | 1 | 2 |
| Ebba Forsberg | 53 | 20 | 29 | 1 | 4 | 4 |
| Filip Kostić | 11 | 4 | 6 | 2 | 2 | 1 |
| Zochonis | 14 | 5 | 3 | 0 | 2 | 4 |
| Paslow Falls/Plant | 28 | 7 | 16 | 1 | 4 | 1 |
| Nemopsis | 11 | 5 | 5 | 2 | 2 | 2 |
| 2011 Atlantic hurricane season | 91 | 38 | 51 | 4 | 9 | 1 |
| Vroni Thalmann-Bieri | 13 | 8 | 6 | 0 | 2 | 0 |
| Glandular frog (disambiguation) | 18 | 4 | 4 | 2 | 1 | 8 |
| Order of Prince Edward Island | 19 | 7 | 9 | 1 | 3 | 3 |
| Donaldson, Minnesota | 11 | 6 | 5 | 2 | 3 | 0 |
| 2025 President's Cup – Men's doubles | 13 | 5 | 6 | 0 | 1 | 1 |
| Tripotamo, Arcadia | 19 | 10 | 8 | 1 | 4 | 1 |
| Alexander Oblinger | 16 | 11 | 0 | 0 | 5 | 0 |
| Mykhailo Holovko | 11 | 6 | 5 | 2 | 1 | 0 |
| List of number-one R&B/hip-hop songs of 2017 (U.S.) | 8 | 0 | 5 | 2 | 0 | 3 |
| Hayil | 23 | 7 | 14 | 0 | 4 | 1 |
| Mitsubishi FBR Systems | 62 | 28 | 27 | 2 | 5 | 2 |
| David Lilley | 17 | 12 | 3 | 0 | 2 | 2 |
| Track & Signal | 17 | 8 | 8 | 3 | 0 | 1 |
| Michiko Neya | 49 | 33 | 10 | 4 | 14 | 4 |
| Zameer (2005 film) | 14 | 6 | 6 | 0 | 5 | 1 |
| Malinovo, Lovech Province | 15 | 7 | 8 | 1 | 1 | 0 |
| List of D.N.Angel chapters | 75 | 26 | 45 | 0 | 14 | 1 |
| Viscount Longueville | 34 | 24 | 8 | 6 | 5 | 0 |
| Sophia Ellis | 17 | 9 | 5 | 0 | 4 | 3 |
| Simon Alcott | 15 | 6 | 7 | 3 | 2 | 2 |
| UAAP Season 24 men's basketball tournament | 9 | 3 | 2 | 0 | 0 | 2 |
| Kalsian Bhattian | 53 | 13 | 27 | 3 | 6 | 3 |
| Coxs River track | 19 | 14 | 5 | 0 | 5 | 3 |
| Cypress Lodge | 31 | 19 | 15 | 2 | 9 | 0 |
| Sireniki | 25 | 14 | 7 | 0 | 7 | 1 |
| 2011 World Championships in Athletics – Women's shot put | 49 | 18 | 26 | 5 | 6 | 4 |
| Amanu | 25 | 6 | 16 | 1 | 5 | 1 |
| Monsters Crash the Pajama Party | 27 | 3 | 3 | 0 | 2 | 0 |
| Walter D'Arcy Ryan | 22 | 10 | 9 | 1 | 3 | 3 |
| Lisa Smokstad | 4 | 3 | 2 | 1 | 1 | 0 |
| Sean Bowen | 6 | 1 | 1 | 4 | 0 | 4 |

---

## Totals — post fuzzy-fix (drop_generic off) (50 pages, 1309 entities, LLM-judged by wizard.fix)

| metric | value |
|---|---|
| entities | 1309 (typed 530, 40%) |
| drops (false positives) | 577 |
| adds (missed) | 71 |
| mistypes (wrong type on typed entity) | 180 |
| type_sugg (label for untyped — coverage) | 101 |
| **identification recall** | **95%** |
| **identification precision** | **56%** |
| **typing accuracy** | **66%** |

Each eval is a fresh random sample, so cross-run deltas include sampling noise.
Typing accuracy is bottlenecked by spaCy NER mislabels (the wizard's job to fix);
precision is gated by generic-noun over-extraction (see `drop_generic`).
