"""Anchor matching — the user's terms of interest, matched against entities.

Anchors come in two shapes:

- **flat list** ``["brigade", "tank"]`` — ``anchors_matched`` reports matched terms.
- **categorized dict** ``{"military_unit": ["brigade", "BDE"], "name": NAME}`` —
  ``anchors_matched`` reports matched *category* labels, turning the POS finder into
  a typed extractor. Category keys are arbitrary; namespace them by domain
  (``military_unit``, ``medical_facility``, …) so packs can be mixed.

Each term matches an entity token **exactly or fuzzily** (see ``match.py``):
case-insensitive, with edit-distance tolerance for typos ("brigdae" -> brigade) but
exact-only for abbreviations ("BDE", "BAT") so they don't collide with real words.

The special ``NAME`` sentinel makes a category match by *rule* instead of a word
list: an entity whose head is a person name (spaCy PERSON, or a Title-case proper
noun that isn't a place/org). Names have too many spellings to enumerate.
"""

from __future__ import annotations

from typing import Iterable, Union

from .match import term_matches

# Sentinels: a category can match by *rule* instead of a word list.
NAME = "@name"    # person names (spaCy PERSON, or an honorific in the chunk)
PLACE = "@place"  # countries/states/cities (spaCy GPE/LOC)

# Honorifics are a strong, deterministic person-name cue (without relying on a name
# list). Title-case alone is too ambiguous — it flags places and capitalized units.
_HONORIFICS = {
    "mr", "mrs", "ms", "miss", "dr", "prof", "sir", "madam", "madame",
    "col", "colonel", "gen", "general", "sgt", "sergeant", "capt", "captain",
    "lt", "lieutenant", "maj", "major", "pvt", "private", "cpl", "corporal",
    "cmdr", "commander", "adm", "admiral", "pfc", "spc", "specialist", "cpt",
}
_PLACE_ENTS = {"GPE", "LOC"}

AnchorSpec = Union[Iterable[str], dict]


def _looks_like_name(ent: dict) -> bool:
    if ent.get("head_ent") == "PERSON":
        return True
    return any(
        t["text"].lower().rstrip(".") in _HONORIFICS for t in ent.get("tokens", [])
    )


def _looks_like_place(ent: dict) -> bool:
    return ent.get("head_ent") in _PLACE_ENTS


def _term_hits(term: str, texts: list[str], lemmas: list[str], fuzzy: bool) -> bool:
    """Match a (possibly multi-word) term against an entity's token sequence.

    Single-word terms match any token (text or lemma); multi-word terms ("World War",
    "machine gun") match a contiguous run of tokens in order.
    """
    words = term.split()
    if len(words) <= 1:
        return (any(term_matches(term, t, fuzzy) for t in texts)
                or any(term_matches(term, l, fuzzy) for l in lemmas))
    n = len(words)
    for i in range(len(texts) - n + 1):
        if all(term_matches(words[k], texts[i + k], fuzzy) for k in range(n)):
            return True
    return False


# Rule sentinels -> predicate. A category may include any of these alongside terms.
_RULES = {NAME: _looks_like_name, PLACE: _looks_like_place}


def _normalize(anchors: AnchorSpec):
    """Return (groups, report_labels) where groups = [(label, terms, rules)]."""
    if isinstance(anchors, dict):
        groups = []
        for label, variants in anchors.items():
            if isinstance(variants, str):
                variants = [variants]
            vs = list(variants)
            rules = [r for r in vs if r in _RULES]
            terms = [v for v in vs if v not in _RULES]
            groups.append((label, terms, rules))
        return groups, True
    # flat list: each term is its own label (a sentinel becomes a rule-only group)
    groups = [(t, [], [t]) if t in _RULES else (t, [t], []) for t in anchors]
    return groups, False


def apply_anchors(
    entities: list[dict],
    anchors: AnchorSpec,
    *,
    fuzzy: bool = True,
    mode: str = "flag",
    model: str | None = None,  # accepted for back-compat; unused
) -> list[dict]:
    """Tag (and optionally filter) ``entities`` by ``anchors``.

    Sets ``anchors_matched`` on each entity to the matched terms (flat list) or
    category labels (dict). With ``mode="filter"``, only matched entities return.
    """
    if mode not in ("flag", "filter"):
        raise ValueError(f"mode must be 'flag' or 'filter', got {mode!r}")

    groups, _ = _normalize(anchors)

    for ent in entities:
        toks = ent.get("tokens", [])
        texts = [t["text"] for t in toks]
        lemmas = [t.get("lemma", t["text"]) for t in toks]

        matched = []
        for label, terms, rules in groups:
            hit = any(_term_hits(v, texts, lemmas, fuzzy) for v in terms)
            if not hit:
                hit = any(_RULES[r](ent) for r in rules)
            if hit:
                matched.append(label)
        ent["anchors_matched"] = sorted(set(matched))

    if mode == "filter":
        return [e for e in entities if e["anchors_matched"]]
    return entities
