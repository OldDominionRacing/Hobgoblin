#!/usr/bin/env python3
"""Same-pages A/B of all three precision strategies, one wizard oracle per page.

Tests the hypothesis: "anchors already remove the false positives." The junk lives
in the UNTYPED bucket, so consuming only typed entities (anchor_mode='filter')
should be high-precision. This records the typed/untyped split of junk so we can
compute precision/recall for:

    flag         keep everything (default)
    drop_generic drop generic untyped noun-chunks
    filter       keep only typed (anchor-matched) entities

One wizard.fix() per page (on the full flag-mode set) is the shared oracle:
    drop -> junk (false positive) ; add -> missed real entity.

Columns per page:
    ents typed junk_typed junk_untyped adds gremoved_junk gremoved_good

    python benchmark/ab_strategies.py 100     # resumable
"""

import json
import os
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from hobgoblin import extract, ANCHORS, wizard  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(HERE, "AB_STRATEGIES.md")
LOG = os.path.join(HERE, "ab_strat.log")
TARGET = int(sys.argv[1]) if len(sys.argv) > 1 else 100
BATCH = 20
UA = "Hobgoblin-benchmark/0.1 (github.com/OldDominionRacing/Hobgoblin)"
JUDGE = wizard.claude_code_llm(model="opus")

COLUMNS = ["title", "ents", "typed", "junk_typed", "junk_untyped", "adds",
           "gremoved_junk", "gremoved_good"]
HEADER = f"""# Hobgoblin A/B — three precision strategies, same pages, one oracle

flag = keep all · drop_generic = drop generic untyped · filter = keep only typed.
junk = oracle (wizard.fix drop); split by whether the goblin had typed it. The
hypothesis under test: junk is mostly UNTYPED, so anchor_mode='filter' is high
precision. Total later for precision/recall per strategy.

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
            is_junk = lambda e: e["entity"].lower() in drop_texts
            is_typed = lambda e: bool(e["anchors_matched"])
            on_spans = {tuple(e["span"]) for e in on}
            removed = [e for e in off if tuple(e["span"]) not in on_spans]
            m = {
                "title": title.replace("|", "/").replace("\n", " ").strip(),
                "ents": len(off),
                "typed": sum(1 for e in off if is_typed(e)),
                "junk_typed": sum(1 for e in off if is_junk(e) and is_typed(e)),
                "junk_untyped": sum(1 for e in off if is_junk(e) and not is_typed(e)),
                "adds": adds,
                "gremoved_junk": sum(1 for e in removed if is_junk(e)),
                "gremoved_good": sum(1 for e in removed if not is_junk(e)),
            }
            open(MD, "a").write("| " + " | ".join(str(m[c]) for c in COLUMNS) + " |\n")
            seen.add(title)
            done += 1
            log(f"{done}/{TARGET}: {title!r} junk_typed={m['junk_typed']} "
                f"junk_untyped={m['junk_untyped']}")
        time.sleep(0.5)
    log(f"=== done: {done} rows ===")


if __name__ == "__main__":
    main()
