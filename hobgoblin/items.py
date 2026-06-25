"""Detect "items of interest" — phone, email, URL, money, address.

Everything here is deterministic: regex + spaCy token alignment, plus optional
``usaddress`` (a CRF tagger) to validate/parse street addresses. Each item is
returned with char span, token span, and a representative root token index so
the relatedness scorer can measure distance to entities.
"""

from __future__ import annotations

import re

try:  # optional, declared dependency; degrade gracefully if absent
    import usaddress
except Exception:  # noqa: BLE001  # pragma: no cover
    usaddress = None

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
URL_RE = re.compile(r"\b(?:https?://|www\.)[^\s,;]+", re.IGNORECASE)
PHONE_RE = re.compile(
    r"(?<!\d)(?:\+?1[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}(?!\d)"
)
MONEY_RE = re.compile(r"\$\s?\d[\d,]*(?:\.\d+)?")
_STREET_SUFFIX = (
    r"Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Lane|Ln|Drive|Dr|Court|Ct|"
    r"Way|Place|Pl|Terrace|Ter|Circle|Cir|Highway|Hwy|Parkway|Pkwy"
)
ADDRESS_RE = re.compile(
    r"\b\d{1,6}\s+(?:[A-Z][A-Za-z]*\.?\s+){1,4}(?:" + _STREET_SUFFIX + r")\b\.?"
    r"(?:,?\s+[A-Z][A-Za-z]+)*"  # optional city
    r"(?:,?\s+[A-Z]{2})?"  # optional state
    r"(?:\s+\d{5}(?:-\d{4})?)?",  # optional ZIP
)

# (label, compiled-regex) in priority order — earlier wins on overlap.
_PATTERNS = [
    ("email", EMAIL_RE),
    ("url", URL_RE),
    ("address", ADDRESS_RE),
    ("phone", PHONE_RE),
    ("money", MONEY_RE),
]


def _parse_address(text: str):
    """Return usaddress components dict, or None if it doesn't look like one."""
    if usaddress is None:
        return None
    try:
        tagged, _kind = usaddress.tag(text)
    except Exception:  # noqa: BLE001 - RepeatedLabelError etc.
        return None
    # Require at least a street number + a street name component.
    if "AddressNumber" in tagged and any(
        k.startswith("StreetName") for k in tagged
    ):
        return dict(tagged)
    return None


def detect(doc) -> list[dict]:
    """Find items of interest in a spaCy ``doc``.

    Returns a list of dicts: ``type``, ``text``, ``span`` (char), ``tok_start``,
    ``tok_end``, ``root_i`` (token index of the item's syntactic head), and for
    addresses an optional ``components`` dict from usaddress.
    """
    text = doc.text
    items: list[dict] = []
    claimed: list[tuple[int, int]] = []  # char ranges already taken

    for label, pattern in _PATTERNS:
        for m in pattern.finditer(text):
            cs, ce = m.start(), m.end()
            if any(cs < oe and os < ce for os, oe in claimed):
                continue  # overlaps a higher-priority item

            span = doc.char_span(cs, ce, alignment_mode="expand")
            if span is None:
                continue

            item = {
                "type": label,
                "text": text[cs:ce],
                "span": [cs, ce],
                "tok_start": span.start,
                "tok_end": span.end,
                "root_i": span.root.i,
            }
            if label == "address":
                comps = _parse_address(text[cs:ce])
                if comps is None and usaddress is not None:
                    # usaddress is available and rejected it -> probably not an address
                    continue
                if comps is not None:
                    item["components"] = comps

            items.append(item)
            claimed.append((cs, ce))

    items.sort(key=lambda it: it["span"][0])
    return items
