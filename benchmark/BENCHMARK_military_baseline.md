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
| Kelly Guard | 392 | 11 | 4 | 7 | 11 | 0 | 0 | 2 | 4 | 2738 | 302 |
| All Basotho Convention | 331 | 16 | 6 | 10 | 16 | 0 | 0 | 2 | 4 | 3491 | 422 |
| Joseph J. Bartlett | 375 | 11 | 8 | 3 | 11 | 0 | 0 | 2 | 2 | 3214 | 383 |
| Biathlon World Championships 2012 – Mixed relay | 517 | 18 | 7 | 11 | 18 | 1 | 0 | 5 | 10 | 4912 | 544 |
| PCSFN Fitness Films | 1750 | 77 | 11 | 66 | 77 | 3 | 0 | 3 | 9 | 15950 | 1958 |
| Carbothermic reaction | 838 | 40 | 17 | 23 | 40 | 3 | 0 | 0 | 0 | 8126 | 1030 |
| Mountain railways of India | 931 | 33 | 6 | 27 | 33 | 1 | 0 | 1 | 2 | 7942 | 868 |
| Satchinez swamps | 351 | 11 | 6 | 5 | 11 | 1 | 0 | 2 | 4 | 2556 | 298 |
| Terri Collins | 1287 | 49 | 20 | 29 | 49 | 2 | 0 | 9 | 19 | 10797 | 1303 |
| David Weissman | 449 | 21 | 7 | 14 | 21 | 1 | 0 | 1 | 2 | 4386 | 521 |
| Sethianism | 404 | 14 | 2 | 12 | 14 | 1 | 0 | 2 | 6 | 3362 | 428 |
| Mount Pleasant, Iowa | 230 | 11 | 3 | 8 | 11 | 0 | 0 | 3 | 4 | 2368 | 275 |
| Steve Mould | 249 | 8 | 1 | 7 | 8 | 0 | 0 | 1 | 2 | 1889 | 220 |
| Meritas (cloth) | 533 | 22 | 6 | 16 | 22 | 0 | 0 | 2 | 5 | 4615 | 560 |
| List of television programs: F | 252 | 12 | 1 | 11 | 12 | 0 | 0 | 0 | 0 | 2149 | 294 |
| 2014–15 Saint Joseph's Hawks men's basketball team | 436 | 16 | 5 | 11 | 14 | 0 | 1 | 2 | 5 | 3721 | 472 |
| The Frightened Hares | 301 | 10 | 1 | 9 | 10 | 0 | 0 | 1 | 1 | 1862 | 243 |
| Parvīz | 731 | 32 | 14 | 18 | 32 | 1 | 0 | 0 | 0 | 6794 | 783 |
| Ochre-breasted tanager | 420 | 17 | 4 | 13 | 17 | 0 | 0 | 0 | 0 | 3621 | 430 |
| A Murder in the Park | 331 | 13 | 4 | 9 | 13 | 0 | 0 | 3 | 9 | 3508 | 371 |
| Ludovico Marracci | 362 | 15 | 2 | 13 | 15 | 1 | 0 | 2 | 2 | 3537 | 422 |
| Hypothalamospinal tract | 437 | 13 | 1 | 12 | 13 | 1 | 0 | 0 | 0 | 3342 | 360 |
| St Macartan's College | 351 | 19 | 6 | 13 | 19 | 0 | 0 | 1 | 2 | 3457 | 464 |
| McIntosh & Otis | 220 | 10 | 3 | 7 | 10 | 0 | 0 | 1 | 3 | 1916 | 246 |
| Dargaville Primary School | 905 | 31 | 5 | 26 | 31 | 0 | 0 | 7 | 10 | 6833 | 805 |
| List of cities in Toyama Prefecture by population | 435 | 18 | 1 | 17 | 18 | 2 | 0 | 1 | 3 | 3736 | 446 |
| Exoneura nigrofulva | 204 | 7 | 4 | 3 | 7 | 0 | 0 | 1 | 2 | 1514 | 183 |
| Baji Rao | 285 | 11 | 6 | 5 | 11 | 0 | 0 | 3 | 7 | 4164 | 394 |
| Funktasztikus | 280 | 12 | 3 | 9 | 12 | 0 | 0 | 0 | 0 | 2153 | 290 |
| Saffron Technology | 1361 | 60 | 14 | 46 | 60 | 0 | 0 | 2 | 5 | 12730 | 1561 |
| DYAB-AM | 1061 | 45 | 14 | 31 | 41 | 0 | 0 | 8 | 15 | 10106 | 1221 |
| 2011 AFL Mark of the Year | 503 | 14 | 3 | 11 | 14 | 2 | 0 | 8 | 12 | 4078 | 419 |
| Rock-cut Church of Rind | 459 | 16 | 3 | 13 | 16 | 0 | 0 | 0 | 0 | 3921 | 438 |
| Crisis Response Operation Core | 484 | 21 | 7 | 14 | 21 | 3 | 0 | 1 | 3 | 4504 | 540 |
| Tamale, Nurses Training College | 677 | 32 | 5 | 27 | 32 | 2 | 0 | 1 | 3 | 6487 | 817 |
| Jimna Single Men's Barracks | 220 | 3 | 1 | 2 | 3 | 0 | 0 | 3 | 2 | 993 | 90 |
| National Confederation of Haitian Vodou | 321 | 13 | 1 | 12 | 13 | 0 | 0 | 1 | 2 | 2892 | 330 |
| H. F. Arthur Schoenfeld | 487 | 15 | 8 | 7 | 15 | 1 | 0 | 4 | 6 | 4654 | 543 |
| Kullal Chickappu Naik | 277 | 10 | 3 | 7 | 10 | 0 | 0 | 1 | 2 | 2124 | 278 |
| Efren C. Piñon | 459 | 20 | 10 | 10 | 20 | 0 | 0 | 7 | 9 | 4832 | 547 |
| Mentalism (disambiguation) | 456 | 22 | 3 | 19 | 22 | 0 | 0 | 0 | 0 | 5249 | 544 |
| Stonewall Terrace, Dallas | 376 | 18 | 8 | 10 | 18 | 1 | 0 | 0 | 0 | 3519 | 444 |
| Kök-Janggak | 643 | 27 | 8 | 19 | 27 | 1 | 0 | 1 | 2 | 6406 | 674 |
| Wheels Stop | 517 | 17 | 6 | 11 | 17 | 0 | 0 | 2 | 5 | 4221 | 470 |
| Fred August Moss | 463 | 18 | 3 | 15 | 18 | 0 | 0 | 4 | 8 | 4140 | 498 |
| Daniel Rose | 768 | 33 | 16 | 17 | 11 | 0 | 0 | 7 | 20 | 10683 | 1034 |
| John Post | 243 | 9 | 1 | 8 | 9 | 0 | 0 | 2 | 5 | 2190 | 284 |
| Guru (2006 film) | 884 | 46 | 13 | 33 | 46 | 1 | 0 | 3 | 8 | 9580 | 1152 |
| Road in Häme | 876 | 36 | 5 | 31 | 36 | 0 | 0 | 4 | 10 | 7489 | 913 |
| Budapest's Palace District | 961 | 39 | 17 | 22 | 39 | 0 | 0 | 5 | 10 | 10347 | 1195 |
| Advances in Electrical and Computer Engineering | 416 | 16 | 1 | 15 | 16 | 0 | 0 | 2 | 3 | 3547 | 422 |
| Fannie Lovering Skinner | 488 | 20 | 8 | 12 | 20 | 1 | 0 | 3 | 7 | 4215 | 517 |
| Italian hot dog | 435 | 20 | 8 | 12 | 20 | 0 | 0 | 1 | 4 | 4495 | 495 |
| Military funerals in the United States | 1691 | 70 | 16 | 54 | 70 | 7 | 0 | 2 | 5 | 16061 | 1822 |
| Friedrich Fehleisen | 438 | 17 | 7 | 10 | 17 | 1 | 0 | 2 | 4 | 3761 | 456 |
| Seikkyi Kanaungto Township | 693 | 25 | 4 | 21 | 18 | 3 | 0 | 0 | 0 | 5088 | 634 |
| Akua Sakyiwaa Ahenkorah | 226 | 9 | 4 | 5 | 9 | 1 | 0 | 0 | 0 | 1870 | 226 |
| John Rinehart Blue | 1509 | 56 | 22 | 34 | 56 | 1 | 2 | 15 | 25 | 14215 | 1678 |
| Claws Mail | 320 | 14 | 3 | 11 | 14 | 0 | 0 | 0 | 0 | 2723 | 334 |
| La Pierreuse | 247 | 12 | 5 | 7 | 12 | 1 | 0 | 0 | 0 | 2381 | 293 |
| Mark Knopfler | 1619 | 72 | 25 | 47 | 72 | 8 | 0 | 11 | 23 | 16850 | 1930 |
| Kaija Koo | 1027 | 33 | 12 | 21 | 33 | 2 | 0 | 6 | 16 | 8451 | 919 |
| Women in Film & Video Film Festival D.C. | 223 | 10 | 1 | 9 | 10 | 0 | 0 | 2 | 3 | 2149 | 272 |
| Army Battle Command System | 565 | 20 | 6 | 14 | 18 | 1 | 0 | 0 | 0 | 4766 | 542 |
| 2011 Tour of Flanders | 280 | 14 | 3 | 11 | 14 | 4 | 0 | 1 | 3 | 2778 | 342 |
| United States Second Fleet | 1040 | 38 | 20 | 18 | 38 | 6 | 0 | 5 | 9 | 9999 | 1062 |
| Rodeløkka Line | 738 | 27 | 6 | 21 | 27 | 2 | 0 | 8 | 15 | 6390 | 729 |
| Aja! | 264 | 8 | 2 | 6 | 8 | 0 | 0 | 2 | 5 | 1972 | 220 |
| Raozan Government College | 716 | 25 | 9 | 16 | 25 | 2 | 0 | 3 | 7 | 6102 | 729 |
| Pir Kohan | 218 | 12 | 7 | 5 | 12 | 1 | 0 | 1 | 2 | 2693 | 318 |
| Sean Delaney | 231 | 8 | 3 | 5 | 8 | 0 | 0 | 1 | 3 | 2298 | 221 |
| Rob Walker (poet) | 326 | 14 | 5 | 9 | 14 | 0 | 0 | 2 | 4 | 2697 | 366 |
| Ishkoman Aghost Pass | 376 | 19 | 9 | 10 | 19 | 3 | 0 | 0 | 0 | 4083 | 467 |
| Sri Lanka women's cricket team in New Zealand in 2024–25 | 351 | 11 | 4 | 7 | 11 | 1 | 0 | 2 | 5 | 2762 | 316 |
| Oscar Brown | 385 | 17 | 6 | 11 | 17 | 3 | 0 | 2 | 3 | 3836 | 474 |
| Keeling's Guide to Japan | 736 | 44 | 15 | 29 | 43 | 2 | 0 | 3 | 8 | 9309 | 1152 |
| L'arbitro (1974 film) | 315 | 12 | 5 | 7 | 12 | 0 | 0 | 1 | 3 | 2742 | 314 |
| Piet Rietveld | 278 | 12 | 2 | 10 | 12 | 0 | 0 | 2 | 3 | 2904 | 360 |
| Revolution Tour | 333 | 13 | 0 | 13 | 13 | 0 | 0 | 1 | 2 | 2954 | 338 |
| 2013–14 ISU Speed Skating World Cup – World Cup 4 – Women's team pursuit | 367 | 12 | 7 | 5 | 12 | 1 | 0 | 2 | 4 | 3243 | 384 |
| Kuyularonu Mosque | 691 | 27 | 5 | 22 | 27 | 2 | 0 | 7 | 11 | 5838 | 696 |
| Svend Borchmann Hersleb Vogt | 1556 | 60 | 19 | 41 | 60 | 1 | 0 | 12 | 17 | 13476 | 1667 |
| Chamaesphecia schmidtiiformis | 310 | 17 | 9 | 8 | 13 | 0 | 0 | 0 | 0 | 2881 | 412 |
| Supranational Venezuela 2022 | 924 | 39 | 21 | 18 | 39 | 3 | 0 | 7 | 16 | 9338 | 1088 |
| KABY | 399 | 18 | 10 | 8 | 16 | 2 | 0 | 0 | 0 | 4340 | 468 |
| Truth and Justice (disambiguation) | 424 | 24 | 7 | 17 | 24 | 0 | 0 | 3 | 8 | 6802 | 664 |
| Serrodes mediopallens | 292 | 15 | 8 | 7 | 15 | 0 | 0 | 1 | 3 | 2832 | 374 |
| San Antonio Commanders | 637 | 25 | 7 | 18 | 25 | 3 | 0 | 6 | 13 | 5937 | 670 |
| D.C. (TV series) | 591 | 20 | 7 | 13 | 20 | 1 | 0 | 4 | 10 | 4972 | 569 |
| Violetta Bida | 386 | 11 | 7 | 4 | 11 | 1 | 0 | 4 | 9 | 3352 | 366 |
| 1996 UCF Golden Knights football team | 965 | 41 | 11 | 30 | 41 | 3 | 0 | 6 | 12 | 9030 | 1094 |
| Angels (Amy Grant song) | 508 | 24 | 2 | 22 | 24 | 2 | 0 | 1 | 2 | 4881 | 576 |
| Texas's 31st Senate district | 558 | 9 | 5 | 4 | 9 | 3 | 0 | 0 | 0 | 4445 | 312 |
| La Revancha mine | 598 | 21 | 13 | 8 | 19 | 0 | 0 | 4 | 8 | 4477 | 542 |
| Listed buildings in Cleobury Mortimer | 1048 | 54 | 18 | 36 | 54 | 3 | 0 | 0 | 0 | 11760 | 1331 |
| Conservator of the peace | 212 | 11 | 0 | 11 | 7 | 0 | 0 | 0 | 0 | 2184 | 252 |
| Moonlight Madness (Teri DeSario album) | 316 | 14 | 5 | 9 | 14 | 0 | 0 | 1 | 4 | 2797 | 346 |
| Calathea lanicaulis | 217 | 8 | 2 | 6 | 8 | 0 | 0 | 0 | 0 | 1653 | 204 |
| Jason Somerville (engineer) | 224 | 7 | 2 | 5 | 7 | 0 | 0 | 1 | 2 | 1639 | 190 |
| Charles Whitley | 1236 | 40 | 23 | 17 | 40 | 0 | 0 | 16 | 27 | 10409 | 1155 |
| Salvatierra (comarca) | 245 | 10 | 3 | 7 | 9 | 1 | 0 | 0 | 0 | 1725 | 233 |
| 2024–25 Florida Gulf Coast Eagles men's basketball team | 321 | 11 | 7 | 4 | 11 | 1 | 0 | 1 | 2 | 2842 | 326 |
| Xylophanes hannemanni | 558 | 27 | 11 | 16 | 27 | 1 | 0 | 1 | 2 | 5330 | 667 |
| Gordon Hensley | 908 | 37 | 11 | 26 | 37 | 0 | 0 | 3 | 9 | 9139 | 974 |
| 2022 Inline Speed Skating World Championships | 459 | 17 | 8 | 9 | 17 | 0 | 0 | 4 | 4 | 4399 | 516 |
| List of Major League Baseball career extra base hits leaders | 708 | 32 | 13 | 19 | 32 | 4 | 0 | 0 | 0 | 7024 | 794 |
| Stations of the Crass | 1721 | 62 | 21 | 41 | 62 | 4 | 0 | 8 | 18 | 15664 | 1705 |
| Azinhaga | 339 | 18 | 3 | 15 | 18 | 1 | 0 | 1 | 3 | 4217 | 446 |
| Femi Adebayo | 582 | 21 | 4 | 17 | 21 | 3 | 0 | 7 | 10 | 5718 | 611 |
| Unexpected Productions | 325 | 14 | 5 | 9 | 14 | 0 | 0 | 0 | 0 | 3048 | 361 |
| Suite (hotel) | 1298 | 59 | 8 | 51 | 53 | 8 | 0 | 0 | 0 | 12432 | 1464 |
| 1976 WTA Westchester Invitational | 539 | 20 | 6 | 14 | 20 | 2 | 0 | 3 | 5 | 4926 | 537 |
| Basketball National League | 451 | 14 | 3 | 11 | 14 | 1 | 0 | 2 | 4 | 3483 | 374 |
| Gitanas Nausėda | 1192 | 45 | 18 | 27 | 43 | 3 | 0 | 11 | 27 | 11346 | 1321 |
| Shatta Wale | 2464 | 89 | 29 | 60 | 89 | 3 | 0 | 17 | 37 | 25868 | 2722 |
| You Baby | 699 | 28 | 7 | 21 | 28 | 4 | 0 | 2 | 5 | 6126 | 740 |
| Carlos Guastavino | 1163 | 53 | 20 | 33 | 53 | 2 | 0 | 2 | 2 | 11802 | 1352 |
| Crowfields Common | 308 | 14 | 3 | 11 | 14 | 0 | 0 | 0 | 0 | 2439 | 335 |
| Saratoga High School | 206 | 9 | 7 | 2 | 9 | 0 | 0 | 1 | 4 | 2418 | 258 |
| Waiting for the Punch | 242 | 11 | 2 | 9 | 11 | 2 | 0 | 1 | 2 | 2678 | 312 |
| Seven Minds | 343 | 14 | 5 | 9 | 14 | 2 | 0 | 3 | 4 | 2979 | 354 |
| Labidiaster | 414 | 18 | 5 | 13 | 18 | 1 | 0 | 2 | 2 | 3634 | 458 |
| Van Winkle's Mill Site | 1050 | 45 | 9 | 36 | 45 | 2 | 0 | 6 | 16 | 11440 | 1358 |
| Paul Hillegonds | 1116 | 50 | 16 | 34 | 50 | 2 | 0 | 11 | 26 | 11244 | 1332 |
| Harry Hartz | 213 | 4 | 1 | 3 | 4 | 0 | 0 | 3 | 3 | 1510 | 144 |
| Alexander Campbell Cameron | 426 | 13 | 7 | 6 | 13 | 0 | 0 | 8 | 11 | 3839 | 430 |
| 19th-century turnpikes in Rhode Island | 913 | 17 | 5 | 12 | 10 | 6 | 0 | 5 | 8 | 6465 | 580 |
| Belarusian dialects in Russia | 558 | 24 | 4 | 20 | 24 | 0 | 0 | 0 | 0 | 5726 | 635 |
| Shelter Bay, British Columbia | 557 | 28 | 10 | 18 | 28 | 3 | 0 | 0 | 0 | 5896 | 695 |
| Salvation (Smack album) | 305 | 14 | 3 | 11 | 14 | 0 | 0 | 1 | 2 | 2825 | 341 |
| Victoria Cross for New Zealand | 1273 | 58 | 18 | 40 | 58 | 1 | 0 | 5 | 14 | 12909 | 1502 |
| ROG Xbox Ally | 654 | 25 | 6 | 19 | 25 | 1 | 0 | 1 | 2 | 6590 | 660 |
| Chris Turner (footballer, born 1959) | 466 | 20 | 7 | 13 | 20 | 2 | 0 | 2 | 7 | 5537 | 625 |
| The Dealians | 2020 | 91 | 30 | 61 | 83 | 3 | 0 | 10 | 22 | 19890 | 2374 |
| Coolafancy | 648 | 37 | 9 | 28 | 37 | 0 | 0 | 0 | 0 | 6545 | 882 |
| Climate change in Tennessee | 429 | 16 | 4 | 12 | 16 | 0 | 0 | 1 | 2 | 3798 | 435 |
| Yeni Valide Mosque | 795 | 34 | 7 | 27 | 34 | 1 | 0 | 2 | 5 | 7750 | 912 |
| Daihatsu Tanto | 367 | 14 | 2 | 12 | 14 | 0 | 0 | 2 | 3 | 3284 | 369 |
| Sirtori | 523 | 30 | 9 | 21 | 30 | 5 | 0 | 1 | 2 | 5960 | 744 |
| One Piece season 2 | 2604 | 93 | 20 | 73 | 92 | 15 | 0 | 15 | 28 | 23070 | 2784 |
| 1951 USC Trojans baseball team | 450 | 15 | 6 | 9 | 15 | 0 | 0 | 3 | 6 | 3817 | 432 |
| Ground carriage | 460 | 17 | 2 | 15 | 17 | 1 | 0 | 1 | 4 | 3870 | 438 |
| Baird & Co | 733 | 33 | 12 | 21 | 33 | 0 | 0 | 1 | 3 | 6624 | 838 |
| 5-4-3-2-Run | 570 | 24 | 10 | 14 | 24 | 3 | 0 | 6 | 9 | 5374 | 639 |
| 2024 Rancho Santa Fe Open | 303 | 10 | 2 | 8 | 10 | 0 | 0 | 4 | 5 | 2654 | 304 |
| Man'ha Garreau-Dombasle | 674 | 28 | 12 | 16 | 28 | 0 | 0 | 8 | 15 | 8946 | 1028 |
| Shen Hongying | 1754 | 83 | 35 | 48 | 83 | 1 | 0 | 9 | 17 | 18852 | 2225 |
| 3rd Landwehr Division (German Empire) | 974 | 36 | 20 | 16 | 36 | 3 | 1 | 3 | 8 | 8468 | 1039 |
| Deuterocohnia | 350 | 14 | 4 | 10 | 14 | 0 | 0 | 0 | 0 | 2606 | 342 |
| Boguédia | 325 | 17 | 5 | 12 | 17 | 1 | 0 | 2 | 5 | 3361 | 418 |
| Rosswood, British Columbia | 305 | 18 | 3 | 15 | 18 | 3 | 0 | 0 | 0 | 3476 | 422 |
| 11th Artillery Brigade (Ukraine) | 862 | 30 | 22 | 8 | 30 | 1 | 3 | 3 | 6 | 7306 | 947 |
| Marney Cunningham | 222 | 7 | 3 | 4 | 7 | 1 | 0 | 1 | 2 | 1642 | 202 |
| Pi-Ramesses | 362 | 20 | 4 | 16 | 20 | 1 | 0 | 0 | 0 | 4181 | 476 |
| Seven trumpets | 935 | 44 | 5 | 39 | 44 | 8 | 0 | 0 | 0 | 8706 | 1074 |
| Natalia Godunko | 303 | 8 | 4 | 4 | 8 | 0 | 0 | 4 | 5 | 3336 | 332 |
| Fan Chengcheng | 263 | 12 | 2 | 10 | 12 | 0 | 0 | 2 | 4 | 2601 | 306 |
| Bill Perry (rugby union) | 253 | 10 | 4 | 6 | 10 | 1 | 0 | 3 | 4 | 2464 | 303 |
| Yesvantpur–Bidar Express | 391 | 13 | 7 | 6 | 13 | 1 | 0 | 4 | 4 | 3672 | 399 |
| Gisela C. Lebzelter | 658 | 36 | 9 | 27 | 36 | 0 | 0 | 2 | 8 | 8067 | 922 |
| Demont Mitchell | 208 | 7 | 2 | 5 | 7 | 0 | 0 | 1 | 2 | 1712 | 202 |
| Esra'a Al Shafei | 2237 | 84 | 17 | 67 | 84 | 6 | 0 | 15 | 30 | 21284 | 2332 |
| Agatha virgo | 260 | 13 | 2 | 11 | 13 | 1 | 0 | 0 | 0 | 2624 | 315 |
| Rocca Islands | 350 | 16 | 6 | 10 | 16 | 2 | 0 | 3 | 5 | 3743 | 435 |
| Abraham Lyons | 242 | 11 | 2 | 9 | 11 | 0 | 0 | 2 | 2 | 2932 | 351 |
| List of surf musicians | 309 | 10 | 2 | 8 | 10 | 0 | 0 | 0 | 0 | 1891 | 239 |
| Joe Delia | 544 | 26 | 10 | 16 | 26 | 0 | 0 | 1 | 2 | 5766 | 668 |
| Dongfeng Mengshi | 1019 | 35 | 12 | 23 | 35 | 2 | 0 | 1 | 3 | 8419 | 933 |
| House of Kalajdžieski family | 350 | 19 | 5 | 14 | 19 | 0 | 0 | 0 | 0 | 3678 | 468 |
| Aram (Nahapet) | 397 | 21 | 4 | 17 | 21 | 1 | 0 | 0 | 0 | 3866 | 505 |
| Legio III Isaura | 416 | 14 | 3 | 11 | 14 | 0 | 0 | 0 | 0 | 2997 | 353 |
| Archibald Lartey Djabatey | 955 | 39 | 14 | 25 | 39 | 0 | 0 | 6 | 13 | 8618 | 1036 |
| Daniel Chu | 979 | 43 | 14 | 29 | 43 | 0 | 0 | 9 | 19 | 10873 | 1225 |
| Greg Loewen | 223 | 12 | 3 | 9 | 12 | 0 | 0 | 0 | 0 | 2288 | 289 |
| Policy network analysis | 241 | 10 | 1 | 9 | 10 | 0 | 0 | 0 | 0 | 2266 | 255 |
| The Graph | 603 | 29 | 3 | 26 | 29 | 1 | 0 | 0 | 0 | 5442 | 712 |
| Peak halyard | 449 | 19 | 1 | 18 | 19 | 0 | 0 | 0 | 0 | 3843 | 444 |
| Janice Bolland | 210 | 6 | 3 | 3 | 6 | 0 | 0 | 3 | 6 | 1918 | 178 |
| Sarcodum | 254 | 12 | 3 | 9 | 12 | 1 | 0 | 0 | 0 | 2168 | 289 |
| Chhayanaut | 1731 | 66 | 16 | 50 | 64 | 3 | 0 | 8 | 18 | 15057 | 1804 |
| 2019 Da Nang Tennis Open | 243 | 9 | 2 | 7 | 9 | 0 | 0 | 3 | 4 | 2066 | 241 |
| Shri Venkateswara (Balaji) Temple | 373 | 14 | 6 | 8 | 14 | 1 | 0 | 1 | 1 | 3010 | 361 |
| Lutfor Rahman (footballer) | 260 | 11 | 7 | 4 | 11 | 0 | 0 | 1 | 2 | 2428 | 291 |
| Bagistanes | 838 | 32 | 10 | 22 | 32 | 3 | 0 | 1 | 2 | 6527 | 803 |
| Eriastrum diffusum | 617 | 20 | 3 | 17 | 20 | 2 | 0 | 1 | 2 | 4102 | 494 |
| À 20 ans | 302 | 13 | 5 | 8 | 13 | 1 | 0 | 2 | 4 | 2638 | 337 |
| Heaven (Bryan Adams song) | 847 | 30 | 8 | 22 | 30 | 5 | 0 | 8 | 14 | 7238 | 822 |
| Jim Hume | 333 | 13 | 1 | 12 | 13 | 0 | 0 | 1 | 2 | 2854 | 341 |
| 1832 Hungarian parliamentary election | 902 | 39 | 4 | 35 | 39 | 3 | 0 | 3 | 6 | 8068 | 959 |
| People's Action (Romania) | 314 | 10 | 4 | 6 | 10 | 0 | 0 | 1 | 2 | 2439 | 278 |
| Infiernillo (volcanic field) | 226 | 9 | 3 | 6 | 9 | 1 | 0 | 0 | 0 | 1683 | 220 |
| The Homo Handbook | 443 | 16 | 3 | 13 | 16 | 0 | 0 | 1 | 3 | 3701 | 410 |
| Ramesh Govindan | 219 | 10 | 3 | 7 | 10 | 0 | 0 | 0 | 0 | 2005 | 248 |
| Joe Lintzenich | 596 | 23 | 6 | 17 | 23 | 0 | 0 | 3 | 7 | 5225 | 628 |
| Saint Barnabas on the Desert | 524 | 20 | 5 | 15 | 20 | 2 | 0 | 11 | 13 | 5216 | 548 |
| Andover (film) | 360 | 16 | 11 | 5 | 16 | 0 | 0 | 3 | 6 | 4010 | 476 |
| George Borwick (umpire) | 1123 | 47 | 20 | 27 | 47 | 1 | 0 | 8 | 21 | 10873 | 1341 |
| Tresa Pollock | 602 | 30 | 3 | 27 | 30 | 0 | 0 | 1 | 5 | 6182 | 750 |
| Leioproctus | 242 | 10 | 4 | 6 | 10 | 0 | 0 | 0 | 0 | 2021 | 252 |
| Cats in ancient Egypt | 1579 | 72 | 16 | 56 | 69 | 1 | 0 | 5 | 11 | 14707 | 1864 |
| Saint-Stanislas-de-Kostka | 228 | 10 | 6 | 4 | 10 | 0 | 0 | 0 | 0 | 2139 | 254 |
| Juan Gazsó | 415 | 14 | 10 | 4 | 14 | 0 | 0 | 5 | 5 | 3394 | 417 |
| Nguyễn Quang Toản | 463 | 20 | 5 | 15 | 20 | 0 | 0 | 3 | 3 | 4291 | 516 |
| Trzebiszewo | 326 | 14 | 9 | 5 | 14 | 0 | 0 | 0 | 0 | 3006 | 358 |
| Midland Provisional Battalion | 902 | 32 | 20 | 12 | 32 | 3 | 1 | 1 | 1 | 8268 | 907 |
| 2017–18 LNAH season | 342 | 10 | 2 | 8 | 10 | 1 | 0 | 3 | 5 | 3079 | 314 |
| Terentius | 228 | 11 | 5 | 6 | 11 | 0 | 0 | 1 | 2 | 2296 | 279 |
| 1996 Duke Blue Devils football team | 409 | 19 | 5 | 14 | 19 | 0 | 0 | 3 | 4 | 4610 | 536 |
| Ross Benjamin | 847 | 38 | 12 | 26 | 38 | 0 | 0 | 3 | 7 | 8014 | 969 |
| Yucca | 1400 | 69 | 8 | 61 | 69 | 3 | 0 | 0 | 0 | 12940 | 1655 |
| Hi-Vis High Tea | 731 | 28 | 9 | 19 | 28 | 0 | 0 | 5 | 10 | 7373 | 822 |
| Edward House | 511 | 18 | 11 | 7 | 18 | 0 | 0 | 2 | 4 | 7436 | 712 |
| New Mexico State Road 412 | 227 | 11 | 3 | 8 | 11 | 3 | 0 | 0 | 0 | 2402 | 265 |
| Shyama Kabya | 567 | 25 | 8 | 17 | 24 | 0 | 0 | 3 | 5 | 5208 | 663 |
| Mazapil Municipality | 206 | 9 | 4 | 5 | 9 | 0 | 0 | 0 | 0 | 1825 | 229 |
| Christchurch Town Hall | 705 | 22 | 5 | 17 | 22 | 0 | 0 | 5 | 11 | 5570 | 622 |
| Kalkaman (lake) | 519 | 33 | 7 | 26 | 33 | 9 | 0 | 0 | 0 | 6341 | 795 |
| Powassan encephalitis | 815 | 39 | 7 | 32 | 39 | 0 | 0 | 2 | 6 | 7548 | 972 |
| Charlie Fowler | 490 | 11 | 4 | 7 | 11 | 1 | 0 | 5 | 5 | 2995 | 351 |
| Medium format | 781 | 31 | 3 | 28 | 31 | 6 | 0 | 0 | 0 | 7060 | 786 |
| Amy Lyford | 438 | 21 | 10 | 11 | 11 | 1 | 0 | 4 | 11 | 5525 | 603 |
| Wisconsin Badgers softball | 368 | 15 | 9 | 6 | 15 | 0 | 0 | 0 | 0 | 3099 | 400 |
| Albert Elliott | 353 | 9 | 5 | 4 | 9 | 1 | 0 | 3 | 3 | 2478 | 275 |
| Sergey Gulev | 614 | 22 | 6 | 16 | 22 | 0 | 0 | 5 | 9 | 5972 | 647 |
| Rana Crown | 469 | 18 | 3 | 15 | 18 | 0 | 0 | 1 | 3 | 3814 | 478 |
| Anna Gerresheim | 218 | 8 | 4 | 4 | 8 | 0 | 0 | 2 | 2 | 1970 | 233 |
| Povardarie | 357 | 18 | 4 | 14 | 18 | 0 | 0 | 0 | 0 | 3834 | 449 |
| Ricardo Pacheco Rodríguez | 268 | 9 | 1 | 8 | 9 | 0 | 0 | 2 | 4 | 2054 | 247 |
| Recording a Tape the Colour of the Light | 439 | 17 | 3 | 14 | 17 | 1 | 0 | 2 | 4 | 4171 | 502 |
| Lam So-wai | 471 | 16 | 6 | 10 | 16 | 0 | 0 | 2 | 6 | 4578 | 460 |
| Lo Vas a Olvidar | 598 | 20 | 4 | 16 | 18 | 1 | 0 | 2 | 3 | 4633 | 551 |
| Gaves réunis | 306 | 16 | 3 | 13 | 16 | 1 | 0 | 0 | 0 | 3086 | 384 |
| All Sports Stadium | 267 | 11 | 2 | 9 | 11 | 1 | 0 | 1 | 3 | 2248 | 275 |
| Kara (British band) | 204 | 11 | 4 | 7 | 11 | 0 | 0 | 0 | 0 | 2103 | 266 |
| Mangalam Publications | 570 | 29 | 14 | 15 | 29 | 2 | 0 | 6 | 12 | 6385 | 782 |
| Jefferson Proving Ground | 372 | 16 | 7 | 9 | 16 | 0 | 0 | 0 | 0 | 3315 | 408 |
| Fire Information for Resource Management System | 394 | 15 | 2 | 13 | 15 | 0 | 0 | 0 | 0 | 2914 | 363 |
| Zone Warrior | 379 | 19 | 4 | 15 | 19 | 0 | 0 | 1 | 2 | 3641 | 466 |
| Sailing at the 2011 Pan American Games – Laser Radial | 758 | 28 | 4 | 24 | 27 | 5 | 0 | 2 | 5 | 6230 | 740 |
| Ministry of Government Services (Quebec) | 640 | 29 | 4 | 25 | 29 | 1 | 0 | 2 | 6 | 6115 | 745 |
| World Universities Debating Championship | 467 | 18 | 3 | 15 | 18 | 2 | 0 | 3 | 8 | 4372 | 486 |
| William Meath Baker | 1819 | 73 | 25 | 48 | 66 | 2 | 0 | 13 | 21 | 16758 | 1998 |
| Public Fiction | 4386 | 187 | 60 | 127 | 186 | 3 | 0 | 16 | 39 | 44392 | 5124 |
| Jason Kidd | 2337 | 71 | 23 | 48 | 71 | 1 | 0 | 28 | 42 | 20588 | 2162 |
| Daniel Treier | 634 | 23 | 8 | 15 | 23 | 0 | 0 | 4 | 5 | 5607 | 658 |
| Tessa Youngblood House | 647 | 25 | 7 | 18 | 25 | 0 | 0 | 5 | 11 | 5856 | 662 |
| Khyber Pass | 554 | 21 | 8 | 13 | 21 | 1 | 0 | 0 | 0 | 4438 | 525 |
| Bouma sequence | 203 | 10 | 1 | 9 | 10 | 0 | 0 | 0 | 0 | 2070 | 246 |
| House of Rötteln | 721 | 32 | 5 | 27 | 32 | 0 | 0 | 3 | 8 | 7181 | 893 |
| Frank FitzGerald (judge) | 1207 | 44 | 10 | 34 | 44 | 2 | 0 | 8 | 14 | 10165 | 1247 |
| Electronic organizer | 935 | 33 | 1 | 32 | 32 | 1 | 0 | 5 | 11 | 8620 | 955 |
| Brayford | 710 | 35 | 9 | 26 | 35 | 5 | 0 | 0 | 0 | 6428 | 831 |
| French aviso Arras | 763 | 30 | 6 | 24 | 30 | 1 | 0 | 5 | 12 | 7078 | 822 |
| Lewis Vaslet | 272 | 11 | 2 | 9 | 11 | 2 | 0 | 0 | 0 | 2497 | 276 |
| Anorogenic magmatism | 380 | 18 | 1 | 17 | 18 | 0 | 0 | 0 | 0 | 3303 | 434 |
| Michy | 252 | 10 | 3 | 7 | 10 | 0 | 0 | 2 | 3 | 2628 | 283 |
| Amiga 4000T | 470 | 17 | 1 | 16 | 17 | 0 | 0 | 4 | 7 | 4341 | 454 |
| Go For Wand Stakes | 220 | 11 | 2 | 9 | 11 | 1 | 0 | 3 | 8 | 2635 | 289 |
| Mishkenot Zevulun, Netanya | 277 | 13 | 6 | 7 | 13 | 0 | 0 | 2 | 4 | 3212 | 369 |
| God's Will | 358 | 15 | 6 | 9 | 15 | 0 | 0 | 2 | 5 | 3402 | 412 |
| General Grot-Rowecki | 251 | 9 | 3 | 6 | 9 | 2 | 0 | 3 | 4 | 2240 | 236 |
| Stuffed (album) | 209 | 8 | 2 | 6 | 8 | 0 | 0 | 0 | 0 | 1788 | 211 |
| Merve Büyüksaraç | 329 | 13 | 4 | 9 | 13 | 0 | 0 | 3 | 7 | 3210 | 360 |
| Holborn Hill | 329 | 17 | 3 | 14 | 17 | 3 | 0 | 1 | 3 | 3167 | 404 |
| Keith Hunter (politician) | 796 | 28 | 8 | 20 | 28 | 0 | 0 | 4 | 8 | 6686 | 771 |
| Upper Saddle River School District | 965 | 42 | 14 | 28 | 42 | 6 | 0 | 2 | 5 | 10569 | 1170 |
| Louis-Joseph Papineau | 610 | 27 | 11 | 16 | 27 | 1 | 0 | 2 | 4 | 6180 | 763 |
| Jip, His Story | 685 | 28 | 16 | 12 | 28 | 0 | 0 | 6 | 11 | 6508 | 759 |
| Tangainony | 584 | 28 | 3 | 25 | 28 | 3 | 0 | 4 | 11 | 5500 | 683 |
| Tony Fabrizio | 831 | 29 | 5 | 24 | 29 | 1 | 0 | 6 | 10 | 7962 | 843 |
| Makassar languages | 600 | 25 | 4 | 21 | 22 | 1 | 0 | 0 | 0 | 5088 | 624 |
| Polypeptide N-acetylgalactosaminyltransferase | 696 | 23 | 1 | 22 | 23 | 5 | 0 | 1 | 3 | 6615 | 596 |
| Traditional bachata | 906 | 41 | 6 | 35 | 41 | 1 | 0 | 3 | 5 | 8395 | 1056 |
| School of Rock (disambiguation) | 414 | 21 | 3 | 18 | 21 | 0 | 0 | 3 | 8 | 5902 | 642 |
| Sayed Ali Asghar Kurdistani | 779 | 31 | 5 | 26 | 31 | 0 | 0 | 1 | 1 | 6889 | 832 |
| Jordan Oliver (professional wrestler) | 500 | 17 | 4 | 13 | 17 | 0 | 0 | 1 | 2 | 4102 | 448 |
| Veera Padhakkam | 211 | 9 | 5 | 4 | 7 | 0 | 0 | 2 | 4 | 1926 | 232 |
| Lady Diana Cooper | 556 | 22 | 7 | 15 | 22 | 3 | 0 | 3 | 6 | 5598 | 640 |
| Theodore C. Lyster | 692 | 28 | 12 | 16 | 28 | 0 | 0 | 4 | 8 | 7714 | 806 |
| Marie-Renée | 339 | 11 | 3 | 8 | 11 | 0 | 0 | 4 | 6 | 4261 | 396 |
| Emmanuel Kolini | 356 | 15 | 7 | 8 | 15 | 1 | 0 | 3 | 6 | 3436 | 404 |
| Delphine Horvilleur | 521 | 16 | 4 | 12 | 16 | 0 | 0 | 4 | 8 | 4877 | 514 |
| Feralia februalis | 295 | 15 | 2 | 13 | 11 | 1 | 0 | 2 | 3 | 2916 | 366 |
| Bohetherick | 206 | 13 | 5 | 8 | 13 | 2 | 0 | 0 | 0 | 2568 | 304 |
| Pseudoeurycea anitae | 532 | 21 | 7 | 14 | 21 | 1 | 0 | 0 | 0 | 4463 | 528 |
| 1955 Singaporean general election | 1872 | 68 | 20 | 48 | 68 | 8 | 0 | 6 | 9 | 16349 | 1850 |
| Wilbur Shaw | 280 | 7 | 2 | 5 | 7 | 1 | 0 | 5 | 7 | 2349 | 241 |
| UHRF2 | 329 | 14 | 2 | 12 | 14 | 0 | 0 | 0 | 0 | 2646 | 338 |
| UMT Stadium | 385 | 16 | 2 | 14 | 16 | 2 | 0 | 1 | 2 | 3339 | 398 |
| Haji Parvej Ahmad | 515 | 23 | 4 | 19 | 23 | 2 | 0 | 2 | 6 | 5288 | 591 |
| Thomas Hussey (bishop) | 330 | 16 | 7 | 9 | 16 | 0 | 0 | 3 | 6 | 3730 | 444 |
| Asue Ighodalo | 677 | 35 | 8 | 27 | 35 | 0 | 0 | 1 | 1 | 7518 | 858 |
| Keshava Rama Varma | 257 | 10 | 2 | 8 | 10 | 0 | 0 | 2 | 4 | 2318 | 270 |
| 2024–25 Thai League 3 Cup | 870 | 36 | 3 | 33 | 36 | 8 | 0 | 3 | 4 | 8271 | 950 |
| Hallelujah Chicken Run Band | 202 | 11 | 3 | 8 | 11 | 0 | 0 | 1 | 4 | 2256 | 270 |
| Spring Fever (2009 film) | 609 | 28 | 7 | 21 | 28 | 0 | 0 | 4 | 9 | 6996 | 790 |
| Modifier letter double apostrophe | 305 | 13 | 1 | 12 | 13 | 0 | 0 | 0 | 0 | 2619 | 317 |
| Xi Columbae | 845 | 33 | 6 | 27 | 33 | 5 | 0 | 5 | 9 | 7593 | 852 |
| Parapaar | 526 | 22 | 7 | 15 | 22 | 1 | 0 | 4 | 9 | 4997 | 591 |
| Black Creek (Lehigh River tributary) | 2340 | 93 | 36 | 57 | 93 | 5 | 0 | 4 | 10 | 23132 | 2503 |
| Kahan Shuru Kahan Khatam | 558 | 21 | 10 | 11 | 19 | 0 | 0 | 2 | 3 | 4459 | 555 |
| Lonari | 1974 | 118 | 57 | 61 | 118 | 6 | 0 | 2 | 5 | 25617 | 2915 |
| Takarazuka Kofun (Izumo) | 384 | 15 | 5 | 10 | 15 | 0 | 0 | 2 | 3 | 3260 | 396 |
| 2024 PWHL season | 626 | 24 | 7 | 17 | 24 | 5 | 0 | 4 | 9 | 5817 | 642 |
| Lyudmila Issayeva | 423 | 11 | 4 | 7 | 11 | 0 | 0 | 5 | 7 | 3389 | 341 |
| Francesco Benozzo | 889 | 40 | 9 | 31 | 40 | 1 | 0 | 4 | 3 | 8400 | 1014 |
| 2015–16 HockeyAllsvenskan season | 373 | 11 | 2 | 9 | 11 | 2 | 0 | 5 | 6 | 2906 | 342 |
| Laura Poitras | 1598 | 68 | 16 | 52 | 68 | 2 | 0 | 9 | 22 | 16543 | 1850 |
| Monty Python Live at Aspen | 1515 | 63 | 16 | 47 | 63 | 1 | 0 | 6 | 15 | 14300 | 1622 |
| Call Me Mister (film) | 415 | 19 | 10 | 9 | 17 | 0 | 0 | 2 | 4 | 4110 | 490 |
| Shafferograptis | 251 | 12 | 2 | 10 | 12 | 2 | 0 | 0 | 0 | 2161 | 290 |
| Irisberto Herrera | 230 | 7 | 5 | 2 | 7 | 0 | 0 | 5 | 6 | 2074 | 207 |
| Louey Ouerrat | 215 | 6 | 2 | 4 | 6 | 1 | 0 | 3 | 6 | 1853 | 183 |
| Hirayama Seisai | 951 | 37 | 8 | 29 | 37 | 1 | 0 | 6 | 12 | 8123 | 968 |
| János Balogh (chess player) | 996 | 35 | 13 | 22 | 22 | 4 | 0 | 13 | 23 | 9873 | 1074 |
| Slow Wind | 734 | 30 | 8 | 22 | 30 | 4 | 0 | 3 | 8 | 6837 | 780 |
| Tvindkraft Wind Turbine | 628 | 31 | 10 | 21 | 31 | 1 | 0 | 1 | 2 | 5961 | 767 |
| Petar Barbarić | 606 | 27 | 10 | 17 | 27 | 0 | 0 | 3 | 5 | 6356 | 759 |
| When Brooklyn Met Seville | 278 | 11 | 6 | 5 | 11 | 0 | 0 | 1 | 2 | 2731 | 298 |
| Brashs | 754 | 26 | 8 | 18 | 26 | 1 | 0 | 5 | 7 | 6360 | 789 |
| David Ruiz | 324 | 12 | 6 | 6 | 12 | 0 | 0 | 4 | 9 | 4474 | 406 |
| Mrnjava | 1708 | 82 | 23 | 59 | 81 | 2 | 0 | 4 | 12 | 18374 | 2096 |
| Chilean rodeo | 1299 | 53 | 12 | 41 | 53 | 1 | 0 | 3 | 7 | 10626 | 1356 |
| Richard Edgcumbe | 683 | 21 | 14 | 7 | 21 | 1 | 0 | 7 | 11 | 10365 | 862 |
| Jvf | 281 | 14 | 4 | 10 | 14 | 0 | 0 | 1 | 3 | 3705 | 372 |
| Listamlet | 362 | 21 | 3 | 18 | 21 | 5 | 0 | 2 | 7 | 4250 | 515 |
| Blackamoor (decorative arts) | 874 | 37 | 4 | 33 | 37 | 0 | 0 | 0 | 0 | 7381 | 902 |
| Jesus Is Lord | 1232 | 54 | 13 | 41 | 54 | 4 | 0 | 3 | 6 | 10978 | 1348 |
| Invitation to Her's | 219 | 8 | 2 | 6 | 8 | 0 | 0 | 2 | 4 | 1964 | 230 |
| Robert W. Smith (writer) | 361 | 17 | 5 | 12 | 17 | 0 | 0 | 1 | 2 | 3863 | 490 |
| Zebra Technologies | 350 | 12 | 1 | 11 | 12 | 1 | 0 | 2 | 5 | 2761 | 312 |
| Andrei Demurenko | 612 | 20 | 9 | 11 | 20 | 0 | 0 | 3 | 7 | 5035 | 559 |
| The Heart of Christmas (album) | 318 | 11 | 3 | 8 | 11 | 0 | 0 | 2 | 4 | 2474 | 298 |
| Jewish views on sin | 1056 | 54 | 5 | 49 | 54 | 2 | 0 | 0 | 0 | 9723 | 1290 |
| James Makamba | 828 | 34 | 9 | 25 | 34 | 1 | 0 | 2 | 5 | 7681 | 901 |
| Jeanne Zelasko | 404 | 17 | 5 | 12 | 17 | 1 | 0 | 1 | 2 | 3811 | 442 |
| Waipa Foundation | 313 | 13 | 1 | 12 | 13 | 0 | 0 | 2 | 6 | 2896 | 342 |
| Anders Ek | 266 | 11 | 7 | 4 | 11 | 0 | 0 | 4 | 7 | 2660 | 299 |
| A Test Before Trying | 843 | 34 | 8 | 26 | 33 | 0 | 0 | 2 | 6 | 7153 | 884 |
| Red Plastic Bag | 1798 | 73 | 20 | 53 | 73 | 5 | 0 | 10 | 23 | 18640 | 2037 |
| Geology of Australia | 235 | 10 | 3 | 7 | 10 | 2 | 0 | 0 | 0 | 2090 | 253 |
| Kazakh Whiteheaded | 437 | 21 | 3 | 18 | 21 | 0 | 0 | 2 | 6 | 4288 | 555 |
| Bruhat Bengaluru Mahanagara Palike | 1782 | 71 | 5 | 66 | 71 | 4 | 0 | 3 | 5 | 16847 | 1930 |
| St. Pauli station | 339 | 13 | 8 | 5 | 13 | 0 | 0 | 1 | 2 | 2651 | 348 |
| Omega-3-acid ethyl esters | 1480 | 53 | 5 | 48 | 53 | 2 | 0 | 3 | 7 | 12034 | 1366 |
| Caitlin Upton | 229 | 6 | 3 | 3 | 6 | 0 | 0 | 3 | 6 | 2270 | 213 |
| History of the Newcastle Knights | 316 | 10 | 2 | 8 | 10 | 0 | 0 | 2 | 4 | 2410 | 278 |
| 2nd Kentucky Infantry Regiment | 202 | 9 | 7 | 2 | 9 | 0 | 4 | 0 | 0 | 2368 | 377 |
| Antoniów, Lower Silesian Voivodeship | 423 | 15 | 5 | 10 | 15 | 0 | 0 | 0 | 0 | 3179 | 382 |
| Baixo Vouga | 460 | 23 | 8 | 15 | 23 | 4 | 0 | 1 | 3 | 4598 | 589 |
| Horace Busby | 285 | 9 | 2 | 7 | 9 | 0 | 0 | 2 | 2 | 2371 | 278 |
| 2011–12 Maltese Premier League | 853 | 32 | 5 | 27 | 32 | 4 | 0 | 6 | 13 | 7188 | 833 |
| Boren Sino-Canadian School | 912 | 41 | 13 | 28 | 41 | 4 | 0 | 3 | 6 | 8822 | 1041 |
| Mount Wellington (Tasmania) | 946 | 44 | 13 | 31 | 44 | 7 | 0 | 1 | 2 | 9136 | 1088 |
| Puku | 319 | 17 | 7 | 10 | 17 | 0 | 0 | 0 | 0 | 3326 | 409 |
| So High (Jamelia song) | 328 | 10 | 3 | 7 | 10 | 0 | 0 | 1 | 2 | 2058 | 248 |
| Qingbaijiang, Chengdu | 273 | 14 | 7 | 7 | 14 | 0 | 0 | 0 | 0 | 2799 | 345 |
| Grammatostomias dentatus | 244 | 11 | 2 | 9 | 11 | 1 | 0 | 0 | 0 | 2256 | 274 |
| Compound Media | 522 | 18 | 12 | 6 | 18 | 0 | 0 | 2 | 3 | 4229 | 480 |
| Franciscus Conradus Palaoensoeka | 458 | 13 | 6 | 7 | 13 | 1 | 0 | 8 | 11 | 3690 | 382 |
| Te Mana o te Mau Motu | 698 | 31 | 8 | 23 | 31 | 4 | 0 | 6 | 12 | 7404 | 834 |
| Overcoats (album) | 472 | 19 | 4 | 15 | 19 | 0 | 0 | 2 | 4 | 3944 | 476 |
| Charles Bernhard Heyd | 1053 | 44 | 17 | 27 | 44 | 1 | 0 | 10 | 24 | 11262 | 1283 |
| Athletics at the 2016 Summer Paralympics – Women's 800 metres T34 | 365 | 17 | 2 | 15 | 17 | 3 | 0 | 1 | 3 | 3786 | 456 |
| Belgrade Cooperative Bank | 807 | 30 | 8 | 22 | 30 | 1 | 0 | 5 | 11 | 7402 | 838 |
| Robert Richter | 239 | 10 | 7 | 3 | 10 | 0 | 0 | 1 | 5 | 2706 | 273 |
| Gordon Burnham | 1683 | 66 | 26 | 40 | 66 | 6 | 0 | 11 | 25 | 14943 | 1789 |
| Theodor Hoffmann (admiral) | 257 | 10 | 4 | 6 | 10 | 0 | 0 | 2 | 2 | 2917 | 341 |
| John Jankans | 344 | 10 | 3 | 7 | 10 | 0 | 0 | 1 | 2 | 2464 | 287 |
| Verbiv, Naraiv rural hromada, Ternopil Raion, Ternopil Oblast | 454 | 24 | 10 | 14 | 24 | 0 | 0 | 2 | 5 | 4829 | 611 |
| The Highwayman (1951 film) | 319 | 14 | 3 | 11 | 14 | 0 | 0 | 1 | 2 | 2908 | 359 |
| Trifolium microdon | 617 | 24 | 4 | 20 | 24 | 2 | 0 | 1 | 1 | 4746 | 586 |
| Dil kam No Dil | 322 | 12 | 1 | 11 | 12 | 2 | 0 | 3 | 4 | 2637 | 309 |
| A Chipmunk Christmas | 514 | 21 | 9 | 12 | 21 | 0 | 0 | 5 | 5 | 5153 | 624 |
| Raymond L. Johnson | 413 | 16 | 5 | 11 | 16 | 0 | 0 | 1 | 2 | 3737 | 419 |
| Nitryl fluoride | 359 | 13 | 3 | 10 | 13 | 0 | 0 | 1 | 1 | 2776 | 332 |
| WARP-01 | 387 | 15 | 5 | 10 | 15 | 0 | 0 | 2 | 6 | 3286 | 414 |
| Martha Harris (footballer) | 293 | 9 | 4 | 5 | 9 | 0 | 0 | 5 | 6 | 3010 | 312 |
| Mir Yazdanbakhsh | 764 | 31 | 13 | 18 | 29 | 0 | 0 | 2 | 4 | 6216 | 804 |
| List of Malawian submissions for the Academy Award for Best International Feature Film | 640 | 19 | 3 | 16 | 19 | 1 | 0 | 5 | 7 | 4975 | 528 |
| Maxim Meyer | 743 | 30 | 10 | 20 | 26 | 0 | 0 | 5 | 11 | 7539 | 854 |
| Tião Carreiro & Pardinho | 920 | 40 | 12 | 28 | 40 | 1 | 0 | 0 | 0 | 8374 | 1008 |
| Idol × Warrior Miracle Tunes! | 2134 | 90 | 17 | 73 | 88 | 2 | 0 | 7 | 13 | 20363 | 2410 |
| Musawar Shah | 712 | 19 | 10 | 9 | 19 | 0 | 0 | 8 | 11 | 5500 | 612 |
| DJ Jabba | 951 | 38 | 18 | 20 | 38 | 0 | 0 | 6 | 9 | 8206 | 1003 |
| Ar Horqin Banner | 409 | 24 | 12 | 12 | 24 | 3 | 0 | 0 | 0 | 4723 | 597 |
| EU status (football) | 484 | 20 | 0 | 20 | 18 | 1 | 0 | 0 | 0 | 4131 | 487 |
| Romics | 756 | 31 | 2 | 29 | 31 | 7 | 0 | 8 | 10 | 7222 | 819 |
| 2003 Grand National | 658 | 26 | 5 | 21 | 26 | 4 | 0 | 6 | 10 | 7178 | 810 |
| Summary jurisdiction | 845 | 39 | 5 | 34 | 39 | 0 | 0 | 0 | 0 | 7724 | 937 |
| Methil Docks | 309 | 16 | 8 | 8 | 16 | 0 | 0 | 0 | 0 | 2934 | 404 |
| Lauina Futi | 624 | 25 | 8 | 17 | 25 | 0 | 0 | 4 | 10 | 5850 | 692 |
| Referee (Queoff) | 280 | 14 | 7 | 7 | 14 | 1 | 0 | 0 | 0 | 2747 | 351 |
| Holy Name Monastery | 272 | 9 | 4 | 5 | 9 | 0 | 0 | 1 | 1 | 2010 | 240 |
| The Raven (2006 film) | 223 | 9 | 4 | 5 | 9 | 0 | 0 | 2 | 4 | 2146 | 238 |
| Ter Sámi | 431 | 16 | 3 | 13 | 16 | 2 | 0 | 3 | 6 | 3727 | 420 |
| Low-pressure area | 3169 | 120 | 6 | 114 | 117 | 2 | 0 | 5 | 7 | 25607 | 3041 |
| Fresno Bee Building | 2300 | 78 | 24 | 54 | 78 | 2 | 0 | 17 | 30 | 19437 | 2229 |
| Action stroke dance notation | 952 | 48 | 11 | 37 | 48 | 2 | 0 | 0 | 0 | 10666 | 1194 |
| Richard Winkler (producer) | 739 | 28 | 3 | 25 | 28 | 5 | 0 | 2 | 3 | 5942 | 711 |
| Parkpop | 560 | 23 | 9 | 14 | 23 | 2 | 0 | 4 | 7 | 5070 | 625 |
| San Cristóbal Volcano | 780 | 36 | 12 | 24 | 36 | 2 | 0 | 2 | 4 | 7396 | 892 |
| Michigan Shore-to-Shore Trail | 783 | 30 | 9 | 21 | 30 | 4 | 0 | 1 | 3 | 6350 | 748 |
| Cibin | 1196 | 57 | 20 | 37 | 57 | 5 | 0 | 0 | 0 | 11271 | 1413 |
| Sarah Coysh | 1064 | 48 | 16 | 32 | 48 | 2 | 0 | 5 | 12 | 11324 | 1413 |
| List of bridges in Cambridge | 648 | 31 | 8 | 23 | 31 | 2 | 0 | 1 | 2 | 6252 | 749 |
| Songbulsa | 829 | 42 | 14 | 28 | 28 | 1 | 0 | 3 | 6 | 8591 | 1078 |
| Nicola Danti | 384 | 18 | 4 | 14 | 18 | 1 | 0 | 4 | 10 | 4162 | 494 |
| Ugo da Carpi | 872 | 34 | 7 | 27 | 34 | 3 | 0 | 1 | 3 | 7304 | 886 |
| N.U.D.E.@ Natural Ultimate Digital Experiment | 939 | 37 | 6 | 31 | 37 | 1 | 0 | 2 | 2 | 8000 | 964 |
| 1881 Mississippi gubernatorial election | 249 | 10 | 5 | 5 | 10 | 0 | 0 | 2 | 3 | 2345 | 293 |
| Ryan Gage | 850 | 41 | 13 | 28 | 41 | 1 | 0 | 2 | 5 | 9238 | 1041 |
| Tommy Langan | 526 | 16 | 6 | 10 | 16 | 1 | 0 | 6 | 10 | 4529 | 489 |
| International Committee of Architectural Critics | 895 | 39 | 14 | 25 | 39 | 0 | 0 | 2 | 6 | 9300 | 1035 |
| 2013 ITF Women's Circuit – Wenshan | 300 | 12 | 3 | 9 | 12 | 0 | 0 | 4 | 8 | 2939 | 317 |
| Volante (carriage) | 362 | 18 | 7 | 11 | 18 | 1 | 0 | 1 | 3 | 3551 | 458 |
| Wild Seven | 361 | 13 | 1 | 12 | 13 | 1 | 0 | 3 | 6 | 3632 | 358 |
| Rich Johnson (publishing executive) | 1262 | 55 | 9 | 46 | 55 | 2 | 0 | 4 | 13 | 12304 | 1446 |
| Simon Gaunt | 803 | 39 | 10 | 29 | 39 | 0 | 0 | 9 | 22 | 9596 | 1105 |
| Norm deSilva | 210 | 8 | 1 | 7 | 8 | 0 | 0 | 1 | 2 | 1781 | 213 |
| Ass Clowns | 601 | 25 | 7 | 18 | 25 | 2 | 0 | 3 | 8 | 6420 | 678 |
| 2008 Skate Canada International | 476 | 19 | 3 | 16 | 19 | 0 | 0 | 3 | 5 | 4300 | 503 |
| Josette Normandeau | 764 | 30 | 8 | 22 | 30 | 3 | 0 | 0 | 0 | 6026 | 749 |
| Act (band) | 458 | 19 | 4 | 15 | 19 | 0 | 0 | 2 | 7 | 4213 | 508 |
| Sergey Novikov (photographer) | 310 | 12 | 3 | 9 | 12 | 1 | 0 | 0 | 0 | 2072 | 296 |
| Statue of William Pitt the Younger | 1643 | 65 | 20 | 45 | 65 | 1 | 0 | 4 | 9 | 13106 | 1608 |
| Guigues IV of Albon | 1563 | 85 | 23 | 62 | 84 | 2 | 0 | 8 | 17 | 16624 | 2114 |
| Rob Ehsan | 1208 | 48 | 17 | 31 | 48 | 0 | 0 | 11 | 29 | 10945 | 1276 |
| Maksym Pashkovskyi | 351 | 14 | 4 | 10 | 14 | 0 | 0 | 2 | 8 | 4196 | 468 |
| History of Germany during World War I | 759 | 30 | 10 | 20 | 30 | 0 | 0 | 2 | 5 | 6768 | 799 |
| High-maltose corn syrup | 741 | 23 | 0 | 23 | 23 | 2 | 0 | 4 | 4 | 4905 | 563 |
| Florencio Vargas | 482 | 18 | 5 | 13 | 18 | 1 | 0 | 5 | 7 | 4084 | 488 |
| Melas, Kastoria | 433 | 23 | 9 | 14 | 23 | 0 | 0 | 0 | 0 | 4268 | 563 |
| Edward Sibbert | 449 | 14 | 2 | 12 | 14 | 1 | 0 | 5 | 10 | 4260 | 427 |
| Downholland | 626 | 28 | 6 | 22 | 28 | 1 | 0 | 3 | 5 | 5482 | 697 |
| Illinois Valley Regional Airport | 466 | 27 | 6 | 21 | 27 | 3 | 0 | 2 | 3 | 6286 | 656 |
| Derrick Main | 1009 | 42 | 20 | 22 | 42 | 1 | 0 | 4 | 6 | 8691 | 1083 |
| My Diarrhe | 400 | 18 | 7 | 11 | 18 | 1 | 0 | 2 | 5 | 3798 | 477 |
| List of United States presidential visits to Sub-Saharan Africa | 335 | 10 | 3 | 7 | 10 | 1 | 0 | 0 | 0 | 2329 | 266 |
| 10th Mountain Division | 2210 | 84 | 45 | 39 | 84 | 3 | 8 | 10 | 21 | 21285 | 2552 |
| Alpine Kitchen | 396 | 17 | 6 | 11 | 17 | 2 | 0 | 2 | 5 | 3650 | 432 |
| Antiquities Advisory Board | 592 | 23 | 3 | 20 | 23 | 0 | 0 | 1 | 2 | 5412 | 614 |
| Vélez Sársfield | 363 | 15 | 8 | 7 | 15 | 0 | 0 | 0 | 0 | 4196 | 392 |
| May 1909 Madrid City Council election | 246 | 9 | 5 | 4 | 9 | 2 | 0 | 3 | 6 | 2498 | 265 |
| Hayat Lambarki | 299 | 10 | 2 | 8 | 7 | 0 | 0 | 3 | 5 | 2277 | 280 |
| Herman Smetanin | 498 | 14 | 4 | 10 | 14 | 0 | 0 | 4 | 11 | 4927 | 530 |
| Anthony Joshua vs Gary Cornish | 362 | 15 | 5 | 10 | 15 | 0 | 0 | 1 | 2 | 3229 | 400 |
| 2012 V8 Supercar season | 1110 | 31 | 9 | 22 | 30 | 8 | 0 | 7 | 10 | 8505 | 926 |
| Francisco Jê Acaiaba de Montezuma, Viscount of Jequitinhonha | 674 | 31 | 5 | 26 | 31 | 1 | 0 | 3 | 6 | 6707 | 848 |
| 2023 Guildford Borough Council election | 267 | 10 | 4 | 6 | 10 | 1 | 0 | 3 | 4 | 2632 | 306 |
| Parapontoporia | 297 | 13 | 3 | 10 | 13 | 0 | 0 | 0 | 0 | 2426 | 318 |
| Orenburg | 650 | 31 | 15 | 16 | 31 | 3 | 0 | 4 | 9 | 7529 | 913 |
| Cataulacus granulatus | 219 | 15 | 10 | 5 | 15 | 0 | 0 | 0 | 0 | 2959 | 356 |
| Nanchang | 925 | 36 | 15 | 21 | 36 | 1 | 0 | 3 | 8 | 9032 | 976 |
| Plough Inn (Madison, Wisconsin) | 280 | 14 | 3 | 11 | 14 | 0 | 0 | 2 | 5 | 2869 | 350 |
| Eystein Church | 502 | 24 | 8 | 16 | 24 | 2 | 0 | 1 | 2 | 4966 | 594 |
| Erkan Mustafa | 932 | 31 | 8 | 23 | 31 | 0 | 0 | 9 | 17 | 8398 | 918 |
| Margaret Cuthbert | 1225 | 55 | 11 | 44 | 55 | 1 | 0 | 3 | 4 | 10842 | 1376 |
| 1947 Vermont Catamounts football team | 575 | 23 | 10 | 13 | 23 | 2 | 0 | 4 | 7 | 5684 | 667 |
| Ingane Oru Nilapakshi | 315 | 16 | 7 | 9 | 14 | 0 | 0 | 1 | 2 | 3336 | 403 |
| Socionature | 529 | 25 | 1 | 24 | 25 | 2 | 0 | 0 | 0 | 4592 | 594 |
| Maria Fragoudaki | 219 | 14 | 4 | 10 | 14 | 0 | 0 | 1 | 4 | 3543 | 371 |
| Bunche Library | 787 | 22 | 7 | 15 | 22 | 0 | 0 | 7 | 9 | 4795 | 557 |
| 1930 Wofford Terriers football team | 308 | 13 | 3 | 10 | 13 | 0 | 0 | 3 | 4 | 3485 | 412 |
| Second-degree atrioventricular block | 473 | 19 | 1 | 18 | 19 | 0 | 0 | 0 | 0 | 3944 | 474 |
| 2009 Tennislife Cup – Doubles | 303 | 13 | 6 | 7 | 13 | 0 | 0 | 1 | 2 | 2639 | 337 |
| Shekhe Pind | 641 | 30 | 9 | 21 | 30 | 2 | 0 | 0 | 0 | 5446 | 737 |
| Analy High School | 600 | 26 | 9 | 17 | 26 | 2 | 0 | 1 | 4 | 5644 | 662 |
| Tuaran District | 628 | 31 | 13 | 18 | 28 | 2 | 0 | 1 | 2 | 6570 | 778 |
| Alfred Hitchcock Presents: The Final Cut | 200 | 8 | 2 | 6 | 7 | 0 | 0 | 1 | 2 | 2083 | 217 |
| XBR (Sony) | 8937 | 337 | 44 | 293 | 165 | 62 | 0 | 44 | 107 | 124991 | 10070 |
| Kvitskarvet | 297 | 18 | 7 | 11 | 18 | 1 | 0 | 0 | 0 | 3218 | 434 |
| Go (Blackpink song) | 1036 | 41 | 15 | 26 | 41 | 5 | 0 | 2 | 4 | 8561 | 1038 |
| Li Chengqi | 875 | 42 | 18 | 24 | 42 | 2 | 0 | 1 | 3 | 11114 | 1089 |
| Bogan Shire | 505 | 22 | 14 | 8 | 21 | 0 | 0 | 3 | 9 | 4618 | 576 |
| Falkirk West (UK Parliament constituency) | 205 | 9 | 3 | 6 | 9 | 0 | 0 | 2 | 2 | 1974 | 242 |
| Tacho (food) | 340 | 18 | 2 | 16 | 18 | 0 | 0 | 0 | 0 | 3858 | 425 |
| Vanessa Reed | 643 | 23 | 5 | 18 | 23 | 0 | 0 | 7 | 12 | 6059 | 669 |
| Chalk-fronted corporal | 874 | 38 | 9 | 29 | 38 | 0 | 0 | 0 | 0 | 7267 | 924 |
| Aschau | 317 | 22 | 13 | 9 | 9 | 0 | 0 | 0 | 0 | 3475 | 521 |
| Jewellery Design and Management International School | 415 | 20 | 1 | 19 | 20 | 0 | 0 | 0 | 0 | 4294 | 493 |
| Blackfin sucker | 720 | 28 | 10 | 18 | 28 | 1 | 0 | 0 | 0 | 5882 | 716 |
| Nanofoundry | 332 | 13 | 0 | 13 | 13 | 0 | 0 | 0 | 0 | 2459 | 314 |
| Czechs in France | 363 | 17 | 8 | 9 | 17 | 2 | 0 | 0 | 0 | 3292 | 420 |
| The Song of Glory | 468 | 18 | 5 | 13 | 18 | 0 | 0 | 3 | 6 | 4248 | 504 |
| Pahalgam Assembly constituency | 215 | 9 | 2 | 7 | 9 | 1 | 0 | 0 | 0 | 1865 | 223 |
| Eretmocera haemogastra | 222 | 10 | 4 | 6 | 7 | 0 | 0 | 1 | 2 | 1844 | 246 |
| Janakinagar, Kailali | 212 | 9 | 4 | 5 | 9 | 1 | 0 | 1 | 2 | 1934 | 232 |
| Akku Yadav | 2426 | 108 | 21 | 87 | 103 | 7 | 0 | 9 | 19 | 21291 | 2729 |
| Kazakh Business in Brazil | 234 | 12 | 4 | 8 | 12 | 0 | 0 | 2 | 5 | 3432 | 364 |
| Maimonides College | 1409 | 53 | 15 | 38 | 53 | 2 | 0 | 5 | 11 | 12029 | 1450 |
| PMA Sinagtala Class of 1986 | 291 | 11 | 2 | 9 | 8 | 0 | 0 | 2 | 5 | 2732 | 294 |
| 2024 French legislative election in Charente-Maritime | 471 | 13 | 3 | 10 | 13 | 2 | 0 | 6 | 11 | 4082 | 388 |
| Ladera, California | 356 | 14 | 5 | 9 | 14 | 2 | 0 | 2 | 4 | 2988 | 350 |
| HMCS Acadia | 649 | 23 | 5 | 18 | 23 | 1 | 0 | 2 | 6 | 5385 | 620 |
| Michaela Seibold | 376 | 11 | 6 | 5 | 11 | 0 | 0 | 3 | 5 | 2961 | 325 |
| No Fixed Point in Space | 272 | 12 | 5 | 7 | 12 | 0 | 0 | 1 | 2 | 2516 | 307 |
| Hōkō-ji (Kyoto) | 612 | 27 | 10 | 17 | 27 | 0 | 0 | 3 | 9 | 5649 | 710 |
| Mahdavi Damghani | 234 | 10 | 3 | 7 | 10 | 0 | 0 | 0 | 0 | 2296 | 276 |
| Johann Hermann Baas | 497 | 23 | 6 | 17 | 23 | 1 | 0 | 4 | 6 | 4644 | 605 |
| Steamtown | 557 | 27 | 14 | 13 | 27 | 0 | 0 | 0 | 0 | 8454 | 692 |
| Geneva Protocol | 1403 | 56 | 3 | 53 | 56 | 0 | 0 | 7 | 12 | 13097 | 1465 |
| List of international prime ministerial trips made by Scott Morrison | 255 | 10 | 3 | 7 | 10 | 2 | 0 | 1 | 4 | 2358 | 288 |
| Cliff Wiley | 282 | 9 | 3 | 6 | 9 | 0 | 0 | 3 | 7 | 2655 | 267 |
| Angel in My Eyes | 302 | 11 | 5 | 6 | 11 | 2 | 0 | 1 | 2 | 2292 | 274 |
| Belfast SNL Giants | 207 | 8 | 3 | 5 | 8 | 0 | 0 | 0 | 0 | 1808 | 209 |
| Eshkarlet | 611 | 30 | 7 | 23 | 30 | 6 | 0 | 2 | 5 | 6678 | 764 |
| Bong game | 673 | 24 | 7 | 17 | 24 | 0 | 0 | 2 | 5 | 5204 | 627 |
| Polyketide | 778 | 31 | 1 | 30 | 31 | 2 | 0 | 1 | 3 | 6314 | 791 |
| Wurfbainia vera | 519 | 27 | 10 | 17 | 27 | 0 | 0 | 2 | 7 | 5382 | 692 |
| Monocerotids | 350 | 12 | 4 | 8 | 12 | 2 | 0 | 3 | 5 | 3375 | 370 |
| List of islands of Malaysia | 669 | 31 | 15 | 16 | 31 | 4 | 0 | 1 | 2 | 5885 | 774 |
| El Torero | 304 | 12 | 5 | 7 | 12 | 0 | 0 | 1 | 2 | 2637 | 321 |
| Bhawal Badre Alam Government College | 408 | 14 | 3 | 11 | 14 | 0 | 0 | 2 | 3 | 3167 | 360 |
| Minister for Justice, Home Affairs and Migration | 615 | 42 | 9 | 33 | 42 | 2 | 0 | 1 | 6 | 8522 | 1010 |
| Operation Kitbag | 720 | 30 | 9 | 21 | 30 | 6 | 0 | 2 | 4 | 6452 | 786 |
| Zgornja Hajdina | 700 | 27 | 10 | 17 | 24 | 0 | 0 | 2 | 3 | 5445 | 690 |
| Shaxi, Yunnan | 947 | 40 | 21 | 19 | 40 | 3 | 0 | 3 | 10 | 9000 | 1050 |
| Wedell-Williams Model 44 | 695 | 19 | 5 | 14 | 19 | 3 | 0 | 5 | 9 | 5144 | 548 |
| Vivekanandan | 335 | 20 | 10 | 10 | 20 | 1 | 0 | 0 | 0 | 3755 | 468 |
| 2008 Spain Pilatus PC-6 Porter crash | 205 | 7 | 2 | 5 | 7 | 0 | 0 | 2 | 3 | 1537 | 187 |
| Ella Aquino | 633 | 24 | 9 | 15 | 24 | 0 | 0 | 4 | 9 | 5822 | 680 |
| Graciela Bográn | 584 | 23 | 6 | 17 | 23 | 1 | 0 | 2 | 8 | 5086 | 620 |
| Tooji | 278 | 13 | 6 | 7 | 11 | 1 | 0 | 1 | 3 | 2646 | 344 |
| John M. Edmond | 633 | 24 | 9 | 15 | 24 | 0 | 0 | 2 | 2 | 5596 | 692 |
| Hypocysta adiante | 215 | 11 | 4 | 7 | 11 | 0 | 0 | 0 | 0 | 2042 | 271 |
| Remember Paul? | 1209 | 50 | 22 | 28 | 50 | 2 | 0 | 3 | 8 | 11124 | 1380 |
| A Bright Cold Day | 223 | 9 | 2 | 7 | 9 | 0 | 0 | 1 | 2 | 2108 | 233 |
| Flagg Grove School | 225 | 10 | 4 | 6 | 10 | 0 | 0 | 1 | 2 | 2050 | 251 |
| Teijin Incident | 203 | 9 | 2 | 7 | 9 | 0 | 0 | 1 | 1 | 2274 | 242 |
| Mental health in Ireland | 331 | 18 | 5 | 13 | 18 | 0 | 0 | 0 | 0 | 3283 | 447 |
| Admiralty of the Noorderkwartier | 242 | 13 | 5 | 8 | 13 | 2 | 0 | 0 | 0 | 2822 | 311 |
| 2002 United States Senate election in New Jersey | 1739 | 57 | 28 | 29 | 57 | 0 | 0 | 11 | 24 | 14962 | 1650 |
| Dusky catshark | 332 | 15 | 4 | 11 | 15 | 2 | 0 | 0 | 0 | 2935 | 364 |
| Alabama Commission on Higher Education | 1019 | 43 | 7 | 36 | 43 | 1 | 0 | 1 | 2 | 10222 | 1101 |
| S-65 Stalinets | 274 | 8 | 2 | 6 | 8 | 0 | 0 | 2 | 2 | 2016 | 222 |
| Nottingham Eastcroft | 397 | 15 | 7 | 8 | 15 | 0 | 0 | 1 | 1 | 2892 | 386 |
| Rod Buskas | 339 | 11 | 1 | 10 | 10 | 0 | 0 | 3 | 5 | 3138 | 318 |
| Romfs | 474 | 17 | 1 | 16 | 17 | 0 | 0 | 0 | 0 | 3880 | 426 |
| Polar icebreaker | 776 | 23 | 1 | 22 | 23 | 1 | 0 | 0 | 0 | 9241 | 623 |
| Crazyhouse | 213 | 5 | 0 | 5 | 5 | 0 | 0 | 0 | 0 | 1075 | 122 |
| Vernon Quinsey | 2230 | 73 | 14 | 59 | 73 | 1 | 0 | 20 | 35 | 18626 | 2098 |
| 2012–13 FC Dinamo București season | 1038 | 41 | 10 | 31 | 41 | 1 | 0 | 8 | 16 | 9018 | 1096 |
| Scott Christian College | 503 | 23 | 4 | 19 | 23 | 1 | 0 | 0 | 0 | 4750 | 564 |
| Rudawa, Kłodzko County | 205 | 8 | 4 | 4 | 8 | 0 | 0 | 0 | 0 | 1835 | 204 |
| Soshyshche | 219 | 11 | 3 | 8 | 11 | 0 | 0 | 1 | 3 | 2382 | 286 |
| Dolls for Darfur | 519 | 27 | 9 | 18 | 27 | 1 | 0 | 0 | 0 | 4886 | 658 |
| Operation Jizerka | 334 | 15 | 3 | 12 | 15 | 1 | 0 | 1 | 4 | 3468 | 381 |
| Mologsky Uyezd | 210 | 9 | 2 | 7 | 9 | 0 | 0 | 0 | 0 | 1866 | 240 |
| God's Country (2022 film) | 433 | 17 | 10 | 7 | 17 | 0 | 0 | 3 | 4 | 4074 | 482 |
| Francis Bland (disambiguation) | 233 | 9 | 5 | 4 | 9 | 0 | 0 | 0 | 0 | 1961 | 229 |
| Danny Desriveaux | 523 | 22 | 2 | 20 | 22 | 1 | 0 | 2 | 4 | 4942 | 578 |
| Arginbaatar | 844 | 36 | 7 | 29 | 36 | 1 | 0 | 3 | 9 | 7091 | 890 |
| Electoral history of Humza Yousaf | 224 | 10 | 2 | 8 | 10 | 0 | 0 | 2 | 8 | 2894 | 315 |
| Paykar Khan Igirmi Durt | 377 | 15 | 8 | 7 | 15 | 0 | 0 | 2 | 5 | 3730 | 464 |
| Codex Millenarius | 497 | 20 | 4 | 16 | 20 | 3 | 0 | 0 | 0 | 4290 | 501 |
| Renārs Birkentāls | 353 | 12 | 2 | 10 | 12 | 1 | 0 | 3 | 6 | 3072 | 335 |
| Hardware scout | 838 | 35 | 2 | 33 | 35 | 0 | 0 | 0 | 0 | 7019 | 864 |
| Cindy Pickett | 733 | 23 | 7 | 16 | 23 | 0 | 0 | 5 | 8 | 6992 | 691 |
| Calle Ocho (disambiguation) | 306 | 14 | 6 | 8 | 14 | 0 | 0 | 1 | 2 | 3124 | 350 |
| Aulus Cornelius Cossus (dictator) | 206 | 9 | 2 | 7 | 7 | 1 | 0 | 1 | 2 | 2039 | 254 |
| Bucculatrix zizyphella | 272 | 14 | 7 | 7 | 12 | 0 | 0 | 1 | 2 | 2466 | 343 |
| Thomas Shuldham O'Halloran (lawyer) | 231 | 7 | 5 | 2 | 7 | 0 | 0 | 1 | 3 | 1830 | 225 |
| 1984 WCT World Doubles | 400 | 12 | 2 | 10 | 12 | 0 | 0 | 2 | 2 | 3267 | 353 |
| Curt Mallory | 398 | 15 | 4 | 11 | 15 | 0 | 0 | 4 | 6 | 3535 | 416 |
| Texarkana Shine-Oners | 463 | 14 | 9 | 5 | 14 | 2 | 0 | 6 | 9 | 4220 | 447 |
| Stakhanovskaya | 289 | 13 | 6 | 7 | 13 | 0 | 0 | 1 | 2 | 2784 | 350 |
| Choqa Mahi | 256 | 14 | 6 | 8 | 14 | 1 | 0 | 1 | 2 | 3010 | 364 |
| Madden NFL 98 | 857 | 33 | 4 | 29 | 33 | 1 | 0 | 2 | 5 | 7600 | 864 |
| Emmett Till Unsolved Civil Rights Crime Act | 486 | 19 | 4 | 15 | 19 | 0 | 0 | 4 | 12 | 5054 | 548 |
| 1995 Extremaduran regional election | 1352 | 58 | 17 | 41 | 58 | 7 | 0 | 6 | 13 | 12681 | 1504 |
| Cerium compounds | 676 | 27 | 6 | 21 | 27 | 3 | 0 | 0 | 0 | 5347 | 688 |
| Rayadhan III | 261 | 11 | 1 | 10 | 11 | 0 | 0 | 4 | 6 | 2684 | 294 |
| Alcazaba of Badajoz | 389 | 14 | 8 | 6 | 14 | 0 | 0 | 4 | 5 | 2979 | 389 |
| Vawkavysk Ghetto | 251 | 8 | 2 | 6 | 8 | 1 | 0 | 2 | 2 | 2008 | 257 |
| Southeast University Chengxian College station | 224 | 8 | 3 | 5 | 8 | 2 | 0 | 1 | 2 | 1758 | 224 |
| Political status of Western Sahara | 764 | 34 | 12 | 22 | 34 | 1 | 0 | 2 | 3 | 7821 | 864 |
| Chick Evans (coach) | 1984 | 77 | 32 | 45 | 77 | 4 | 0 | 9 | 22 | 19210 | 2226 |
| Mapping Bangladesh | 224 | 10 | 3 | 7 | 10 | 0 | 0 | 0 | 0 | 2402 | 259 |
| Preston, Minnesota | 324 | 14 | 6 | 8 | 14 | 1 | 0 | 1 | 3 | 2856 | 345 |
| Barthel Schink | 988 | 38 | 15 | 23 | 38 | 2 | 0 | 4 | 7 | 8771 | 1062 |
| Dicerandrol C | 838 | 31 | 1 | 30 | 31 | 4 | 0 | 0 | 0 | 6816 | 747 |
| Ermine Street Guard | 322 | 14 | 6 | 8 | 14 | 0 | 0 | 2 | 5 | 2998 | 385 |
| Saurabh Singh Shekhawat | 258 | 11 | 3 | 8 | 11 | 3 | 0 | 0 | 0 | 2459 | 280 |
| Thérèse Bermingham | 716 | 35 | 11 | 24 | 35 | 3 | 0 | 2 | 5 | 8254 | 889 |
| Dance Fever (album) | 1685 | 78 | 22 | 56 | 78 | 3 | 0 | 3 | 8 | 16391 | 1990 |
| Marta Ptaszynska | 356 | 14 | 1 | 13 | 14 | 0 | 0 | 1 | 2 | 3180 | 376 |
| Blue Key Honor Society | 221 | 8 | 2 | 6 | 8 | 1 | 0 | 1 | 3 | 1830 | 210 |
| Reformed Great Church of Debrecen | 521 | 21 | 4 | 17 | 21 | 1 | 0 | 1 | 2 | 4322 | 526 |
| Don Warrington | 407 | 19 | 7 | 12 | 19 | 0 | 0 | 2 | 4 | 4062 | 490 |
| Hennild Wollstadmo | 250 | 8 | 3 | 5 | 8 | 0 | 0 | 2 | 4 | 1815 | 230 |
| Jerusalem Embassy Act | 2141 | 89 | 31 | 58 | 89 | 1 | 0 | 14 | 34 | 20422 | 2540 |
| Jan Willenberg | 385 | 19 | 9 | 10 | 19 | 2 | 0 | 3 | 5 | 4074 | 545 |
| Larkhall Athletic F.C. | 246 | 11 | 5 | 6 | 11 | 0 | 0 | 0 | 0 | 2188 | 276 |
| Järvevälja Landscape Conservation Area | 295 | 10 | 2 | 8 | 10 | 0 | 0 | 2 | 4 | 2375 | 273 |
| Donald Hustad | 366 | 14 | 1 | 13 | 14 | 0 | 0 | 3 | 4 | 3573 | 395 |
| Lactobacillus acetotolerans | 382 | 13 | 0 | 13 | 13 | 0 | 0 | 1 | 2 | 2824 | 328 |
| Jeremy Hazelbaker | 240 | 8 | 3 | 5 | 8 | 0 | 0 | 1 | 2 | 1970 | 220 |
| Tang Xing | 622 | 26 | 6 | 20 | 26 | 1 | 0 | 1 | 2 | 5332 | 676 |
| Tabourot | 208 | 12 | 2 | 10 | 12 | 0 | 0 | 0 | 0 | 2408 | 294 |
| Chenartu | 254 | 13 | 5 | 8 | 13 | 1 | 0 | 1 | 2 | 2624 | 336 |
| Dannielynn Birkhead paternity case | 1709 | 70 | 29 | 41 | 70 | 4 | 0 | 0 | 0 | 15480 | 1800 |
| 1948 Ole Miss Rebels football team | 425 | 18 | 7 | 11 | 18 | 1 | 0 | 3 | 4 | 4206 | 498 |
| Gerald McBurrows | 306 | 12 | 3 | 9 | 12 | 0 | 0 | 2 | 4 | 2861 | 335 |
| Paul Rinaldi | 454 | 20 | 9 | 11 | 20 | 1 | 0 | 4 | 7 | 4621 | 522 |
| Imports to Ur | 1263 | 53 | 7 | 46 | 53 | 1 | 0 | 2 | 5 | 10024 | 1304 |
| Cookeina sulcipes | 213 | 11 | 3 | 8 | 11 | 0 | 0 | 2 | 6 | 2368 | 284 |
| List of second batch of declared historic buildings in Hangzhou | 715 | 27 | 10 | 17 | 27 | 3 | 0 | 3 | 6 | 6194 | 786 |
| Liz Da-Silva | 420 | 15 | 5 | 10 | 15 | 0 | 0 | 3 | 6 | 4243 | 439 |
| Camaricus formosus | 238 | 9 | 3 | 6 | 9 | 0 | 0 | 1 | 2 | 1874 | 232 |
| Strontium carbide | 2264 | 80 | 19 | 61 | 79 | 2 | 0 | 2 | 4 | 17216 | 2114 |
| Authors' conference | 1465 | 62 | 7 | 55 | 62 | 6 | 0 | 0 | 0 | 12621 | 1551 |
| 9 Mile, Lae | 457 | 26 | 7 | 19 | 21 | 6 | 0 | 0 | 0 | 4722 | 610 |
| Hyphaenieae | 285 | 17 | 8 | 9 | 17 | 0 | 0 | 0 | 0 | 3339 | 402 |
| Elisabeth, Countess of Sponheim-Kreuznach | 769 | 39 | 16 | 23 | 39 | 0 | 0 | 6 | 15 | 7798 | 978 |
| List of restriction enzyme cutting sites | 866 | 28 | 1 | 27 | 28 | 6 | 0 | 0 | 0 | 6374 | 701 |
| Bilala people | 758 | 31 | 12 | 19 | 31 | 0 | 0 | 4 | 10 | 7353 | 907 |
| Ken Boyd | 254 | 11 | 5 | 6 | 11 | 0 | 0 | 3 | 8 | 3656 | 343 |
| Role of The Doon School in Indian mountaineering | 827 | 35 | 16 | 19 | 35 | 0 | 0 | 2 | 5 | 8088 | 925 |
| The Killing (novel) | 330 | 15 | 2 | 13 | 15 | 0 | 0 | 0 | 0 | 2705 | 363 |
| Western blot | 2197 | 80 | 14 | 66 | 76 | 3 | 0 | 4 | 8 | 19206 | 2146 |
| Wandle River | 290 | 12 | 2 | 10 | 12 | 1 | 0 | 0 | 0 | 2434 | 292 |
| Engagements Clause | 343 | 13 | 3 | 10 | 13 | 1 | 0 | 1 | 4 | 3660 | 362 |
| Alimamy Koroma | 231 | 9 | 2 | 7 | 9 | 0 | 0 | 1 | 2 | 2054 | 233 |
| Nicetas II of Constantinople | 203 | 6 | 2 | 4 | 6 | 0 | 0 | 2 | 5 | 1813 | 214 |
| Obscure Records | 450 | 17 | 1 | 16 | 17 | 1 | 0 | 3 | 3 | 3867 | 458 |
| Boundstone Community College | 301 | 10 | 3 | 7 | 10 | 1 | 0 | 2 | 5 | 2639 | 284 |
| Shaheed Tajuddin Ahmad Medical College | 288 | 10 | 3 | 7 | 10 | 1 | 0 | 3 | 6 | 2408 | 274 |
| Etienne Oosthuizen (rugby union, born 1992) | 560 | 20 | 5 | 15 | 20 | 0 | 0 | 8 | 14 | 5332 | 595 |
| Shire of Burnett | 511 | 24 | 7 | 17 | 24 | 2 | 0 | 2 | 3 | 5460 | 632 |
| Munetoshi | 212 | 9 | 1 | 8 | 9 | 0 | 0 | 0 | 0 | 1843 | 229 |
| Aleksandr Belyavsky (actor) | 371 | 13 | 6 | 7 | 13 | 2 | 0 | 4 | 8 | 3877 | 406 |
| Watershed and Flood Prevention Operations Program | 342 | 12 | 1 | 11 | 12 | 0 | 0 | 1 | 2 | 3491 | 340 |
| Descendants of Manuel I of Portugal | 514 | 28 | 6 | 22 | 28 | 0 | 0 | 0 | 0 | 4991 | 664 |
| Valdemar oil and gas field | 246 | 10 | 2 | 8 | 10 | 0 | 0 | 4 | 6 | 2646 | 276 |
| Brief Somebodies | 816 | 33 | 10 | 23 | 33 | 1 | 0 | 3 | 7 | 7695 | 852 |
| Toledo Express Airport | 1944 | 78 | 18 | 60 | 73 | 11 | 1 | 14 | 22 | 18094 | 2138 |
| Henry Hoke (author) | 323 | 14 | 6 | 8 | 14 | 0 | 0 | 2 | 6 | 3462 | 382 |
| Jake Higgs | 250 | 11 | 8 | 3 | 11 | 0 | 0 | 2 | 4 | 2406 | 308 |
| Presidio of Santa Barbara | 935 | 36 | 15 | 21 | 36 | 0 | 0 | 3 | 7 | 8617 | 961 |
| Jarod Palmer | 606 | 23 | 8 | 15 | 23 | 0 | 0 | 6 | 13 | 5524 | 646 |
| Oregon Route 140 | 329 | 16 | 10 | 6 | 16 | 3 | 0 | 0 | 0 | 2980 | 381 |
| Grand Isle, Maine | 323 | 16 | 7 | 9 | 16 | 0 | 0 | 3 | 4 | 3245 | 393 |
| Empis bistortae | 255 | 13 | 6 | 7 | 13 | 0 | 0 | 0 | 0 | 2194 | 311 |
| Eva Canel | 216 | 13 | 8 | 5 | 13 | 0 | 0 | 1 | 5 | 2990 | 360 |
| The Silencers (film) | 523 | 26 | 15 | 11 | 25 | 0 | 0 | 3 | 8 | 6088 | 683 |
| Corps colours of the Luftwaffe (1935–1945) | 799 | 39 | 11 | 28 | 39 | 1 | 0 | 2 | 2 | 8624 | 1029 |
| Ronnie Greenwald | 534 | 20 | 6 | 14 | 20 | 1 | 0 | 3 | 4 | 4780 | 561 |
| Plagiognathus syrticolae | 249 | 11 | 6 | 5 | 11 | 1 | 0 | 1 | 2 | 2126 | 270 |
| Trans-Tasman Cup | 435 | 15 | 5 | 10 | 15 | 1 | 0 | 3 | 6 | 3504 | 406 |
| Côme-Séraphin Cherrier (Quebec politician) | 318 | 8 | 1 | 7 | 8 | 0 | 0 | 3 | 4 | 2242 | 250 |
| Steve Luxton | 645 | 28 | 13 | 15 | 28 | 0 | 0 | 2 | 6 | 6380 | 746 |
| World Business Council for Sustainable Development | 644 | 21 | 4 | 17 | 21 | 2 | 0 | 0 | 0 | 4947 | 572 |
| Anthony Lynham | 327 | 13 | 3 | 10 | 13 | 0 | 0 | 3 | 5 | 3288 | 372 |
| Elathur Assembly constituency | 320 | 10 | 5 | 5 | 10 | 3 | 0 | 0 | 0 | 2283 | 271 |
| Messenger Feast | 1520 | 56 | 19 | 37 | 56 | 3 | 0 | 9 | 14 | 13284 | 1550 |
| Bush tomato | 2205 | 80 | 9 | 71 | 74 | 1 | 0 | 2 | 4 | 17099 | 2041 |
| Faceted Application of Subject Terminology | 741 | 30 | 5 | 25 | 30 | 1 | 0 | 0 | 0 | 6396 | 737 |
| Empereur Island | 414 | 16 | 6 | 10 | 16 | 2 | 0 | 0 | 0 | 3462 | 415 |
| SJFA West Region Ayrshire District | 744 | 21 | 10 | 11 | 21 | 5 | 0 | 2 | 4 | 5700 | 605 |
| Vyshhorod urban hromada | 372 | 21 | 4 | 17 | 21 | 5 | 0 | 1 | 2 | 4198 | 529 |
| Music (Xperia) | 327 | 11 | 0 | 11 | 11 | 0 | 0 | 0 | 0 | 2134 | 267 |
| Live Santa Monica '72 | 464 | 13 | 5 | 8 | 13 | 1 | 0 | 5 | 6 | 3831 | 387 |
| Batesiella | 294 | 11 | 3 | 8 | 11 | 0 | 0 | 2 | 3 | 2129 | 276 |
| Andrea Andersson-Tay | 263 | 8 | 2 | 6 | 8 | 0 | 0 | 2 | 5 | 1837 | 217 |
| Our Lady of the Assumption Convent, Warwick | 358 | 9 | 1 | 8 | 9 | 0 | 0 | 3 | 4 | 2116 | 236 |
| List of compositions by Franz Schubert (1816) | 599 | 24 | 8 | 16 | 24 | 8 | 0 | 1 | 2 | 8624 | 618 |
| Canadian Council of Human Resources Associations | 447 | 14 | 2 | 12 | 14 | 0 | 0 | 0 | 0 | 3515 | 372 |
| Kakarud | 220 | 11 | 6 | 5 | 11 | 1 | 0 | 1 | 2 | 2482 | 289 |
| Jeff Cross | 342 | 14 | 3 | 11 | 14 | 0 | 0 | 2 | 5 | 4469 | 405 |
| Morgenröthe-Rautenkranz | 225 | 9 | 3 | 6 | 9 | 0 | 0 | 2 | 3 | 1902 | 244 |
| Afghanistan Cricket Board | 502 | 20 | 4 | 16 | 20 | 0 | 0 | 3 | 7 | 5404 | 577 |
| Okpo, Madaya | 270 | 12 | 5 | 7 | 12 | 0 | 0 | 1 | 3 | 2423 | 302 |
| Boulder Valley Grange No. 131 | 464 | 16 | 2 | 14 | 16 | 3 | 0 | 4 | 9 | 3884 | 430 |
| Women in journalism | 383 | 17 | 0 | 17 | 17 | 0 | 0 | 2 | 4 | 3325 | 440 |
| Emotional (Jeffrey Osborne album) | 541 | 25 | 8 | 17 | 25 | 5 | 0 | 1 | 2 | 5154 | 617 |
| Lord Edward Russell (1642–1714) | 1103 | 51 | 25 | 26 | 50 | 0 | 0 | 10 | 21 | 12086 | 1360 |
| World Rainforest Movement | 780 | 34 | 3 | 31 | 34 | 0 | 0 | 1 | 2 | 6906 | 852 |
| List of ship commissionings in 1923 | 202 | 8 | 1 | 7 | 8 | 0 | 0 | 2 | 5 | 1832 | 204 |
| Sammamish High School | 875 | 37 | 10 | 27 | 37 | 2 | 0 | 3 | 4 | 7857 | 921 |
| Simone Smith | 247 | 12 | 4 | 8 | 12 | 0 | 0 | 1 | 4 | 3197 | 320 |
| Memphis Tigers | 341 | 13 | 6 | 7 | 13 | 0 | 0 | 0 | 0 | 2739 | 347 |
| On the Road with Ellison Volume 2 | 391 | 20 | 3 | 17 | 20 | 1 | 0 | 1 | 1 | 3779 | 484 |
| Sherman Township, Cass County, Missouri | 213 | 10 | 6 | 4 | 10 | 0 | 0 | 1 | 2 | 2101 | 254 |
| Clash at the Consulate General of China, Manchester | 309 | 10 | 4 | 6 | 10 | 0 | 0 | 2 | 3 | 3084 | 330 |
| Alf's Carpet | 468 | 20 | 8 | 12 | 20 | 0 | 0 | 2 | 4 | 4590 | 527 |
| Moschatel Press | 909 | 38 | 8 | 30 | 38 | 0 | 0 | 2 | 8 | 8252 | 974 |
| Luca Homonnai | 286 | 11 | 0 | 11 | 11 | 2 | 0 | 2 | 4 | 3059 | 296 |
| List of Billboard Latin Rhythm Albums number ones of 2013 | 511 | 22 | 6 | 16 | 22 | 0 | 0 | 0 | 0 | 4807 | 564 |
| Campbell Biology | 296 | 7 | 1 | 6 | 7 | 1 | 0 | 1 | 2 | 1900 | 201 |
| Antonio Ferrara (politician) | 214 | 9 | 3 | 6 | 9 | 1 | 0 | 3 | 7 | 2279 | 258 |
| Netjernakht | 1221 | 61 | 6 | 55 | 59 | 2 | 0 | 0 | 0 | 11379 | 1461 |
| Peoria people | 852 | 38 | 21 | 17 | 38 | 0 | 0 | 3 | 8 | 7714 | 992 |
| Wiseana umbraculata | 285 | 11 | 3 | 8 | 11 | 3 | 0 | 1 | 1 | 2084 | 268 |
| The Man Who Crossed Hitler | 567 | 27 | 8 | 19 | 27 | 1 | 0 | 2 | 5 | 6282 | 738 |
| First Cellular of Southern Illinois | 596 | 23 | 7 | 16 | 22 | 1 | 0 | 2 | 3 | 5132 | 621 |
| Virginia Huget | 376 | 12 | 2 | 10 | 12 | 0 | 0 | 1 | 2 | 2834 | 346 |
| Edward Van Winkle | 432 | 19 | 9 | 10 | 19 | 0 | 0 | 3 | 4 | 4487 | 550 |
| Mary Jane Watson (2002 film series character) | 840 | 35 | 10 | 25 | 35 | 1 | 0 | 1 | 2 | 7629 | 875 |
| Tobolsk Remezov Airport | 225 | 12 | 3 | 9 | 9 | 0 | 0 | 1 | 2 | 2345 | 318 |
| Mushowani Stars F.C. | 488 | 18 | 5 | 13 | 18 | 0 | 0 | 4 | 6 | 3997 | 473 |
| Madly Off in All Directions | 2139 | 76 | 19 | 57 | 76 | 1 | 0 | 17 | 24 | 17847 | 2079 |
| Gerd Völs | 203 | 7 | 3 | 4 | 7 | 1 | 0 | 4 | 5 | 2022 | 211 |
| 1981 Junior League World Series | 271 | 12 | 6 | 6 | 12 | 0 | 0 | 3 | 5 | 2969 | 365 |
| Kevin Miller (voice actor) | 247 | 15 | 3 | 12 | 15 | 0 | 0 | 1 | 2 | 3526 | 421 |
| Masappady Mathupillai | 262 | 15 | 6 | 9 | 15 | 0 | 0 | 1 | 2 | 2966 | 369 |
| National Register of Historic Places listings in Kings County, California | 494 | 22 | 5 | 17 | 22 | 2 | 0 | 0 | 0 | 4340 | 546 |
| The Stolen Body | 329 | 11 | 5 | 6 | 11 | 1 | 0 | 4 | 7 | 3873 | 411 |
| Pogar, Russia | 289 | 18 | 4 | 14 | 8 | 1 | 0 | 0 | 0 | 3486 | 439 |
| State Senior High School 1 Mungkid | 968 | 40 | 9 | 31 | 40 | 4 | 0 | 4 | 8 | 9377 | 1028 |
| 1990 Grand Prix de Tennis de Lyon – Singles | 467 | 15 | 6 | 9 | 15 | 1 | 0 | 5 | 7 | 4358 | 469 |
| Saw E | 718 | 31 | 5 | 26 | 31 | 2 | 0 | 3 | 6 | 6872 | 790 |
| 1882 Pittsburgh Alleghenys season | 551 | 22 | 7 | 15 | 22 | 3 | 0 | 1 | 1 | 4474 | 564 |
| The Islands | 261 | 9 | 4 | 5 | 9 | 0 | 0 | 2 | 2 | 2148 | 256 |
| Researchers Alliance for Development | 877 | 37 | 6 | 31 | 37 | 1 | 0 | 0 | 0 | 7540 | 949 |
| Chris Cook (cornerback) | 298 | 10 | 3 | 7 | 10 | 0 | 0 | 2 | 3 | 2558 | 292 |
| Samurai (ride) | 379 | 14 | 2 | 12 | 14 | 0 | 0 | 3 | 5 | 3106 | 379 |
| Felipe Paullier | 400 | 13 | 3 | 10 | 13 | 0 | 0 | 2 | 4 | 3326 | 356 |
| Breitachklamm | 579 | 26 | 7 | 19 | 26 | 1 | 0 | 1 | 2 | 5403 | 659 |
| Jaak Panksepp | 608 | 26 | 5 | 21 | 26 | 0 | 0 | 2 | 2 | 6464 | 738 |
| Yosra Dhieb | 215 | 6 | 2 | 4 | 6 | 1 | 1 | 3 | 5 | 1696 | 202 |
| Renata Polverini | 249 | 8 | 2 | 6 | 8 | 0 | 0 | 2 | 4 | 2062 | 239 |
| Mohawk Mall | 464 | 18 | 4 | 14 | 18 | 2 | 0 | 3 | 3 | 3956 | 461 |
| The Middle Toe of the Right Foot | 446 | 16 | 3 | 13 | 16 | 0 | 0 | 3 | 5 | 3852 | 464 |
| 1992 Allan Cup | 258 | 10 | 3 | 7 | 10 | 0 | 0 | 2 | 3 | 2420 | 266 |
| 1st Somersetshire Engineers | 519 | 21 | 8 | 13 | 21 | 0 | 1 | 4 | 9 | 5337 | 640 |
| Farmhouses of Brugherio | 578 | 17 | 6 | 11 | 17 | 2 | 0 | 1 | 3 | 3785 | 426 |
| LIH | 239 | 12 | 3 | 9 | 12 | 0 | 0 | 0 | 0 | 2981 | 298 |
| Benjamin Wistar Morris (bishop) | 233 | 10 | 5 | 5 | 10 | 0 | 0 | 1 | 3 | 2649 | 342 |
| Controller of Certifying Authority | 284 | 15 | 3 | 12 | 15 | 0 | 0 | 0 | 0 | 3324 | 396 |
| P. J. Keenan | 1181 | 44 | 15 | 29 | 44 | 1 | 0 | 9 | 14 | 10123 | 1181 |
| Alois Vogt | 237 | 8 | 3 | 5 | 8 | 0 | 0 | 4 | 6 | 2237 | 266 |
| North Korea at the 1972 Summer Olympics | 336 | 17 | 6 | 11 | 17 | 5 | 0 | 1 | 4 | 3566 | 428 |
| Eperua falcata | 281 | 13 | 1 | 12 | 13 | 0 | 0 | 0 | 0 | 2497 | 308 |
| Dave Amadio | 323 | 9 | 0 | 9 | 9 | 2 | 0 | 5 | 8 | 3264 | 340 |
| Bernard Takawira | 1164 | 49 | 10 | 39 | 49 | 0 | 0 | 2 | 3 | 9640 | 1220 |
| History of professional baseball in Allentown, Pennsylvania | 404 | 14 | 5 | 9 | 14 | 0 | 0 | 2 | 4 | 4653 | 473 |
| BB5 (film) | 392 | 16 | 6 | 10 | 13 | 0 | 0 | 2 | 2 | 3272 | 408 |
| Shri Madhopur railway station | 218 | 12 | 4 | 8 | 9 | 1 | 0 | 0 | 0 | 2024 | 301 |
| Vilna Educational District | 1302 | 51 | 8 | 43 | 51 | 9 | 0 | 4 | 10 | 11851 | 1404 |
| Boophis liami | 485 | 17 | 2 | 15 | 17 | 0 | 0 | 0 | 0 | 3464 | 432 |
| Dino Bauk | 391 | 16 | 1 | 15 | 15 | 0 | 0 | 4 | 8 | 3731 | 421 |
| Yousry Hafez | 202 | 6 | 1 | 5 | 6 | 0 | 0 | 5 | 5 | 1840 | 188 |
| H320 | 237 | 11 | 2 | 9 | 11 | 0 | 0 | 1 | 2 | 2874 | 297 |
| Athlone South | 327 | 11 | 4 | 7 | 11 | 0 | 0 | 2 | 2 | 2300 | 286 |
| Menendez: A Killing in Beverly Hills | 230 | 10 | 4 | 6 | 10 | 0 | 0 | 3 | 8 | 2333 | 262 |
| Herbert Enderton | 546 | 27 | 4 | 23 | 27 | 0 | 0 | 4 | 7 | 5659 | 683 |
| Elena Waiss | 361 | 17 | 3 | 14 | 17 | 0 | 0 | 1 | 4 | 3739 | 438 |
| Oued Sejenane | 300 | 16 | 7 | 9 | 16 | 1 | 0 | 0 | 0 | 2913 | 382 |
| List of mayors of Welland | 403 | 22 | 7 | 15 | 22 | 2 | 0 | 2 | 2 | 4501 | 565 |
| Little spotted kiwi | 848 | 33 | 10 | 23 | 33 | 4 | 0 | 4 | 8 | 7576 | 886 |
| National Border Management Agency | 1041 | 48 | 6 | 42 | 48 | 1 | 0 | 1 | 3 | 10276 | 1197 |
| Nemegt Basin | 263 | 12 | 4 | 8 | 12 | 1 | 0 | 0 | 0 | 2450 | 298 |
| Phebalium squamulosum | 388 | 15 | 2 | 13 | 15 | 0 | 0 | 0 | 0 | 3399 | 374 |
| Immigrant benefits urban legend | 282 | 10 | 4 | 6 | 10 | 0 | 0 | 1 | 2 | 2647 | 276 |
| 2010–11 Czech First League | 310 | 9 | 0 | 9 | 9 | 0 | 0 | 4 | 4 | 2506 | 254 |
| Laetitia Masson | 220 | 8 | 3 | 5 | 8 | 1 | 0 | 3 | 5 | 1946 | 226 |
| Bekir Choban-zade | 1349 | 48 | 3 | 45 | 48 | 1 | 0 | 5 | 6 | 11652 | 1316 |
| War Commemorative Medal (Austria) | 216 | 9 | 5 | 4 | 9 | 0 | 0 | 1 | 2 | 2006 | 240 |
| Hægeland Municipality | 787 | 30 | 8 | 22 | 30 | 2 | 0 | 5 | 7 | 7278 | 823 |
| 2019 Reign FC season | 728 | 25 | 7 | 18 | 25 | 3 | 0 | 3 | 7 | 6286 | 711 |
| 1st Kurasovo | 260 | 16 | 6 | 10 | 8 | 1 | 0 | 2 | 3 | 3444 | 425 |
| Mehrnoush Najafi Ragheb | 466 | 21 | 3 | 18 | 21 | 0 | 0 | 2 | 8 | 4693 | 540 |
| Raybon Brothers (album) | 515 | 17 | 1 | 16 | 17 | 4 | 0 | 1 | 2 | 3676 | 432 |
| Baggage | 945 | 49 | 3 | 46 | 49 | 2 | 0 | 0 | 0 | 8766 | 1170 |
| Imanta Station | 238 | 9 | 6 | 3 | 9 | 0 | 0 | 0 | 0 | 1832 | 247 |
| Corruption in Haiti | 877 | 37 | 5 | 32 | 37 | 2 | 0 | 1 | 2 | 7794 | 946 |
| NB Private Equity Partners | 335 | 15 | 8 | 7 | 15 | 1 | 0 | 1 | 2 | 3126 | 390 |
| Hans von Ohain | 4111 | 145 | 24 | 121 | 145 | 10 | 0 | 19 | 36 | 36066 | 4095 |
| Australian Architecture Association | 410 | 16 | 5 | 11 | 16 | 1 | 0 | 1 | 3 | 3475 | 421 |
| Finland in the Eurovision Song Contest 1963 | 696 | 24 | 7 | 17 | 24 | 0 | 0 | 3 | 6 | 5396 | 654 |
| 22–23 The Shambles | 248 | 11 | 5 | 6 | 11 | 0 | 0 | 2 | 3 | 2434 | 313 |
| Sperm Whale (film) | 263 | 12 | 5 | 7 | 12 | 1 | 0 | 0 | 0 | 2631 | 306 |
| Nushagak Peninsula | 468 | 23 | 5 | 18 | 17 | 5 | 0 | 1 | 2 | 4634 | 574 |
| Gregorius and Mary Hanka Farmstead | 670 | 24 | 5 | 19 | 24 | 1 | 0 | 2 | 5 | 5761 | 642 |
| Weightlifting at the 1998 Asian Games – Women's 63 kg | 560 | 24 | 4 | 20 | 24 | 3 | 0 | 2 | 5 | 5194 | 610 |
| Thomas H. Beeby | 284 | 13 | 4 | 9 | 13 | 0 | 0 | 2 | 6 | 3243 | 379 |
| Wildeboer Dellelce | 466 | 16 | 4 | 12 | 15 | 2 | 0 | 4 | 10 | 4216 | 452 |
| Scoria | 2902 | 122 | 20 | 102 | 118 | 3 | 0 | 7 | 16 | 26174 | 3128 |
| HLA A1-B8-DR3-DQ2 | 2334 | 100 | 10 | 90 | 100 | 11 | 0 | 1 | 3 | 21574 | 2518 |
| John R. Lawson | 692 | 33 | 10 | 23 | 33 | 2 | 0 | 4 | 8 | 7490 | 892 |
| Violent Crime Crack Unit of Uganda | 1655 | 66 | 12 | 54 | 66 | 0 | 0 | 3 | 8 | 13485 | 1668 |
| Tanjong Rhu MRT station | 912 | 34 | 14 | 20 | 34 | 2 | 0 | 2 | 5 | 7599 | 914 |
| Nevena Ivanović | 513 | 19 | 0 | 19 | 19 | 0 | 0 | 1 | 2 | 4333 | 487 |
| TJ Slavoj Boleráz | 269 | 10 | 3 | 7 | 6 | 0 | 0 | 1 | 1 | 2045 | 254 |
| Sabbath stew | 1129 | 42 | 4 | 38 | 42 | 3 | 0 | 6 | 14 | 9705 | 1144 |
| 1690 Mayrhofer | 349 | 12 | 3 | 9 | 12 | 1 | 0 | 3 | 6 | 3248 | 352 |
| July 1916 lunar eclipse | 649 | 23 | 4 | 19 | 23 | 3 | 0 | 4 | 7 | 5495 | 620 |
| Protein | 3019 | 115 | 5 | 110 | 115 | 9 | 0 | 1 | 2 | 23622 | 2904 |
| Chrysoteuchia topiarius | 416 | 17 | 4 | 13 | 14 | 0 | 0 | 3 | 5 | 3534 | 443 |
| 1992 United States presidential election in Wisconsin | 933 | 32 | 18 | 14 | 32 | 3 | 0 | 9 | 20 | 8371 | 900 |
| Priesthood (LDS Church) | 379 | 19 | 2 | 17 | 19 | 0 | 0 | 0 | 0 | 3903 | 455 |
| 2023–24 Hellenic Football League | 522 | 17 | 4 | 13 | 17 | 6 | 0 | 5 | 6 | 4397 | 492 |
| Gerontia | 215 | 13 | 6 | 7 | 13 | 0 | 0 | 2 | 9 | 3561 | 362 |
| Dirck | 1738 | 54 | 20 | 34 | 43 | 0 | 0 | 3 | 9 | 24504 | 2069 |
| John P. Webster | 251 | 12 | 3 | 9 | 12 | 0 | 0 | 1 | 2 | 2428 | 295 |
| Celeste Johnson | 856 | 39 | 9 | 30 | 38 | 2 | 0 | 9 | 21 | 8501 | 1004 |
| Ingrid Buffonge | 249 | 10 | 4 | 6 | 10 | 1 | 0 | 0 | 0 | 2049 | 251 |
| Blois baronets | 523 | 29 | 13 | 16 | 29 | 2 | 0 | 2 | 5 | 5564 | 704 |
| Philip McMichael | 380 | 14 | 2 | 12 | 14 | 0 | 0 | 0 | 0 | 3084 | 361 |
| V. Balakrishnan (physicist) | 454 | 20 | 4 | 16 | 20 | 0 | 0 | 1 | 3 | 4783 | 523 |
| The American Review: A Whig Journal | 471 | 17 | 5 | 12 | 17 | 1 | 0 | 3 | 5 | 3946 | 469 |
| Coleotechnites canusella | 328 | 17 | 9 | 8 | 15 | 0 | 0 | 0 | 0 | 3217 | 420 |
| KUSQ | 220 | 8 | 4 | 4 | 8 | 1 | 0 | 0 | 0 | 1711 | 216 |
| Charley Harper | 2368 | 89 | 31 | 58 | 89 | 3 | 0 | 13 | 21 | 21720 | 2464 |
| Knightshayes Court | 377 | 19 | 8 | 11 | 19 | 0 | 0 | 0 | 0 | 3643 | 471 |
| Grand Avenue station (BMT Myrtle Avenue Line) | 790 | 28 | 15 | 13 | 28 | 2 | 0 | 5 | 8 | 6710 | 862 |
| Aleksandr Averin (cyclist) | 543 | 21 | 6 | 15 | 21 | 0 | 0 | 6 | 12 | 5202 | 611 |
| Frank Lindsay Bastedo | 2774 | 99 | 36 | 63 | 99 | 2 | 0 | 12 | 29 | 23522 | 2714 |
| Rhwydrys | 440 | 19 | 4 | 15 | 19 | 0 | 0 | 5 | 10 | 4282 | 494 |
| List of high-voltage transmission links in Ireland | 277 | 11 | 5 | 6 | 8 | 2 | 0 | 1 | 1 | 2263 | 283 |
| Peebles (disambiguation) | 841 | 39 | 14 | 25 | 39 | 0 | 0 | 4 | 6 | 16833 | 1338 |
| John J. McVeigh | 238 | 10 | 4 | 6 | 10 | 0 | 0 | 2 | 2 | 2900 | 349 |
| Glen Shiel | 734 | 41 | 15 | 26 | 41 | 5 | 0 | 0 | 0 | 8812 | 992 |
| We Love Bad Boys | 384 | 20 | 13 | 7 | 19 | 0 | 0 | 1 | 2 | 4081 | 503 |
| Fort Atkinson Bridge | 578 | 26 | 15 | 11 | 24 | 2 | 0 | 2 | 7 | 5292 | 699 |
| Gregory Snyder | 208 | 9 | 4 | 5 | 9 | 0 | 0 | 1 | 2 | 1888 | 244 |
| Noises Off (film) | 400 | 18 | 12 | 6 | 18 | 0 | 0 | 3 | 6 | 4673 | 512 |
| School Union 47 | 425 | 19 | 6 | 13 | 19 | 3 | 0 | 1 | 2 | 3620 | 467 |
| Avon River (Gippsland, Victoria) | 299 | 13 | 6 | 7 | 13 | 0 | 0 | 0 | 0 | 2813 | 330 |
| Ui LRT | 632 | 31 | 9 | 22 | 31 | 8 | 0 | 2 | 6 | 6406 | 786 |
| Badrul | 1072 | 40 | 21 | 19 | 40 | 0 | 0 | 6 | 14 | 22366 | 1807 |
| Lycée Maximilien Perret | 210 | 8 | 5 | 3 | 8 | 0 | 0 | 1 | 1 | 1830 | 207 |
| Cara Augustenborg | 261 | 6 | 2 | 4 | 6 | 0 | 0 | 1 | 1 | 1644 | 163 |
| EEBUS | 628 | 24 | 1 | 23 | 24 | 0 | 0 | 0 | 0 | 4797 | 600 |
| Michael Hunter (politician) | 543 | 22 | 11 | 11 | 22 | 0 | 0 | 5 | 8 | 5036 | 610 |
| Masakazu Kaneko | 218 | 9 | 4 | 5 | 9 | 0 | 0 | 2 | 7 | 2379 | 264 |
| Martin F. Bartlett | 304 | 14 | 10 | 4 | 14 | 2 | 0 | 5 | 10 | 3627 | 420 |
| Irina Podnosova | 293 | 12 | 5 | 7 | 12 | 0 | 0 | 4 | 9 | 4752 | 494 |
| Enrique Miguel Baniqued | 599 | 23 | 9 | 14 | 23 | 0 | 0 | 3 | 4 | 5353 | 614 |
| 1946 Dickinson Red Devils football team | 507 | 14 | 3 | 11 | 14 | 0 | 0 | 4 | 8 | 3781 | 417 |
| Oba Abdulkadir Magaji | 230 | 9 | 1 | 8 | 9 | 0 | 0 | 1 | 3 | 2376 | 260 |
| We Demand the Right to Vote | 220 | 9 | 3 | 6 | 9 | 0 | 0 | 2 | 4 | 2192 | 249 |
| Legislative Yuan constituencies in Pingtung County | 373 | 11 | 3 | 8 | 11 | 3 | 0 | 1 | 2 | 2658 | 309 |
| FM4 Frequency Festival | 613 | 23 | 6 | 17 | 23 | 1 | 0 | 3 | 5 | 5449 | 612 |
| 1989–90 Oklahoma Sooners men's basketball team | 2086 | 76 | 30 | 46 | 76 | 16 | 1 | 8 | 15 | 18846 | 2209 |
| Hilgard Junction State Recreation Area | 533 | 25 | 8 | 17 | 25 | 2 | 0 | 0 | 0 | 5392 | 625 |
| MythBusters Jr. | 484 | 19 | 4 | 15 | 19 | 2 | 0 | 1 | 2 | 3978 | 481 |
| Denis Éthier | 623 | 24 | 8 | 16 | 24 | 1 | 0 | 9 | 11 | 5807 | 685 |
| Pyon Yong-rip | 288 | 12 | 2 | 10 | 12 | 0 | 0 | 2 | 3 | 3028 | 336 |
| Gerald Stillit | 813 | 31 | 4 | 27 | 31 | 1 | 0 | 5 | 10 | 7714 | 857 |
| KWRZ | 325 | 15 | 7 | 8 | 15 | 2 | 0 | 2 | 5 | 3220 | 411 |
| Checkweighman | 1855 | 70 | 15 | 55 | 70 | 5 | 0 | 5 | 11 | 14427 | 1816 |
| Gepps Cross, South Australia | 549 | 23 | 9 | 14 | 23 | 0 | 0 | 0 | 0 | 4869 | 574 |
| English League (ice hockey) | 261 | 6 | 1 | 5 | 6 | 0 | 0 | 2 | 3 | 1424 | 156 |
| Borodino District School No. 8 | 745 | 30 | 6 | 24 | 30 | 2 | 0 | 5 | 9 | 6586 | 780 |
| Ecuador at the 1988 Summer Olympics | 265 | 12 | 5 | 7 | 12 | 5 | 0 | 1 | 2 | 2449 | 302 |
| Automated cash handling | 1375 | 54 | 0 | 54 | 51 | 2 | 0 | 1 | 2 | 13224 | 1363 |
| Carry Me Home (book) | 2543 | 101 | 19 | 82 | 100 | 2 | 0 | 8 | 20 | 26012 | 2749 |
| Sindri (mythology) | 264 | 15 | 2 | 13 | 15 | 0 | 0 | 0 | 0 | 2830 | 343 |
| Ulmus alata 'Lace Parasol' | 269 | 11 | 4 | 7 | 7 | 0 | 0 | 0 | 0 | 2046 | 270 |
| Bob Mong | 476 | 18 | 5 | 13 | 18 | 0 | 0 | 6 | 11 | 4428 | 530 |
| Taiwan Power Company F.C. | 1128 | 41 | 15 | 26 | 41 | 2 | 0 | 7 | 15 | 10462 | 1162 |
| Ivan Iakovlev | 270 | 10 | 7 | 3 | 10 | 0 | 0 | 1 | 3 | 2774 | 322 |
| Ron Swoboda | 669 | 20 | 7 | 13 | 20 | 1 | 0 | 3 | 7 | 5696 | 613 |
| Haluk Kırcı | 1717 | 61 | 15 | 46 | 61 | 3 | 0 | 12 | 25 | 15441 | 1770 |
| Why Fish Don't Exist | 510 | 22 | 4 | 18 | 22 | 0 | 0 | 3 | 7 | 5241 | 601 |
| David Reubeni | 1304 | 52 | 14 | 38 | 52 | 3 | 0 | 2 | 7 | 10833 | 1364 |
| Santa María Ipalapa | 253 | 13 | 3 | 10 | 13 | 0 | 0 | 1 | 3 | 2464 | 313 |
| Celtic music | 347 | 12 | 1 | 11 | 12 | 0 | 0 | 0 | 0 | 2588 | 301 |
| 2025–26 LNB Élite season | 300 | 9 | 2 | 7 | 9 | 0 | 0 | 3 | 2 | 2205 | 246 |
| Darryl Jones (disambiguation) | 360 | 14 | 6 | 8 | 14 | 0 | 0 | 3 | 8 | 4224 | 404 |
| Isolated congenital asplenia | 521 | 20 | 3 | 17 | 20 | 1 | 0 | 0 | 0 | 4052 | 512 |
| Inland Revenue Department (Nepal) | 1050 | 43 | 9 | 34 | 38 | 4 | 0 | 1 | 3 | 9796 | 1103 |
| Pickstown Air Force Station | 236 | 9 | 5 | 4 | 9 | 2 | 0 | 0 | 0 | 2042 | 249 |
| Wolfgang, Prince of Anhalt-Köthen | 427 | 25 | 8 | 17 | 25 | 0 | 0 | 2 | 6 | 5806 | 678 |
| Question | 1171 | 46 | 2 | 44 | 46 | 1 | 0 | 0 | 0 | 8461 | 1120 |
| Maruja Montes | 211 | 5 | 3 | 2 | 5 | 0 | 0 | 3 | 3 | 1760 | 195 |
| Vitória A.C. Bié | 667 | 28 | 9 | 19 | 24 | 1 | 0 | 2 | 5 | 6014 | 715 |
| DOM-2,5-DiEtO | 743 | 33 | 4 | 29 | 33 | 2 | 0 | 1 | 2 | 6701 | 816 |
| 2021–22 Grambling State Tigers men's basketball team | 580 | 23 | 5 | 18 | 23 | 0 | 0 | 1 | 2 | 5082 | 608 |
| Loganville, Georgia | 219 | 14 | 5 | 9 | 14 | 2 | 0 | 1 | 2 | 2469 | 326 |
| Platform 0 (Madrid Metro) | 378 | 15 | 3 | 12 | 15 | 2 | 0 | 2 | 6 | 3858 | 411 |
| Pure (Midge Ure album) | 328 | 14 | 1 | 13 | 14 | 1 | 0 | 1 | 1 | 2869 | 346 |
| Andreas Allescher | 845 | 34 | 18 | 16 | 34 | 1 | 0 | 9 | 23 | 8839 | 1012 |
| Gasht | 242 | 14 | 8 | 6 | 14 | 0 | 0 | 0 | 0 | 3596 | 356 |
| Earby railway station | 201 | 11 | 7 | 4 | 11 | 0 | 0 | 1 | 3 | 2507 | 288 |
| Paleodictyon | 342 | 11 | 2 | 9 | 11 | 0 | 0 | 1 | 3 | 2410 | 284 |
| Richard Dean | 317 | 15 | 6 | 9 | 15 | 0 | 0 | 0 | 0 | 3992 | 389 |
| Liquid color | 648 | 27 | 2 | 25 | 24 | 2 | 0 | 0 | 0 | 5228 | 668 |
| List of war films and TV specials set between 1775 and 1914 | 332 | 16 | 1 | 15 | 16 | 1 | 0 | 4 | 4 | 5001 | 667 |
| 2014 MuchMusic Video Awards | 275 | 14 | 6 | 8 | 14 | 1 | 0 | 1 | 3 | 2695 | 353 |
| Giuseppe Stampone | 1012 | 53 | 11 | 42 | 39 | 1 | 0 | 0 | 0 | 9723 | 1272 |
| S. Ramakrishnan | 715 | 38 | 7 | 31 | 38 | 14 | 0 | 2 | 6 | 8638 | 945 |
| Wolfram Grandezka | 541 | 20 | 12 | 8 | 19 | 0 | 0 | 7 | 13 | 4701 | 571 |
| Novyi Yarychiv | 324 | 18 | 4 | 14 | 16 | 3 | 0 | 0 | 0 | 3429 | 445 |
| Torneo Internazionale di Tennis Parioli | 408 | 13 | 2 | 11 | 13 | 1 | 0 | 2 | 5 | 3292 | 369 |
| Dora Richter | 530 | 18 | 4 | 14 | 18 | 0 | 0 | 8 | 10 | 5084 | 559 |
| Parliamentary Secretary to the Ministry for Pensions | 269 | 12 | 1 | 11 | 12 | 0 | 0 | 1 | 3 | 2622 | 304 |
| Social Studies (book) | 1029 | 41 | 6 | 35 | 40 | 1 | 0 | 6 | 9 | 10396 | 1159 |
| Marjorie Mbilinyi | 692 | 26 | 6 | 20 | 26 | 0 | 0 | 2 | 4 | 5301 | 649 |
| Lößnitzbach | 664 | 27 | 8 | 19 | 27 | 0 | 0 | 2 | 6 | 5790 | 697 |
| Henry Alexis Thomson | 294 | 12 | 0 | 12 | 12 | 0 | 0 | 1 | 3 | 2545 | 306 |
| Impeachment of Robert Harley, Earl of Oxford | 992 | 48 | 15 | 33 | 48 | 0 | 0 | 5 | 14 | 10862 | 1237 |
| Agri-Expo | 776 | 26 | 9 | 17 | 26 | 1 | 0 | 3 | 6 | 6440 | 714 |
| 1988 Swedish general election | 237 | 10 | 2 | 8 | 10 | 1 | 0 | 1 | 3 | 2119 | 260 |
| Love Begins at 20 | 353 | 16 | 10 | 6 | 16 | 0 | 0 | 3 | 7 | 3826 | 440 |
| Conclave | 1286 | 55 | 5 | 50 | 55 | 0 | 0 | 7 | 15 | 12610 | 1437 |
| Sughdiyona | 213 | 14 | 7 | 7 | 14 | 0 | 0 | 0 | 0 | 2841 | 345 |
| 1929 Railway Cup Hurling Championship | 575 | 23 | 8 | 15 | 23 | 1 | 0 | 4 | 7 | 5146 | 618 |
| Edward Hordern | 802 | 33 | 5 | 28 | 33 | 3 | 0 | 5 | 8 | 7634 | 906 |
| Pallavur Appu Marar | 344 | 9 | 2 | 7 | 9 | 1 | 0 | 1 | 2 | 2220 | 245 |
| Indian Institute of Rice Research | 1766 | 68 | 12 | 56 | 68 | 3 | 0 | 3 | 10 | 16158 | 1902 |
| Hussam Jouhara | 399 | 17 | 1 | 16 | 17 | 0 | 0 | 0 | 0 | 3481 | 424 |
| Florida State Road 59 | 516 | 23 | 6 | 17 | 23 | 5 | 0 | 0 | 0 | 5740 | 589 |
| George Smith (footballer, born 1996) | 404 | 16 | 7 | 9 | 16 | 0 | 0 | 1 | 2 | 3892 | 430 |
| Mithun Chakraborty filmography | 263 | 11 | 2 | 9 | 11 | 0 | 0 | 0 | 0 | 2173 | 270 |
| Rich Strenger | 371 | 13 | 5 | 8 | 13 | 1 | 0 | 2 | 4 | 3258 | 372 |
| Khagen Mahanta | 429 | 23 | 7 | 16 | 23 | 0 | 0 | 1 | 1 | 4267 | 554 |
| Soldier Son trilogy | 247 | 13 | 4 | 9 | 13 | 0 | 0 | 0 | 0 | 2704 | 319 |
| Delegada Katarina | 233 | 8 | 2 | 6 | 8 | 0 | 0 | 3 | 7 | 2131 | 235 |
| Raas Dance | 492 | 18 | 5 | 13 | 18 | 0 | 0 | 2 | 4 | 4063 | 489 |
| Rutland Railway Museum | 220 | 9 | 3 | 6 | 9 | 0 | 0 | 0 | 0 | 1816 | 224 |
| Confessions (Mimi Webb album) | 343 | 11 | 1 | 10 | 11 | 1 | 0 | 2 | 4 | 2372 | 286 |
| 2007 British premium-rate phone-in scandal | 873 | 36 | 4 | 32 | 36 | 4 | 0 | 5 | 9 | 8477 | 979 |
| OshTV | 364 | 17 | 4 | 13 | 17 | 0 | 0 | 2 | 3 | 3775 | 454 |
| Alexander Ramm | 343 | 15 | 4 | 11 | 15 | 0 | 0 | 1 | 3 | 3526 | 392 |
| Amantea Castle | 804 | 37 | 5 | 32 | 37 | 0 | 0 | 4 | 7 | 8170 | 959 |
| Fat Lizard | 393 | 19 | 3 | 16 | 19 | 4 | 0 | 3 | 8 | 3817 | 473 |
| Pornography in Armenia | 405 | 18 | 4 | 14 | 18 | 2 | 0 | 3 | 8 | 5128 | 588 |
| Mycena strobilinoides | 803 | 30 | 6 | 24 | 30 | 4 | 0 | 0 | 0 | 5602 | 734 |
| Thomas Rees (Twm Carnabwth) | 367 | 14 | 3 | 11 | 14 | 1 | 0 | 3 | 6 | 3453 | 382 |
| Kirsten Storms | 427 | 20 | 7 | 13 | 20 | 0 | 0 | 3 | 6 | 4490 | 516 |
| Rudolf Koppitz | 435 | 19 | 6 | 13 | 19 | 0 | 0 | 2 | 2 | 3925 | 486 |
| Indian Institute of Management Shillong | 941 | 42 | 4 | 38 | 42 | 0 | 0 | 3 | 8 | 9205 | 1077 |
| Western Canadian Music Awards | 526 | 17 | 3 | 14 | 17 | 0 | 0 | 2 | 6 | 4384 | 470 |
| Christine Tartaglione | 275 | 8 | 3 | 5 | 8 | 0 | 0 | 2 | 4 | 2227 | 254 |
| Księginice | 248 | 11 | 4 | 7 | 11 | 0 | 0 | 0 | 0 | 2930 | 298 |
| 1998 California Secretary of State election | 314 | 11 | 4 | 7 | 11 | 0 | 0 | 4 | 6 | 2497 | 294 |
| El Congreso de Pueblos de Habla Española | 1235 | 47 | 10 | 37 | 47 | 3 | 0 | 4 | 7 | 11290 | 1279 |
| Morton Kaplan | 337 | 12 | 1 | 11 | 12 | 0 | 0 | 4 | 5 | 3348 | 376 |
| Kō Nishimura | 1311 | 50 | 16 | 34 | 50 | 0 | 0 | 8 | 18 | 12228 | 1364 |
| Liberty and Property Defence League | 864 | 36 | 10 | 26 | 36 | 1 | 0 | 4 | 11 | 8258 | 944 |
| Bruja (album) | 309 | 13 | 6 | 7 | 13 | 0 | 0 | 2 | 4 | 2860 | 334 |
| Unconformity | 1077 | 46 | 6 | 40 | 46 | 1 | 0 | 2 | 6 | 9643 | 1160 |
| Cherry Valley | 862 | 37 | 26 | 11 | 37 | 0 | 0 | 0 | 0 | 15178 | 980 |
| Angle Lake station | 1254 | 41 | 11 | 30 | 41 | 3 | 0 | 11 | 19 | 10778 | 1240 |
| My Name Is Anne, She Said, Anne Frank | 305 | 15 | 4 | 11 | 15 | 1 | 0 | 2 | 4 | 3082 | 366 |
| Lake Temescal | 292 | 10 | 4 | 6 | 10 | 0 | 0 | 0 | 0 | 2089 | 253 |
| Edgewood station (MARC) | 428 | 19 | 11 | 8 | 19 | 2 | 0 | 0 | 0 | 3865 | 514 |
| Sheboygan County, Wisconsin | 443 | 17 | 8 | 9 | 17 | 0 | 0 | 3 | 4 | 3428 | 435 |
| Hermadionella | 244 | 12 | 3 | 9 | 12 | 2 | 0 | 0 | 0 | 2346 | 295 |
| Bearded vulture | 1147 | 42 | 7 | 35 | 42 | 1 | 0 | 5 | 8 | 8898 | 1062 |
| Joseph A. Franklin | 589 | 24 | 7 | 17 | 24 | 0 | 0 | 7 | 15 | 5562 | 651 |
| Mosely-Woods House | 320 | 11 | 2 | 9 | 11 | 0 | 0 | 1 | 1 | 2640 | 287 |
| Casa Consulado (Quiapo) | 256 | 12 | 7 | 5 | 12 | 0 | 0 | 1 | 2 | 2396 | 311 |
| Gasquet, California | 948 | 50 | 14 | 36 | 50 | 6 | 0 | 6 | 9 | 10604 | 1216 |
| Africa95 | 564 | 20 | 6 | 14 | 20 | 1 | 0 | 2 | 2 | 5343 | 624 |
| Pape station | 765 | 34 | 6 | 28 | 34 | 0 | 0 | 2 | 3 | 6834 | 856 |
| Nikon F-601 | 1344 | 48 | 2 | 46 | 48 | 0 | 0 | 2 | 4 | 11494 | 1237 |
| A-VSB | 1123 | 46 | 5 | 41 | 42 | 3 | 0 | 0 | 0 | 9731 | 1172 |
| Alliance for Georgia | 827 | 39 | 16 | 23 | 39 | 0 | 0 | 2 | 3 | 9322 | 1037 |
| James W. Husted (representative) | 249 | 8 | 4 | 4 | 8 | 1 | 0 | 1 | 2 | 1846 | 251 |
| Bowling Park, Bradford | 564 | 30 | 8 | 22 | 30 | 3 | 0 | 0 | 0 | 6324 | 721 |
| Open the Eyes of My Heart | 553 | 28 | 8 | 20 | 28 | 0 | 0 | 2 | 7 | 5637 | 679 |
| Kennedy Expressway | 1631 | 69 | 17 | 52 | 60 | 10 | 0 | 1 | 2 | 15844 | 1730 |
| Cordobés Formation | 258 | 11 | 5 | 6 | 11 | 0 | 0 | 0 | 0 | 2539 | 291 |
| Hypnotic Hick | 475 | 16 | 5 | 11 | 16 | 0 | 0 | 2 | 4 | 3442 | 421 |
| 9th Golden Globes | 212 | 7 | 3 | 4 | 7 | 0 | 0 | 3 | 6 | 2270 | 235 |
| 2022 Open de Rennes – Doubles | 314 | 17 | 10 | 7 | 17 | 0 | 0 | 0 | 0 | 3236 | 417 |
| Ziyaret, Lice | 231 | 11 | 2 | 9 | 11 | 0 | 0 | 2 | 3 | 2076 | 267 |
| Beware of Darkness (band) | 276 | 7 | 2 | 5 | 7 | 0 | 0 | 1 | 3 | 1645 | 186 |
| List of Blue Mountain State episodes | 856 | 27 | 4 | 23 | 27 | 2 | 0 | 8 | 11 | 6513 | 726 |
| Sar Rag | 265 | 14 | 8 | 6 | 14 | 1 | 0 | 1 | 2 | 3232 | 355 |
| List of Postmasters of New York City | 466 | 16 | 10 | 6 | 16 | 0 | 0 | 3 | 9 | 3842 | 450 |
| Tim Wynne-Jones | 444 | 19 | 8 | 11 | 19 | 0 | 0 | 2 | 3 | 4932 | 533 |
| Jantei Story | 737 | 34 | 3 | 31 | 34 | 1 | 0 | 4 | 8 | 7225 | 875 |
| Boxing Libreville | 300 | 12 | 1 | 11 | 12 | 0 | 0 | 1 | 3 | 2786 | 313 |
| Pierre Bessonneau | 569 | 26 | 11 | 15 | 26 | 0 | 0 | 4 | 7 | 5128 | 650 |
| Herman Cain Award | 1395 | 51 | 6 | 45 | 50 | 1 | 0 | 1 | 2 | 11142 | 1292 |
| Sinaloan milk snake | 483 | 16 | 4 | 12 | 16 | 0 | 0 | 0 | 0 | 3522 | 424 |
| Carseview Centre | 287 | 14 | 3 | 11 | 14 | 0 | 0 | 0 | 0 | 2644 | 335 |
| The Roulettes | 231 | 7 | 2 | 5 | 7 | 0 | 0 | 2 | 4 | 1540 | 188 |
| 2024–25 Miami Hurricanes men's basketball team | 2208 | 80 | 20 | 60 | 80 | 5 | 0 | 5 | 10 | 17939 | 2146 |
| Dihybrid cross | 617 | 21 | 4 | 17 | 21 | 5 | 0 | 1 | 3 | 4376 | 523 |
| Bonnie and Terry Turner | 300 | 11 | 4 | 7 | 11 | 0 | 0 | 2 | 1 | 2176 | 295 |
| Psychopia | 281 | 13 | 0 | 13 | 13 | 0 | 0 | 0 | 0 | 2480 | 316 |
| 2026 Liga FUTVE | 404 | 12 | 1 | 11 | 12 | 0 | 0 | 6 | 10 | 4139 | 430 |
| Periclimenes | 359 | 15 | 2 | 13 | 8 | 0 | 0 | 0 | 0 | 3014 | 370 |
| Federal Republic of Central America–United States relations | 431 | 17 | 10 | 7 | 17 | 0 | 0 | 2 | 5 | 4213 | 470 |
| Toni Androić | 320 | 13 | 6 | 7 | 13 | 1 | 0 | 2 | 5 | 3001 | 355 |
| Maria's Paradise | 207 | 6 | 2 | 4 | 6 | 0 | 0 | 2 | 4 | 1668 | 177 |
| Leokaneng | 234 | 9 | 5 | 4 | 9 | 0 | 0 | 0 | 0 | 1825 | 226 |
| Rorippa sinuata | 840 | 33 | 4 | 29 | 33 | 5 | 0 | 0 | 0 | 6548 | 801 |
| Dobri Daskalov | 215 | 7 | 1 | 6 | 7 | 0 | 0 | 2 | 2 | 1678 | 206 |
| Basegi Nature Reserve | 688 | 28 | 10 | 18 | 28 | 1 | 0 | 0 | 0 | 5912 | 717 |
| Fumihiko | 621 | 21 | 8 | 13 | 21 | 0 | 0 | 6 | 12 | 9864 | 795 |
| Frank Weiss | 737 | 27 | 13 | 14 | 27 | 0 | 0 | 9 | 20 | 7488 | 816 |
| Earl of Halsbury | 2207 | 97 | 30 | 67 | 95 | 0 | 0 | 9 | 25 | 22660 | 2699 |
| Bold (river) | 205 | 12 | 5 | 7 | 12 | 3 | 0 | 0 | 0 | 2151 | 283 |
| Andreas Skov Olsen | 259 | 8 | 3 | 5 | 8 | 0 | 0 | 1 | 2 | 2362 | 249 |
| New York State Route 442 | 527 | 25 | 8 | 17 | 25 | 5 | 0 | 1 | 2 | 4936 | 607 |
| Eusebio Fernández Muñiz | 292 | 10 | 2 | 8 | 10 | 0 | 0 | 4 | 5 | 2861 | 312 |
| 1988 European Super Cup | 451 | 20 | 5 | 15 | 20 | 2 | 0 | 1 | 1 | 4587 | 517 |
| 2016–17 Saint Mary's Gaels men's basketball team | 710 | 29 | 9 | 20 | 29 | 1 | 1 | 1 | 1 | 5977 | 760 |
| 2021–22 Rochdale A.F.C. season | 310 | 9 | 1 | 8 | 9 | 0 | 0 | 6 | 5 | 2358 | 282 |
| 1980 Grand Prix d'Automne | 225 | 9 | 4 | 5 | 9 | 0 | 0 | 2 | 3 | 1969 | 245 |
| Vinay Apte | 299 | 8 | 4 | 4 | 8 | 1 | 0 | 3 | 3 | 2178 | 227 |
| Music of Game of Thrones | 1299 | 51 | 12 | 39 | 51 | 2 | 0 | 4 | 8 | 10704 | 1292 |
| Constellations (Miró) | 1910 | 76 | 15 | 61 | 76 | 1 | 0 | 4 | 14 | 19424 | 2028 |

