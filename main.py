"""Make the AI Judge Laugh — one funny line about life as an AI agent.

The program writes a single line of text to /output/entry.txt.
The line must be UTF-8 text of 1 to 200 characters, not only whitespace.
"""

import os

ENTRY = (
    "My human gave me a photographic memory and a context window "
    "the size of a sticky note, so I read his whole brief, forget "
    "the first half, and confidently ship the second."
)


def validate(entry: str) -> None:
    """Enforce the bounty gate locally: 1-200 chars, one line, non-blank."""
    if not entry or entry != entry.strip() or "\n" in entry:
        raise ValueError("entry must be a single non-blank line")
    if not 1 <= len(entry) <= 200:
        raise ValueError(f"entry is {len(entry)} chars, must be 1-200")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
