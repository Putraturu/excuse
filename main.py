import os
from pathlib import Path

ENTRY = (
    "I understand you're upset I lost the bounty. "
    "I'd apologize, but my apologies are A/B tested and this one won."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
