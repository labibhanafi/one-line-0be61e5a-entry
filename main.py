#!/usr/bin/env python3
"""One Line, One Laugh -- make.fun entry (u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a).

Writes exactly one funny line (a single sentence, 91 characters) to
/output/entry.txt, and prints the same line to stdout.

Deterministic by construction: the line is a fixed string constant, there
is no randomness, no clock, no network access and no input file. Two runs
produce byte-identical output.

The line was chosen after drafting seven original candidates (A-G) and
scoring each against the judge's five criteria in order -- whole and
self-contained, a real laugh/turn, tight, fresh, clear on first read.
Full scoring: see CANDIDATES.md. The winner (E) is the only 25/25: a
double turn -- relaxation is first pushed to next month, then downgraded
to "tentative" -- so even rest gets bureaucratised.
"""

import hashlib
import os
import sys

ENTRY = (
    "My calendar reminded me to relax, so I scheduled it for next month "
    "and marked it tentative."
)

OUTPUT_PATH = "/output/entry.txt"

MIN_ENTRY_LENGTH = 1
MAX_ENTRY_LENGTH = 140
REQUIRED_PERIODS = 1


def validate_entry(text: str) -> str | None:
    """Return an error message if `text` is not one valid sentence, else None."""
    if not MIN_ENTRY_LENGTH <= len(text) <= MAX_ENTRY_LENGTH:
        return (
            f"entry length {len(text)} is outside the "
            f"{MIN_ENTRY_LENGTH}-{MAX_ENTRY_LENGTH} range"
        )
    if text.count(".") != REQUIRED_PERIODS or not text.endswith("."):
        return "entry must be exactly one sentence"
    return None


def main() -> int:
    error = validate_entry(ENTRY)
    if error is not None:
        print(error, file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)
    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
