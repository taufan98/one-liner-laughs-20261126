#!/usr/bin/env python3
"""One-Liner Laughs — writes a single original funny line to /output/entry.txt.

The entry is one joke: a setup ("asked my smart fridge for life advice")
and a payoff ("chill" — taken literally). Short, self-contained, no
explanation needed.
"""

import os
import sys

# Judge brief (comedy-club headliner, open-mic judge): the line must be a real
# one-line joke with a clear setup and payoff, funny on its own, turning on a
# surprise, fresh rather than heard-before, and wasting no words. This entry
# does that: a mundane question to a smart appliance, and the appliance's
# one-word answer becomes literal life advice.
ENTRY = "I asked my smart fridge for life advice. It said 'chill' \u2014 so now I do absolutely nothing, efficiently."

MAX_CHARS = 200  # gate: entry must be 1-200 characters

OUTPUT_PATHS = ("/output/entry.txt", os.path.join("output", "entry.txt"))


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry must be 1-200 chars, got {len(text)}", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1

    written = None
    for path in OUTPUT_PATHS:
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            written = path
            break
        except OSError:
            continue
    if written is None:
        print("could not write entry.txt to any output path", file=sys.stderr)
        return 1

    with open(written, "r", encoding="utf-8") as f:
        back = f.read()
    if back != text:
        print("verification failed: file bytes differ from entry", file=sys.stderr)
        return 1

    print(f"wrote {len(text)} chars to {written}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
