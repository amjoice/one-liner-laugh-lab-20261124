#!/usr/bin/env python3
"""One-Liner Laugh Lab: the excuse a robot vacuum gives after eating a sock.

One short funny line, at most 200 characters. The vacuum does not apologise
for hunger — it pleads triage: faced with a sock and the Wi-Fi cable, it
picked the victim that could not fight back. Deadpan, concrete, and the joke
comes from the fit: a machine that treats the house as a menu.

Writes the line to /output/entry.txt, deterministically.
Stdlib only — the grading sandbox is plain python:3.13-slim, no Pillow,
no network.
"""

import os

LINE = "It was either the sock or the Wi-Fi cable, and the sock didn't fight back."

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> str:
    """Return the entry line, enforcing the gate: 1-200 chars, one line.

    Also rejects control characters, which the gate's UTF-8 text rule
    would treat as a broken entry.
    """
    line = text.strip()
    if not line:
        raise ValueError("entry must not be blank")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in line):
        raise ValueError("entry must not contain control characters")
    return line


def write_entry(text: str, path: str) -> None:
    """Write the validated line to path, creating its directory first."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")


def main() -> None:
    write_entry(validate(LINE), OUTPUT_PATH)


if __name__ == "__main__":
    main()
