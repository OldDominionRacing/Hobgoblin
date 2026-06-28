"""Tests for the expanded item-type detection and its validators."""

import pytest

from hobgoblin import detect_items
from hobgoblin.items import _luhn_ok, _ipv4_ok

pytest.importorskip("spacy", reason="spaCy not installed")

try:
    import spacy

    _NLP = spacy.load("en_core_web_sm")
except Exception:  # noqa: BLE001
    pytest.skip(
        "en_core_web_sm not installed: python -m spacy download en_core_web_sm",
        allow_module_level=True,
    )


def _types(text):
    return {(it["type"], it["text"]) for it in detect_items(_NLP(text))}


def test_luhn_validator():
    assert _luhn_ok("4111 1111 1111 1111")  # valid test number
    assert not _luhn_ok("4111 1111 1111 1112")
    assert not _luhn_ok("1234")  # too short


def test_ipv4_validator():
    assert _ipv4_ok("192.168.1.1")
    assert not _ipv4_ok("999.1.1.1")
    assert not _ipv4_ok("1.2.3")


def test_numeric_and_temporal_types():
    found = _types("Wire 25% on 03/14/2025 at 4:30 PM.")
    labels = {t for t, _ in found}
    assert {"percent", "date", "time"} <= labels


def test_sensitive_id_types():
    found = _types("Card 4111 1111 1111 1111 SSN 123-45-6789.")
    labels = {t for t, _ in found}
    assert "credit_card" in labels
    assert "ssn" in labels


def test_bad_card_rejected_by_luhn():
    found = _types("Card 4111 1111 1111 1112 here.")
    assert not any(t == "credit_card" for t, _ in found)


def test_network_types():
    found = _types(
        "host 192.168.1.1 mac 00:1A:2B:3C:4D:5E "
        "uuid 550e8400-e29b-41d4-a716-446655440000"
    )
    labels = {t for t, _ in found}
    assert {"ipv4", "mac", "uuid"} <= labels


def test_social_and_geo_types():
    found = _types("Follow @acme_co and #launch; pin 37.7749, -122.4194.")
    labels = {t for t, _ in found}
    assert {"handle", "hashtag", "coordinate"} <= labels


def test_measurement_and_direction_elements():
    found = _types("Sianów lies 9 mi east of Koszalin, 23 km north-east.")
    labels = {t for t, _ in found}
    assert "measurement" in labels   # 9 mi / 23 km
    assert "direction" in labels     # east / north-east


def test_measurement_demoted_from_entities():
    from hobgoblin import extract, item_index, ANCHORS
    ents = extract("The course measured 9 km today.", anchors=ANCHORS)
    assert "9 km" not in {e["entity"] for e in ents}          # demoted to an element
    assert any(i["type"] == "measurement" for i in item_index(ents))


def test_anchor_elevates_demoted_element():
    from hobgoblin import extract, ANCHORS
    anc = dict(ANCHORS, distance=["km"])
    ents = extract("The course measured 9 km today.", anchors=anc)
    elevated = [e for e in ents if "distance" in e["anchors_matched"]]
    assert elevated and elevated[0]["entity"] == "9 km"       # anchor brings it back


def test_invalid_ip_not_detected():
    found = _types("bad ip 999.1.1.1 here")
    assert not any(t == "ipv4" for t, _ in found)
