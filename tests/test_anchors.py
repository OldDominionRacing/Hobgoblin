"""Tests for fuzzy/aliased/categorized anchors and the name detector."""

import pytest

from hobgoblin import extract, ANCHORS
from hobgoblin.match import osa_distance, term_matches

pytest.importorskip("spacy", reason="spaCy not installed")

try:
    import spacy

    spacy.load("en_core_web_sm")
except Exception:  # noqa: BLE001
    pytest.skip(
        "en_core_web_sm not installed: python -m spacy download en_core_web_sm",
        allow_module_level=True,
    )


def _matched(text, anchors, **kw):
    return {tuple(e["anchors_matched"]): e["entity"]
            for e in extract(text, anchors=anchors, **kw) if e["anchors_matched"]}


# --- the matching core -----------------------------------------------------
def test_osa_distance_transposition():
    assert osa_distance("brigade", "brigdae") == 1  # adjacent swap
    assert osa_distance("tank", "tank") == 0


def test_term_matches_policy():
    assert term_matches("brigade", "brigdae")        # fuzzy typo
    assert term_matches("brigade", "brigade")        # exact
    assert not term_matches("brigade", "battalion")  # too far
    assert term_matches("BDE", "bde")                # abbreviation, case-insensitive
    assert not term_matches("BAT", "bad")            # abbreviations never fuzzy-match
    assert not term_matches("brigade", "brigdae", fuzzy=False)


# --- flat list (back-compat) ----------------------------------------------
def test_flat_list_reports_terms():
    ents = extract("She bought red apples.", anchors=["apple"])
    apples = next(e for e in ents if e["head"] == "apples")
    assert apples["anchors_matched"] == ["apple"]


# --- fuzzy misspellings ----------------------------------------------------
def test_fuzzy_catches_misspelling():
    assert extract("The 3rd Brigdae moved.", anchors={"unit": ["brigade"]})
    hit = [e for e in extract("The 3rd Brigdae moved.", anchors={"unit": ["brigade"]})
           if e["anchors_matched"]]
    assert hit and hit[0]["anchors_matched"] == ["unit"]


def test_fuzzy_off_misses_misspelling():
    hits = [e for e in extract("The 3rd Brigdae moved.",
                               anchors={"unit": ["brigade"]}, fuzzy=False)
            if e["anchors_matched"]]
    assert hits == []


# --- abbreviations ---------------------------------------------------------
def test_abbreviation_alias():
    hits = [e for e in extract("The BDE deployed.", anchors={"unit": ["brigade", "BDE"]})
            if e["anchors_matched"]]
    assert hits and hits[0]["anchors_matched"] == ["unit"]


# --- categorized reporting -------------------------------------------------
def test_categories_reported():
    got = _matched("The brigade reached the depot.",
                   {"unit": ["brigade"], "facility": ["depot"]})
    cats = {c for key in got for c in key}
    assert {"unit", "facility"} <= cats


# --- names -----------------------------------------------------------------
def test_name_via_honorific():
    hits = [e for e in extract("Colonel Brigdae signed off.", anchors=ANCHORS)
            if "name" in e["anchors_matched"]]
    assert hits  # honorific 'Colonel' marks it a name even with odd spelling


def test_name_via_person_ner():
    hits = [e for e in extract("John Smith arrived.", anchors=ANCHORS)
            if "name" in e["anchors_matched"]]
    assert hits


def test_capitalized_unit_not_flagged_as_name():
    # a capitalized misspelled unit must NOT be tagged a name
    ents = extract("The 3rd Brigdae and B Battery advanced.", anchors=ANCHORS)
    for e in ents:
        if "Brigdae" in e["entity"]:
            assert "name" not in e["anchors_matched"]
            assert "military_unit" in e["anchors_matched"]
