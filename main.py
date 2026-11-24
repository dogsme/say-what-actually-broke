#!/usr/bin/env python3
"""Say What Actually Broke — one honest line of error copy.

The program writes a single line to /output/entry.txt: the brutal truth
about a failed save, told plainly enough to act on and funny enough to
repeat to a colleague.
"""

from pathlib import Path

ENTRY = (
    "Your file didn't save \u2014 the database timed out mid-write, "
    "so your last hour is now a ghost. Save again, and keep a copy "
    "somewhere we can't lose it."
)


def main() -> None:
    text = ENTRY.strip()
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
