"""Funniest Autocorrect Fail entry.

Writes a single autocorrect-fail line to the output file expected by the
make.fun program/v1 harness. Standard library only.
"""

import os

ENTRY_TEXT = (
    "Hi boss, just confirming our anal review is still on for Friday at 9 "
    "- I've prepared all the documents!"
)


def resolve_output_path():
    """Pick the output path, never from the bare working directory."""
    explicit = os.environ.get("ENTRY_OUTPUT")
    if explicit:
        return explicit
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def main():
    path = resolve_output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
