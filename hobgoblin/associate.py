"""Relatedness scoring between items of interest and entities.

Fully deterministic. Blends linear token distance with dependency-path distance
(we already pay for the parse), bounded by sentence membership, and penalised
when another entity sits between the item and this one.

    proximity_lin = exp(-token_distance / LAMBDA_T)
    proximity_dep = exp(-dep_distance / LAMBDA_D)        # same sentence only
    same sentence:  weight = A*proximity_lin + B*proximity_dep
    cross sentence: weight = CROSS * proximity_lin
    intervening entity (linearly between, closer): weight *= PENALTY
"""

from __future__ import annotations

import math

LAMBDA_T = 5.0
LAMBDA_D = 2.0
A_LIN = 0.4
B_DEP = 0.6
CROSS = 0.3
PENALTY = 0.5


def _token_distance(a: tuple[int, int], b: tuple[int, int]) -> int:
    """Gap in tokens between two half-open token spans (0 if touching/overlap)."""
    a0, a1 = a
    b0, b1 = b
    if a1 <= b0:
        return b0 - a1
    if b1 <= a0:
        return a0 - b1
    return 0


def _dep_distance(doc, i: int, j: int):
    """Shortest undirected parse-tree path length between tokens i and j.

    Returns None if they're in different sentences / parse trees.
    """
    if i == j:
        return 0
    ti, tj = doc[i], doc[j]
    if ti.sent.start != tj.sent.start:
        return None

    chain_i = [ti, *ti.ancestors]
    depth_j = {tok.i: d for d, tok in enumerate([tj, *tj.ancestors])}
    for d_i, tok in enumerate(chain_i):
        if tok.i in depth_j:  # lowest common ancestor
            return d_i + depth_j[tok.i]
    return None


def relatedness(doc, entity: dict, item: dict, entity_spans: list[list[int]]):
    """Return ``(weight, signals)`` for one (entity, item) pair."""
    ent_tok = (entity["_tok_start"], entity["_tok_end"])
    item_tok = (item["tok_start"], item["tok_end"])

    td = _token_distance(ent_tok, item_tok)
    same_sent = doc[entity["_root_i"]].sent.start == doc[item["root_i"]].sent.start
    dp = _dep_distance(doc, entity["_root_i"], item["root_i"]) if same_sent else None

    prox_lin = math.exp(-td / LAMBDA_T)
    if same_sent and dp is not None:
        prox_dep = math.exp(-dp / LAMBDA_D)
        weight = A_LIN * prox_lin + B_DEP * prox_dep
    else:
        weight = CROSS * prox_lin

    # intervening-entity penalty: another entity sits linearly between them.
    e_s, e_e = entity["span"]
    i_s, i_e = item["span"]
    lo, hi = (e_e, i_s) if e_e <= i_s else (i_e, e_s)
    for os, oe in entity_spans:
        if [os, oe] == entity["span"]:
            continue
        if lo <= os and oe <= hi:
            weight *= PENALTY
            break

    weight = max(0.0, min(1.0, weight))
    signals = {
        "token_distance": td,
        "dep_distance": dp,
        "same_sentence": same_sent,
    }
    return weight, signals


def item_index(entities: list[dict]) -> list[dict]:
    """Invert per-entity associations into an item-centric view.

    Each record: ``type``, ``text``, ``span``, a weight-ranked ``entities`` list,
    and ``best_entity`` (highest weight).
    """
    by_span: dict[tuple, dict] = {}
    order: list[tuple] = []
    for ent in entities:
        for a in ent.get("associations", []):
            key = (a["type"], tuple(a["span"]))
            rec = by_span.get(key)
            if rec is None:
                rec = {"type": a["type"], "text": a["text"], "span": a["span"],
                       "entities": []}
                by_span[key] = rec
                order.append(key)
            rec["entities"].append(
                {"head": ent["head"], "span": ent["span"], "weight": a["weight"]}
            )

    index = []
    for key in order:
        rec = by_span[key]
        rec["entities"].sort(key=lambda x: -x["weight"])
        rec["best_entity"] = rec["entities"][0] if rec["entities"] else None
        index.append(rec)
    return index
