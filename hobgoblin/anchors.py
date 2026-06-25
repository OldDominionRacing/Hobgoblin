"""Anchor matching — the user's terms of interest, matched against entities.

Anchors come in two shapes:

- **flat list** ``["brigade", "tank"]`` — ``anchors_matched`` reports matched terms.
- **categorized dict** ``{"unit": ["brigade", "BDE"], "name": NAME}`` —
  ``anchors_matched`` reports matched *category* labels, turning the POS finder into
  a typed extractor.

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

NAME = "@name"  # sentinel: use the deterministic name detector for this category

# Honorifics are a strong, deterministic person-name cue (without relying on a name
# list). Title-case alone is too ambiguous — it flags places and capitalized units.
_HONORIFICS = {
    "mr", "mrs", "ms", "miss", "dr", "prof", "sir", "madam", "madame",
    "col", "colonel", "gen", "general", "sgt", "sergeant", "capt", "captain",
    "lt", "lieutenant", "maj", "major", "pvt", "private", "cpl", "corporal",
    "cmdr", "commander", "adm", "admiral", "pfc", "spc", "specialist", "cpt",
}

AnchorSpec = Union[Iterable[str], dict]


def _normalize(anchors: AnchorSpec):
    """Return (groups, report_labels) where groups = [(label, variants, use_name)]."""
    if isinstance(anchors, dict):
        groups = []
        for label, variants in anchors.items():
            if isinstance(variants, str):
                if variants == NAME:
                    groups.append((label, [], True))
                    continue
                variants = [variants]
            vs = list(variants)
            use_name = NAME in vs
            groups.append((label, [v for v in vs if v != NAME], use_name))
        return groups, True
    # flat list: each term is its own label
    groups = [(t, [], True) if t == NAME else (t, [t], False) for t in anchors]
    return groups, False


def _looks_like_name(ent: dict) -> bool:
    if ent.get("head_ent") == "PERSON":
        return True
    return any(
        t["text"].lower().rstrip(".") in _HONORIFICS for t in ent.get("tokens", [])
    )


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
        tokens = set()
        for t in ent.get("tokens", []):
            tokens.add(t["text"])
            tokens.add(t.get("lemma", t["text"]))

        matched = []
        for label, variants, use_name in groups:
            hit = any(
                term_matches(v, tok, fuzzy) for v in variants for tok in tokens
            )
            if not hit and use_name and _looks_like_name(ent):
                hit = True
            if hit:
                matched.append(label)
        ent["anchors_matched"] = sorted(set(matched))

    if mode == "filter":
        return [e for e in entities if e["anchors_matched"]]
    return entities
