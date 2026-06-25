"""Deterministic fuzzy string matching for anchors.

Optimal String Alignment (a.k.a. restricted Damerau-Levenshtein) distance, which
counts insertions, deletions, substitutions, and adjacent transpositions. The
transposition case is what catches typos like "brigdae" -> "brigade" at distance 1.

Matching policy keeps false positives down:
- abbreviations (ALL-CAPS terms) and very short terms (<= 3 chars) match EXACTLY
  only -- fuzzy-matching "BAT" would collide with "bad"/"cat"/"bot";
- longer terms allow a length-scaled edit budget.
"""

from __future__ import annotations


def osa_distance(a: str, b: str, max_dist: int | None = None) -> int:
    """Optimal String Alignment distance. Early-exits past ``max_dist``."""
    la, lb = len(a), len(b)
    if max_dist is not None and abs(la - lb) > max_dist:
        return max_dist + 1
    prev2: list[int] = []
    prev = list(range(lb + 1))
    for i in range(1, la + 1):
        cur = [i] + [0] * lb
        row_min = cur[0]
        for j in range(1, lb + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost)
            if i > 1 and j > 1 and a[i - 1] == b[j - 2] and a[i - 2] == b[j - 1]:
                cur[j] = min(cur[j], prev2[j - 2] + 1)
            row_min = min(row_min, cur[j])
        if max_dist is not None and row_min > max_dist:
            return max_dist + 1
        prev2, prev = prev, cur
    return prev[lb]


def _threshold(n: int) -> int:
    """Conservative edit budget for a term of length ``n``."""
    if n <= 3:
        return 0
    if n <= 6:
        return 1
    if n <= 9:
        return 2
    return 3


def term_matches(term: str, token: str, fuzzy: bool = True) -> bool:
    """True if ``token`` matches ``term`` exactly, or fuzzily when allowed."""
    t, k = term.lower(), token.lower()
    if t == k:
        return True
    if not fuzzy:
        return False
    if term.isupper() or len(t) <= 3:  # abbreviations / very short -> exact only
        return False
    thr = _threshold(len(t))
    if abs(len(t) - len(k)) > thr:
        return False
    return osa_distance(t, k, thr) <= thr
