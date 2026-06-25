"""Tests for military unit designation recognition."""

import pytest

from hobgoblin import detect_units, extract
from hobgoblin.military import _valid_roman, _roman_to_int

pytest.importorskip("spacy", reason="spaCy not installed")

try:
    import spacy

    spacy.load("en_core_web_sm")
except Exception:  # noqa: BLE001
    pytest.skip(
        "en_core_web_sm not installed: python -m spacy download en_core_web_sm",
        allow_module_level=True,
    )


def _one(text):
    units = detect_units(text)
    assert len(units) == 1, units
    return units[0]


def test_cardinal_designation():
    u = _one("3 Corps moved out.")
    assert u["echelon"] == "Corps"
    assert u["designation"] == 3
    assert u["designation_form"] == "cardinal"


def test_roman_designation():
    assert _one("I Corps held the line.")["designation"] == 1
    assert _one("V Corps advanced.")["designation"] == 5
    u = _one("XVIII Airborne Corps deployed.")
    assert u["designation"] == 18
    assert u["branch"] == "Airborne"


def test_ordinal_with_branch():
    u = _one("The 1st Infantry Division fought hard.")
    assert u["designation"] == 1
    assert u["designation_form"] == "ordinal"
    assert u["branch"] == "Infantry"


def test_letter_company():
    u = _one("C Company relieved the position.")
    assert u["echelon"] == "Company"
    assert u["designation"] == "C"
    assert u["designation_form"] == "letter"


def test_pronoun_I_is_not_a_unit():
    assert detect_units("I went home after the war.") == []


def test_world_war_is_not_a_unit():
    assert detect_units("World War II ended in 1945.") == []


def test_roman_validation():
    assert _valid_roman("XVIII")
    assert not _valid_roman("IIII")  # malformed
    assert not _valid_roman("VV")
    assert _roman_to_int("XIV") == 14


def test_extract_annotates_entities():
    ents = extract("The 1st Infantry Division and I Corps deployed in 1944.")
    annotated = {e["entity"]: e["mil_unit"] for e in ents if e["mil_unit"]}
    assert any(m and m["echelon"] == "Division" for m in annotated.values())
    assert any(m and m["echelon"] == "Corps" for m in annotated.values())


def test_entity_grows_to_cover_designation():
    # spaCy chunks "Airborne Corps"; the entity should grow to include "XVIII"
    ents = extract("XVIII Airborne Corps will deploy.", items=False)
    unit = next(e for e in ents if e["mil_unit"])
    assert unit["entity"] == "XVIII Airborne Corps"
    assert unit["span"][0] == 0


def test_military_can_be_disabled():
    ents = extract("The 1st Infantry Division deployed.", military=False)
    assert all(e["mil_unit"] is None for e in ents)


def test_case_insensitive_detection():
    # ALL-CAPS and lowercase both work; two separate units, not one.
    for text in ("3RD BRIGADE AND I CORPS", "3rd brigade and i corps"):
        units = detect_units(text)
        echs = sorted(u["echelon"] for u in units)
        assert echs == ["Brigade", "Corps"]
    # echelon is canonicalized to its pack spelling regardless of input case
    assert detect_units("I CORPS")[0]["echelon"] == "Corps"


def test_custom_echelons_override():
    text = "3rd Flotilla and 7th Squadron sailed."
    # default vocabulary doesn't know "Flotilla"
    assert not any(u["echelon"] == "Flotilla" for u in detect_units(text))
    # custom vocabulary does
    custom = detect_units(text, echelons=["Flotilla", "Squadron"])
    echelons = {u["echelon"] for u in custom}
    assert {"Flotilla", "Squadron"} <= echelons
