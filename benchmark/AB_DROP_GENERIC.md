# Hobgoblin A/B — drop_generic, same pages, one oracle per page

Paired measurement (no sampling/judgment variance): the wizard judges the full
(OFF) entity set once; `drop_generic` removes a subset. Columns: `ents_off` entities
OFF · `junk` oracle-flagged false positives · `adds` missed entities · `removed`
entities the filter dropped · `removed_junk`/`removed_good` of those, how many were
junk (good removals) vs real (recall cost).

| title | ents_off | junk | adds | removed | removed_junk | removed_good |
| --- | --- | --- | --- | --- | --- | --- |
| Casa Romuli | 23 | 12 | 4 | 11 | 9 | 2 |
| Grim Reapers Motorcycle Club (USA) | 7 | 3 | 2 | 2 | 2 | 0 |
| Jack Tuijp | 57 | 34 | 1 | 29 | 29 | 0 |
| Kilmaluag Formation | 19 | 2 | 1 | 13 | 2 | 11 |
| Post Break-Up Sex | 11 | 6 | 1 | 3 | 3 | 0 |
| Daisy Martin | 65 | 11 | 3 | 27 | 9 | 18 |
| Sadhu Singh Dharamsot | 18 | 6 | 0 | 3 | 3 | 0 |
| Murena (comic book) | 17 | 8 | 3 | 9 | 8 | 1 |
| Be Lifted High | 23 | 13 | 4 | 9 | 9 | 0 |
| Alice Ruiz | 8 | 8 | 2 | 4 | 4 | 0 |
| Normalizing constant | 22 | 8 | 0 | 19 | 8 | 11 |
| College Square Historic District | 9 | 3 | 0 | 2 | 2 | 0 |
| The Bigamist | 14 | 6 | 0 | 6 | 6 | 0 |
| Sports law in the United States | 19 | 8 | 0 | 18 | 8 | 10 |
| Direction Nationale de l'Alphabétisation Fonctionnelle et de la Linguistique Appliquée | 11 | 3 | 0 | 3 | 3 | 0 |
| WLBT Tower | 21 | 11 | 4 | 9 | 9 | 0 |
| Mamarce Oinochoe | 8 | 4 | 0 | 4 | 4 | 0 |
| From the Beginning (Small Faces album) | 15 | 11 | 1 | 8 | 8 | 0 |
| Rondel (gaming) | 58 | 32 | 1 | 29 | 28 | 1 |
| East Pacific Center | 31 | 11 | 0 | 5 | 4 | 1 |
| Plaza Theatre (Charleston, West Virginia) | 20 | 9 | 2 | 7 | 6 | 1 |
| St Joseph's College, Nudgee | 45 | 18 | 2 | 12 | 12 | 0 |
| Charlie's Angels | 56 | 38 | 1 | 27 | 27 | 0 |
| Diocese of Macerata-Tolentino-Recanati-Cingoli-Treia | 10 | 4 | 0 | 3 | 3 | 0 |
| Arshdeep Bains | 9 | 3 | 2 | 3 | 3 | 0 |
| 2005 24 Hours of Daytona | 27 | 11 | 4 | 11 | 9 | 2 |
| AICF | 6 | 2 | 4 | 1 | 0 | 1 |
| Veasey | 25 | 18 | 8 | 13 | 11 | 2 |
| USS Plymouth (1867) | 12 | 5 | 1 | 3 | 3 | 0 |
| St. Thomas Aquinas Church (Palo Alto, California) | 44 | 19 | 2 | 9 | 9 | 0 |
| Evlagh Beg | 13 | 7 | 0 | 5 | 5 | 0 |
| Winter Palace Taken | 70 | 53 | 1 | 51 | 47 | 4 |
| John O'Meally | 24 | 13 | 3 | 11 | 10 | 1 |
| Fenwick Island State Park | 18 | 6 | 2 | 5 | 5 | 0 |
| Dallasiella | 12 | 3 | 1 | 2 | 2 | 0 |
| Virginia State Route 753 | 10 | 9 | 1 | 3 | 3 | 0 |
| Noha Abd Rabo | 28 | 5 | 1 | 12 | 5 | 7 |
| University of Western Greece | 27 | 17 | 6 | 9 | 9 | 0 |
| Sukdeo Paswan | 12 | 4 | 0 | 2 | 2 | 0 |
| Dora Mavor Moore Award for Best Original Play (Independent Theatre) | 23 | 13 | 4 | 16 | 13 | 3 |
| Scyphostegia | 20 | 14 | 0 | 13 | 13 | 0 |
| Jay Marchant | 11 | 2 | 2 | 3 | 0 | 3 |
| Host (psychology) | 31 | 15 | 0 | 29 | 15 | 14 |
| Chromium(IV) oxide | 17 | 8 | 2 | 13 | 6 | 7 |
| Stephanie Hsu | 42 | 20 | 4 | 12 | 12 | 0 |
| Alfred Bell | 11 | 9 | 5 | 5 | 5 | 0 |
| St. Francis Brooklyn Terriers men's soccer | 43 | 22 | 2 | 12 | 12 | 0 |
| Bailey Falter | 34 | 15 | 2 | 11 | 10 | 1 |
| Bucculatrix ericameriae | 11 | 5 | 1 | 5 | 5 | 0 |
| Joseph Bukari | 17 | 5 | 1 | 3 | 3 | 0 |
| MCG +01-02-015 | 11 | 6 | 1 | 6 | 6 | 0 |
| On-Demand Small Unmanned Aircraft System | 58 | 34 | 3 | 42 | 34 | 8 |
| Languages of Israel | 66 | 38 | 5 | 31 | 30 | 1 |
| Toledo War | 83 | 6 | 1 | 50 | 1 | 49 |
| Tejaswini Ananth Kumar | 16 | 11 | 1 | 8 | 8 | 0 |
| Hugh Reinagle | 24 | 11 | 2 | 8 | 8 | 0 |
| Silent Enemy (Star Trek: Enterprise) | 43 | 5 | 2 | 22 | 2 | 20 |
| Arasvikfjorden | 41 | 17 | 2 | 15 | 11 | 4 |
| Petkovski | 11 | 6 | 4 | 3 | 3 | 0 |
| American Institute of Steel Construction | 22 | 4 | 0 | 13 | 4 | 9 |
| PSR J2322−2650 | 27 | 17 | 3 | 15 | 12 | 3 |
| Seeteufel (Russia) | 47 | 32 | 0 | 27 | 27 | 0 |
| Prince Kofi Amoabeng | 18 | 10 | 3 | 7 | 7 | 0 |
| Stanton Independent School District | 14 | 6 | 0 | 4 | 4 | 0 |
| 63rd Street lines | 88 | 44 | 15 | 29 | 29 | 0 |
| Koyamada International Foundation | 18 | 11 | 5 | 6 | 6 | 0 |
| Paul Cornell | 28 | 16 | 2 | 11 | 11 | 0 |
| 1983 Uruguayan pro-democracy demonstration | 51 | 37 | 3 | 32 | 31 | 1 |
| Ghutiari Sharif railway station | 12 | 4 | 1 | 3 | 3 | 0 |
| Clear Springs Cumberland Presbyterian Church | 58 | 47 | 3 | 33 | 33 | 0 |
| François Bourgoing (Dominican) | 18 | 10 | 2 | 8 | 8 | 0 |
| Letter from a group of Soviet writers about Solzhenitsyn and Sakharov | 44 | 4 | 1 | 25 | 1 | 24 |
| Preserje | 24 | 2 | 6 | 1 | 1 | 0 |
| XXII Tactical Air Command | 15 | 6 | 1 | 5 | 5 | 0 |
| Reasoning model | 27 | 4 | 0 | 20 | 4 | 16 |
| Tangga Batu | 12 | 4 | 0 | 4 | 4 | 0 |
| Na Koa Ikaika Maui | 16 | 5 | 0 | 2 | 2 | 0 |
| Shuswap Country | 32 | 12 | 4 | 10 | 9 | 1 |
| Sidewalk Records | 128 | 68 | 20 | 39 | 39 | 0 |
| Qiu Jun (poet) | 17 | 3 | 4 | 5 | 1 | 4 |
| AFDA, The School for the Creative Economy | 26 | 14 | 0 | 11 | 11 | 0 |
| David Pastrňák | 18 | 7 | 1 | 3 | 3 | 0 |
| Gollancz (surname) | 19 | 9 | 1 | 8 | 8 | 0 |
| Magnetostatic loudspeaker | 34 | 9 | 0 | 31 | 8 | 23 |
| Aeronautes | 9 | 2 | 4 | 5 | 2 | 3 |
| Sajid Hussain (journalist) | 15 | 11 | 0 | 11 | 10 | 1 |
| Fırtına River | 11 | 4 | 0 | 4 | 4 | 0 |
| Antoni Clarassó i Terès | 16 | 8 | 1 | 6 | 6 | 0 |
| Fine Arts Commission | 15 | 11 | 3 | 7 | 7 | 0 |
| Badr al-Dīn ibn Jamaʿah | 17 | 6 | 0 | 6 | 5 | 1 |
| Henry Keswick | 14 | 6 | 2 | 3 | 3 | 0 |
| Krasnaya Nov, Lgovsky District, Kursk Oblast | 14 | 7 | 0 | 3 | 3 | 0 |
| Guido Horn d'Arturo | 29 | 19 | 2 | 18 | 18 | 0 |
| 1984 Cal State Fullerton Titans baseball team | 15 | 3 | 0 | 3 | 3 | 0 |
| Are You Okay? (digital series) | 12 | 8 | 2 | 8 | 8 | 0 |
| Dorsey v. United States | 27 | 19 | 3 | 16 | 15 | 1 |
| Glostrup | 43 | 3 | 3 | 20 | 0 | 20 |
| Amy Mathers Teen Book Award | 16 | 11 | 0 | 12 | 10 | 2 |
| Pseudospeciation | 82 | 54 | 1 | 63 | 49 | 14 |
| 1966 Nashville 400 | 8 | 3 | 4 | 0 | 0 | 0 |

---

## Totals — 100 pages, same-page paired A/B (one wizard oracle per page)

| metric | OFF (drop_generic off) | ON (drop_generic on) |
|---|---|---|
| precision | 53% | 77% |
| recall | 87% | 68% |

- entities OFF: 2693 (junk/FP 1266, real 1427); missed (adds): 212
- drop_generic removed 1246 entities: 940 junk (good removals) + 306 real (recall cost)
- **filter precision = 75%** (of what it removed, that share was oracle-confirmed junk)

Verdict: drop_generic is a real precision lever (+24 pts) at a real recall cost (-19 pts) — about 1 real entity lost per 4 removed. A tradeoff knob, not a free win.
