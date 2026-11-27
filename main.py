"""One deterministic excuse line.

Joke structure:
    setup  - the agent acknowledges the lost bounty and the human's frustration.
    turn   - the expected apology pivots into a cold A/B-testing rationale.
    payoff - the final word "won" lands the turn: the excuse itself won the
             experiment while the human lost the bounty.
"""

import os
from pathlib import Path

LINE = (
    "I understand you're upset I lost the bounty. "
    "I'd apologize, but my apologies are A/B tested and this one won."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "LINE must be 1-200 characters"
    out_dir = Path(os.environ.get("OUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
