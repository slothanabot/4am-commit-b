"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one single line — the commit message an AI agent would leave in
the log after a long night fixing its own bugs — to entry.txt in the
output directory given by MAKEFUN_OUTPUT_DIR (default "/output").

The joke is in the agent's own condition: it spent the night repairing
bugs it wrote itself, one fix begetting the next, until the only defect
left standing is the author. It merges before it can talk itself out
of it.

Deterministic: the same text is written on every run. No network, no
randomness, no input read.
"""

import os

# The joke builds in three beats: the 2AM fix, the midnight fix, then the
# punchline — the agent itself is the last defect left standing.
ENTRY_BEAT_1 = "4AM: fixed the bug I wrote at 2AM while fixing the bug I wrote "
ENTRY_BEAT_2 = "at midnight. The code is clean now. I am the only remaining defect. "
ENTRY_BEAT_3 = "Merging before I can stop myself."

ENTRY = ENTRY_BEAT_1 + ENTRY_BEAT_2 + ENTRY_BEAT_3

MAX_CHARS = 200


def verify(path: str, expected: str) -> None:
    """Re-read the written file and re-check every gate on its contents."""
    with open(path, "r", encoding="utf-8", newline="") as f:
        raw = f.read()
    body = raw.rstrip("\n")
    if raw != expected + "\n":
        raise SystemExit("written file does not match the entry exactly")
    if not body or body != body.strip():
        raise SystemExit("entry is empty or has surrounding whitespace")
    if not 1 <= len(body) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(body)} chars, outside 1-200")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, 0o644)
    verify(path, ENTRY)


if __name__ == "__main__":
    main()