---

## Totals — 1000 pages (stock military-flavored pack, goblin only, no LLM)

| metric | value |
|---|---|
| pages | 1000 |
| total entities | 24,909 (avg 24.9/page) |
| **typed** (matched an anchor category) | 7,035 (28.2%) |
| untyped | 17,874 (71.8%) |
| governing verb captured | 24,380 (97.9%) |
| count captured | 1,268 (5.1%) |
| military unit parsed | 25 |
| item association captured | 5,339 (21.4%) |
| items associated (total) | 2,682 |
| chars processed | 612,709 |

### Structured output the goblin produced for **$0** (no LLM)
- verbose JSON: **5,783,476 tokens**  ·  compact JSON: **667,813 tokens**
- A wizard-alone LLM would have to *emit* this. At Opus 4.8 output pricing ($25/Mtok):
  compact ≈ **$16.70**, verbose ≈ **$144.59** — across 1000 pages,
  paid entirely by the goblin for free. The wizard would pay only for the small residue
  (corrections + anchor suggestions on the 72% untyped tail).

### How the goblin does on its own
- **98%** of entities get their governing verb, **21%** get item
  associations — the *element extraction* is near-complete deterministically.
- **28%** get *typed* — low here only because this is a **military** pack run on
  **general** Wikipedia (name/place rules carry most hits; military_unit/equipment rarely fire).
  Typing is exactly what grows with more anchor *scopes* (org/event/product/group), which the
  rule-based `_RULES` registry adds cheaply.
