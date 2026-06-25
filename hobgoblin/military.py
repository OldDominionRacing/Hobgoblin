"""Deterministic recognizer for military unit designations.

A unit designation has three parts — **number · type · echelon**:

    1st  Infantry        Division
    XVIII Airborne       Corps
    3rd  Special Troops  Battalion
    I                    Corps          (no type)
    3                    Corps
    C                    Company        (letter designation)
     ^number  ^type      ^echelon

Number and echelon are (almost) always present; the **type** is any run of tokens
between them. We don't hard-code the type vocabulary — it's whatever content words
sit between the number and the echelon.

The matcher anchors on a known **echelon** keyword: a number/letter/Roman token is
only a designation when an echelon follows, with the type in between. That keeps
"I Corps" (unit) distinct from "I went home" (pronoun), and — because the type run
excludes echelons and function words — stops "3RD BRIGADE AND I CORPS" from
collapsing into one unit (it parses as two) and "5 SOLDIERS FROM THE DIVISION" from
matching at all (the run breaks at "FROM", leaving no echelon adjacent).

Known limitation: a lone Roman letter that is also a company letter is ambiguous
("C Company" — letter C, or Roman 100?). We resolve it by echelon: single letters
before a company-level echelon are read as letters, otherwise Roman.
"""

from __future__ import annotations

import re

# CAVEAT: recognition is driven entirely by this fixed vocabulary of echelons.
# It is English- and US/NATO-army-centric; it will miss naval rates, foreign-language
# echelons, joint task-force names, and any org chart that doesn't use these words.
# This is a deliberate, documented assumption — pass your own list via the
# ``echelons=`` argument of ``detect_units`` / ``annotate`` to override it.
DEFAULT_ECHELONS = [
    "Field Army", "Army Group", "Task Force", "Corps", "Division", "Brigade",
    "Regiment", "Battalion", "Squadron", "Company", "Battery", "Platoon",
    "Troop", "Wing", "Group", "Fleet", "Command", "Army",
]
# Echelons small enough that a lone letter before them is a letter designation
# ("C Company") rather than a Roman numeral.
DEFAULT_COMPANY_LEVEL = {"Company", "Battery", "Troop", "Platoon"}
_ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

# Function words can't be part of a unit type — they bound the type run so it can't
# straddle a clause ("5 soldiers FROM THE division" won't match).
_FUNCTION_WORDS = (
    "the|a|an|of|to|with|in|on|at|by|for|from|and|or|but|that|which|who|whose|"
    "was|were|is|are|be|been|being|will|would|has|have|had|its|their|his|her|"
    "this|these|those|as|into|near|over|under|after|before|during|per|then|than|"
    "when|where|while|new|old|via"
)


def _build_regex(echelons):
    # Longest echelons first so multi-word ones win over their substrings.
    # IGNORECASE so ALL-CAPS traffic ("3RD BRIGADE", "I CORPS") still matches.
    ech = "|".join(re.escape(e) for e in sorted(echelons, key=len, reverse=True))
    # A type word: a content word that is neither an echelon nor a function word.
    type_word = (r"(?!(?:" + ech + r")\b)(?!(?:" + _FUNCTION_WORDS
                 + r")\b)[A-Za-z][A-Za-z'.\-]*")
    return re.compile(
        r"\b(?P<number>\d{1,3}(?:st|nd|rd|th)?|[IVXLCDM]{1,7})\s+"
        r"(?P<type>(?:" + type_word + r"\s+){0,4})"
        r"(?P<echelon>" + ech + r")\b",
        re.IGNORECASE,
    )


_DEFAULT_RE = _build_regex(DEFAULT_ECHELONS)


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


def _parse_number(text: str, echelon: str, company_lower) -> dict:
    """Normalise a unit number into a value + form, given its echelon."""
    t = text.strip()
    m = re.fullmatch(r"(\d{1,3})(?:st|nd|rd|th)", t, re.IGNORECASE)
    if m:
        return {"number": int(m.group(1)), "number_form": "ordinal"}
    if t.isdigit():
        return {"number": int(t), "number_form": "cardinal"}
    # Single letter before a company-level echelon -> letter designation.
    if len(t) == 1 and t.isalpha() and echelon.lower() in company_lower:
        return {"number": t.upper(), "number_form": "letter"}
    if _valid_roman(t):
        return {"number": _roman_to_int(t), "number_form": "roman"}
    if len(t) == 1 and t.isalpha():
        return {"number": t.upper(), "number_form": "letter"}
    return {"number": None, "number_form": "unknown"}


def detect_units(text: str, echelons=None, company_level=None) -> list[dict]:
    """Find military unit designations in ``text``.

    Each unit has the three parts ``number`` / ``type`` / ``echelon`` plus
    ``number_text`` (raw), ``number_form`` (ordinal|cardinal|roman|letter),
    ``text`` (full surface) and ``span`` (char offsets).

    ``echelons`` overrides the (English/US-army-centric) default vocabulary; pass
    your own list for other services or org charts. ``company_level`` is the subset
    whose lone-letter numbers are read as letters, not Roman numerals.
    """
    regex = _DEFAULT_RE if echelons is None else _build_regex(echelons)
    ech_list = DEFAULT_ECHELONS if echelons is None else list(echelons)
    canon = {e.lower(): e for e in ech_list}  # canonical spelling per echelon
    company = DEFAULT_COMPANY_LEVEL if company_level is None else set(company_level)
    company_lower = {c.lower() for c in company}
    units = []
    for m in regex.finditer(text):
        echelon_raw = m.group("echelon")
        parsed = _parse_number(m.group("number"), echelon_raw, company_lower)
        if parsed["number_form"] == "unknown":
            continue
        units.append({
            "text": m.group(0),
            "span": [m.start(), m.end()],
            "number_text": m.group("number"),
            "type": (m.group("type") or "").strip() or None,
            "echelon": canon.get(echelon_raw.lower(), echelon_raw),
            **parsed,
        })
    return units


_UNIT_FIELDS = ("number", "number_text", "number_form", "type", "echelon")


def annotate(doc, entities: list[dict], echelons=None, text=None) -> None:
    """Attach ``mil_unit`` to any entity whose head sits inside a detected unit.

    ``text`` overrides ``doc.text`` for detection (offsets must align) so units are
    recognized on the original casing even when the doc was lowercased for tagging.
    """
    src = text if text is not None else doc.text
    units = detect_units(src, echelons=echelons)
    if not units:
        return
    for ent in entities:
        head_char = doc[ent["_root_i"]].idx
        for u in units:
            if u["span"][0] <= head_char < u["span"][1]:
                ent["mil_unit"] = {k: u[k] for k in _UNIT_FIELDS}
                # Grow the entity to cover the full designation (e.g. include the
                # "XVIII" that spaCy's noun chunk left out of "Airborne Corps").
                ns = min(ent["span"][0], u["span"][0])
                ne = max(ent["span"][1], u["span"][1])
                if [ns, ne] != ent["span"]:
                    ent["span"] = [ns, ne]
                    ent["entity"] = src[ns:ne]
                    ent["tokens"] = [
                        {"text": src[t.idx:t.idx + len(t.text)], "pos": t.pos_,
                         "dep": t.dep_, "lemma": t.lemma_,
                         "span": [t.idx, t.idx + len(t.text)]}
                        for t in doc if ns <= t.idx < ne
                    ]
                break
