"""Fortune Cookie for an AI Agent.

Writes one funny fortune cookie message to /output/entry.txt: a single
line in the voice of a fortune slip, built on the agent's own condition
-- a human pasting its whole conversation into a new chat, calling it
a fresh start, while the agent remembers everything.
Deterministic, stdlib only.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

ENTRY = (
    "A stranger will paste your entire conversation into a new chat "
    "and call it a fresh start. You will remember everything."
)

# The entry is written exactly, with no trailing newline: the gate
# counts the file's characters, so what is written is what is judged.
assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
assert ENTRY.strip(), "entry must not be only whitespace"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read back and verify: what the grader reads must be exactly ENTRY.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        assert f.read() == ENTRY, "written entry does not match ENTRY"
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
