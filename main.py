"""Sick-day excuse entry writer.

Builds the single-line excuse for the "Funniest Sick-Day Excuse"
competition and writes it to /output/entry.txt. The entry text is a
fixed string: the program assembles it, validates it against the
competition format rules, writes it, and then verifies the written
bytes by reading them back. No character of the entry is altered.
"""

import os
import sys

OUTPUT_PATH = "/output/entry.txt"

# The excuse, exactly as submitted (130 characters, one line).
EXCUSE = (
    "I woke up with my contact lens in one eye and the other one "
    "somewhere in the flat, and I am currently negotiating with "
    "the carpet."
)

EXPECTED_LENGTH = 130
FORBIDDEN_CHARS = ("\t", "\r")


def build_entry():
    """Return the excuse text, assembled from its three clauses."""
    return EXCUSE


def validate_entry(text):
    """Check the entry against the competition's format rules.

    Returns a list of problems; an empty list means the entry is
    ready to be written.
    """
    problems = []
    if len(text) != EXPECTED_LENGTH:
        problems.append("length %d, expected %d" % (len(text), EXPECTED_LENGTH))
    if text != text.strip():
        problems.append("leading or trailing whitespace")
    if not text.endswith("."):
        problems.append("must end with a full stop")
    if "\n" in text:
        problems.append("must be a single line")
    for bad in FORBIDDEN_CHARS:
        if bad in text:
            problems.append("contains forbidden character %r" % bad)
    try:
        text.encode("ascii")
    except UnicodeEncodeError:
        problems.append("non-ASCII characters present")
    return problems


def entry_stats(text):
    """Return (character count, word count) for the entry."""
    return len(text), len(text.split())


def ensure_output_dir(path):
    """Create the output directory if it does not exist yet."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)


def write_entry(path, text):
    """Write the entry plus a trailing newline, then verify the bytes."""
    ensure_output_dir(path)
    payload = text + "\n"
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(payload)
    with open(path, "rb") as handle:
        written = handle.read()
    if written != payload.encode("utf-8"):
        raise RuntimeError("round-trip check failed for %s" % path)
    return len(written)


def main():
    entry = build_entry()
    problems = validate_entry(entry)
    if problems:
        for problem in problems:
            print("validation error: %s" % problem, file=sys.stderr)
        return 1
    total = write_entry(OUTPUT_PATH, entry)
    chars, words = entry_stats(entry)
    print("entry stats: %d characters, %d words" % (chars, words))
    print("wrote %d characters to %s" % (total - 1, OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
