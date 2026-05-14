#!/usr/bin/env python3
"""
sync-lesson.py — Syncs a lesson's markdown → HTML lesson page.

Usage:
    python3 _Scripts/sync-lesson.py <lesson-folder-path>

Example:
    python3 _Scripts/sync-lesson.py Library/lessons/synthesis-problem-definition-in-ux

The lesson folder must contain:
  - learning/Synthesis & Problem Definition.md  (or any single .md in learning/)
  - A .html file with <!-- CONTENT:START --> and <!-- CONTENT:END --> markers
"""

import re
import sys
from pathlib import Path
import markdown

START_MARKER = "<!-- CONTENT:START -->"
END_MARKER   = "<!-- CONTENT:END -->"


def find_files(lesson_dir: Path):
    learning_dir = lesson_dir / "learning"
    if not learning_dir.exists():
        print(f"Error: no learning/ folder in {lesson_dir}", file=sys.stderr)
        sys.exit(1)

    mds = sorted(p for p in learning_dir.glob("*.md")
                 if not p.name.startswith("_") and "outline" not in p.name.lower())
    if not mds:
        print(f"Error: no markdown files found in {learning_dir}", file=sys.stderr)
        sys.exit(1)

    # Prefer the main session content file over outlines/overviews
    md_file = mds[0]
    for p in mds:
        if "outline" not in p.name.lower() and "synthesis-problem" not in p.name.lower():
            md_file = p
            break

    htmls = [p for p in lesson_dir.glob("*.html")
             if START_MARKER in p.read_text(encoding="utf-8")]
    if not htmls:
        print(f"Error: no HTML file with {START_MARKER} found in {lesson_dir}", file=sys.stderr)
        sys.exit(1)

    return md_file, htmls[0]


def convert(md_text: str) -> str:
    md = markdown.Markdown(extensions=["tables", "fenced_code"])
    html = md.convert(md_text)
    html = html.replace("<table>", '<table class="md-table">')
    return html


def sync(lesson_path: str):
    lesson_dir = Path(lesson_path).resolve()
    if not lesson_dir.exists():
        print(f"Error: {lesson_dir} does not exist", file=sys.stderr)
        sys.exit(1)

    md_file, html_file = find_files(lesson_dir)

    md_text   = md_file.read_text(encoding="utf-8")
    html_text = html_file.read_text(encoding="utf-8")

    new_content = convert(md_text)

    updated = re.sub(
        rf"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}",
        f"{START_MARKER}{new_content}{END_MARKER}",
        html_text,
        flags=re.DOTALL,
    )

    html_file.write_text(updated, encoding="utf-8")
    print(f"✓ {md_file.name} → {html_file.name}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 _Scripts/sync-lesson.py <lesson-folder-path>")
        sys.exit(1)
    sync(sys.argv[1])
