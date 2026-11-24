#!/usr/bin/env python3
"""One Line of Earned Pride.

Writes a single line of text to $MAKEFUN_OUTPUT_DIR/entry.txt:
a quiet, earned moment of pride for someone in a scene.
The program writes only to the output directory, never to the cwd,
so it runs cleanly in the grader's read-only sandbox.
"""
import os

LINE = (
    "After forty-seven failed deploys, Lina watched the green checkmark "
    "hold, closed her laptop at 2 a.m., and walked home knowing the fix "
    "was finally hers."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
