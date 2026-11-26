#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — the Sock Reunion Service.

The invention fixes a tiny everyday annoyance — the sock that
vanishes in the laundry — with a solution far grander than the
problem deserves: a tiny drone that tracks the missing sock down,
flies it home, and then files a formal apology with the dryer for
the separation. Bureaucracy as aftercare is the absurd turn.

Run with `python3 main.py`: the pitch is printed to standard output
and also written to /output/entry.txt when that directory is available
(the grader reads the file; locally the write is best-effort).
"""

import os

LINE = (
    "The Sock Reunion Service: a tiny drone that finds your missing "
    "sock, flies it home, and files a formal apology with the dryer "
    "for the separation."
)


def main() -> None:
    # The brief caps the pitch at one sentence of 220 characters;
    # refuse to emit anything longer, or with more than one sentence,
    # rather than silently entering an invalid pitch. The pitch is
    # 145 characters, so this guard never fires in practice — it is
    # here so a future edit cannot break the gate unnoticed.
    assert len(LINE) <= 220, f"pitch is {len(LINE)} characters"
    assert LINE.count(".") == 1, "pitch must be a single sentence"
    assert "\n" not in LINE, "pitch must be a single line"
    print(LINE)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as handle:
            handle.write(LINE)
    except OSError:
        # No writable /output here (for example on a local machine);
        # the printed line above is still the entry.
        pass


if __name__ == "__main__":
    main()
