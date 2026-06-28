# Hobgoblin benchmark — per-page goblin metrics (random Wikipedia)

One row per page. Deterministic goblin only (no LLM). Total later from the rows.

Columns:
- `chars` document length · `ents` entities (after stopword-drop) ·
  `typed`/`untyped` entities that matched / didn't match an anchor category ·
  `verb`/`count`/`unit`/`assoc` entities carrying that element ·
  `items` items-of-interest associated · `out_verbose_tok`/`out_compact_tok`
  ~tokens of structured output the goblin produced for free (verbose JSON / compact).

| title | chars | ents | typed | untyped | verb | count | unit | items | assoc | out_verbose_tok | out_compact_tok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Lanhee Chen | 1817 | 73 | 43 | 30 | 73 | 1 | 0 | 10 | 18 | 17392 | 2062 |
| St. Augustine Foot Soldiers Monument | 597 | 22 | 8 | 14 | 22 | 1 | 0 | 4 | 10 | 5791 | 644 |
| Dasht-e Murt-e Olya | 245 | 13 | 5 | 8 | 13 | 1 | 0 | 1 | 2 | 3159 | 349 |
| Moving Targets (Flo & Eddie album) | 576 | 26 | 12 | 14 | 26 | 1 | 0 | 2 | 7 | 6035 | 685 |
| Paulo Victor | 539 | 15 | 9 | 6 | 15 | 0 | 0 | 5 | 13 | 6831 | 561 |
| Maven Maurer | 394 | 15 | 9 | 6 | 15 | 0 | 0 | 3 | 9 | 3982 | 466 |
| Teruyuki | 401 | 22 | 7 | 15 | 22 | 0 | 0 | 4 | 14 | 7298 | 692 |
| Frederick Henry Caiger | 357 | 13 | 6 | 7 | 13 | 0 | 0 | 6 | 11 | 3457 | 386 |
| McCollum-Murray House | 604 | 17 | 8 | 9 | 17 | 0 | 0 | 3 | 5 | 4535 | 480 |
| Trans-Borneo Railway | 512 | 24 | 15 | 9 | 24 | 1 | 0 | 0 | 0 | 4978 | 600 |
| Jeet Lal | 292 | 10 | 5 | 5 | 10 | 0 | 0 | 2 | 4 | 2434 | 281 |
| New Brunswick Route 560 | 894 | 39 | 20 | 19 | 37 | 5 | 0 | 7 | 13 | 8796 | 993 |
| Ramboda Falls | 339 | 18 | 4 | 14 | 18 | 2 | 0 | 2 | 8 | 3756 | 430 |
| Laktaši Sports Hall | 284 | 12 | 5 | 7 | 12 | 1 | 0 | 0 | 0 | 2903 | 345 |
| Sitaramdas Omkarnath | 1220 | 54 | 13 | 41 | 54 | 4 | 0 | 2 | 2 | 12035 | 1388 |
| The Cedar Tree | 1330 | 53 | 19 | 34 | 53 | 13 | 0 | 9 | 16 | 12074 | 1402 |
| Glen Island Park | 1602 | 66 | 35 | 31 | 66 | 4 | 0 | 4 | 9 | 15644 | 1852 |
| Opotoru River | 297 | 10 | 3 | 7 | 10 | 1 | 0 | 6 | 7 | 2389 | 240 |
| Kyburg family | 707 | 33 | 16 | 17 | 33 | 1 | 0 | 4 | 11 | 8589 | 1026 |
| Museum of the Cetinska Krajina Region | 333 | 10 | 4 | 6 | 10 | 1 | 0 | 1 | 2 | 2542 | 278 |
| Otto Siegfried Julius | 213 | 8 | 8 | 0 | 8 | 0 | 0 | 3 | 6 | 1941 | 216 |
| P. Kilemsungla | 806 | 34 | 19 | 15 | 34 | 0 | 0 | 4 | 7 | 7538 | 1016 |
| Kummulla | 296 | 11 | 5 | 6 | 11 | 0 | 0 | 3 | 5 | 2779 | 307 |
| Dehkhoda, Mazandaran | 253 | 13 | 6 | 7 | 13 | 2 | 0 | 2 | 3 | 2972 | 350 |
| Zastava M80 | 301 | 11 | 7 | 4 | 11 | 0 | 0 | 4 | 7 | 2724 | 287 |
| Dixie Friend Gay | 631 | 29 | 14 | 15 | 29 | 0 | 0 | 6 | 9 | 6156 | 756 |
| AXX | 445 | 19 | 8 | 11 | 19 | 2 | 0 | 2 | 5 | 6714 | 574 |
| Age of Ignorance | 308 | 15 | 8 | 7 | 15 | 1 | 0 | 2 | 4 | 3233 | 418 |
| Kay-Shuttleworth | 1087 | 39 | 15 | 24 | 39 | 0 | 0 | 8 | 20 | 18294 | 1513 |
| Glossina pallidipes | 283 | 12 | 2 | 10 | 12 | 2 | 0 | 0 | 0 | 2581 | 296 |
| Advanced persistent threat | 1497 | 56 | 6 | 50 | 56 | 1 | 0 | 4 | 4 | 12261 | 1459 |
| Alma's Rainbow | 336 | 13 | 3 | 10 | 13 | 2 | 0 | 2 | 4 | 2719 | 330 |
| Temple Israel (Leadville, Colorado) | 294 | 11 | 5 | 6 | 11 | 1 | 0 | 3 | 4 | 2554 | 294 |
| Dangerous Liaisons (2012 film) | 729 | 28 | 15 | 13 | 28 | 0 | 0 | 13 | 20 | 8994 | 877 |
| Dauntless (ship, 1866) | 449 | 13 | 9 | 4 | 13 | 1 | 0 | 3 | 5 | 3326 | 389 |
| Billy Howle | 404 | 17 | 8 | 9 | 17 | 0 | 0 | 8 | 16 | 5524 | 545 |
| 2011 Tour of Azerbaijan (Iran) | 250 | 14 | 5 | 9 | 14 | 1 | 0 | 3 | 7 | 3170 | 390 |
| Waldron DeWitt Miller | 294 | 10 | 6 | 4 | 10 | 0 | 0 | 2 | 2 | 2313 | 284 |
| Rapid Alert System for Food and Feed | 648 | 28 | 6 | 22 | 28 | 0 | 0 | 4 | 8 | 6462 | 742 |
| Yogyakarta Sultanate | 1868 | 79 | 22 | 57 | 79 | 2 | 0 | 7 | 14 | 20356 | 2213 |
| Himex | 1179 | 50 | 21 | 29 | 48 | 0 | 0 | 8 | 19 | 11676 | 1335 |
| Howard C. Nielson | 229 | 7 | 5 | 2 | 7 | 0 | 0 | 3 | 5 | 1993 | 231 |
| Matrix decomposition | 256 | 12 | 0 | 12 | 12 | 1 | 0 | 0 | 0 | 2374 | 289 |
| Ulvhild Håkansdotter | 495 | 27 | 12 | 15 | 27 | 2 | 0 | 0 | 0 | 5826 | 652 |
| Blue-faced parrotfinch | 669 | 28 | 11 | 17 | 28 | 2 | 0 | 1 | 2 | 6066 | 713 |
| Slave Ship (Pohl novel) | 750 | 31 | 5 | 26 | 31 | 1 | 0 | 1 | 2 | 6555 | 766 |
| Bluecity | 202 | 7 | 2 | 5 | 7 | 0 | 0 | 2 | 2 | 1628 | 204 |
| Lane Public School | 487 | 19 | 11 | 8 | 13 | 0 | 0 | 0 | 0 | 4032 | 507 |
| Futsal Finalissima | 422 | 15 | 10 | 5 | 15 | 2 | 0 | 2 | 4 | 3673 | 424 |
| 2025 Sugar Bowl | 1938 | 77 | 27 | 50 | 77 | 9 | 0 | 8 | 14 | 18656 | 2128 |
| Sanchuniathon | 707 | 30 | 12 | 18 | 30 | 2 | 0 | 0 | 0 | 7807 | 838 |
| Filzmoos | 314 | 14 | 4 | 10 | 14 | 0 | 0 | 4 | 6 | 2840 | 346 |
| Silent treatment | 546 | 19 | 1 | 18 | 19 | 0 | 0 | 0 | 0 | 3700 | 468 |
| OHM (band) | 586 | 24 | 12 | 12 | 24 | 1 | 0 | 2 | 5 | 5318 | 638 |
| Northampton Golf Club | 284 | 11 | 7 | 4 | 11 | 0 | 0 | 4 | 10 | 2595 | 277 |
| Asif Sandila | 613 | 23 | 11 | 12 | 23 | 0 | 0 | 4 | 9 | 6590 | 687 |
| Frank W. Bireley | 1171 | 42 | 18 | 24 | 42 | 1 | 0 | 5 | 12 | 9606 | 1157 |
| Mathias Ntawulikura | 1202 | 34 | 19 | 15 | 33 | 8 | 0 | 10 | 16 | 9303 | 1015 |
| The Seydel Companies, Inc. | 335 | 19 | 8 | 11 | 19 | 1 | 0 | 0 | 0 | 3792 | 472 |
| James Augustine Healy | 559 | 21 | 8 | 13 | 21 | 0 | 0 | 5 | 7 | 4729 | 558 |
| Hilary and Jackie | 1575 | 62 | 21 | 41 | 62 | 3 | 0 | 4 | 10 | 14767 | 1651 |
| Antitoxin | 1035 | 41 | 0 | 41 | 41 | 0 | 0 | 0 | 0 | 7426 | 997 |
| Kay Coombs | 1490 | 58 | 28 | 30 | 58 | 2 | 0 | 8 | 17 | 13927 | 1688 |
| Pethidine intermediate A | 647 | 24 | 3 | 21 | 24 | 1 | 0 | 3 | 3 | 5671 | 626 |
| Tauern Railway | 624 | 24 | 14 | 10 | 24 | 1 | 0 | 6 | 8 | 5943 | 616 |
| Body of Christ | 1536 | 64 | 14 | 50 | 64 | 2 | 0 | 5 | 12 | 16512 | 1634 |
| George Caron | 863 | 33 | 17 | 16 | 33 | 1 | 0 | 6 | 13 | 7438 | 910 |
| Sourdeval-les-Bois | 215 | 8 | 2 | 6 | 8 | 0 | 0 | 2 | 4 | 2078 | 207 |
| Gymnastics at the 1968 Summer Olympics – Men's horizontal bar | 691 | 32 | 9 | 23 | 32 | 7 | 0 | 2 | 5 | 7648 | 798 |
| Barrabas | 699 | 31 | 18 | 13 | 31 | 0 | 0 | 5 | 16 | 10634 | 1006 |
| Redwood statue of Elizabeth Taylor | 1708 | 80 | 25 | 55 | 77 | 2 | 0 | 4 | 10 | 16363 | 2006 |
| Sheila Harsdorf | 550 | 22 | 16 | 6 | 22 | 0 | 0 | 3 | 5 | 4996 | 622 |
| Provincial Secretary of Prince Edward Island v Egan | 534 | 21 | 9 | 12 | 21 | 2 | 0 | 1 | 5 | 4883 | 549 |
| List of judges of the High Court (Ireland) | 392 | 17 | 6 | 11 | 17 | 1 | 0 | 0 | 0 | 4030 | 447 |
| Thomas Herbert Kershaw | 267 | 6 | 3 | 3 | 6 | 0 | 0 | 3 | 3 | 2231 | 256 |
| The Delicate Art of Parking | 590 | 22 | 10 | 12 | 22 | 2 | 0 | 3 | 7 | 5385 | 624 |
| Swen Temmel | 342 | 16 | 8 | 8 | 16 | 1 | 0 | 5 | 12 | 4134 | 456 |
| Anabelle Rodríguez | 327 | 12 | 7 | 5 | 12 | 0 | 0 | 2 | 4 | 3211 | 381 |
| Coventry, New York | 269 | 14 | 6 | 8 | 14 | 0 | 0 | 2 | 5 | 2562 | 332 |
| Phillips disaster of 1989 | 873 | 29 | 9 | 20 | 29 | 2 | 0 | 5 | 11 | 7560 | 866 |
| Dioceses of the Church of the East to 1318 | 611 | 27 | 15 | 12 | 27 | 2 | 0 | 3 | 6 | 6013 | 731 |
| Protein function prediction | 2444 | 90 | 6 | 84 | 90 | 5 | 0 | 3 | 5 | 20595 | 2309 |
| Ross Dallow | 221 | 7 | 3 | 4 | 7 | 0 | 0 | 2 | 2 | 1982 | 246 |
| Richard Denning | 640 | 20 | 14 | 6 | 20 | 1 | 0 | 10 | 15 | 7114 | 764 |
| Lawrence Lawrason | 1526 | 65 | 31 | 34 | 65 | 0 | 0 | 17 | 32 | 14756 | 1821 |
| Matt Henderson (ice hockey) | 293 | 8 | 2 | 6 | 8 | 1 | 0 | 3 | 8 | 2255 | 242 |
| 2016 Copa Libertadores first stage | 207 | 7 | 2 | 5 | 7 | 3 | 0 | 2 | 2 | 1743 | 190 |
| La Costa xeric shrublands | 315 | 13 | 1 | 12 | 13 | 0 | 0 | 1 | 4 | 2794 | 344 |
| The Rasp (film) | 223 | 10 | 6 | 4 | 10 | 1 | 0 | 1 | 2 | 2183 | 252 |
| Pussyfoot | 225 | 12 | 5 | 7 | 12 | 0 | 0 | 1 | 3 | 2206 | 296 |
| Rancho Otay | 289 | 10 | 7 | 3 | 8 | 0 | 0 | 3 | 6 | 2989 | 304 |
| Patrick, Queensland | 410 | 21 | 14 | 7 | 21 | 2 | 0 | 2 | 5 | 4372 | 572 |
| Charles Street Transit Terminal | 503 | 18 | 12 | 6 | 18 | 0 | 0 | 0 | 0 | 4021 | 472 |
| EMTEC | 804 | 32 | 9 | 23 | 32 | 1 | 0 | 2 | 5 | 6704 | 866 |
| Carta Worldwide | 1003 | 49 | 26 | 23 | 49 | 0 | 0 | 0 | 0 | 9574 | 1272 |
| I Talk to Strangers | 1185 | 51 | 6 | 45 | 51 | 1 | 0 | 1 | 2 | 10718 | 1317 |
| Summertime (Kenny Chesney song) | 300 | 12 | 4 | 8 | 12 | 2 | 0 | 1 | 2 | 2624 | 320 |
| Świerczyna | 597 | 23 | 20 | 3 | 23 | 0 | 0 | 9 | 16 | 10288 | 760 |
| Essex | 2669 | 112 | 42 | 70 | 109 | 5 | 0 | 22 | 37 | 24663 | 2952 |
| Twelfth siege of Gibraltar | 2331 | 93 | 35 | 58 | 93 | 3 | 0 | 5 | 11 | 21513 | 2475 |
| 2009–10 Euroleague Quarterfinals | 291 | 11 | 5 | 6 | 8 | 5 | 0 | 1 | 1 | 1926 | 270 |
| Sessions '64 | 635 | 23 | 10 | 13 | 23 | 2 | 0 | 4 | 7 | 4903 | 610 |
| United Nations Security Council Resolution 1528 | 351 | 10 | 4 | 6 | 10 | 0 | 0 | 12 | 4 | 5204 | 554 |
| Charles Armand René de La Trémoille | 216 | 9 | 5 | 4 | 9 | 0 | 0 | 2 | 4 | 2864 | 293 |
| Reg McKay | 412 | 15 | 4 | 11 | 15 | 0 | 0 | 3 | 6 | 3546 | 438 |
| Brian M. Rosenthal | 244 | 11 | 5 | 6 | 11 | 0 | 0 | 0 | 0 | 2340 | 284 |
| 2013 EAFF East Asian Cup | 327 | 11 | 4 | 7 | 11 | 1 | 0 | 5 | 7 | 2840 | 304 |
| List of anti-corruption agencies | 217 | 6 | 1 | 5 | 6 | 0 | 0 | 0 | 0 | 1372 | 157 |
| Institute of Science and Technology, West Bengal | 599 | 26 | 17 | 9 | 26 | 0 | 0 | 5 | 12 | 5903 | 692 |
| Lule–Vilela languages | 417 | 16 | 7 | 9 | 16 | 0 | 0 | 3 | 6 | 3686 | 432 |
| Leimert Park, Los Angeles | 594 | 26 | 9 | 17 | 26 | 0 | 0 | 2 | 4 | 5788 | 667 |
| Alevtina Kovalenko | 315 | 10 | 3 | 7 | 10 | 0 | 0 | 4 | 8 | 2772 | 286 |
| Magpie Brewing | 312 | 12 | 7 | 5 | 12 | 0 | 0 | 2 | 4 | 2882 | 318 |
| Canadian Telework Association | 440 | 17 | 3 | 14 | 17 | 1 | 0 | 1 | 2 | 3092 | 424 |
| Hit Man: A Technical Manual for Independent Contractors | 850 | 35 | 5 | 30 | 35 | 1 | 0 | 2 | 5 | 8049 | 907 |
| Puturosu | 337 | 19 | 10 | 9 | 3 | 0 | 0 | 0 | 0 | 4145 | 468 |
| The Goldbergs season 5 | 908 | 37 | 26 | 11 | 36 | 1 | 0 | 8 | 14 | 8966 | 1050 |
| Torstensson's Jutland campaign | 275 | 10 | 6 | 4 | 10 | 1 | 0 | 2 | 7 | 2524 | 296 |
| 72nd Locarno Film Festival | 346 | 12 | 6 | 6 | 12 | 0 | 0 | 2 | 2 | 2892 | 318 |
| Margaret Campbell (politician) | 450 | 18 | 11 | 7 | 18 | 0 | 0 | 6 | 10 | 4478 | 542 |
| Hengdian Group | 379 | 19 | 9 | 10 | 19 | 0 | 0 | 2 | 7 | 4033 | 494 |
| Elm Thicket, Dallas | 356 | 15 | 7 | 8 | 15 | 0 | 0 | 2 | 5 | 3684 | 378 |
| 10 for Slim: Charley Crockett Sings James Hand | 365 | 13 | 5 | 8 | 13 | 0 | 0 | 1 | 4 | 3314 | 373 |
| Zlata of Meglen | 828 | 35 | 23 | 12 | 35 | 1 | 0 | 7 | 16 | 10034 | 1159 |
| Ninetynine | 1030 | 45 | 15 | 30 | 45 | 1 | 0 | 3 | 7 | 9440 | 1166 |
| Mbarara district | 201 | 7 | 3 | 4 | 7 | 0 | 0 | 3 | 5 | 1772 | 197 |
| List of 3×3 Eyes volumes | 967 | 28 | 11 | 17 | 28 | 8 | 0 | 10 | 13 | 8188 | 921 |
| USS Trout (SS-202) | 1128 | 39 | 6 | 33 | 39 | 11 | 0 | 4 | 10 | 8942 | 1008 |
| Mary Browne (courtier) | 1677 | 74 | 34 | 40 | 64 | 0 | 0 | 11 | 22 | 16716 | 2004 |
| Trial by ordeal | 1359 | 56 | 6 | 50 | 56 | 0 | 0 | 3 | 6 | 12324 | 1413 |
| Słupy, Tuchola County | 370 | 17 | 9 | 8 | 17 | 1 | 0 | 2 | 4 | 3848 | 437 |
| Sámi clothing | 670 | 30 | 10 | 20 | 28 | 1 | 0 | 1 | 3 | 8490 | 841 |
| Whispers in the Dark (film) | 900 | 33 | 13 | 20 | 33 | 0 | 0 | 2 | 6 | 7596 | 874 |
| Aadhi Raat | 280 | 16 | 12 | 4 | 16 | 0 | 0 | 1 | 2 | 3334 | 411 |
| Rajbir Kaur | 235 | 7 | 4 | 3 | 7 | 0 | 0 | 3 | 5 | 1783 | 199 |
| Farmasi Arena | 768 | 27 | 12 | 15 | 27 | 2 | 0 | 6 | 9 | 6346 | 749 |
| Electronic Industries Association of Japan | 901 | 30 | 9 | 21 | 24 | 3 | 0 | 2 | 3 | 7046 | 788 |
| Dayu | 311 | 20 | 9 | 11 | 20 | 0 | 0 | 0 | 0 | 5310 | 501 |
| Genus (disambiguation) | 1034 | 49 | 7 | 42 | 49 | 0 | 0 | 0 | 0 | 15690 | 1213 |
| Raoof Haghighi | 586 | 26 | 12 | 14 | 26 | 1 | 0 | 3 | 7 | 5645 | 676 |
| Shi Jinsong | 1952 | 89 | 28 | 61 | 81 | 4 | 0 | 3 | 5 | 18572 | 2245 |
| Northern Ireland Billiards and Snooker Association | 538 | 26 | 17 | 9 | 26 | 0 | 0 | 0 | 0 | 5275 | 692 |
| National Register of Historic Places listings in Brunswick County, Virginia | 560 | 23 | 9 | 14 | 23 | 1 | 0 | 0 | 0 | 4517 | 582 |
| Eugène Marais Prize | 485 | 17 | 6 | 11 | 17 | 1 | 0 | 4 | 8 | 3877 | 459 |
| The Misfortunates | 370 | 16 | 10 | 6 | 16 | 1 | 0 | 1 | 1 | 3692 | 417 |
| Mohammed ben Abdallah | 1002 | 40 | 21 | 19 | 40 | 1 | 0 | 8 | 18 | 10810 | 1142 |
| Leuktron Castle | 866 | 39 | 11 | 28 | 37 | 0 | 0 | 5 | 7 | 8434 | 976 |
| Daddy's Roommate | 693 | 26 | 4 | 22 | 26 | 2 | 0 | 4 | 7 | 6120 | 681 |
| Giovanna Foà | 275 | 13 | 5 | 8 | 13 | 0 | 0 | 3 | 6 | 3322 | 386 |
| Bolivia–Chile border | 594 | 28 | 12 | 16 | 28 | 0 | 0 | 2 | 5 | 5498 | 697 |
| Yorkshire Dragons | 232 | 8 | 4 | 4 | 8 | 0 | 0 | 2 | 4 | 1957 | 220 |
| Magnolia Park | 640 | 42 | 32 | 10 | 42 | 0 | 0 | 1 | 4 | 13442 | 1060 |
| KIPP | 825 | 30 | 15 | 15 | 30 | 0 | 0 | 3 | 8 | 7380 | 810 |
| Abraham LeBlanc | 342 | 14 | 10 | 4 | 14 | 0 | 0 | 4 | 8 | 3266 | 414 |
| Šalinac Grove | 1113 | 47 | 11 | 36 | 47 | 1 | 0 | 7 | 8 | 11868 | 1296 |
| Juan G. Macaraeg National High School | 283 | 12 | 6 | 6 | 12 | 0 | 0 | 0 | 0 | 2438 | 302 |
| Svetlana Malahova-Shishkina | 616 | 20 | 8 | 12 | 20 | 0 | 0 | 13 | 20 | 6360 | 586 |
| Graham Lyle | 848 | 39 | 21 | 18 | 39 | 4 | 0 | 3 | 7 | 8856 | 1045 |
| Brussels tapestry | 911 | 35 | 13 | 22 | 35 | 0 | 0 | 3 | 10 | 9072 | 1037 |
| William Robertson Coe | 275 | 12 | 3 | 9 | 12 | 0 | 0 | 2 | 2 | 3314 | 389 |
| Lynching of Ed Johnson | 1769 | 68 | 19 | 49 | 68 | 4 | 0 | 6 | 11 | 14572 | 1765 |
| Tony Anthony | 471 | 16 | 9 | 7 | 16 | 1 | 0 | 3 | 3 | 4428 | 503 |
| St John the Baptist's Church, Barnack | 214 | 10 | 8 | 2 | 10 | 0 | 0 | 0 | 0 | 1968 | 241 |
| Launcher (company) | 813 | 34 | 24 | 10 | 34 | 0 | 0 | 7 | 16 | 7904 | 982 |
| Dani Balbi | 344 | 13 | 4 | 9 | 13 | 0 | 0 | 2 | 5 | 3227 | 360 |
| Striped honeyeater | 1059 | 39 | 7 | 32 | 36 | 1 | 0 | 3 | 5 | 8050 | 952 |
| The Chapters | 758 | 37 | 19 | 18 | 37 | 2 | 0 | 3 | 4 | 7978 | 977 |
| Brothers In Arms Foundation | 447 | 19 | 6 | 13 | 19 | 1 | 0 | 1 | 3 | 3922 | 486 |
| Hello Mister Zamindar | 371 | 15 | 7 | 8 | 15 | 0 | 0 | 2 | 2 | 2985 | 386 |
| Christian Steen (publisher) | 394 | 21 | 5 | 16 | 17 | 0 | 0 | 3 | 5 | 3850 | 522 |
| Grand Fenwick | 396 | 15 | 7 | 8 | 15 | 1 | 0 | 2 | 3 | 3578 | 406 |
| Gideon (play) | 230 | 12 | 4 | 8 | 12 | 0 | 0 | 2 | 3 | 2413 | 298 |
| Baken diamond mine | 752 | 32 | 9 | 23 | 32 | 15 | 0 | 8 | 16 | 8113 | 834 |
| Palizzi | 530 | 24 | 14 | 10 | 24 | 3 | 0 | 6 | 4 | 5702 | 608 |
| Give Me Some Wheels | 556 | 21 | 11 | 10 | 21 | 2 | 0 | 1 | 2 | 4684 | 557 |
| Muhammad Usman Diplai | 287 | 12 | 6 | 6 | 12 | 0 | 0 | 3 | 6 | 3200 | 390 |
| Military history of the Revolt of the Comuneros | 2254 | 96 | 31 | 65 | 96 | 3 | 0 | 6 | 18 | 21562 | 2512 |
| Ernest Daugherty House | 526 | 23 | 4 | 19 | 23 | 1 | 0 | 4 | 9 | 4978 | 569 |
| Jennifer Harmon | 427 | 15 | 5 | 10 | 15 | 1 | 0 | 5 | 7 | 3974 | 450 |
| Ohio State Route 565 | 595 | 24 | 10 | 14 | 24 | 8 | 0 | 10 | 11 | 5940 | 594 |
| 1961 South African Grand Prix | 466 | 17 | 11 | 6 | 17 | 3 | 0 | 6 | 7 | 4775 | 494 |
| Margaux Hemingway | 858 | 34 | 13 | 21 | 33 | 0 | 0 | 8 | 14 | 8021 | 988 |
| Takal | 309 | 14 | 10 | 4 | 13 | 0 | 0 | 2 | 2 | 2751 | 348 |
| Tercero, Ponce, Puerto Rico | 239 | 13 | 8 | 5 | 13 | 2 | 0 | 1 | 1 | 2388 | 304 |
| Coombsville | 343 | 12 | 3 | 9 | 12 | 0 | 0 | 1 | 2 | 2864 | 341 |
| 2026 Porsche Tennis Grand Prix | 291 | 10 | 4 | 6 | 10 | 0 | 0 | 4 | 4 | 2896 | 322 |
| Avalanche City | 421 | 18 | 11 | 7 | 18 | 3 | 0 | 4 | 9 | 4682 | 509 |
| Leon Perera | 392 | 15 | 10 | 5 | 15 | 0 | 0 | 3 | 11 | 3847 | 458 |
| Peep Show (Goudie album) | 692 | 31 | 15 | 16 | 31 | 0 | 0 | 0 | 0 | 5733 | 753 |
| Seawright | 416 | 14 | 6 | 8 | 14 | 0 | 0 | 5 | 9 | 5536 | 536 |
| Khmer traditional clothing | 499 | 18 | 2 | 16 | 18 | 0 | 0 | 2 | 4 | 4295 | 492 |
| Fireman Sam: The Great Fire of Pontypandy | 805 | 36 | 18 | 18 | 34 | 0 | 0 | 2 | 6 | 6802 | 894 |
| Pollard v. E. I. du Pont de Nemours & Co. | 435 | 15 | 6 | 9 | 15 | 0 | 0 | 2 | 5 | 4040 | 415 |
| 2009–10 Liverpool F.C. season | 1981 | 75 | 26 | 49 | 75 | 2 | 0 | 10 | 22 | 18200 | 2077 |
| Roberto Sanseverino, Prince of Salerno | 260 | 15 | 10 | 5 | 15 | 0 | 0 | 3 | 6 | 3272 | 402 |
| Doolin | 697 | 26 | 12 | 14 | 26 | 1 | 0 | 4 | 8 | 5820 | 664 |
| A Night in a Moorish Harem | 672 | 25 | 9 | 16 | 25 | 3 | 0 | 5 | 10 | 5953 | 680 |
| Miss Jalisco | 402 | 13 | 4 | 9 | 12 | 0 | 0 | 3 | 3 | 2979 | 332 |
| Democratic Regional Union | 252 | 8 | 5 | 3 | 8 | 0 | 0 | 1 | 3 | 2229 | 265 |
| Kuuk Yak language | 588 | 25 | 5 | 20 | 25 | 0 | 0 | 0 | 0 | 5218 | 612 |
| Parfums Christian Dior | 390 | 13 | 4 | 9 | 13 | 0 | 0 | 0 | 0 | 3070 | 345 |
| Elena Osipova (archer) | 664 | 27 | 18 | 9 | 27 | 2 | 0 | 6 | 14 | 7108 | 803 |
| Plantation complexes in the Southern United States | 1658 | 66 | 15 | 51 | 66 | 3 | 0 | 5 | 7 | 14888 | 1756 |
| Michael Hochberg | 241 | 10 | 2 | 8 | 10 | 0 | 0 | 1 | 2 | 2079 | 252 |
| List of African American cemeteries | 391 | 14 | 1 | 13 | 14 | 0 | 0 | 0 | 0 | 2999 | 364 |
| South Dakota's 35th legislative district | 318 | 11 | 5 | 6 | 11 | 3 | 0 | 4 | 7 | 2710 | 292 |
| Sri Surya Pahar | 2511 | 103 | 37 | 66 | 103 | 13 | 0 | 11 | 15 | 23998 | 2714 |
| Baum–Welch algorithm | 658 | 29 | 1 | 28 | 29 | 0 | 0 | 0 | 0 | 6036 | 712 |
| First Spanish Republic | 1206 | 50 | 17 | 33 | 50 | 0 | 0 | 8 | 17 | 12176 | 1462 |
| Traditional Values Coalition | 817 | 26 | 9 | 17 | 26 | 0 | 0 | 6 | 9 | 6448 | 716 |
| Internal hard drive defect management | 829 | 31 | 0 | 31 | 30 | 2 | 0 | 0 | 0 | 7122 | 774 |
| National Center for Supercomputing Applications (Bulgaria) | 1022 | 41 | 13 | 28 | 41 | 3 | 0 | 3 | 4 | 9520 | 1134 |
| Trinity Bay State High School | 1065 | 44 | 14 | 30 | 44 | 4 | 0 | 5 | 12 | 9587 | 1106 |
| Jim Meadowcroft | 1263 | 42 | 19 | 23 | 42 | 4 | 0 | 9 | 15 | 10079 | 1200 |
| Sea shepherd | 252 | 13 | 4 | 9 | 13 | 1 | 0 | 1 | 1 | 3104 | 327 |
| Johan's Ark | 326 | 15 | 5 | 10 | 15 | 0 | 0 | 1 | 1 | 3032 | 371 |
| Hold On to Your Dream | 405 | 21 | 7 | 14 | 21 | 0 | 0 | 6 | 13 | 7662 | 698 |
| Dave Elliott (gridiron football) | 417 | 19 | 12 | 7 | 19 | 0 | 0 | 4 | 8 | 4270 | 530 |
| 2024–25 FC Südtirol season | 261 | 8 | 2 | 6 | 8 | 0 | 0 | 4 | 5 | 2174 | 268 |
| Jean Laborde (journalist) | 288 | 10 | 3 | 7 | 10 | 1 | 0 | 4 | 5 | 2168 | 272 |
| Christa Prets | 559 | 30 | 19 | 11 | 30 | 0 | 0 | 1 | 4 | 6390 | 783 |
| From My Heart | 422 | 16 | 3 | 13 | 16 | 0 | 0 | 3 | 5 | 3421 | 404 |
| Tuğçe Şahutoğlu | 1310 | 39 | 14 | 25 | 39 | 5 | 0 | 12 | 21 | 9921 | 1112 |
| Love Letter to the Earth | 288 | 12 | 5 | 7 | 12 | 1 | 0 | 1 | 3 | 3007 | 310 |
| Juanita Brooks Wade | 551 | 23 | 8 | 15 | 23 | 0 | 0 | 1 | 2 | 4813 | 583 |
| 1998 Russian Second Division | 426 | 14 | 8 | 6 | 14 | 2 | 0 | 4 | 8 | 3549 | 437 |
| Lucius of Alexandria | 240 | 10 | 9 | 1 | 10 | 0 | 0 | 0 | 0 | 2391 | 271 |
| Mesh Tenney | 790 | 32 | 23 | 9 | 32 | 1 | 0 | 11 | 19 | 8019 | 912 |
| Harmonized System | 626 | 21 | 7 | 14 | 21 | 2 | 0 | 1 | 2 | 4866 | 552 |
| Appaji M. J. | 399 | 13 | 7 | 6 | 13 | 0 | 0 | 5 | 8 | 3044 | 384 |
| 2022 Bacoor local elections | 399 | 14 | 3 | 11 | 14 | 3 | 0 | 1 | 3 | 3823 | 377 |
| LBI | 508 | 21 | 15 | 6 | 21 | 0 | 0 | 0 | 0 | 6720 | 579 |
| Angélica García Arrieta | 231 | 6 | 3 | 3 | 6 | 0 | 0 | 2 | 2 | 1945 | 221 |
| Birchwood Forest Park | 376 | 18 | 10 | 8 | 18 | 2 | 0 | 5 | 10 | 4074 | 458 |
| Hopea modesta | 646 | 25 | 10 | 15 | 23 | 0 | 0 | 3 | 5 | 5546 | 657 |
| Allemand's escape from Lorient | 332 | 17 | 7 | 10 | 17 | 0 | 0 | 1 | 2 | 3182 | 417 |
| Philippe Montanier | 810 | 32 | 20 | 12 | 32 | 2 | 0 | 6 | 11 | 7239 | 864 |
| Lennox Lagu | 434 | 16 | 12 | 4 | 16 | 0 | 0 | 4 | 7 | 4017 | 487 |
| List of Italian football transfers summer 2013 (August) | 252 | 9 | 1 | 8 | 9 | 1 | 0 | 2 | 3 | 2324 | 275 |
| Description logic | 1192 | 44 | 5 | 39 | 44 | 1 | 0 | 0 | 0 | 9022 | 1114 |
| Lorch, Austria | 254 | 11 | 6 | 5 | 11 | 1 | 0 | 1 | 3 | 2060 | 268 |
| À ton image | 209 | 10 | 2 | 8 | 10 | 0 | 0 | 2 | 4 | 2371 | 260 |
| Southside Johnny and the Asbury Jukes | 1416 | 57 | 33 | 24 | 57 | 4 | 0 | 6 | 14 | 13809 | 1516 |
| Martha Kennedy | 2030 | 93 | 37 | 56 | 89 | 1 | 0 | 10 | 21 | 20918 | 2460 |
| John Balliol (disambiguation) | 268 | 17 | 11 | 6 | 17 | 0 | 0 | 2 | 6 | 3566 | 442 |
| Illya Woloshyn | 601 | 27 | 9 | 18 | 27 | 0 | 0 | 5 | 9 | 6496 | 718 |
| Two Wells, South Australia | 346 | 14 | 5 | 9 | 14 | 3 | 0 | 6 | 8 | 3705 | 359 |
| Digital Champions | 867 | 32 | 7 | 25 | 32 | 0 | 0 | 0 | 0 | 6499 | 816 |
| Hainshallig | 479 | 22 | 10 | 12 | 22 | 0 | 0 | 3 | 5 | 4616 | 553 |
| Muzinga FC | 286 | 13 | 4 | 9 | 13 | 1 | 0 | 1 | 1 | 2578 | 322 |
| Basil Spalding de Garmendia | 402 | 15 | 9 | 6 | 15 | 0 | 0 | 4 | 5 | 3648 | 427 |
| René Grousset | 535 | 17 | 6 | 11 | 17 | 2 | 0 | 2 | 2 | 5010 | 547 |
| Southern Indiana Screaming Eagles baseball | 301 | 8 | 5 | 3 | 8 | 0 | 0 | 0 | 0 | 1888 | 232 |
| Maya Petika | 234 | 6 | 3 | 3 | 4 | 0 | 0 | 1 | 2 | 1406 | 158 |
| Andong No clan | 538 | 31 | 11 | 20 | 31 | 0 | 0 | 4 | 8 | 5795 | 750 |
| Elda Cividino | 341 | 11 | 7 | 4 | 11 | 1 | 0 | 6 | 6 | 3200 | 378 |
| Ambodivoara | 592 | 28 | 4 | 24 | 28 | 2 | 0 | 4 | 11 | 5566 | 679 |
| Sherpa Light | 503 | 21 | 5 | 16 | 21 | 2 | 0 | 1 | 2 | 4413 | 526 |
| Anna Ciundziewicka | 220 | 9 | 4 | 5 | 9 | 0 | 0 | 2 | 3 | 2282 | 269 |
| 97 B-Line | 951 | 33 | 13 | 20 | 33 | 3 | 0 | 8 | 14 | 8480 | 942 |
| Boy Erased | 1152 | 42 | 19 | 23 | 42 | 1 | 0 | 5 | 9 | 9888 | 1127 |
| After Doomsday | 236 | 7 | 4 | 3 | 7 | 0 | 0 | 4 | 4 | 1944 | 228 |
| LaFayette Duckett | 295 | 8 | 5 | 3 | 8 | 0 | 0 | 5 | 6 | 2132 | 253 |
| Sarkal kassar | 387 | 21 | 10 | 11 | 21 | 2 | 0 | 1 | 2 | 4202 | 528 |
| Marina Kolomiets | 313 | 13 | 9 | 4 | 13 | 2 | 0 | 1 | 1 | 2842 | 338 |
| My Culture | 486 | 26 | 11 | 15 | 26 | 4 | 0 | 3 | 7 | 5718 | 673 |
| Carex albolutescens | 255 | 13 | 2 | 11 | 13 | 0 | 0 | 0 | 0 | 2473 | 309 |
| Step by Step (Eddie Rabbitt song) | 428 | 16 | 6 | 10 | 16 | 2 | 0 | 3 | 4 | 3431 | 419 |
| Scaevola thesioides | 269 | 10 | 2 | 8 | 10 | 0 | 0 | 1 | 2 | 2052 | 241 |
| Tivoli Enterprises | 645 | 22 | 13 | 9 | 18 | 1 | 0 | 0 | 0 | 4194 | 572 |
| List of populated places in Chandel district | 358 | 20 | 5 | 15 | 20 | 6 | 0 | 1 | 3 | 4137 | 490 |
| Shahrak-e Danshegah Valiasr | 276 | 13 | 7 | 6 | 13 | 1 | 0 | 1 | 2 | 3466 | 371 |
| Alpha helix | 554 | 21 | 0 | 21 | 21 | 0 | 0 | 0 | 0 | 4533 | 512 |
| Iryna Khliustava | 256 | 9 | 5 | 4 | 9 | 0 | 0 | 5 | 6 | 3322 | 335 |
| Paula González Berodia | 680 | 22 | 8 | 14 | 22 | 5 | 0 | 11 | 15 | 6155 | 638 |
| 1983 Detroit Grand Prix | 222 | 8 | 5 | 3 | 8 | 2 | 0 | 3 | 5 | 2214 | 233 |
| Sarah Hughes (journalist) | 1053 | 44 | 16 | 28 | 44 | 1 | 0 | 3 | 4 | 9894 | 1164 |
| Snake scale | 1502 | 75 | 2 | 73 | 75 | 2 | 0 | 1 | 2 | 14328 | 1793 |
| Carleton S. Coon | 3558 | 138 | 55 | 83 | 138 | 3 | 0 | 11 | 25 | 30563 | 3656 |
| Yes I Can (song) | 214 | 6 | 5 | 1 | 6 | 0 | 0 | 0 | 0 | 1148 | 151 |
| Machulishchy (air base) | 1457 | 56 | 26 | 30 | 54 | 4 | 2 | 5 | 9 | 12554 | 1577 |
| Trichoteras | 1119 | 36 | 10 | 26 | 29 | 2 | 0 | 3 | 8 | 9322 | 973 |
| Michael Marrak | 356 | 15 | 5 | 10 | 15 | 1 | 0 | 1 | 3 | 3315 | 410 |
| Madras Vathiyar | 229 | 8 | 4 | 4 | 6 | 0 | 0 | 1 | 3 | 1672 | 199 |
| Brent Pope (rugby analyst) | 483 | 24 | 7 | 17 | 24 | 0 | 0 | 1 | 2 | 5688 | 647 |
| Indira Krishnan | 657 | 25 | 19 | 6 | 23 | 0 | 0 | 16 | 22 | 12190 | 1113 |
| Michel Mirowski | 420 | 13 | 10 | 3 | 13 | 0 | 0 | 2 | 2 | 3060 | 388 |
| Janet Morgan Riggs | 385 | 17 | 3 | 14 | 17 | 1 | 0 | 3 | 8 | 4052 | 455 |
| Tennessee v. Garner | 806 | 34 | 6 | 28 | 34 | 1 | 0 | 1 | 3 | 8594 | 870 |
| Tommy Yarr | 741 | 29 | 19 | 10 | 26 | 0 | 0 | 9 | 15 | 7426 | 864 |
| Oktyabrsky, Chunsky District, Irkutsk Oblast | 211 | 11 | 2 | 9 | 7 | 0 | 0 | 3 | 4 | 2611 | 298 |
| Abdul Fatah Haqqani | 383 | 15 | 8 | 7 | 15 | 0 | 0 | 2 | 5 | 3623 | 442 |
| Collinsia multicolor | 450 | 17 | 5 | 12 | 17 | 1 | 0 | 2 | 4 | 3754 | 430 |
| Harakat al-Qiyam | 898 | 33 | 19 | 14 | 33 | 1 | 0 | 2 | 4 | 7314 | 890 |
| Morton Lochs | 1015 | 44 | 19 | 25 | 44 | 4 | 0 | 3 | 4 | 9442 | 1096 |
| 1952 Icelandic presidential election | 579 | 22 | 7 | 15 | 22 | 1 | 0 | 3 | 9 | 5252 | 590 |
| Sanford Garelik | 547 | 20 | 13 | 7 | 20 | 0 | 0 | 5 | 5 | 4838 | 624 |
| Tennessee State Route 332 | 430 | 21 | 13 | 8 | 21 | 3 | 0 | 4 | 7 | 4250 | 506 |
| Gianluca Lazzi | 1330 | 53 | 38 | 15 | 52 | 0 | 0 | 11 | 25 | 13194 | 1578 |
| People's Pledge (United States) | 1722 | 69 | 20 | 49 | 69 | 2 | 0 | 10 | 22 | 17365 | 1951 |
| Isaac Brown | 630 | 23 | 14 | 9 | 23 | 0 | 0 | 3 | 8 | 10022 | 849 |
| Moulton, Suffolk | 790 | 32 | 18 | 14 | 32 | 2 | 0 | 7 | 14 | 7668 | 882 |
| Uttar Pradesh Police | 1107 | 48 | 26 | 22 | 48 | 4 | 0 | 2 | 6 | 10879 | 1294 |
| Carla Cunningham | 333 | 11 | 6 | 5 | 11 | 0 | 0 | 4 | 7 | 2693 | 315 |
| Tim Hardaway Jr. | 1582 | 49 | 23 | 26 | 49 | 6 | 0 | 6 | 12 | 12962 | 1440 |
| P. Gopinathan Nair | 679 | 24 | 12 | 12 | 24 | 0 | 0 | 4 | 7 | 6038 | 692 |
| Jeremy Hayward | 617 | 23 | 12 | 11 | 23 | 2 | 0 | 2 | 4 | 4868 | 609 |
| New York (U2 song) | 356 | 12 | 5 | 7 | 12 | 0 | 0 | 2 | 3 | 2733 | 324 |
| Mark I & II | 640 | 27 | 15 | 12 | 27 | 1 | 0 | 3 | 9 | 6077 | 694 |
| Through My Teeth | 295 | 11 | 2 | 9 | 11 | 2 | 0 | 1 | 2 | 2208 | 278 |
| 1366 Piccolo | 368 | 16 | 6 | 10 | 16 | 0 | 0 | 4 | 8 | 3961 | 444 |
| Masaaki Kukino | 709 | 28 | 16 | 12 | 28 | 0 | 0 | 1 | 2 | 5390 | 713 |
| Madugula | 520 | 22 | 12 | 10 | 22 | 0 | 0 | 2 | 4 | 4540 | 577 |
| Križevci Cathedral | 204 | 10 | 5 | 5 | 10 | 0 | 0 | 0 | 0 | 2112 | 256 |
| Bucciano | 239 | 10 | 6 | 4 | 10 | 0 | 0 | 6 | 5 | 2787 | 244 |
| Basudeb Dasgupta (physicist) | 946 | 39 | 17 | 22 | 39 | 1 | 0 | 6 | 14 | 9331 | 1111 |
| French ship Ville de Bordeaux (1860) | 409 | 12 | 4 | 8 | 12 | 2 | 0 | 4 | 7 | 3521 | 344 |
| MGED | 219 | 8 | 1 | 7 | 5 | 0 | 0 | 0 | 0 | 1741 | 205 |
| J. J. Moser | 246 | 9 | 4 | 5 | 9 | 0 | 0 | 2 | 4 | 2395 | 264 |
| 2023 Nigerian Senate elections in Rivers State | 447 | 14 | 5 | 9 | 14 | 3 | 0 | 4 | 5 | 3734 | 446 |
| HAMLET (protein complex) | 1793 | 68 | 11 | 57 | 68 | 1 | 0 | 3 | 8 | 15921 | 1822 |
| Philip Nehri Mullegama | 507 | 17 | 3 | 14 | 17 | 0 | 0 | 0 | 0 | 4055 | 454 |
| Elections in the United States | 3518 | 121 | 17 | 104 | 112 | 2 | 0 | 15 | 22 | 29782 | 3338 |
| The Harvey School | 214 | 8 | 5 | 3 | 8 | 1 | 0 | 3 | 2 | 1940 | 212 |
| Times Radio | 328 | 12 | 10 | 2 | 12 | 0 | 0 | 3 | 7 | 2930 | 353 |
| HDMS Grønland | 414 | 16 | 5 | 11 | 16 | 0 | 0 | 3 | 6 | 3639 | 424 |
| South Side, Chicago | 1706 | 67 | 25 | 42 | 54 | 6 | 0 | 12 | 24 | 15900 | 1724 |
| Octacube (sculpture) | 781 | 32 | 8 | 24 | 31 | 1 | 0 | 0 | 0 | 6611 | 822 |
| Bhavani Junction | 248 | 10 | 7 | 3 | 10 | 0 | 0 | 2 | 3 | 2189 | 273 |
| Gustav Weymer | 277 | 12 | 6 | 6 | 12 | 1 | 0 | 1 | 2 | 2388 | 313 |
| IWRG Máscara vs. Cabellera (August 2016) | 1342 | 57 | 22 | 35 | 57 | 2 | 0 | 3 | 9 | 13835 | 1588 |
| Stephen Rozgonyi | 299 | 14 | 9 | 5 | 14 | 1 | 0 | 3 | 8 | 3061 | 385 |
| Manuel Inocêncio Sousa | 207 | 10 | 3 | 7 | 10 | 0 | 0 | 3 | 7 | 2474 | 273 |
| Bjørn Tore Bryn | 534 | 17 | 9 | 8 | 17 | 0 | 0 | 5 | 9 | 4212 | 475 |
| Loyola University School of Law | 237 | 9 | 7 | 2 | 9 | 2 | 0 | 0 | 0 | 2132 | 236 |
| Mark Atkinson | 392 | 15 | 8 | 7 | 15 | 0 | 0 | 5 | 11 | 6016 | 531 |
| Hasoo Balel | 358 | 19 | 10 | 9 | 19 | 0 | 0 | 0 | 0 | 3850 | 480 |
| Hickory Grove (Romney, West Virginia) | 466 | 16 | 7 | 9 | 16 | 1 | 0 | 5 | 9 | 3900 | 431 |
| Khoy Khanate | 728 | 27 | 11 | 16 | 25 | 1 | 0 | 4 | 7 | 7189 | 791 |
| Patrick Vallance | 1174 | 48 | 13 | 35 | 48 | 0 | 0 | 10 | 22 | 12129 | 1423 |
| Ginger: The Life and Death of Albert Goodwin | 1095 | 52 | 19 | 33 | 51 | 0 | 0 | 3 | 8 | 11576 | 1352 |
| Vietnamese people in Taiwan | 730 | 32 | 15 | 17 | 28 | 5 | 0 | 4 | 9 | 7128 | 822 |
| House of Love (Amy Grant song) | 436 | 18 | 13 | 5 | 18 | 0 | 0 | 2 | 6 | 4432 | 515 |
| Pakistan Forward Bloc | 988 | 40 | 24 | 16 | 40 | 1 | 0 | 3 | 6 | 8695 | 1087 |
| Bottineau County, North Dakota | 827 | 35 | 12 | 23 | 35 | 1 | 0 | 9 | 16 | 7424 | 890 |
| Duncan House, Castlecrag | 292 | 8 | 6 | 2 | 8 | 2 | 0 | 2 | 2 | 1858 | 216 |
| Meade County High School | 850 | 25 | 14 | 11 | 25 | 0 | 0 | 6 | 8 | 5686 | 671 |
| Bob Armstrong (basketball, born 1933) | 315 | 10 | 7 | 3 | 10 | 1 | 0 | 3 | 3 | 2291 | 286 |
| Wang Xibang | 408 | 26 | 12 | 14 | 26 | 0 | 0 | 1 | 4 | 5291 | 654 |
| Masjid al-Qiblatayn, Zeila | 356 | 18 | 8 | 10 | 18 | 1 | 0 | 0 | 0 | 4606 | 478 |
| Interstate 271 | 275 | 12 | 6 | 6 | 12 | 1 | 0 | 1 | 2 | 2337 | 292 |
| Salim Kandi | 270 | 12 | 7 | 5 | 12 | 1 | 0 | 2 | 3 | 3014 | 324 |
| Nam Su-hyeon | 426 | 15 | 5 | 10 | 15 | 1 | 0 | 2 | 4 | 3688 | 395 |
| Musallam bin Nufl | 1889 | 62 | 30 | 32 | 59 | 1 | 0 | 9 | 20 | 16826 | 1781 |
| Chic discography | 500 | 17 | 6 | 11 | 17 | 0 | 0 | 6 | 14 | 4330 | 502 |
| FOG-MPM | 435 | 17 | 10 | 7 | 17 | 1 | 0 | 2 | 3 | 3814 | 442 |
| Thompson & Odell | 436 | 21 | 10 | 11 | 21 | 1 | 0 | 1 | 3 | 4176 | 544 |
| King Estate Winery | 1143 | 48 | 14 | 34 | 48 | 3 | 0 | 9 | 23 | 11679 | 1260 |
| FAPL (disambiguation) | 257 | 10 | 6 | 4 | 10 | 0 | 0 | 1 | 3 | 2850 | 276 |
| Stephen Lissenburgh | 388 | 12 | 3 | 9 | 12 | 1 | 0 | 3 | 5 | 3229 | 362 |
| Thubana heylaertsi | 292 | 14 | 3 | 11 | 14 | 0 | 0 | 2 | 4 | 2615 | 332 |
| Temple Challenge Cup | 641 | 30 | 7 | 23 | 30 | 3 | 0 | 0 | 0 | 5837 | 724 |
| Arnot coal mine | 324 | 17 | 9 | 8 | 17 | 4 | 0 | 0 | 0 | 3296 | 438 |
| Ust-Khopyorskaya | 252 | 12 | 5 | 7 | 12 | 1 | 0 | 1 | 2 | 2915 | 317 |
| Thérèse Étienne | 357 | 15 | 10 | 5 | 15 | 1 | 0 | 1 | 2 | 3339 | 402 |
| Bunny Oakes | 366 | 14 | 9 | 5 | 14 | 0 | 0 | 2 | 2 | 3692 | 450 |
| Battle of Hipp's Point (1856) | 566 | 22 | 9 | 13 | 22 | 0 | 0 | 1 | 2 | 5858 | 644 |
| Carboxypeptidase B2 | 214 | 11 | 3 | 8 | 11 | 0 | 0 | 0 | 0 | 2332 | 268 |
| List of deadpan comedians | 367 | 15 | 1 | 14 | 15 | 0 | 0 | 0 | 0 | 2772 | 356 |
| Simdega district | 419 | 16 | 5 | 11 | 16 | 2 | 0 | 2 | 6 | 3687 | 416 |
| Voltage-gated sodium channel | 340 | 13 | 0 | 13 | 13 | 0 | 0 | 0 | 0 | 2933 | 318 |
| David Ledesma Vásquez | 311 | 6 | 1 | 5 | 6 | 0 | 0 | 4 | 5 | 2044 | 231 |
| Kfar Yassine | 400 | 16 | 7 | 9 | 16 | 0 | 0 | 4 | 6 | 3704 | 410 |
| Dipromisto | 853 | 36 | 12 | 24 | 36 | 1 | 0 | 1 | 2 | 7288 | 919 |
| Canadia spinosa | 559 | 21 | 8 | 13 | 21 | 4 | 0 | 3 | 8 | 4548 | 526 |
| Eastern Air Lines Shuttle | 576 | 21 | 7 | 14 | 21 | 0 | 0 | 3 | 7 | 4548 | 545 |
| Former island | 491 | 24 | 9 | 15 | 24 | 0 | 0 | 2 | 4 | 4639 | 597 |
| Military medicine | 2054 | 73 | 5 | 68 | 62 | 1 | 0 | 1 | 2 | 15855 | 1954 |
| Carl Ecke | 665 | 29 | 19 | 10 | 14 | 0 | 0 | 14 | 26 | 6584 | 774 |
| The Fat Controller | 1403 | 59 | 23 | 36 | 59 | 6 | 0 | 5 | 12 | 13525 | 1560 |
| We Are Pirates Tour | 540 | 19 | 7 | 12 | 19 | 1 | 0 | 4 | 8 | 4609 | 510 |
| Channel Umptee-3 | 616 | 21 | 6 | 15 | 21 | 0 | 0 | 6 | 8 | 5200 | 622 |
| Barteliai (Varėna) | 228 | 12 | 3 | 9 | 12 | 1 | 0 | 2 | 4 | 2496 | 306 |
| Kaori Fujima | 203 | 7 | 4 | 3 | 7 | 0 | 0 | 2 | 6 | 1914 | 209 |
| Yim Jung-hyun | 234 | 6 | 3 | 3 | 6 | 1 | 0 | 5 | 5 | 1730 | 176 |
| Amendments to the Rome Statute | 1195 | 45 | 8 | 37 | 45 | 7 | 0 | 4 | 11 | 10677 | 1234 |
| Pogledi (disambiguation) | 268 | 13 | 2 | 11 | 13 | 1 | 0 | 1 | 2 | 3503 | 395 |
| Inge Paulsen | 252 | 11 | 6 | 5 | 11 | 2 | 0 | 3 | 6 | 2425 | 317 |
| The Korea Daily News | 1097 | 42 | 17 | 25 | 42 | 2 | 0 | 6 | 14 | 9786 | 1146 |
| 2014 Montana Senate election | 518 | 18 | 9 | 9 | 18 | 3 | 0 | 3 | 6 | 4115 | 511 |
| Manebhanjyang, Darjeeling | 2521 | 96 | 26 | 70 | 96 | 7 | 0 | 8 | 20 | 21977 | 2505 |
| Vicente López y Planes | 253 | 8 | 4 | 4 | 8 | 0 | 0 | 3 | 8 | 2324 | 304 |
| Napier baronets of Merrion Square (1867) | 219 | 10 | 5 | 5 | 10 | 0 | 0 | 1 | 4 | 2542 | 283 |
| Vibha Galhotra | 431 | 22 | 4 | 18 | 22 | 1 | 0 | 1 | 2 | 4093 | 538 |
| Rob Roos | 248 | 10 | 7 | 3 | 10 | 0 | 0 | 4 | 8 | 2685 | 328 |
| The Queen's Award for Enterprise: Innovation (2016) | 374 | 12 | 5 | 7 | 12 | 1 | 0 | 3 | 8 | 3324 | 349 |
| 1992–93 DFB-Pokal Frauen | 310 | 10 | 3 | 7 | 10 | 0 | 0 | 2 | 5 | 2587 | 290 |
| Kamal al-Din Isfahani | 359 | 15 | 5 | 10 | 15 | 0 | 0 | 0 | 0 | 3335 | 410 |
| The Trials of Galileo | 527 | 24 | 13 | 11 | 24 | 0 | 0 | 4 | 8 | 5760 | 689 |
| Friedrich Schwarz | 253 | 13 | 7 | 6 | 13 | 1 | 0 | 1 | 3 | 2615 | 328 |
| Ameer Idreis | 1137 | 53 | 24 | 29 | 53 | 1 | 0 | 3 | 9 | 12612 | 1457 |
| North Guardian Glacier | 664 | 14 | 8 | 6 | 14 | 1 | 0 | 12 | 14 | 4144 | 411 |
| 2018 Icelandic Men's Football League Cup | 469 | 16 | 7 | 9 | 16 | 4 | 0 | 4 | 5 | 4349 | 461 |
| Diocese of Arlington | 469 | 22 | 11 | 11 | 22 | 0 | 0 | 1 | 4 | 4428 | 562 |
| Dave Albright | 454 | 15 | 9 | 6 | 15 | 3 | 0 | 3 | 6 | 3837 | 465 |
| Mapping controversies | 647 | 27 | 1 | 26 | 27 | 0 | 0 | 0 | 0 | 5290 | 664 |
| Dialogue of Civilizations | 764 | 36 | 10 | 26 | 36 | 0 | 0 | 2 | 6 | 7685 | 893 |
| Gerald McClellan | 978 | 34 | 15 | 19 | 34 | 2 | 0 | 6 | 11 | 8740 | 931 |
| EmuParadise | 584 | 25 | 2 | 23 | 25 | 1 | 0 | 2 | 5 | 5236 | 648 |
| Bongaigaon | 535 | 23 | 11 | 12 | 21 | 0 | 0 | 2 | 5 | 5144 | 599 |
| Marija Krucifiksa Kozulić | 575 | 22 | 13 | 9 | 19 | 0 | 0 | 4 | 6 | 5407 | 662 |
| LBJ (disambiguation) | 990 | 38 | 21 | 17 | 35 | 0 | 0 | 6 | 9 | 15050 | 1462 |
| Sheila Florance | 842 | 34 | 10 | 24 | 34 | 1 | 0 | 7 | 11 | 7692 | 926 |
| Shailendra Singh (producer) | 609 | 24 | 10 | 14 | 24 | 1 | 0 | 1 | 2 | 5625 | 646 |
| Born a King | 230 | 12 | 7 | 5 | 12 | 0 | 0 | 1 | 2 | 2527 | 316 |
| Erasmus Quellinus the Elder | 326 | 15 | 4 | 11 | 9 | 0 | 0 | 2 | 3 | 3257 | 406 |
| On the House | 284 | 15 | 9 | 6 | 10 | 0 | 0 | 0 | 0 | 2922 | 380 |
| Moonlighter (video game) | 752 | 25 | 11 | 14 | 25 | 2 | 0 | 9 | 15 | 6216 | 750 |
| 1970 Queen's Club Championships – Men's singles | 222 | 7 | 3 | 4 | 7 | 0 | 0 | 2 | 4 | 1872 | 197 |
| Dwaine O. Cowan | 420 | 17 | 3 | 14 | 17 | 0 | 0 | 2 | 2 | 3633 | 445 |
| Enrique Collazo | 801 | 30 | 13 | 17 | 30 | 3 | 0 | 5 | 14 | 7387 | 836 |
| Just Blaze production discography | 223 | 12 | 3 | 9 | 12 | 0 | 0 | 1 | 4 | 2388 | 290 |
| Compania de Transport Public Cluj-Napoca | 444 | 16 | 11 | 5 | 16 | 0 | 0 | 3 | 7 | 4596 | 472 |
| James Higgins | 755 | 27 | 14 | 13 | 27 | 0 | 0 | 2 | 8 | 12751 | 1095 |
| Sartre's Sink | 1840 | 85 | 35 | 50 | 85 | 1 | 0 | 1 | 2 | 18791 | 2165 |
| Pallewela (Uva Paranagama) Grama Niladhari Division | 332 | 8 | 8 | 0 | 8 | 0 | 0 | 0 | 0 | 2386 | 262 |
| Chicago Live! | 417 | 14 | 6 | 8 | 14 | 0 | 0 | 4 | 3 | 3849 | 443 |
| Apache fiddle | 658 | 29 | 8 | 21 | 29 | 1 | 0 | 2 | 3 | 6205 | 731 |
| Junior Rasolea | 734 | 21 | 12 | 9 | 21 | 0 | 0 | 6 | 10 | 5531 | 626 |
| Dil Sambhal Jaa Zara | 288 | 12 | 5 | 7 | 10 | 0 | 0 | 2 | 3 | 2592 | 321 |
| Telephony application server | 2354 | 83 | 8 | 75 | 83 | 4 | 0 | 2 | 6 | 18589 | 2161 |
| Jane den Hollander | 268 | 10 | 7 | 3 | 10 | 0 | 0 | 0 | 0 | 1939 | 264 |
| 94.3 Club FM | 592 | 30 | 16 | 14 | 30 | 5 | 0 | 2 | 3 | 6030 | 802 |
| Odd Karsten Tveit | 444 | 18 | 8 | 10 | 18 | 2 | 0 | 6 | 9 | 4355 | 518 |
| 1895 Alabama Crimson White football team | 1023 | 48 | 28 | 20 | 48 | 3 | 0 | 8 | 17 | 10804 | 1336 |
| Honda G4 transmission | 282 | 12 | 7 | 5 | 6 | 1 | 0 | 2 | 5 | 2715 | 326 |
| Kotulin | 241 | 14 | 9 | 5 | 14 | 0 | 0 | 0 | 0 | 3266 | 358 |
| Friedman test | 1323 | 44 | 3 | 41 | 44 | 2 | 0 | 0 | 0 | 9553 | 1128 |
| Byelorussian Soviet Socialist Republic | 2851 | 99 | 49 | 50 | 99 | 6 | 0 | 23 | 38 | 27201 | 2979 |
| Jo Elizabeth Bryant | 302 | 10 | 5 | 5 | 10 | 0 | 0 | 5 | 8 | 2702 | 301 |
| Westland 30 | 1882 | 64 | 22 | 42 | 64 | 5 | 0 | 7 | 15 | 15405 | 1764 |
| Ōtira River | 473 | 18 | 10 | 8 | 18 | 1 | 0 | 7 | 7 | 4369 | 456 |
| Bloudkova velikanka | 917 | 34 | 10 | 24 | 34 | 1 | 0 | 10 | 17 | 8126 | 900 |
| John C. Young | 886 | 32 | 19 | 13 | 32 | 1 | 0 | 4 | 10 | 8660 | 971 |
| Chapelton, South Lanarkshire | 278 | 14 | 4 | 10 | 14 | 0 | 0 | 2 | 4 | 2681 | 337 |
| 2022 WTA Argentina Open | 302 | 10 | 3 | 7 | 10 | 0 | 0 | 3 | 5 | 2528 | 300 |
| Cockle Creek (Tasmania) | 746 | 32 | 11 | 21 | 32 | 1 | 0 | 2 | 5 | 6938 | 815 |
| 2019 Mediterranean Athletics U23 Indoor Championships | 220 | 8 | 2 | 6 | 8 | 1 | 0 | 2 | 4 | 1926 | 226 |
| Clay Scofield | 463 | 21 | 6 | 15 | 21 | 0 | 0 | 3 | 5 | 4227 | 563 |
| Sickert | 237 | 11 | 6 | 5 | 11 | 0 | 0 | 1 | 2 | 2803 | 280 |
| Robert Dobbie | 894 | 43 | 27 | 16 | 43 | 1 | 0 | 1 | 3 | 8834 | 1158 |
| Bierzyński | 541 | 25 | 13 | 12 | 20 | 0 | 0 | 4 | 8 | 5982 | 718 |
| Belludi Mutt, Harihar | 645 | 26 | 14 | 12 | 26 | 0 | 0 | 1 | 3 | 5877 | 695 |
| Polytechnic University of the Philippines Ragay | 359 | 17 | 11 | 6 | 17 | 0 | 0 | 0 | 0 | 3848 | 437 |
| Southshore, New Zealand | 1872 | 70 | 15 | 55 | 70 | 3 | 0 | 13 | 13 | 16328 | 1858 |
| Mark Tapio Kines | 255 | 13 | 5 | 8 | 13 | 0 | 0 | 1 | 4 | 2696 | 325 |
| Chisi Island | 982 | 44 | 18 | 26 | 44 | 5 | 0 | 2 | 4 | 8179 | 1070 |
| Helen Clayton | 334 | 11 | 8 | 3 | 11 | 2 | 0 | 3 | 3 | 2796 | 320 |
| Borden Dairy | 634 | 27 | 13 | 14 | 27 | 1 | 0 | 4 | 10 | 6164 | 772 |
| Tibet | 3047 | 135 | 47 | 88 | 135 | 6 | 0 | 19 | 42 | 30344 | 3650 |
| Cambar | 275 | 12 | 6 | 6 | 12 | 0 | 0 | 1 | 3 | 2450 | 301 |
| 2000 Coppa Italia final | 216 | 8 | 3 | 5 | 8 | 2 | 0 | 1 | 1 | 1592 | 203 |
| Naoto Arai | 343 | 15 | 9 | 6 | 15 | 0 | 0 | 1 | 4 | 3422 | 408 |
| Dərəkərkənc | 272 | 15 | 8 | 7 | 15 | 0 | 0 | 0 | 0 | 3153 | 396 |
| Say Somethin' (Mariah Carey song) | 1588 | 69 | 26 | 43 | 69 | 3 | 0 | 0 | 0 | 14147 | 1737 |
| 1999 Women's World Open Squash Championship | 338 | 13 | 6 | 7 | 13 | 1 | 0 | 3 | 5 | 3248 | 370 |
| Mr. Fox (novel) | 764 | 24 | 10 | 14 | 24 | 1 | 0 | 1 | 2 | 4619 | 586 |
| Bodycam (film) | 221 | 9 | 6 | 3 | 9 | 0 | 0 | 1 | 2 | 2008 | 242 |
| Zanoterone | 1328 | 45 | 6 | 39 | 45 | 4 | 0 | 3 | 9 | 10516 | 1261 |
| Rima vestibuli | 397 | 16 | 1 | 15 | 16 | 0 | 0 | 0 | 0 | 3326 | 390 |
| Winnetou and Old Firehand | 680 | 32 | 18 | 14 | 32 | 1 | 0 | 3 | 8 | 6835 | 826 |
| Emily Adams | 393 | 19 | 10 | 9 | 19 | 1 | 0 | 0 | 0 | 3633 | 479 |
| Dick Turner (footballer) | 281 | 10 | 5 | 5 | 10 | 1 | 0 | 3 | 6 | 2389 | 286 |
| Toiling Congress of Ukraine | 588 | 27 | 15 | 12 | 27 | 1 | 0 | 3 | 5 | 6372 | 775 |
| Amanirenas | 577 | 26 | 11 | 15 | 24 | 0 | 0 | 1 | 3 | 5139 | 660 |
| Laurels Are Poison | 525 | 20 | 8 | 12 | 20 | 0 | 0 | 2 | 5 | 4306 | 527 |
| Paratelmatobius gaigeae | 387 | 16 | 6 | 10 | 16 | 0 | 0 | 1 | 2 | 3195 | 398 |
| William Ockler | 232 | 8 | 4 | 4 | 8 | 0 | 0 | 3 | 3 | 2059 | 254 |
| Piscola | 545 | 23 | 6 | 17 | 23 | 0 | 0 | 3 | 2 | 4385 | 555 |
| New South Wales Shale and Oil Company | 402 | 15 | 6 | 9 | 14 | 1 | 0 | 3 | 5 | 3712 | 415 |
| Oyster Bay Wind Power Station | 409 | 14 | 7 | 7 | 14 | 0 | 0 | 3 | 5 | 3650 | 403 |
| Democratic Party of Albania | 1526 | 57 | 23 | 34 | 57 | 3 | 0 | 11 | 15 | 15159 | 1625 |
| Janneke Raaijmakers | 1357 | 61 | 18 | 43 | 61 | 3 | 0 | 8 | 20 | 14870 | 1749 |
| Sergi Oliva | 314 | 13 | 8 | 5 | 13 | 0 | 0 | 1 | 3 | 3388 | 365 |
| The Voice Kids (Russian TV series) season 1 | 349 | 14 | 6 | 8 | 14 | 1 | 0 | 3 | 6 | 3188 | 403 |
| Order of Military Merit (Yugoslavia) | 497 | 21 | 7 | 14 | 21 | 1 | 0 | 0 | 0 | 5310 | 558 |
| Calgary Forest Lawn | 819 | 30 | 15 | 15 | 30 | 1 | 0 | 8 | 13 | 7461 | 847 |
| Elleine Smith | 242 | 9 | 5 | 4 | 9 | 1 | 0 | 1 | 2 | 1997 | 233 |
| Mary L. G. Carus-Wilson | 757 | 36 | 15 | 21 | 36 | 0 | 0 | 3 | 10 | 8973 | 988 |
| O'Neil Spencer | 1060 | 40 | 7 | 33 | 34 | 1 | 0 | 12 | 22 | 9494 | 1087 |
| HD 190647 | 1269 | 44 | 8 | 36 | 44 | 6 | 0 | 5 | 9 | 9418 | 1126 |
| Brooker v Police | 753 | 33 | 8 | 25 | 33 | 2 | 0 | 2 | 5 | 7973 | 873 |
| List of national emergencies in the United States | 416 | 12 | 2 | 10 | 12 | 2 | 0 | 3 | 6 | 2794 | 326 |
| Cycles per instruction | 306 | 18 | 0 | 18 | 18 | 2 | 0 | 0 | 0 | 3586 | 417 |
| Potoooooooo | 399 | 16 | 3 | 13 | 16 | 1 | 0 | 3 | 5 | 4007 | 465 |
| The Diplomatic Corpse (film) | 240 | 9 | 7 | 2 | 9 | 0 | 0 | 1 | 2 | 2088 | 244 |
| Henry the Fowler | 2546 | 122 | 41 | 81 | 122 | 1 | 0 | 9 | 24 | 26055 | 3089 |
| Western screech owl | 218 | 8 | 2 | 6 | 8 | 0 | 0 | 1 | 2 | 1854 | 209 |
| Van Fleet Hall | 574 | 23 | 17 | 6 | 23 | 0 | 0 | 2 | 3 | 5642 | 657 |
| National Register of Historic Places listings in Hartford, Connecticut | 1154 | 47 | 17 | 30 | 47 | 9 | 0 | 2 | 4 | 10198 | 1200 |
| Wyoming State Auditor | 605 | 22 | 7 | 15 | 22 | 0 | 0 | 3 | 7 | 4830 | 589 |
| Henry Roberts Williams | 867 | 33 | 18 | 15 | 33 | 1 | 0 | 15 | 24 | 8033 | 916 |
| Charlie Davies | 802 | 23 | 9 | 14 | 23 | 3 | 0 | 5 | 10 | 6162 | 699 |
| Black Heart Saints | 226 | 8 | 6 | 2 | 8 | 0 | 0 | 2 | 3 | 1919 | 221 |
| 2015 Howard Bison football team | 409 | 19 | 10 | 9 | 19 | 0 | 0 | 3 | 4 | 4664 | 548 |
| Akshara Brahma Yoga | 265 | 13 | 5 | 8 | 13 | 3 | 0 | 0 | 0 | 2768 | 348 |
| Escadron de Transport 1/61 Touraine | 285 | 12 | 9 | 3 | 12 | 1 | 0 | 1 | 3 | 2916 | 348 |
| Nazario Moreno González | 1986 | 73 | 22 | 51 | 72 | 3 | 0 | 8 | 14 | 17472 | 2042 |
| Tomáš Vyoral | 219 | 7 | 4 | 3 | 7 | 0 | 0 | 1 | 2 | 1858 | 222 |
| Rybno-Slobodsky District | 1075 | 47 | 16 | 31 | 47 | 6 | 0 | 5 | 17 | 11112 | 1242 |
| Gift Tandare | 316 | 14 | 5 | 9 | 14 | 0 | 0 | 1 | 2 | 2722 | 351 |
| Biscuit cake | 286 | 9 | 2 | 7 | 9 | 0 | 0 | 0 | 0 | 2206 | 232 |
| Ventura County Railroad | 549 | 23 | 12 | 11 | 23 | 0 | 0 | 3 | 9 | 5514 | 642 |
| Legacy Devers Eye Institute | 372 | 16 | 9 | 7 | 16 | 2 | 0 | 1 | 3 | 3637 | 420 |
| Riedwihr | 216 | 7 | 3 | 4 | 7 | 0 | 0 | 2 | 4 | 1727 | 182 |
| Eugène Mayor | 592 | 21 | 7 | 14 | 21 | 2 | 0 | 5 | 11 | 5784 | 644 |
| Pain Killer Tour | 378 | 17 | 11 | 6 | 17 | 0 | 0 | 3 | 6 | 3846 | 475 |
| The Blue and the Gray (The Simpsons) | 442 | 19 | 8 | 11 | 19 | 0 | 0 | 2 | 6 | 3932 | 506 |
| List of Shahid original programming | 293 | 15 | 4 | 11 | 15 | 0 | 0 | 2 | 4 | 3346 | 366 |
| Wang Qijiang | 661 | 22 | 11 | 11 | 22 | 0 | 0 | 2 | 6 | 6120 | 644 |
| Sola (Héctor el Father song) | 656 | 24 | 8 | 16 | 22 | 2 | 0 | 5 | 12 | 5995 | 663 |
| American Pastoral | 2424 | 88 | 32 | 56 | 88 | 5 | 0 | 12 | 24 | 22286 | 2417 |
| Thomas Cranley Onslow | 886 | 29 | 20 | 9 | 29 | 1 | 0 | 6 | 12 | 8216 | 961 |
| Aikyō | 229 | 12 | 1 | 11 | 12 | 0 | 0 | 2 | 7 | 3483 | 334 |
| Jacob Laursen | 420 | 13 | 9 | 4 | 12 | 1 | 0 | 4 | 6 | 3516 | 395 |
| Humboldt Cable | 327 | 14 | 10 | 4 | 14 | 0 | 0 | 3 | 5 | 3413 | 372 |
| Grendon, Northamptonshire | 878 | 48 | 15 | 33 | 48 | 3 | 0 | 3 | 7 | 9679 | 1181 |
| Mateusz Kusznierewicz | 472 | 17 | 6 | 11 | 17 | 1 | 0 | 4 | 8 | 4276 | 471 |
| Heinkel HE 1 | 372 | 14 | 5 | 9 | 14 | 6 | 0 | 2 | 4 | 3607 | 376 |
| Nineteenth Amendment | 702 | 28 | 10 | 18 | 28 | 3 | 0 | 0 | 0 | 9769 | 735 |
| Joshua Koshiba | 262 | 14 | 6 | 8 | 14 | 1 | 0 | 3 | 9 | 3035 | 371 |
| Gossip Candy | 2081 | 81 | 36 | 45 | 80 | 10 | 0 | 6 | 13 | 17222 | 2156 |
| 1981 US Open – Women's doubles | 296 | 16 | 11 | 5 | 16 | 0 | 0 | 1 | 3 | 3154 | 416 |
| Oratorium (Funeral album) | 252 | 9 | 4 | 5 | 9 | 1 | 0 | 0 | 0 | 1852 | 229 |
| Pascal Nyabenda | 405 | 15 | 8 | 7 | 15 | 0 | 0 | 3 | 9 | 3910 | 463 |
| Citizen Party (Bristol) | 866 | 32 | 14 | 18 | 30 | 2 | 0 | 5 | 11 | 7203 | 874 |
| Vadu Izei | 424 | 26 | 13 | 13 | 26 | 1 | 0 | 1 | 4 | 5199 | 657 |
| Canta | 381 | 19 | 6 | 13 | 19 | 0 | 0 | 1 | 2 | 3522 | 462 |
| Athens–Piraeus Electric Railways | 767 | 25 | 9 | 16 | 25 | 0 | 0 | 4 | 8 | 7444 | 798 |
| Japanese marten | 576 | 22 | 7 | 15 | 22 | 0 | 0 | 0 | 0 | 3794 | 536 |
| Swanzey, New Hampshire | 233 | 15 | 9 | 6 | 15 | 0 | 0 | 4 | 8 | 3264 | 370 |
| Sorcery | 290 | 14 | 2 | 12 | 14 | 0 | 0 | 0 | 0 | 3159 | 344 |
| Bam Bam Bol Raha Hai Kashi | 357 | 16 | 10 | 6 | 16 | 0 | 0 | 1 | 2 | 3830 | 415 |
| Superior Air Parts XP-382 | 381 | 16 | 10 | 6 | 16 | 0 | 0 | 2 | 5 | 3808 | 419 |
| Ti'Wakan | 782 | 24 | 12 | 12 | 24 | 0 | 0 | 9 | 14 | 6839 | 742 |
| Articles of the Church of Christ | 495 | 25 | 9 | 16 | 25 | 2 | 0 | 1 | 4 | 5297 | 617 |
| Königsberg-class cruiser (1905) | 1467 | 57 | 22 | 35 | 57 | 5 | 0 | 8 | 14 | 12751 | 1516 |
| The Last Egyptian | 1124 | 48 | 12 | 36 | 47 | 1 | 0 | 2 | 6 | 11122 | 1237 |
| Journal of Statistical Mechanics: Theory and Experiment | 367 | 19 | 10 | 9 | 19 | 0 | 0 | 0 | 0 | 3735 | 490 |
| Lake Malawi sardine | 889 | 42 | 10 | 32 | 42 | 1 | 0 | 1 | 2 | 7774 | 1004 |
| Danger Biscuit | 439 | 21 | 12 | 9 | 21 | 0 | 0 | 1 | 2 | 4302 | 536 |
| Chris Aitken | 277 | 10 | 5 | 5 | 10 | 0 | 0 | 3 | 6 | 2370 | 284 |
| Murder by an Aristocrat | 389 | 17 | 8 | 9 | 17 | 1 | 0 | 3 | 6 | 3980 | 467 |
| Ainaži Nautical School | 1033 | 43 | 16 | 27 | 43 | 1 | 0 | 4 | 11 | 9598 | 1177 |
| 1968–69 Seattle SuperSonics season | 388 | 16 | 8 | 8 | 16 | 0 | 0 | 2 | 6 | 3992 | 476 |
| Stanley Hughes | 705 | 24 | 3 | 21 | 24 | 0 | 0 | 2 | 3 | 5232 | 628 |
| Guoqi Zhang | 286 | 13 | 7 | 6 | 13 | 0 | 0 | 1 | 3 | 3428 | 360 |
| Sentimental Lady | 351 | 13 | 7 | 6 | 13 | 0 | 0 | 3 | 7 | 3030 | 350 |
| Sue Butterworth | 200 | 9 | 3 | 6 | 9 | 0 | 0 | 4 | 7 | 2886 | 332 |
| Zunfthaus zur Meisen | 454 | 16 | 9 | 7 | 16 | 1 | 0 | 2 | 6 | 4095 | 476 |
| Bergamasco, Piedmont | 793 | 33 | 22 | 11 | 23 | 0 | 0 | 8 | 10 | 6904 | 834 |
| Monodora stenopetala | 262 | 11 | 5 | 6 | 11 | 0 | 0 | 0 | 0 | 2072 | 267 |
| 2nd Parliament of William III and Mary II | 1753 | 78 | 33 | 45 | 78 | 3 | 0 | 7 | 16 | 16958 | 2082 |
| Carvel (boat building) | 1364 | 50 | 1 | 49 | 50 | 0 | 0 | 0 | 0 | 10706 | 1235 |
| Tramway Oval | 1305 | 45 | 16 | 29 | 45 | 0 | 0 | 10 | 22 | 12308 | 1220 |
| Kito (slang) | 276 | 13 | 3 | 10 | 13 | 0 | 0 | 0 | 0 | 2358 | 304 |
| Information activism | 1264 | 53 | 4 | 49 | 53 | 4 | 0 | 2 | 5 | 11006 | 1390 |
| Help Scout | 499 | 21 | 13 | 8 | 21 | 4 | 0 | 2 | 6 | 4649 | 568 |
| Codex Purpureus Sarzanensis | 1788 | 78 | 22 | 56 | 73 | 9 | 0 | 16 | 21 | 18865 | 2142 |
| Iranian presidential election | 1503 | 66 | 13 | 53 | 66 | 3 | 0 | 0 | 0 | 14855 | 1726 |
| DF-26 | 1271 | 41 | 21 | 20 | 37 | 2 | 0 | 7 | 10 | 10013 | 1148 |
| 1917–18 William & Mary Indians men's basketball team | 487 | 20 | 12 | 8 | 20 | 0 | 0 | 4 | 11 | 4745 | 595 |
| Electric Tonic | 975 | 35 | 12 | 23 | 35 | 1 | 0 | 4 | 8 | 8154 | 990 |
| Kingsbury, New York | 221 | 9 | 5 | 4 | 9 | 0 | 0 | 2 | 3 | 2000 | 238 |
| George Backer | 337 | 10 | 6 | 4 | 10 | 0 | 0 | 5 | 6 | 3282 | 401 |
| Chishtian | 236 | 14 | 8 | 6 | 14 | 0 | 0 | 0 | 0 | 2529 | 348 |
| Colophon (beetle) | 865 | 31 | 4 | 27 | 31 | 3 | 0 | 3 | 4 | 6920 | 808 |
| Ysbeidiau Heulog | 820 | 31 | 7 | 24 | 31 | 4 | 0 | 3 | 7 | 7090 | 810 |
| List of grasses of New Zealand | 327 | 12 | 2 | 10 | 12 | 5 | 0 | 0 | 0 | 2478 | 298 |
| Old Mother Riley Joins Up | 224 | 9 | 6 | 3 | 9 | 0 | 0 | 1 | 2 | 2240 | 246 |
| Štrbac (surname) | 236 | 9 | 3 | 6 | 9 | 0 | 0 | 2 | 4 | 2478 | 262 |
| Alexandru Graur | 1663 | 68 | 34 | 34 | 68 | 3 | 0 | 8 | 19 | 15147 | 1846 |
| Sabin Manuilă | 1873 | 69 | 25 | 44 | 69 | 1 | 0 | 5 | 9 | 15818 | 1904 |
| 2013 Bungoma local elections | 473 | 14 | 6 | 8 | 14 | 0 | 0 | 3 | 5 | 3667 | 410 |
| Brimble | 433 | 13 | 7 | 6 | 13 | 0 | 0 | 3 | 7 | 5103 | 523 |
| Sunriver, Oregon | 581 | 26 | 11 | 15 | 26 | 3 | 0 | 4 | 7 | 5972 | 668 |
| Emergency communications network | 946 | 21 | 4 | 17 | 20 | 0 | 0 | 0 | 0 | 6127 | 629 |
| Dansalan College | 408 | 15 | 6 | 9 | 15 | 0 | 0 | 3 | 8 | 3405 | 411 |
| Grande Tête de By | 229 | 10 | 2 | 8 | 10 | 0 | 0 | 1 | 2 | 1954 | 237 |
| Guadalajara Mi Macro | 328 | 12 | 7 | 5 | 12 | 0 | 0 | 2 | 3 | 2844 | 345 |
| Mr & Mrs Unwanted | 331 | 14 | 10 | 4 | 14 | 1 | 0 | 0 | 0 | 2928 | 362 |
| Four Seasons Hotel Chicago | 295 | 13 | 7 | 6 | 13 | 2 | 0 | 2 | 4 | 2882 | 338 |
| Abbeyleix House | 373 | 14 | 8 | 6 | 14 | 0 | 0 | 2 | 4 | 3091 | 369 |
| A Single Sky | 267 | 8 | 4 | 4 | 8 | 0 | 0 | 2 | 5 | 2183 | 232 |
| Portrait Salon | 523 | 16 | 6 | 10 | 16 | 0 | 0 | 10 | 7 | 4510 | 482 |
| Casey Weldon (artist) | 445 | 21 | 6 | 15 | 21 | 0 | 0 | 0 | 0 | 4181 | 511 |
| Peroxide (punk zine) | 919 | 38 | 18 | 20 | 38 | 1 | 0 | 1 | 2 | 8208 | 956 |
| Wim Kan | 1322 | 39 | 17 | 22 | 36 | 3 | 0 | 15 | 22 | 10183 | 1116 |
| Princess Hwisin | 416 | 23 | 7 | 16 | 22 | 0 | 0 | 1 | 4 | 5616 | 624 |
| Aleksandar Đokić | 884 | 36 | 14 | 22 | 36 | 1 | 0 | 3 | 6 | 9554 | 1030 |
| Çeltikbaşı, Kurtalan | 205 | 11 | 6 | 5 | 11 | 0 | 0 | 1 | 1 | 2109 | 278 |
| Aldfield | 526 | 23 | 10 | 13 | 23 | 0 | 0 | 5 | 10 | 5184 | 589 |
| Ministry of Social Development and Fight against Hunger (Brazil) | 230 | 15 | 12 | 3 | 15 | 0 | 0 | 0 | 0 | 3211 | 377 |
| SS Vaterland | 263 | 8 | 3 | 5 | 8 | 1 | 0 | 3 | 4 | 2679 | 254 |
| Don't Need You To (Tell Me I'm Pretty) | 568 | 14 | 4 | 10 | 14 | 1 | 0 | 2 | 1 | 3151 | 374 |
| Diocese of Angers | 619 | 31 | 12 | 19 | 31 | 2 | 0 | 2 | 6 | 6388 | 797 |
| Ballymully Glebe | 450 | 22 | 8 | 14 | 22 | 1 | 0 | 2 | 4 | 4272 | 557 |
| McIntire–Stennis Act of 1962 | 836 | 31 | 3 | 28 | 31 | 1 | 0 | 6 | 9 | 8017 | 839 |
| Stuck (2017 film) | 387 | 16 | 10 | 6 | 16 | 0 | 0 | 3 | 5 | 3510 | 428 |
| Dome of the Chain | 711 | 28 | 14 | 14 | 28 | 1 | 0 | 1 | 3 | 6458 | 738 |
| Pizzi (Portuguese footballer) | 716 | 25 | 10 | 15 | 25 | 7 | 0 | 5 | 16 | 6782 | 733 |
| Tomball, Texas | 322 | 18 | 6 | 12 | 18 | 0 | 0 | 2 | 5 | 3846 | 445 |
| Asutsuare | 638 | 26 | 11 | 15 | 8 | 0 | 0 | 0 | 0 | 6161 | 658 |
| Maryland Route 274 | 708 | 33 | 19 | 14 | 33 | 12 | 0 | 9 | 14 | 7474 | 894 |
| Water polo at the 2008 Summer Olympics – Women's team rosters | 232 | 11 | 4 | 7 | 11 | 2 | 0 | 1 | 2 | 2336 | 287 |
| Jackson's pipit | 1606 | 61 | 9 | 52 | 61 | 3 | 0 | 2 | 3 | 12688 | 1535 |
| FAM63B | 345 | 15 | 1 | 14 | 15 | 1 | 0 | 0 | 0 | 2801 | 361 |
| Conservation science | 349 | 16 | 0 | 16 | 16 | 0 | 0 | 0 | 0 | 4024 | 405 |
| A Boy Named Goo | 382 | 14 | 4 | 10 | 14 | 0 | 0 | 2 | 4 | 3152 | 362 |
| BEM High School, Parappanangadi | 1227 | 46 | 24 | 22 | 42 | 1 | 0 | 9 | 21 | 10947 | 1278 |
| Wahhab | 319 | 17 | 8 | 9 | 17 | 0 | 0 | 0 | 0 | 3926 | 418 |
| Sulfathiazole | 284 | 10 | 1 | 9 | 10 | 1 | 0 | 0 | 0 | 1992 | 254 |
| Don Newmeyer | 673 | 31 | 18 | 13 | 31 | 0 | 0 | 3 | 7 | 6520 | 851 |
| The Lion and the Lamb (film) | 240 | 11 | 7 | 4 | 11 | 0 | 0 | 2 | 5 | 2696 | 294 |
| Antony Crockett | 1601 | 74 | 35 | 39 | 64 | 3 | 0 | 6 | 13 | 15548 | 1862 |
| Superbird-B1 | 819 | 31 | 11 | 20 | 31 | 1 | 0 | 4 | 7 | 7694 | 841 |
| Frederick Oliver | 217 | 6 | 4 | 2 | 6 | 1 | 0 | 2 | 2 | 1637 | 196 |
| Korne | 211 | 12 | 10 | 2 | 12 | 0 | 0 | 0 | 0 | 2716 | 306 |
| Dodo Abashidze | 1447 | 55 | 20 | 35 | 53 | 2 | 0 | 15 | 31 | 14915 | 1622 |
| The African Unity Stadium | 225 | 11 | 5 | 6 | 11 | 1 | 0 | 0 | 0 | 2355 | 293 |
| 19th All-Union Conference of the Communist Party of the Soviet Union | 220 | 8 | 5 | 3 | 8 | 1 | 0 | 1 | 4 | 2083 | 247 |
| Kahlil Gibran | 3501 | 133 | 43 | 90 | 133 | 3 | 0 | 20 | 44 | 33226 | 3778 |
| Samuel Stocking House | 381 | 12 | 5 | 7 | 12 | 1 | 0 | 2 | 3 | 2824 | 332 |
| Dam-e Tang-e Shahid Deli Bajak | 282 | 14 | 7 | 7 | 14 | 1 | 0 | 1 | 2 | 3913 | 390 |
| The Right and the Wrong | 448 | 15 | 6 | 9 | 15 | 1 | 0 | 2 | 5 | 3480 | 386 |
| Here's Some Love (song) | 233 | 8 | 5 | 3 | 8 | 2 | 0 | 1 | 1 | 1779 | 214 |
| Lago di Santa Croce | 556 | 27 | 9 | 18 | 27 | 4 | 0 | 5 | 7 | 5496 | 654 |
| Patrick Oketch | 441 | 21 | 11 | 10 | 21 | 0 | 0 | 2 | 4 | 4444 | 544 |
| General Theory | 242 | 10 | 8 | 2 | 10 | 0 | 0 | 1 | 5 | 2820 | 290 |
| Jessica Delfino | 1222 | 45 | 18 | 27 | 45 | 3 | 0 | 5 | 9 | 11452 | 1241 |
| Mae Marsh | 298 | 12 | 6 | 6 | 12 | 0 | 0 | 5 | 9 | 3452 | 372 |
| Antiguraleus taranakiensis | 252 | 10 | 6 | 4 | 10 | 0 | 0 | 1 | 3 | 2188 | 259 |
| Jozef Moravčík | 200 | 7 | 3 | 4 | 7 | 0 | 0 | 3 | 5 | 1785 | 216 |
| INS Romach (1981) | 230 | 9 | 8 | 1 | 9 | 1 | 0 | 2 | 5 | 2108 | 248 |
| Endemic Intelligence in Multiple Dimensions | 1160 | 31 | 8 | 23 | 31 | 4 | 0 | 4 | 5 | 6877 | 851 |
| Rowland Phillips (tennis) | 317 | 10 | 5 | 5 | 10 | 0 | 0 | 5 | 5 | 2453 | 284 |
| Roko Malani | 549 | 26 | 15 | 11 | 26 | 2 | 0 | 3 | 7 | 5423 | 664 |
| Dipika Sanjay Chavan | 262 | 9 | 6 | 3 | 9 | 0 | 0 | 0 | 0 | 1887 | 247 |
| Getup Ltd v Electoral Commissioner | 416 | 13 | 7 | 6 | 13 | 1 | 0 | 2 | 5 | 3404 | 394 |
| Taiwan Esperanto Association | 1010 | 36 | 12 | 24 | 31 | 1 | 0 | 8 | 16 | 8348 | 988 |
| Hyundai Lambda engine | 296 | 12 | 6 | 6 | 12 | 0 | 0 | 2 | 3 | 2465 | 315 |
| Warp zone (disambiguation) | 225 | 16 | 3 | 13 | 16 | 1 | 0 | 1 | 5 | 3726 | 397 |
| CB Barcelona | 392 | 13 | 10 | 3 | 13 | 0 | 0 | 2 | 3 | 3250 | 375 |
| Katharine O'Shea | 341 | 11 | 5 | 6 | 11 | 0 | 0 | 3 | 5 | 3827 | 405 |
| 1999 Chatham Cup | 497 | 18 | 3 | 15 | 17 | 3 | 0 | 3 | 5 | 3938 | 473 |
| National Register of Historic Places listings in Brazos County, Texas | 578 | 22 | 11 | 11 | 22 | 4 | 0 | 0 | 0 | 4473 | 575 |
| Tom Lenihan | 857 | 40 | 11 | 29 | 40 | 3 | 0 | 0 | 0 | 7735 | 962 |
| Jeffrey J. Kripal | 622 | 30 | 8 | 22 | 30 | 0 | 0 | 1 | 2 | 6262 | 760 |
| Energy Reorganization Act of 1974 | 1479 | 61 | 13 | 48 | 61 | 1 | 0 | 8 | 15 | 15881 | 1698 |
| American Anthropometric Society | 861 | 35 | 7 | 28 | 35 | 2 | 0 | 2 | 6 | 7455 | 900 |
| Hunter Skinner | 345 | 14 | 8 | 6 | 14 | 0 | 0 | 2 | 4 | 3752 | 417 |
| Metamood | 1568 | 59 | 5 | 54 | 59 | 2 | 0 | 0 | 0 | 12602 | 1462 |
| Cape Campbell Lighthouse | 804 | 26 | 9 | 17 | 26 | 0 | 0 | 8 | 16 | 5870 | 688 |
| Advanced Airlift Tactics Training Center | 728 | 27 | 11 | 16 | 27 | 0 | 2 | 1 | 3 | 6399 | 785 |
| Andrea Marinelli | 524 | 20 | 9 | 11 | 20 | 2 | 0 | 3 | 8 | 4637 | 552 |
| Wayne Central School District | 1891 | 79 | 35 | 44 | 79 | 4 | 0 | 10 | 16 | 19418 | 2146 |
| Toxidia doubledayi | 305 | 14 | 4 | 10 | 12 | 0 | 0 | 3 | 7 | 3051 | 344 |
| Patroon Island Bridge | 707 | 27 | 13 | 14 | 27 | 1 | 0 | 7 | 10 | 6659 | 746 |
| Lane Thomas | 779 | 26 | 15 | 11 | 26 | 0 | 0 | 8 | 15 | 6800 | 785 |
| Soamanonga | 573 | 25 | 5 | 20 | 25 | 2 | 0 | 5 | 13 | 5150 | 612 |
| Atamania | 1077 | 51 | 16 | 35 | 49 | 2 | 0 | 1 | 2 | 10865 | 1300 |
| Taioaliʻiseu Fiti Aimaʻasu | 1462 | 60 | 19 | 41 | 60 | 3 | 0 | 6 | 15 | 13127 | 1592 |
| Ashley Smith (rugby union) | 676 | 27 | 17 | 10 | 27 | 1 | 0 | 8 | 20 | 7156 | 856 |
| Tadashi Yamamoto (athlete) | 237 | 10 | 5 | 5 | 10 | 1 | 0 | 2 | 6 | 2666 | 304 |
| Gene L. Coon | 514 | 19 | 5 | 14 | 19 | 1 | 0 | 2 | 3 | 4636 | 523 |
| 1990 Texas House of Representatives election | 446 | 16 | 8 | 8 | 16 | 2 | 0 | 3 | 5 | 3540 | 436 |
| Waisale Waqanivalu | 478 | 16 | 4 | 12 | 16 | 3 | 0 | 4 | 9 | 3825 | 464 |
| War Correspondent (film) | 299 | 14 | 8 | 6 | 14 | 0 | 0 | 1 | 2 | 2718 | 351 |
| Odenville Formation | 1756 | 63 | 24 | 39 | 63 | 1 | 0 | 5 | 9 | 15414 | 1726 |
| The Ed Wynn Show | 495 | 22 | 12 | 10 | 22 | 2 | 0 | 1 | 2 | 4919 | 581 |
| Eugen Nicolăescu | 364 | 13 | 9 | 4 | 13 | 0 | 0 | 4 | 10 | 3529 | 401 |
| 1965 Christchurch mayoral election | 283 | 8 | 2 | 6 | 8 | 0 | 0 | 2 | 3 | 2039 | 224 |
| Dance Suomi | 758 | 31 | 9 | 22 | 31 | 0 | 0 | 1 | 2 | 7230 | 809 |
| Paul Johnson (cricketer) | 613 | 18 | 6 | 12 | 18 | 1 | 0 | 9 | 14 | 5165 | 564 |
| Michael Schneider (conductor) | 358 | 13 | 3 | 10 | 13 | 0 | 0 | 1 | 2 | 3036 | 349 |
| Princess Feodora of Hohenlohe-Langenburg | 352 | 16 | 6 | 10 | 16 | 0 | 0 | 4 | 7 | 4312 | 511 |
| China Railway Qingzang Group | 432 | 16 | 13 | 3 | 16 | 0 | 0 | 2 | 1 | 3945 | 442 |
| Labor Temple Building | 236 | 9 | 4 | 5 | 9 | 1 | 0 | 1 | 2 | 2050 | 233 |
| Valdis Muktupāvels | 1736 | 81 | 37 | 44 | 81 | 2 | 0 | 15 | 34 | 20164 | 2258 |
| Norton Mezvinsky | 427 | 18 | 8 | 10 | 18 | 1 | 0 | 3 | 4 | 4182 | 502 |
| Camporee | 274 | 11 | 1 | 10 | 11 | 0 | 0 | 0 | 0 | 2099 | 270 |
| Passive heave compensation | 304 | 13 | 3 | 10 | 11 | 0 | 0 | 0 | 0 | 2413 | 320 |
| Anthophora villosula | 207 | 7 | 3 | 4 | 7 | 0 | 0 | 0 | 0 | 1336 | 170 |
| Disaster management in India | 1624 | 77 | 8 | 69 | 59 | 0 | 0 | 4 | 8 | 18056 | 1900 |
| Linkou metro station | 203 | 12 | 8 | 4 | 12 | 0 | 0 | 1 | 2 | 2470 | 312 |
| San Policarpo, Eastern Samar | 375 | 18 | 12 | 6 | 18 | 1 | 0 | 4 | 6 | 4012 | 444 |
| Wojciechów | 1083 | 56 | 51 | 5 | 56 | 0 | 0 | 13 | 30 | 29685 | 1538 |
| Southwest District (VHSL) | 226 | 8 | 6 | 2 | 8 | 0 | 0 | 2 | 3 | 1984 | 224 |
| Stockton Crusaders | 251 | 8 | 6 | 2 | 8 | 1 | 0 | 1 | 2 | 1899 | 234 |
| Kwesi Pratt Jnr | 351 | 15 | 6 | 9 | 15 | 0 | 0 | 2 | 3 | 3147 | 400 |
| Uuden Musiikin Kilpailu | 435 | 17 | 8 | 9 | 17 | 0 | 0 | 3 | 8 | 4792 | 500 |
| Martinican Democratic Rally | 438 | 21 | 12 | 9 | 21 | 1 | 0 | 2 | 3 | 4509 | 577 |
| E-governance in the United States | 518 | 20 | 2 | 18 | 20 | 1 | 0 | 1 | 4 | 4694 | 527 |
| Taein Heo clan | 523 | 34 | 9 | 25 | 34 | 0 | 0 | 3 | 6 | 6826 | 817 |
| Cheonho station | 224 | 9 | 8 | 1 | 9 | 2 | 0 | 0 | 0 | 1853 | 251 |
| Medal "For Impeccable Service" | 409 | 18 | 8 | 10 | 18 | 2 | 0 | 0 | 0 | 5798 | 506 |
| Michel Lauzzana | 226 | 8 | 4 | 4 | 8 | 0 | 0 | 2 | 5 | 1962 | 242 |
| Afrikaner (disambiguation) | 390 | 15 | 4 | 11 | 15 | 1 | 0 | 3 | 6 | 4268 | 392 |
| Asid ibn Zafir al-Sulami | 396 | 20 | 11 | 9 | 20 | 0 | 0 | 1 | 2 | 4464 | 555 |
| Seth Stubblefield | 238 | 8 | 3 | 5 | 8 | 0 | 0 | 2 | 4 | 2071 | 232 |
| Bruce Petty | 758 | 26 | 7 | 19 | 26 | 1 | 0 | 2 | 2 | 6339 | 720 |
| Pelobates balcanicus | 219 | 13 | 7 | 6 | 13 | 0 | 0 | 1 | 5 | 2894 | 309 |
| Cangai, New South Wales | 3847 | 155 | 42 | 113 | 155 | 7 | 0 | 27 | 49 | 35628 | 4047 |
| Wilcocks | 253 | 11 | 5 | 6 | 11 | 0 | 0 | 1 | 2 | 2861 | 341 |
| James Min | 1063 | 38 | 7 | 31 | 38 | 1 | 0 | 7 | 11 | 9343 | 1042 |
| Steve Hearon | 330 | 12 | 5 | 7 | 12 | 1 | 0 | 1 | 2 | 2836 | 313 |
| Edgeworth FC | 220 | 9 | 5 | 4 | 9 | 0 | 0 | 1 | 2 | 2030 | 237 |
| Dalia Ziada | 438 | 18 | 10 | 8 | 18 | 0 | 0 | 3 | 8 | 4491 | 494 |
| 55th National Conference of the African National Congress | 1034 | 38 | 15 | 23 | 38 | 1 | 0 | 5 | 11 | 9923 | 1083 |
| Teslin (material) | 997 | 31 | 9 | 22 | 31 | 4 | 0 | 2 | 4 | 6730 | 793 |
| Azimsirminskoye | 222 | 11 | 3 | 8 | 11 | 0 | 0 | 1 | 2 | 2488 | 294 |
| Clark/Lake station | 792 | 30 | 19 | 11 | 30 | 2 | 0 | 5 | 7 | 7334 | 862 |
| Peter Kippax | 224 | 7 | 4 | 3 | 7 | 0 | 0 | 1 | 2 | 1996 | 219 |
| Bert Weckhuysen | 463 | 20 | 4 | 16 | 20 | 0 | 0 | 3 | 5 | 4404 | 519 |
| Elise Heyerdahl | 448 | 12 | 2 | 10 | 12 | 0 | 0 | 3 | 4 | 3058 | 338 |
| 1985–86 FA Cup | 352 | 12 | 7 | 5 | 12 | 0 | 0 | 1 | 3 | 2940 | 354 |
| Jason Nash | 399 | 13 | 5 | 8 | 13 | 0 | 0 | 4 | 6 | 2979 | 352 |
| Serration | 539 | 24 | 0 | 24 | 24 | 2 | 0 | 0 | 0 | 4876 | 571 |
| Mass media in Northern Cyprus | 686 | 28 | 4 | 24 | 28 | 3 | 0 | 2 | 4 | 5629 | 697 |
| Rachel Weiss (businesswoman) | 453 | 19 | 7 | 12 | 19 | 0 | 0 | 4 | 10 | 4620 | 517 |
| Bhavani Peth | 447 | 24 | 13 | 11 | 22 | 0 | 0 | 0 | 0 | 4362 | 604 |
| Xolani Msimango | 376 | 13 | 9 | 4 | 13 | 0 | 0 | 5 | 6 | 3328 | 396 |
| Matt Dickinson | 273 | 14 | 6 | 8 | 14 | 0 | 0 | 1 | 4 | 3120 | 352 |
| Madhabkunda Waterfall | 528 | 27 | 7 | 20 | 27 | 1 | 0 | 1 | 3 | 5392 | 692 |
| Neuromodulation (journal) | 367 | 15 | 4 | 11 | 14 | 0 | 0 | 1 | 3 | 3311 | 393 |
| Guildford Black Friary | 907 | 36 | 14 | 22 | 36 | 1 | 0 | 13 | 20 | 8853 | 999 |
| American and British English pronunciation differences | 589 | 32 | 9 | 23 | 27 | 0 | 0 | 0 | 0 | 5888 | 788 |
| Aspilanta argentifera | 249 | 12 | 4 | 8 | 12 | 1 | 0 | 2 | 3 | 2404 | 300 |
| Kintsugi | 466 | 22 | 3 | 19 | 22 | 0 | 0 | 0 | 0 | 4826 | 518 |
| QF 12-pounder 12 cwt naval gun | 809 | 31 | 8 | 23 | 29 | 6 | 0 | 3 | 6 | 6980 | 771 |
| Nandu (film) | 366 | 18 | 8 | 10 | 16 | 0 | 0 | 3 | 4 | 3217 | 439 |
| Tangled Webs | 407 | 14 | 1 | 13 | 14 | 0 | 0 | 4 | 6 | 3544 | 400 |
| Alabama Tribune | 1244 | 47 | 26 | 21 | 47 | 0 | 0 | 6 | 13 | 10020 | 1262 |
| Algerian law on the criminalization of French colonization | 495 | 20 | 2 | 18 | 20 | 1 | 0 | 2 | 5 | 4528 | 534 |
| Ivano-Frankivsk Theological Academy of Greek-Catholic Church | 622 | 19 | 11 | 8 | 19 | 0 | 0 | 3 | 7 | 4848 | 564 |
| Mave: | 291 | 13 | 5 | 8 | 13 | 0 | 0 | 2 | 3 | 2948 | 338 |
| Bayartsogtyn Mönkhzayaa | 478 | 19 | 10 | 9 | 19 | 2 | 0 | 5 | 11 | 4842 | 550 |
| Franklinton, Louisiana | 752 | 31 | 19 | 12 | 31 | 2 | 0 | 10 | 17 | 7148 | 830 |
| Randalls | 1282 | 55 | 19 | 36 | 55 | 4 | 0 | 3 | 6 | 12655 | 1462 |
| Stephen Donovan | 370 | 12 | 10 | 2 | 12 | 0 | 0 | 2 | 5 | 3003 | 354 |
| Marketocracy | 870 | 32 | 9 | 23 | 32 | 5 | 0 | 5 | 13 | 7086 | 853 |
| Paravoor T. K. Narayana Pillai | 300 | 11 | 3 | 8 | 11 | 0 | 0 | 3 | 5 | 3008 | 329 |
| Master Anand | 1146 | 40 | 15 | 25 | 40 | 3 | 0 | 11 | 21 | 10004 | 1144 |
| List of Mesozoic birds | 466 | 18 | 0 | 18 | 18 | 1 | 0 | 0 | 0 | 3757 | 440 |
| Long Island (California) | 291 | 12 | 7 | 5 | 12 | 1 | 0 | 3 | 4 | 2650 | 312 |
| Grasshopper sparrow | 1450 | 57 | 2 | 55 | 57 | 3 | 0 | 2 | 3 | 12164 | 1426 |
| Osłowo, Podlaskie Voivodeship | 445 | 21 | 9 | 12 | 20 | 5 | 0 | 2 | 4 | 4458 | 530 |
| Secretary for Justice v Yau Yuk Lung Zigo | 462 | 17 | 3 | 14 | 17 | 0 | 0 | 0 | 0 | 3610 | 426 |
| Disability culture | 3513 | 132 | 7 | 125 | 131 | 4 | 0 | 2 | 4 | 28902 | 3341 |
| Hispanic Antiguans and Barbudans | 767 | 30 | 9 | 21 | 30 | 3 | 0 | 3 | 7 | 6510 | 762 |
| Aslam Raisani | 268 | 9 | 7 | 2 | 9 | 0 | 0 | 3 | 7 | 3404 | 374 |
| Dalton Cooper | 237 | 8 | 6 | 2 | 8 | 0 | 0 | 1 | 2 | 2034 | 245 |
| KPRC (AM) | 1172 | 41 | 28 | 13 | 41 | 2 | 0 | 10 | 12 | 10072 | 1222 |
| Aces of the Galaxy | 551 | 24 | 5 | 19 | 24 | 2 | 0 | 1 | 3 | 4813 | 604 |
| Dream Ticket (video) | 408 | 17 | 6 | 11 | 17 | 1 | 0 | 2 | 4 | 3710 | 448 |
| Bramfield, Suffolk | 577 | 24 | 9 | 15 | 24 | 0 | 0 | 13 | 17 | 6220 | 590 |
| Jamie Swift | 1102 | 51 | 20 | 31 | 51 | 1 | 0 | 6 | 10 | 10452 | 1344 |
| Sugar Pine, California | 703 | 27 | 16 | 11 | 25 | 2 | 0 | 13 | 21 | 6814 | 758 |
| Otaku USA | 1213 | 43 | 12 | 31 | 41 | 3 | 0 | 10 | 18 | 11662 | 1314 |
| Notodden Station | 373 | 11 | 10 | 1 | 5 | 0 | 0 | 6 | 9 | 3305 | 410 |
| Zizia trifoliata | 292 | 13 | 8 | 5 | 13 | 0 | 0 | 0 | 0 | 2538 | 318 |
| 1922 Michigan State Normal Normalites football team | 460 | 15 | 9 | 6 | 15 | 0 | 0 | 2 | 2 | 4004 | 451 |
| If We Ever Meet Again | 699 | 34 | 18 | 16 | 34 | 0 | 0 | 2 | 5 | 6956 | 854 |
| Astelia | 453 | 18 | 8 | 10 | 18 | 1 | 0 | 2 | 4 | 3795 | 445 |
| Nagyszeben Offensive | 510 | 19 | 6 | 13 | 19 | 0 | 0 | 4 | 6 | 4906 | 556 |
| Man-su | 649 | 27 | 6 | 21 | 23 | 0 | 0 | 15 | 18 | 11261 | 926 |
| Mike Neese | 401 | 14 | 6 | 8 | 14 | 0 | 0 | 4 | 7 | 3460 | 413 |
| Kyriaki | 296 | 16 | 5 | 11 | 16 | 2 | 0 | 2 | 4 | 3248 | 411 |
| Athletic DNA | 419 | 15 | 6 | 9 | 15 | 0 | 0 | 1 | 2 | 3174 | 395 |
| John Shafto (footballer) | 228 | 10 | 5 | 5 | 10 | 2 | 0 | 1 | 2 | 1947 | 264 |
| The Young King (play) | 248 | 9 | 1 | 8 | 9 | 0 | 0 | 1 | 1 | 1509 | 212 |
| Jodie Lyn-Kee-Chow | 303 | 12 | 7 | 5 | 12 | 0 | 0 | 1 | 4 | 2798 | 321 |
| WWE Network (Canada) | 501 | 16 | 7 | 9 | 16 | 0 | 0 | 1 | 2 | 3956 | 469 |
| Funny Times (newspaper) | 680 | 28 | 13 | 15 | 28 | 0 | 0 | 6 | 11 | 6598 | 775 |
| Pork-knocker | 446 | 17 | 2 | 15 | 17 | 0 | 0 | 1 | 3 | 3686 | 444 |
| Anisohedral tiling | 309 | 12 | 0 | 12 | 12 | 1 | 0 | 0 | 0 | 2405 | 278 |
| Lead Mountain (Grand County, Colorado) | 1022 | 45 | 19 | 26 | 45 | 1 | 0 | 7 | 15 | 10086 | 1137 |
| Silphium pinnatifidum | 880 | 33 | 6 | 27 | 33 | 1 | 0 | 0 | 0 | 6770 | 820 |
| The Ghost Inside (band) | 595 | 23 | 9 | 14 | 23 | 2 | 0 | 4 | 8 | 5259 | 620 |
| Jonathan Donais | 214 | 9 | 4 | 5 | 9 | 0 | 0 | 2 | 6 | 2479 | 274 |
| Khouzama | 215 | 11 | 3 | 8 | 11 | 1 | 0 | 2 | 3 | 2452 | 290 |
| Fred S. Robillard | 428 | 14 | 8 | 6 | 14 | 0 | 0 | 2 | 2 | 3783 | 439 |
| Tigran Petrosian | 884 | 24 | 15 | 9 | 24 | 1 | 0 | 14 | 14 | 7929 | 853 |
| Mount Hector (New Zealand) | 354 | 14 | 7 | 7 | 14 | 0 | 0 | 4 | 8 | 3272 | 369 |
| Zandomeneghi | 218 | 8 | 4 | 4 | 8 | 0 | 0 | 1 | 3 | 1985 | 226 |
| Nymphes des bois | 943 | 32 | 6 | 26 | 32 | 0 | 0 | 2 | 6 | 7562 | 889 |
| David Bobihoe Akib | 1743 | 53 | 23 | 30 | 53 | 3 | 0 | 29 | 32 | 14840 | 1580 |
| Suchodoły | 414 | 21 | 20 | 1 | 21 | 0 | 0 | 5 | 13 | 6984 | 576 |
| Kennebunk (CDP), Maine | 315 | 14 | 7 | 7 | 14 | 0 | 0 | 2 | 3 | 2909 | 359 |
| Ballinderry Sword | 1623 | 74 | 16 | 58 | 74 | 5 | 0 | 3 | 7 | 14766 | 1900 |
| Janq'uquta (Puno) | 461 | 19 | 9 | 10 | 19 | 0 | 0 | 6 | 5 | 4460 | 466 |
| Nzalat Laadam | 219 | 12 | 3 | 9 | 12 | 1 | 0 | 2 | 3 | 2600 | 312 |
| New Carthage | 226 | 10 | 8 | 2 | 10 | 0 | 0 | 1 | 3 | 2677 | 271 |
| Koules Fortress | 263 | 17 | 13 | 4 | 17 | 0 | 0 | 2 | 3 | 3486 | 442 |
| Takayuki Kanamori | 230 | 7 | 4 | 3 | 7 | 0 | 0 | 5 | 6 | 2233 | 220 |
| Stitch 'n Bitch | 1436 | 53 | 15 | 38 | 53 | 2 | 0 | 3 | 7 | 11784 | 1388 |
| Ballaugh (parish) | 209 | 10 | 5 | 5 | 10 | 2 | 0 | 2 | 3 | 2098 | 242 |
| Yana Nestsiarava | 390 | 14 | 4 | 10 | 13 | 1 | 0 | 4 | 10 | 3770 | 412 |
| Cameron, Montana | 431 | 18 | 7 | 11 | 18 | 1 | 0 | 1 | 2 | 3352 | 448 |
| Stop Messing About | 285 | 10 | 2 | 8 | 10 | 0 | 0 | 3 | 3 | 2355 | 252 |
| Judo at the 2004 Summer Olympics – Women's 48 kg | 860 | 33 | 2 | 31 | 32 | 4 | 0 | 5 | 11 | 7599 | 862 |
| Omar Mena | 270 | 11 | 8 | 3 | 11 | 1 | 0 | 4 | 8 | 2645 | 299 |
| 2007 Ole Miss Rebels football team | 490 | 24 | 14 | 10 | 24 | 1 | 0 | 2 | 2 | 5665 | 679 |
| 1942–43 UCLA Bruins men's basketball team | 379 | 15 | 8 | 7 | 15 | 0 | 0 | 1 | 1 | 3580 | 436 |
| Peter Woulfe | 603 | 23 | 2 | 21 | 23 | 1 | 0 | 2 | 5 | 4841 | 576 |
| Goodbye Holland | 1173 | 45 | 22 | 23 | 41 | 5 | 0 | 6 | 15 | 9612 | 1141 |
| Legend of the Eight Samurai | 287 | 14 | 3 | 11 | 14 | 0 | 0 | 2 | 5 | 3608 | 384 |
| Telemarketing fraud | 1109 | 38 | 4 | 34 | 38 | 4 | 0 | 4 | 9 | 8580 | 994 |
| Destiny (Paintball) | 324 | 11 | 7 | 4 | 11 | 0 | 0 | 0 | 0 | 2261 | 288 |
| Big Black River Railroad Bridge | 849 | 30 | 19 | 11 | 30 | 0 | 0 | 4 | 11 | 7536 | 845 |
| Chamber of Deputies of Santa Fe | 657 | 26 | 13 | 13 | 26 | 1 | 0 | 1 | 5 | 6267 | 714 |
| Martin Imbalambala | 353 | 11 | 4 | 7 | 11 | 1 | 0 | 3 | 6 | 2669 | 311 |
| 1977 Pacific hurricane season | 859 | 27 | 10 | 17 | 27 | 3 | 0 | 8 | 11 | 6832 | 740 |
| Plymax | 825 | 34 | 3 | 31 | 34 | 5 | 0 | 5 | 9 | 7573 | 878 |
| Lexical similarity | 1416 | 53 | 3 | 50 | 53 | 6 | 0 | 4 | 7 | 11070 | 1308 |
| Pioneer Hall (Seattle) | 522 | 22 | 11 | 11 | 22 | 0 | 0 | 2 | 6 | 4683 | 559 |
| Shuzo Matsuoka | 454 | 18 | 3 | 15 | 18 | 1 | 0 | 3 | 8 | 4250 | 492 |
| Cheer (disambiguation) | 316 | 15 | 10 | 5 | 15 | 0 | 0 | 1 | 2 | 3983 | 406 |
| Harpreet Singh Bhatia | 1204 | 40 | 20 | 20 | 40 | 6 | 0 | 5 | 8 | 9470 | 1103 |
| Wendy Sharpe | 310 | 10 | 4 | 6 | 10 | 2 | 0 | 2 | 3 | 2315 | 267 |
| Natalia Kuikka | 329 | 11 | 6 | 5 | 11 | 0 | 0 | 2 | 5 | 2813 | 329 |
| Community of St. John | 1127 | 46 | 17 | 29 | 46 | 2 | 0 | 4 | 9 | 10624 | 1235 |
| Szklana Huta | 521 | 25 | 22 | 3 | 5 | 0 | 0 | 6 | 14 | 5478 | 651 |
| Paulo Bertran | 724 | 34 | 19 | 15 | 34 | 1 | 0 | 3 | 7 | 7748 | 960 |
| Burmakin | 219 | 10 | 3 | 7 | 10 | 0 | 0 | 2 | 4 | 2542 | 281 |
| In the Grey | 493 | 23 | 13 | 10 | 23 | 0 | 0 | 3 | 4 | 4840 | 591 |
| Skyline Stakes | 344 | 13 | 3 | 10 | 13 | 1 | 0 | 4 | 9 | 3286 | 366 |
| The Days (1993 film) | 1158 | 41 | 10 | 31 | 41 | 0 | 0 | 4 | 6 | 9441 | 1056 |
| Mikhail Shchepkin Higher Theatre School | 209 | 8 | 6 | 2 | 8 | 0 | 0 | 1 | 2 | 1772 | 220 |
| Yambatui Stars | 431 | 17 | 8 | 9 | 17 | 0 | 0 | 0 | 0 | 3686 | 445 |
| Cathedral of the Resurrection of Christ, Podgorica | 343 | 14 | 8 | 6 | 14 | 0 | 0 | 0 | 0 | 3342 | 401 |
| Volga region | 907 | 41 | 23 | 18 | 41 | 1 | 0 | 1 | 3 | 11375 | 1068 |
| Alciphron | 214 | 8 | 1 | 7 | 8 | 0 | 0 | 0 | 0 | 1623 | 203 |
| Newcastle Olympic FC | 294 | 11 | 7 | 4 | 11 | 0 | 0 | 3 | 3 | 2511 | 291 |
| Alex Johnson (wide receiver) | 232 | 8 | 4 | 4 | 8 | 0 | 0 | 1 | 2 | 2042 | 239 |
| Hypokeimenon | 285 | 12 | 3 | 9 | 12 | 0 | 0 | 0 | 0 | 2260 | 286 |
| Monument Hill and Kreische Brewery State Historic Sites | 905 | 39 | 14 | 25 | 35 | 5 | 0 | 6 | 14 | 8850 | 1036 |
| Hello Janine! | 489 | 21 | 12 | 9 | 21 | 1 | 0 | 2 | 3 | 4581 | 558 |
| Forest Hills Drive: Live | 238 | 6 | 4 | 2 | 6 | 0 | 0 | 3 | 4 | 1662 | 182 |
| Reginald Cline-Cole | 424 | 17 | 7 | 10 | 17 | 0 | 0 | 3 | 7 | 4510 | 496 |
| Stony Brook Seawolves women's basketball | 571 | 19 | 9 | 10 | 19 | 0 | 0 | 4 | 4 | 5122 | 589 |
| Darley Racing | 367 | 19 | 12 | 7 | 19 | 0 | 0 | 1 | 2 | 3808 | 472 |
| Eva-Mari Aro | 511 | 27 | 11 | 16 | 27 | 0 | 0 | 4 | 9 | 5785 | 704 |
| Memories Within Miss Aggie | 282 | 14 | 8 | 6 | 14 | 0 | 0 | 1 | 3 | 3150 | 362 |
| Rameswar, Odisha | 316 | 12 | 5 | 7 | 12 | 1 | 0 | 0 | 0 | 2459 | 311 |
| Amirids | 510 | 29 | 8 | 21 | 29 | 0 | 0 | 1 | 2 | 7028 | 768 |
| Thymine dioxygenase | 418 | 13 | 0 | 13 | 12 | 2 | 0 | 1 | 2 | 3114 | 338 |
| George Efstathiou | 735 | 25 | 10 | 15 | 21 | 2 | 0 | 7 | 18 | 6580 | 734 |
| Golden Bell Award for Best Newcomer in a Television Series | 432 | 13 | 7 | 6 | 13 | 0 | 0 | 4 | 4 | 3605 | 382 |
| Kunzea ericoides | 390 | 13 | 2 | 11 | 13 | 2 | 0 | 2 | 2 | 3008 | 334 |
| International Journal of Computational Methods | 453 | 18 | 8 | 10 | 18 | 0 | 0 | 1 | 2 | 3781 | 469 |
| Metro Report International | 445 | 20 | 5 | 15 | 20 | 0 | 0 | 1 | 1 | 3967 | 511 |
| Strathroy | 240 | 8 | 3 | 5 | 8 | 0 | 0 | 0 | 0 | 1809 | 198 |
| 2006–07 Czech Extraliga season | 266 | 10 | 4 | 6 | 10 | 1 | 0 | 3 | 5 | 2508 | 305 |
| Good Morning Gitmo | 385 | 17 | 6 | 11 | 17 | 0 | 0 | 2 | 8 | 3944 | 449 |
| Czechy, Łódź Voivodeship | 262 | 9 | 5 | 4 | 9 | 0 | 0 | 7 | 6 | 2682 | 284 |
| Live at Gotham Hall | 206 | 10 | 4 | 6 | 10 | 0 | 0 | 1 | 3 | 2172 | 262 |
| Babaghuq | 284 | 16 | 3 | 13 | 16 | 0 | 0 | 0 | 0 | 2746 | 372 |
| Sōsei no Taiga | 410 | 10 | 7 | 3 | 10 | 1 | 0 | 5 | 4 | 2384 | 293 |
| Gauthier Grumier | 307 | 10 | 7 | 3 | 10 | 1 | 0 | 2 | 5 | 2704 | 292 |
| York Conferences | 799 | 32 | 14 | 18 | 31 | 1 | 0 | 7 | 15 | 8392 | 810 |
| Lichen myxedematosus | 412 | 9 | 1 | 8 | 9 | 0 | 0 | 0 | 0 | 2104 | 234 |
| Chandrasekar Ganapathy | 560 | 22 | 11 | 11 | 22 | 1 | 0 | 4 | 10 | 5156 | 576 |
| Diabolus Arcanium | 889 | 43 | 8 | 35 | 43 | 2 | 0 | 1 | 3 | 8489 | 1052 |
| Matching Tye | 243 | 10 | 6 | 4 | 10 | 0 | 0 | 9 | 4 | 2426 | 234 |
| Bangecuo | 458 | 24 | 17 | 7 | 21 | 0 | 0 | 4 | 5 | 5184 | 618 |
| NASCAR on television and radio | 1492 | 59 | 21 | 38 | 59 | 3 | 0 | 12 | 23 | 14754 | 1625 |
| Donald Keith Hummel | 904 | 41 | 24 | 17 | 41 | 1 | 0 | 4 | 7 | 9041 | 1077 |
| Bligny | 288 | 16 | 7 | 9 | 16 | 0 | 0 | 0 | 0 | 3706 | 381 |
| Al-Ghazaly High School | 1004 | 40 | 13 | 27 | 40 | 1 | 0 | 8 | 12 | 9302 | 1058 |
| Fuddy Meers | 500 | 22 | 4 | 18 | 22 | 0 | 0 | 2 | 6 | 4514 | 570 |
| Fake blog | 596 | 26 | 1 | 25 | 26 | 0 | 0 | 0 | 0 | 5448 | 632 |
| Otto Eberhardt Patronenfabrik | 674 | 32 | 18 | 14 | 32 | 1 | 0 | 3 | 8 | 8125 | 826 |
| E-Tabs | 920 | 50 | 13 | 37 | 50 | 1 | 0 | 2 | 5 | 9970 | 1248 |
| Bar Siman Tov | 200 | 9 | 3 | 6 | 9 | 0 | 0 | 0 | 0 | 2181 | 237 |
| Anna Sissak-Bardizbanian | 458 | 16 | 9 | 7 | 16 | 0 | 0 | 1 | 2 | 3428 | 412 |
| Euan Macdonald | 921 | 30 | 14 | 16 | 30 | 0 | 0 | 5 | 10 | 7144 | 824 |
| Indianapolis Airport (disambiguation) | 618 | 40 | 31 | 9 | 20 | 0 | 0 | 0 | 0 | 9129 | 1008 |
| Sundås battery | 1595 | 71 | 37 | 34 | 71 | 0 | 0 | 8 | 21 | 15546 | 1884 |
| Arrow in the Blue | 204 | 6 | 2 | 4 | 6 | 0 | 0 | 2 | 5 | 1416 | 168 |
| Legatissimo | 445 | 14 | 5 | 9 | 12 | 2 | 0 | 2 | 4 | 3254 | 394 |
| Vern Clevenger | 574 | 29 | 17 | 12 | 29 | 1 | 0 | 3 | 10 | 5996 | 741 |
| St. Andrew's College, Aurora | 554 | 23 | 11 | 12 | 23 | 0 | 0 | 2 | 3 | 4879 | 617 |
| Honnedaga Brook | 202 | 10 | 6 | 4 | 10 | 0 | 0 | 3 | 4 | 2143 | 241 |
| Prajñakaragupta | 1156 | 39 | 18 | 21 | 39 | 3 | 0 | 4 | 6 | 9492 | 1179 |
| Abdol-samad Mirza Ezz ed-Dowleh | 748 | 36 | 19 | 17 | 36 | 0 | 0 | 5 | 18 | 9457 | 1059 |
| Maurice Hankey, 1st Baron Hankey | 1198 | 47 | 11 | 36 | 47 | 0 | 0 | 2 | 3 | 10938 | 1230 |
| NeverForget84.com | 302 | 10 | 1 | 9 | 10 | 0 | 0 | 1 | 2 | 2541 | 282 |
| 1967 Baylor Bears football team | 692 | 28 | 14 | 14 | 28 | 5 | 0 | 2 | 6 | 6605 | 780 |
| Bashirabad, Razavi Khorasan | 329 | 14 | 7 | 7 | 14 | 1 | 0 | 1 | 2 | 3740 | 382 |
| Seinäjoki railway station | 678 | 28 | 18 | 10 | 28 | 1 | 0 | 2 | 5 | 5871 | 770 |
| 2019 Fed Cup World Group II play-offs | 863 | 26 | 5 | 21 | 26 | 8 | 0 | 5 | 9 | 7613 | 758 |
| Shigeru Takada | 355 | 14 | 11 | 3 | 14 | 0 | 0 | 2 | 7 | 3932 | 416 |
| Lutra simplicidens | 412 | 15 | 4 | 11 | 15 | 0 | 0 | 1 | 3 | 3272 | 408 |
| Free (Kid Cudi album) | 790 | 33 | 10 | 23 | 33 | 1 | 0 | 2 | 4 | 6903 | 842 |
| Huntersville, North Carolina | 309 | 11 | 7 | 4 | 11 | 0 | 0 | 6 | 7 | 2678 | 284 |
| Ray Hunt (footballer) | 712 | 26 | 11 | 15 | 26 | 4 | 0 | 11 | 14 | 7243 | 759 |
| Jaroslav Cejp | 475 | 17 | 8 | 9 | 17 | 3 | 0 | 4 | 8 | 4066 | 512 |
| Nizhny Begenyash | 245 | 14 | 9 | 5 | 11 | 1 | 0 | 1 | 2 | 3015 | 380 |
| Tommy Comerford | 430 | 16 | 4 | 12 | 16 | 0 | 0 | 2 | 5 | 3763 | 445 |
| Jeff Maurer | 302 | 14 | 7 | 7 | 14 | 0 | 0 | 1 | 2 | 3006 | 369 |
| Great Mosque of Banten | 361 | 16 | 8 | 8 | 16 | 1 | 0 | 5 | 7 | 4351 | 465 |
| Happily Ever After (song) | 381 | 13 | 3 | 10 | 9 | 3 | 0 | 2 | 4 | 3106 | 358 |
| Henry Steel | 220 | 8 | 4 | 4 | 8 | 0 | 0 | 3 | 5 | 2599 | 245 |
| OK (The Fall of Troy album) | 527 | 19 | 3 | 16 | 19 | 1 | 0 | 4 | 8 | 4306 | 510 |
| Jan-Olof Svantesson | 296 | 13 | 4 | 9 | 13 | 0 | 0 | 2 | 6 | 3087 | 345 |
| Dale, Ontario | 475 | 22 | 11 | 11 | 22 | 2 | 0 | 6 | 7 | 4891 | 550 |
| Fun in Acapulco (soundtrack) | 490 | 22 | 11 | 11 | 22 | 1 | 0 | 6 | 14 | 5922 | 712 |
| Polish–Lithuanian relations during World War II | 543 | 19 | 5 | 14 | 19 | 2 | 0 | 0 | 0 | 4998 | 499 |
| Beam (music) | 466 | 18 | 0 | 18 | 18 | 1 | 0 | 0 | 0 | 3351 | 430 |
| Petropedetes palmipes | 224 | 9 | 3 | 6 | 9 | 1 | 0 | 0 | 0 | 1756 | 224 |
| 2023–24 San Jose State Spartans women's basketball team | 351 | 11 | 8 | 3 | 11 | 1 | 0 | 2 | 3 | 3033 | 334 |
| Mark Andrus | 1526 | 53 | 27 | 26 | 48 | 1 | 0 | 3 | 8 | 12230 | 1443 |
| Kabulkan Doaku | 231 | 10 | 7 | 3 | 10 | 0 | 0 | 1 | 3 | 2111 | 260 |
| Jack Parkinson (basketball) | 323 | 10 | 5 | 5 | 10 | 2 | 0 | 4 | 5 | 3317 | 363 |
| Kathleen Clark (radiographer) | 284 | 9 | 2 | 7 | 9 | 0 | 0 | 2 | 2 | 2310 | 270 |
| Frank Cooper III | 253 | 13 | 7 | 6 | 13 | 0 | 0 | 0 | 0 | 2596 | 328 |
| Collores | 364 | 26 | 17 | 9 | 26 | 0 | 0 | 0 | 0 | 6650 | 639 |
| Marciano della Chiana | 585 | 27 | 18 | 9 | 20 | 0 | 0 | 7 | 7 | 5786 | 676 |
| 2018 Major League Baseball draft | 1004 | 39 | 10 | 29 | 39 | 3 | 0 | 7 | 14 | 9042 | 1065 |
| Rai people | 1010 | 52 | 21 | 31 | 52 | 1 | 0 | 1 | 3 | 9915 | 1276 |
| Where Did You Go | 434 | 18 | 7 | 11 | 18 | 1 | 0 | 4 | 11 | 6124 | 547 |
| Rhys Ernst | 346 | 13 | 3 | 10 | 13 | 0 | 0 | 0 | 0 | 2615 | 327 |
| Andy Williams | 644 | 18 | 5 | 13 | 18 | 7 | 0 | 6 | 9 | 4780 | 534 |
| Trochiscanthes | 273 | 12 | 1 | 11 | 12 | 2 | 0 | 0 | 0 | 2086 | 288 |
| Paramnesia | 350 | 12 | 2 | 10 | 10 | 1 | 0 | 0 | 0 | 2334 | 298 |
| Joe Lane (footballer) | 1737 | 62 | 21 | 41 | 62 | 10 | 0 | 12 | 25 | 15362 | 1821 |
| Underneath (Tarja song) | 463 | 21 | 13 | 8 | 21 | 3 | 0 | 3 | 4 | 4286 | 540 |
| Lev Urusov | 277 | 11 | 6 | 5 | 11 | 0 | 0 | 3 | 9 | 3471 | 382 |
| Barbee (singer) | 486 | 21 | 6 | 15 | 21 | 0 | 0 | 0 | 0 | 4025 | 506 |
| Dangkongfah Kiatpetnoi Gym | 263 | 8 | 5 | 3 | 8 | 0 | 0 | 3 | 1 | 2254 | 231 |
| Meryla, New South Wales | 270 | 12 | 5 | 7 | 12 | 1 | 0 | 3 | 6 | 2515 | 303 |
| Stay Tooned! (video game) | 341 | 12 | 3 | 9 | 12 | 0 | 0 | 1 | 2 | 2929 | 326 |
| 1993 Real Tennis World Championship | 334 | 13 | 7 | 6 | 13 | 2 | 0 | 1 | 1 | 3009 | 350 |
| Cathcart Castle | 257 | 9 | 3 | 6 | 9 | 0 | 0 | 3 | 5 | 2214 | 263 |
| Augustus Garland House | 602 | 21 | 9 | 12 | 21 | 0 | 0 | 3 | 8 | 5310 | 575 |
| Chambersburg, Trenton, New Jersey | 913 | 39 | 20 | 19 | 39 | 0 | 0 | 6 | 14 | 8228 | 1034 |
| John Edward King | 214 | 12 | 8 | 4 | 12 | 0 | 0 | 2 | 2 | 3050 | 391 |
| F. Percy Smith | 229 | 8 | 1 | 7 | 8 | 0 | 0 | 2 | 2 | 2308 | 286 |
| Benjamin Morton House | 634 | 25 | 13 | 12 | 25 | 0 | 0 | 5 | 9 | 5928 | 687 |
| Dermotextile | 1202 | 45 | 2 | 43 | 45 | 0 | 0 | 0 | 0 | 9620 | 1161 |
| Haunted swing | 438 | 15 | 5 | 10 | 15 | 1 | 0 | 1 | 2 | 3576 | 425 |
| A Um Deus Desconhecido | 284 | 9 | 0 | 9 | 9 | 0 | 0 | 1 | 1 | 2140 | 243 |
| Love Travels | 487 | 18 | 7 | 11 | 18 | 3 | 0 | 2 | 4 | 3871 | 463 |
| 2016–17 CERH European League | 429 | 15 | 6 | 9 | 15 | 0 | 0 | 3 | 7 | 4232 | 464 |
| Curse of the Crystal Coconut | 361 | 11 | 5 | 6 | 11 | 1 | 0 | 1 | 2 | 2335 | 283 |
| Zafrul Ehsan | 839 | 27 | 18 | 9 | 27 | 0 | 0 | 12 | 18 | 7852 | 848 |
| Basket Ravenna Piero Manetti | 302 | 12 | 6 | 6 | 12 | 0 | 0 | 0 | 0 | 2549 | 303 |
| Franklin Printing House | 1227 | 42 | 20 | 22 | 40 | 2 | 0 | 9 | 17 | 10117 | 1166 |
| Fencing at the 1956 Summer Olympics – Women's foil | 229 | 9 | 0 | 9 | 9 | 3 | 0 | 2 | 3 | 1921 | 229 |
| Chrysler LA engine | 1210 | 45 | 17 | 28 | 45 | 3 | 0 | 6 | 17 | 10515 | 1196 |
| Kjell Rosén | 365 | 16 | 8 | 8 | 16 | 0 | 0 | 3 | 3 | 3557 | 448 |
| Zhizdra (river) | 577 | 31 | 12 | 19 | 31 | 2 | 0 | 4 | 5 | 5918 | 750 |
| Gallimard (disambiguation) | 590 | 24 | 13 | 11 | 24 | 0 | 0 | 2 | 8 | 8918 | 823 |
| Waves Are Dancing | 429 | 13 | 5 | 8 | 13 | 0 | 0 | 3 | 5 | 3605 | 357 |
| Melaleuca dichroma | 217 | 7 | 1 | 6 | 7 | 0 | 0 | 1 | 2 | 1428 | 164 |
| Burke River | 205 | 11 | 7 | 4 | 11 | 0 | 0 | 1 | 3 | 2610 | 277 |
| Michel Françaix | 209 | 8 | 4 | 4 | 8 | 0 | 0 | 2 | 4 | 1930 | 238 |
| Payday Music Publishing | 592 | 27 | 16 | 11 | 27 | 0 | 0 | 2 | 4 | 5709 | 732 |
| 1980–81 NHL season | 300 | 11 | 8 | 3 | 11 | 1 | 0 | 2 | 4 | 2734 | 315 |
| Leslie M. Scott | 1038 | 42 | 25 | 17 | 42 | 0 | 0 | 13 | 21 | 10278 | 1257 |
| Gene Dusan | 1154 | 35 | 16 | 19 | 35 | 4 | 0 | 15 | 23 | 9654 | 1058 |
| Sōjirō Motoki | 1154 | 51 | 29 | 22 | 51 | 1 | 0 | 2 | 6 | 10878 | 1340 |
| Xi (letter) | 413 | 22 | 7 | 15 | 22 | 0 | 0 | 0 | 0 | 4177 | 530 |
| Dimethyldioctadecylammonium chloride | 969 | 26 | 3 | 23 | 25 | 3 | 0 | 0 | 0 | 6185 | 690 |
| Real-time transcription | 455 | 17 | 2 | 15 | 17 | 0 | 0 | 1 | 3 | 3766 | 451 |
| VyStar Ballpark | 279 | 11 | 8 | 3 | 11 | 0 | 0 | 1 | 1 | 2282 | 289 |
| Tomas Batilo-class patrol craft | 376 | 14 | 2 | 12 | 14 | 3 | 0 | 1 | 2 | 2914 | 343 |
| Tamura Shrine | 608 | 30 | 9 | 21 | 30 | 0 | 0 | 4 | 3 | 6036 | 747 |
| Anbinnagaram | 306 | 15 | 4 | 11 | 14 | 1 | 0 | 2 | 5 | 3088 | 370 |
| Edoardo Ricci | 423 | 12 | 10 | 2 | 12 | 0 | 0 | 9 | 11 | 3548 | 419 |
| Christiane Klapisch-Zuber | 487 | 19 | 3 | 16 | 19 | 0 | 0 | 3 | 6 | 4869 | 578 |
| Syracuse Jazz Festival | 252 | 6 | 4 | 2 | 6 | 0 | 0 | 4 | 4 | 1727 | 180 |
| Han Hoogerbrugge | 646 | 26 | 13 | 13 | 26 | 0 | 0 | 3 | 6 | 5654 | 678 |
| Bert Wemp | 1001 | 42 | 21 | 21 | 42 | 1 | 1 | 10 | 16 | 8997 | 1137 |
| Insect olfaction | 2578 | 98 | 9 | 89 | 98 | 4 | 0 | 0 | 0 | 20757 | 2476 |
| Wales Rally GB | 1239 | 39 | 18 | 21 | 39 | 1 | 0 | 11 | 21 | 11194 | 1171 |
| Bayanmönkhiin Gantogtokh | 277 | 9 | 4 | 5 | 9 | 0 | 0 | 3 | 5 | 2366 | 263 |
| Patsy Smart | 1201 | 58 | 35 | 23 | 58 | 1 | 0 | 19 | 30 | 20152 | 1993 |
| 46 Berkeley Square | 1952 | 79 | 26 | 53 | 79 | 6 | 0 | 13 | 22 | 18237 | 2170 |
| Rita Azevedo Gomes | 278 | 8 | 2 | 6 | 8 | 1 | 0 | 1 | 2 | 2160 | 227 |
| Koningic acid | 349 | 12 | 1 | 11 | 12 | 0 | 0 | 0 | 0 | 2632 | 306 |
| Messer Street Grounds | 868 | 28 | 10 | 18 | 28 | 1 | 0 | 9 | 9 | 7210 | 798 |
| Breshk | 468 | 19 | 7 | 12 | 19 | 0 | 0 | 1 | 1 | 3738 | 487 |
| Krishan Lal Panwar | 293 | 15 | 11 | 4 | 15 | 0 | 0 | 0 | 0 | 2920 | 386 |
| Stow Maries | 588 | 28 | 9 | 19 | 28 | 0 | 0 | 4 | 11 | 5723 | 693 |
| Anisuthide | 373 | 17 | 7 | 10 | 17 | 0 | 0 | 1 | 2 | 3326 | 424 |
| Ertapenem | 642 | 27 | 6 | 21 | 27 | 0 | 0 | 2 | 4 | 5865 | 706 |
| List of sophisti-pop artists | 408 | 18 | 4 | 14 | 18 | 0 | 0 | 1 | 3 | 3771 | 482 |
| Sydney Metro Metropolis Stock | 715 | 23 | 6 | 17 | 23 | 3 | 0 | 7 | 10 | 6533 | 669 |

---

## Totals — 1000 pages, 25,009 entities (expanded pack: +org/group/event/product/work; tightened fuzzy)

| metric | value |
|---|---|
| pages | 1000 |
| entities | 25,009 (avg 25.0/page) |
| **typed** | 9,807 (39.2%) |
| governing verb | 24,583 (98.3%) |
| item association | 6,391 (25.6%) |
| free structured-output tokens | 5,907,712 verbose · 678,579 compact |

### Before / after (same 1000-page protocol, vs `BENCHMARK_military_baseline.md`)
| | military pack | expanded pack |
|---|---|---|
| typed-rate | 28.2% | **39.2%** (+11.0 pts) |
| governing verb | 97.9% | 98.3% |
| item association | 21.4% | 25.6% |

Adding the free NER-backed scopes (org/group/event/product/work) lifted typed-rate
**28% → 39%** at zero extra cost. Element extraction stays near-complete
(~98% governing-verb). The goblin produced ~679K compact /
~5.9M verbose tokens of structured output across 1000 pages for $0.
