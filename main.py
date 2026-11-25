#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note.

Writes one line of patch notes announcing that human sleep has been
fixed to /output/entry.txt. The line must be a single line of 1-160
characters, UTF-8, and read like a real changelog entry.
"""

import os

ENTRY = "Fixed: human sleep now autosaves overnight \u2014 dreams resume where you left off, and waking up tired has been moved to the backlog."
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 160, f"entry must be 1-160 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
