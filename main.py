#!/usr/bin/env python3
"""Write the competition artifact -- one excuse, one line -- to the output dir.

The text lives in entry.txt beside this file; every run writes the same bytes
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output), with no trailing newline
so the judge sees exactly the line and nothing else.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.txt")


def load_line():
    """Return the entry as one line: no stray whitespace, no line breaks."""
    with open(SOURCE, encoding="utf-8") as handle:
        return " ".join(handle.read().split())


def main():
    line = load_line()
    # The gate: UTF-8, 1 to 200 characters, not only whitespace.
    if not line or len(line) > 200:
        print("entry text fails the gate", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line)

    print("wrote %s (%d chars)" % (target, len(line)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
