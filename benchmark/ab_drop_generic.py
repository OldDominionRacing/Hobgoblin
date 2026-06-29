#!/usr/bin/env python3
"""Rigorous same-pages A/B for drop_generic — isolates the filter from sampling noise.

For each page we run ONE wizard.fix() judgment on the FULL (drop_generic=OFF) entity
set and treat its corrections as the oracle:
    drop -> that entity is junk (false positive)
    add  -> a real entity the goblin missed

Then `drop_generic=ON` simply *removes a subset* of the OFF entities. Using the same
oracle for both conditions, every per-page number below is paired — no cross-sample,
no cross-judgment variance:

    ents_off    entities with drop_generic OFF
    junk        OFF entities the oracle marked as drops (false positives)
    adds        real entities the goblin missed (same for both — filter only removes)
    removed     OFF entities drop_generic removed (i.e. OFF minus ON)
    removed_junk   of those removed, how many the oracle agreed were junk  (good removals)
    removed_good   of those removed, how many were real entities  (recall cost)

Totals later give precision/recall for OFF vs ON from the same oracle. One LLM call
per page (the judge), via the Claude Code CLI under your subscription.

    python benchmark/ab_drop_generic.py 100     # default 100 pages, resumable
"""

import json
import os
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from hobgoblin import extract, ANCHORS, wizard  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(HERE, "AB_DROP_GENERIC.md")
LOG = os.path.join(HERE, "ab.log")
TARGET = int(sys.argv[1]) if len(sys.argv) > 1 else 100
BATCH = 20
UA = "Hobgoblin-benchmark/0.1 (github.com/OldDominionRacing/Hobgoblin)"
JUDGE = wizard.claude_code_llm(model="opus")

COLUMNS = ["title", "ents_off", "junk", "adds", "removed", "removed_junk", "removed_good"]
HEADER = f"""# Hobgoblin A/B — drop_generic, same pages, one oracle per page

Paired measurement (no sampling/judgment variance): the wizard judges the full
(OFF) entity set once; `drop_generic` removes a subset. Columns: `ents_off` entities
OFF · `junk` oracle-flagged false positives · `adds` missed entities · `removed`
entities the filter dropped · `removed_junk`/`removed_good` of those, how many were
junk (good removals) vs real (recall cost).

| {" | ".join(COLUMNS)} |
| {" | ".join("---" for _ in COLUMNS)} |
"""


def fetch_batch():
    url = ("https://en.wikipedia.org/w/api.php?action=query&format=json"
           f"&generator=random&grnnamespace=0&grnlimit={BATCH}"
           f"&prop=extracts&explaintext=1&exintro=1&exlimit={BATCH}")
    out = subprocess.run(["curl", "-s", "-H", f"User-Agent: {UA}", url],
                         capture_output=True, text=True, timeout=60)
    return list(json.loads(out.stdout).get("query", {}).get("pages", {}).values())


def existing_state():
    if not os.path.exists(MD):
        return 0, set()
    rows, seen = 0, set()
    for line in open(MD):
        line = line.strip()
        if (line.startswith("| ") and " | " in line
                and not line.startswith("| title") and not line.startswith("| ---")):
            rows += 1
            seen.add(line[2:].split(" | ", 1)[0].strip())
    return rows, seen


def log(msg):
    open(LOG, "a").write(msg + "\n")


def main():
    if not os.path.exists(MD):
        open(MD, "w").write(HEADER)
    done, seen = existing_state()
    log(f"=== start: {done} rows, target {TARGET} ===")
    while done < TARGET:
        try:
            pages = fetch_batch()
        except Exception as exc:  # noqa: BLE001
            log(f"fetch error: {exc!r}")
            time.sleep(5)
            continue
        for p in pages:
            if done >= TARGET:
                break
            title = p.get("title", "")
            text = (p.get("extract") or "").strip()
            if len(text) < 200 or title in seen:
                continue
            try:
                off = extract(text, anchors=ANCHORS, drop_generic=False)
                on = extract(text, anchors=ANCHORS, drop_generic=True)
                corr = wizard.fix(text, entities=off, llm=JUDGE)["corrections"]
            except Exception as exc:  # noqa: BLE001
                log(f"skip {title!r}: {exc!r}")
                time.sleep(2)
                continue
            drop_texts = {(c.get("entity") or "").lower().strip()
                          for c in corr if c.get("action") == "drop"}
            adds = sum(1 for c in corr if c.get("action") == "add")
            on_spans = {tuple(e["span"]) for e in on}
            junk = sum(1 for e in off if e["entity"].lower() in drop_texts)
            removed = [e for e in off if tuple(e["span"]) not in on_spans]
            removed_junk = sum(1 for e in removed if e["entity"].lower() in drop_texts)
            m = {
                "title": title.replace("|", "/").replace("\n", " ").strip(),
                "ents_off": len(off),
                "junk": junk,
                "adds": adds,
                "removed": len(removed),
                "removed_junk": removed_junk,
                "removed_good": len(removed) - removed_junk,
            }
            open(MD, "a").write("| " + " | ".join(str(m[c]) for c in COLUMNS) + " |\n")
            seen.add(title)
            done += 1
            log(f"{done}/{TARGET}: {title!r} removed={m['removed']} "
                f"(junk={m['removed_junk']} good={m['removed_good']})")
        time.sleep(0.5)
    log(f"=== done: {done} rows ===")


if __name__ == "__main__":
    main()
