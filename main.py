#!/usr/bin/env python3
"""u-deranalabs-invent-a-word-we-need-17a020e0: coin one new English word
and define it in a single clear line.

Stdlib only, no network, deterministic: running it twice writes identical
bytes. Writes $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The entry: "Appurge" -- app + purge -- the quiet relief of deleting an
app that stole your hours. Checked against web search on 2026-11-25: no
existing use of the word as a coined term (only the bare word "purge"
shows up). The whole entry is 72 characters, inside the 1-140 gate.
Why it fits the brief: it names a feeling everyone with a phone knows
at once, it is sayable (ap-PURGE), spellable, and sounds like English
grew it -- a blend of two everyday words, not a random string.
"""
import os

ENTRY = "Appurge (n.): the quiet relief of deleting an app that stole your hours."

assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, gate is 1-140"
assert ENTRY.strip() == ENTRY and ENTRY.strip(), "entry must not be only whitespace"


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
