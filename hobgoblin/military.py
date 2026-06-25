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

# Branch qualifiers that can sit between a designator and its echelon. A fixed
# vocabulary (not "any capitalized word") so the matcher can't run the branch
# group across connectors/echelons, e.g. "3RD BRIGADE AND I CORPS".
_BRANCHES = [
    "Infantry", "Airborne", "Armored", "Armoured", "Cavalry", "Marine",
    "Mountain", "Mechanized", "Motorized", "Artillery", "Aviation", "Engineer",
    "Sustainment", "Ranger", "Naval", "Logistics", "Signal", "Medical",
    "Military", "Air", "Assault", "Field", "Special", "Forces", "Airlift",
    "Bombardment", "Fighter", "Reconnaissance", "Support", "Combat", "Heavy",
    "Light", "Maneuver", "Security", "Police",
]


def _build_regex(echelons):
    # Longest echelons first so multi-word ones win over their substrings.
    # IGNORECASE so ALL-CAPS traffic ("3RD BRIGADE", "I CORPS") still matches.
    alts = "|".join(re.escape(e) for e in sorted(echelons, key=len, reverse=True))
    branch = "|".join(_BRANCHES)
    return re.compile(
        r"\b(?P<desig>\d{1,3}(?:st|nd|rd|th)?|[IVXLCDM]{1,7})\s+"
        r"(?P<branch>(?:(?:" + branch + r")\s+){0,3})"
        r"(?P<echelon>" + alts + r")\b",
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


def _parse_designation(text: str, echelon: str, company_lower) -> dict:
    """Normalise a designator into a value + form, given its echelon."""
    t = text.strip()
    m = re.fullmatch(r"(\d{1,3})(?:st|nd|rd|th)", t, re.IGNORECASE)
    if m:
        return {"designation": int(m.group(1)), "designation_form": "ordinal"}
    if t.isdigit():
        return {"designation": int(t), "designation_form": "cardinal"}
    # Single letter before a company-level echelon -> letter designation.
    if len(t) == 1 and t.isalpha() and echelon.lower() in company_lower:
        return {"designation": t.upper(), "designation_form": "letter"}
    if _valid_roman(t):
        return {"designation": _roman_to_int(t), "designation_form": "roman"}
    if len(t) == 1 and t.isalpha():
        return {"designation": t, "designation_form": "letter"}
    return {"designation": None, "designation_form": "unknown"}


def detect_units(text: str, echelons=None, company_level=None) -> list[dict]:
    """Find military unit designations in ``text``.

    Each unit: ``text``, ``span`` (char), ``echelon``, ``branch`` (or None),
    ``designation`` (normalised int/letter), ``designation_text``, ``designation_form``.

    ``echelons`` overrides the (English/US-army-centric) default vocabulary; pass
    your own list for other services or org charts. ``company_level`` is the subset
    whose lone-letter designators are read as letters, not Roman numerals.
    """
    regex = _DEFAULT_RE if echelons is None else _build_regex(echelons)
    ech_list = DEFAULT_ECHELONS if echelons is None else list(echelons)
    canon = {e.lower(): e for e in ech_list}  # canonical spelling per echelon
    company = DEFAULT_COMPANY_LEVEL if company_level is None else set(company_level)
    company_lower = {c.lower() for c in company}
    units = []
    for m in regex.finditer(text):
        echelon_raw = m.group("echelon")
        parsed = _parse_designation(m.group("desig"), echelon_raw, company_lower)
        if parsed["designation_form"] == "unknown":
            continue
        branch = (m.group("branch") or "").strip() or None
        units.append({
            "text": m.group(0),
            "span": [m.start(), m.end()],
            "echelon": canon.get(echelon_raw.lower(), echelon_raw),
            "branch": branch,
            "designation_text": m.group("desig"),
            **parsed,
        })
    return units


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
                ent["mil_unit"] = {
                    k: u[k] for k in
                    ("echelon", "branch", "designation",
                     "designation_text", "designation_form")
                }
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
