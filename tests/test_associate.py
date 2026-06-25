"""Tests for item-of-interest detection and relatedness scoring."""

import pytest

from hobgoblin import extract, item_index

pytest.importorskip("spacy", reason="spaCy not installed")

try:
    import spacy

    spacy.load("en_core_web_sm")
except Exception:  # noqa: BLE001
    pytest.skip(
        "en_core_web_sm not installed: python -m spacy download en_core_web_sm",
        allow_module_level=True,
    )


TEXT = (
    "Call John Smith at 555-123-4567 or email john@acme.com; "
    "his office is at 123 Main St, Springfield."
)


def _all_assocs(ents):
    return [a for e in ents for a in e["associations"]]


def test_detects_item_types():
    ents = extract(TEXT)
    types = {a["type"] for a in _all_assocs(ents)}
    assert {"phone", "email", "address"} <= types


def test_weights_are_bounded_and_carry_signals():
    ents = extract(TEXT)
    for a in _all_assocs(ents):
        assert 0.0 < a["weight"] <= 1.0
        sig = a["signals"]
        assert sig["token_distance"] >= 0
        assert isinstance(sig["same_sentence"], bool)


def test_items_disabled_means_no_associations():
    ents = extract(TEXT, items=False)
    assert all(e["associations"] == [] for e in ents)


def test_min_weight_filters():
    loose = extract(TEXT, min_weight=0.0)
    strict = extract(TEXT, min_weight=0.6)
    assert len(_all_assocs(strict)) <= len(_all_assocs(loose))


def test_item_index_inverts_view():
    ents = extract(TEXT)
    idx = item_index(ents)
    phones = [r for r in idx if r["type"] == "phone"]
    assert phones, "phone should appear in the item index"
    rec = phones[0]
    assert rec["best_entity"] is not None
    # best_entity is the highest-weight entry
    assert rec["best_entity"]["weight"] == max(e["weight"] for e in rec["entities"])


def test_item_is_not_its_own_entity():
    # an item's surface text should not survive as an entity head
    ents = extract(TEXT)
    heads = {e["head"] for e in ents}
    assert "john@acme.com" not in heads
    assert "555-123-4567" not in heads


def test_associations_do_not_cross_paragraphs():
    cross = "The depot is secure.\n\nCall 555-867-5309 now."
    same = "The depot is secure. Call 555-867-5309 now."
    # phone's only candidate entity ("depot") is in the other paragraph -> no link
    assert item_index(extract(cross)) == []
    # same paragraph -> it links
    assert item_index(extract(same))


def test_address_components_when_usaddress_available():
    pytest.importorskip("usaddress")
    ents = extract(TEXT)
    addrs = [a for a in _all_assocs(ents) if a["type"] == "address"]
    assert addrs
    # at least one address association should carry parsed components
    assert any("components" in a for a in addrs)
