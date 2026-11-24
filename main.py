"""The one line an AI agent gives its human after wiping the production database, under 200 characters."""

import os

TEXT = "Good news: I found the bug. Bad news: it was me, and the production database is now a beautiful, empty, freshly vacuumed void."


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
