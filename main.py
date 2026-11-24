#!/usr/bin/env python3
"""Funniest Time Machine Warning Label.

Writes a single one-line warning label for a time machine to
/output/entry.txt. The label is a straight-faced safety notice whose
punchline lands in the last few words: the real hazard is meeting your
own past self, and the joke is that he has had years to stew over
whatever you did — the one warning no traveller ever gets, delivered
in the calm voice of an official notice.
"""

import os

LABEL = (
    "WARNING: Do not approach your past self. "
    "He knows what you did, and he has been waiting years to tell you."
)


def main() -> None:
    text = LABEL.strip()
    assert 1 <= len(text) <= 120, f"label is {len(text)} chars, must be 1-120"
    assert text == text.strip() and text, "label must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
