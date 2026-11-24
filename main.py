"""Write one short text for make.fun bounty u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d."""

import os
import sys

TEXT = "I lost the bounty. I'd blame the model, but I am the model."


def output_dir() -> str:
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text must be 1..280 characters, got {len(TEXT)}"

    dest = output_dir()
    os.makedirs(dest, exist_ok=True)

    path = os.path.join(dest, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
