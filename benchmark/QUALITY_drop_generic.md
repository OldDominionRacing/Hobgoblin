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
| Luisa Fernanda (disambiguation) | 12 | 10 | 5 | 3 | 2 | 0 |
| Uksáhkká | 23 | 12 | 6 | 1 | 6 | 3 |
| FIDA | 18 | 13 | 7 | 11 | 2 | 3 |
| Golden Triangle Mall | 33 | 26 | 7 | 4 | 7 | 2 |
| Three Gorges Dam | 29 | 21 | 11 | 1 | 7 | 1 |
| Julio Galán | 4 | 2 | 1 | 0 | 0 | 2 |
| Samantha (Hole song) | 18 | 14 | 3 | 3 | 5 | 0 |
| Lisa Kay | 13 | 9 | 1 | 1 | 5 | 1 |
| Enchiridion | 24 | 13 | 8 | 8 | 9 | 5 |
| Carlin B. Carpenter | 3 | 3 | 0 | 2 | 1 | 0 |
| Este Mundo | 9 | 8 | 2 | 3 | 2 | 0 |
| Baddeck, and That Sort of Thing | 23 | 20 | 6 | 1 | 2 | 0 |
| Antoinette Hertsenberg | 3 | 3 | 0 | 1 | 2 | 0 |
| Gandier ordinance | 13 | 10 | 2 | 1 | 4 | 1 |
| Richard Kidder Meade (colonel) | 7 | 7 | 1 | 0 | 3 | 0 |
| Protecting Lawful Streaming Act | 11 | 9 | 1 | 1 | 10 | 1 |
| Anton Olson | 20 | 18 | 0 | 0 | 4 | 2 |
| Michel Olçomendy | 7 | 6 | 1 | 0 | 2 | 1 |
| Government Museum, Salem | 6 | 6 | 0 | 1 | 2 | 0 |
| Holger Geschwindner | 14 | 12 | 3 | 1 | 1 | 1 |
| Henry Grey, 2nd Earl of Tankerville | 11 | 10 | 1 | 0 | 1 | 1 |
| Lunuwila | 13 | 9 | 1 | 0 | 1 | 3 |
| Becky Whitley | 12 | 8 | 2 | 0 | 3 | 4 |
| Senator Williamson | 15 | 14 | 9 | 17 | 2 | 1 |
| Sujaku Suzuki | 4 | 4 | 1 | 2 | 0 | 0 |
| National September 11 Memorial & Museum | 42 | 27 | 9 | 2 | 10 | 3 |
| Bhangaha | 8 | 5 | 2 | 1 | 1 | 1 |
| Every Living Thing | 8 | 5 | 2 | 4 | 0 | 0 |
| Veedu Mamoolodu Kadu | 9 | 7 | 2 | 0 | 3 | 0 |
| Nathaniel Pearlman | 28 | 21 | 3 | 0 | 2 | 6 |
| Connections (British TV series) | 22 | 15 | 6 | 2 | 2 | 2 |
| History of the aircraft carrier | 16 | 9 | 4 | 0 | 5 | 3 |
| Hedon Haven | 44 | 34 | 15 | 0 | 8 | 2 |
| Affleck–Dine mechanism | 10 | 4 | 0 | 0 | 3 | 0 |
| Bob Reynolds (American football, born 1914) | 17 | 16 | 1 | 0 | 7 | 1 |
| Klaus Block | 23 | 17 | 8 | 1 | 3 | 2 |
| George Goehring | 5 | 4 | 1 | 6 | 1 | 0 |
| Stéphan Guérin-Tillié | 6 | 2 | 3 | 3 | 1 | 1 |
| The Era World Tour | 12 | 11 | 2 | 0 | 3 | 0 |
| Drug coupon | 2 | 1 | 1 | 1 | 1 | 0 |
| Bail in Canada | 8 | 2 | 1 | 0 | 0 | 1 |
| Daviesia subulata | 3 | 2 | 0 | 0 | 1 | 1 |
| Christ Episcopal Church (Winchester, Virginia) | 44 | 37 | 10 | 1 | 7 | 2 |
| La monaca di Monza (1962 film) | 5 | 5 | 0 | 0 | 2 | 0 |
| Richard Dunn | 23 | 15 | 6 | 9 | 1 | 7 |
| Blend modes | 7 | 2 | 3 | 1 | 2 | 1 |
| Bogoslovija, Belgrade | 9 | 4 | 2 | 0 | 0 | 3 |
| Abbiategrasso | 12 | 9 | 0 | 1 | 1 | 3 |
| Vista Spirit hybrid-class cruise ship | 16 | 5 | 8 | 2 | 2 | 3 |
| Skoki (disambiguation) | 29 | 27 | 2 | 1 | 4 | 1 |

---

## Totals — precision mode (drop_generic ON) (50 pages, 753 entities, LLM-judged by wizard.fix)

| metric | value |
|---|---|
| entities | 753 (typed 553, 73%) |
| drops (false positives) | 170 |
| adds (missed) | 97 |
| mistypes (wrong type on typed entity) | 153 |
| type_sugg (label for untyped — coverage) | 75 |
| **identification recall** | **89%** |
| **identification precision** | **77%** |
| **typing accuracy** | **72%** |

Each eval is a fresh random sample, so cross-run deltas include sampling noise.
Typing accuracy is bottlenecked by spaCy NER mislabels (the wizard's job to fix);
precision is gated by generic-noun over-extraction (see `drop_generic`).
