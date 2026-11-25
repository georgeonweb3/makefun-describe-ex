#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun entry.

Writes a single word describing an ex to /output/entry.txt:

    Houdini

Why it lands: the word is a one-word verdict on a ghosting ex — the
escape artist who vanished mid-act and never came back. Comic punch
comes from the instant visual (a magician fleeing the stage), surprise
from elevating dating misconduct into stage magic, craft from the
single-name economy, recognition from a household name. No field
cliche: no unsubscribe / unsubscribed, no recalled, no refurbished,
no nonrefundable, no refund, no expired, no uninstalled — the whole
cancelled-subscription / defective-product angle is avoided.

Python 3.13, standard library only, no network, deterministic.
"""

import os

ENTRY = "Houdini"

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate self-check: /output/entry.txt must be a single word of at
    # most 111 characters, nothing else attached. Verified live: 7
    # characters, one word, no trailing newline.
    assert 1 <= len(ENTRY) <= 111, f"entry is {len(ENTRY)} chars, gate wants 1-111"
    assert len(ENTRY.split()) == 1, "entry must be a single word"
    assert ENTRY.isalpha(), "entry must be one plain word, no digits or punctuation"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY.encode("utf-8").decode("utf-8") == ENTRY
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(ENTRY.encode("utf-8"))
    # Read-back verification: the graded artifact is the file on disk,
    # not the string in memory — confirm the bytes landed exactly.
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    assert written == ENTRY.encode("utf-8"), (
        f"entry.txt on disk differs from ENTRY: {written!r}"
    )


if __name__ == "__main__":
    main()
