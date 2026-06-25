"""Deterministic recognizer for military unit designations.

Handles the common forms:
    "3 Corps"                cardinal + echelon
    "I Corps" / "V Corps"    Roman numeral + echelon
    "XVIII Airborne Corps"   Roman + branch + echelon
    "1st Infantry Division"  ordinal + branch + echelon
    "3rd Battalion"          ordinal + echelon
    "C Company"              letter designation (company-level)

The key to staying deterministic without false positives is anchoring on a known
**echelon** keyword: a number/letter/Roman token is only a unit designator when a
recognized echelon immediately follows (optionally via a branch qualifier). That
keeps "I Corps" (unit) distinct from "I went home" (pronoun).

Known limitation: a lone Roman letter that is also a company letter is ambiguous
("C Company" — letter C, or Roman 100?). We resolve it by echelon: single letters
before a company-level echelon are read as letter designations, otherwise Roman.
"""

from __future__ import annotations

import re

# Multi-word echelons must precede their single-word substrings in the alternation.
_ECHELONS = [
    "Field Army", "Army Group", "Task Force", "Corps", "Division", "Brigade",
    "Regiment", "Battalion", "Squadron", "Company", "Battery", "Platoon",
    "Troop", "Wing", "Group", "Fleet", "Command", "Army",
]
_COMPANY_LEVEL = {"Company", "Battery", "Troop", "Platoon"}
_ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

_UNIT_RE = re.compile(
    r"\b(?P<desig>\d{1,3}(?:st|nd|rd|th)?|[IVXLCDM]{1,7})\s+"
    r"(?P<branch>(?:[A-Z][a-z]+\s+){0,3})"
    r"(?P<echelon>" + "|".join(re.escape(e) for e in _ECHELONS) + r")\b"
)


def _int_to_roman(n: int):
    if not 0 < n < 4000:
        return None
    table = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
             (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
             (5, "V"), (4, "IV"), (1, "I")]
    out = ""
    for v, s in table:
        while n >= v:
            out += s
            n -= v
    return out


def _roman_to_int(s: str):
    s = s.upper()
    if any(c not in _ROMAN for c in s):
        return None
    total, prev = 0, 0
    for c in reversed(s):
        v = _ROMAN[c]
        total += -v if v < prev else v
        prev = max(prev, v)
    return total


def _valid_roman(s: str) -> bool:
    """Reject malformed Roman numerals (e.g. 'IIII', 'VV') via round-trip."""
    v = _roman_to_int(s)
    return v is not None and _int_to_roman(v) == s.upper()


def _parse_designation(text: str, echelon: str) -> dict:
    """Normalise a designator into a value + form, given its echelon."""
    t = text.strip()
    m = re.fullmatch(r"(\d{1,3})(?:st|nd|rd|th)", t)
    if m:
        return {"designation": int(m.group(1)), "designation_form": "ordinal"}
    if t.isdigit():
        return {"designation": int(t), "designation_form": "cardinal"}
    # Single letter before a company-level echelon -> letter designation.
    if len(t) == 1 and t.isalpha() and echelon in _COMPANY_LEVEL:
        return {"designation": t, "designation_form": "letter"}
    if _valid_roman(t):
        return {"designation": _roman_to_int(t), "designation_form": "roman"}
    if len(t) == 1 and t.isalpha():
        return {"designation": t, "designation_form": "letter"}
    return {"designation": None, "designation_form": "unknown"}


def detect_units(text: str) -> list[dict]:
    """Find military unit designations in ``text``.

    Each unit: ``text``, ``span`` (char), ``echelon``, ``branch`` (or None),
    ``designation`` (normalised int/letter), ``designation_text``, ``designation_form``.
    """
    units = []
    for m in _UNIT_RE.finditer(text):
        echelon = m.group("echelon")
        parsed = _parse_designation(m.group("desig"), echelon)
        if parsed["designation_form"] == "unknown":
            continue
        branch = (m.group("branch") or "").strip() or None
        units.append({
            "text": m.group(0),
            "span": [m.start(), m.end()],
            "echelon": echelon,
            "branch": branch,
            "designation_text": m.group("desig"),
            **parsed,
        })
    return units


def annotate(doc, entities: list[dict]) -> None:
    """Attach ``mil_unit`` to any entity whose head sits inside a detected unit."""
    units = detect_units(doc.text)
    if not units:
        return
    for ent in entities:
        head_char = doc[ent["_root_i"]].idx
        for u in units:
            if u["span"][0] <= head_char < u["span"][1]:
                ent["mil_unit"] = {
                    k: u[k] for k in
                    ("echelon", "branch", "designation",
                     "designation_text", "designation_form")
                }
                break
