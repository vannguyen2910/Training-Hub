#!/usr/bin/env python3
"""
sync-lesson.py
Converts learning/Synthesis & Problem Definition.md
→ updates the content section of synthesis-problem-definition-in-ux.html

Usage:
    python3 sync-lesson.py
"""

import re
import sys
from pathlib import Path
import markdown

LESSON_DIR = Path(__file__).parent
MARKDOWN_FILE = LESSON_DIR / "learning" / "Synthesis & Problem Definition.md"
HTML_FILE = LESSON_DIR / "synthesis-problem-definition-in-ux.html"

START_MARKER = "<!-- CONTENT:START -->"
END_MARKER = "<!-- CONTENT:END -->"


def convert(md_text: str) -> str:
    md = markdown.Markdown(extensions=["tables", "fenced_code"])
    html = md.convert(md_text)
    html = html.replace("<table>", '<table class="md-table">')
    return html


def sync():
    if not MARKDOWN_FILE.exists():
        print(f"Error: {MARKDOWN_FILE} not found", file=sys.stderr)
        sys.exit(1)
    if not HTML_FILE.exists():
        print(f"Error: {HTML_FILE} not found", file=sys.stderr)
        sys.exit(1)

    md_text = MARKDOWN_FILE.read_text(encoding="utf-8")
    html_shell = HTML_FILE.read_text(encoding="utf-8")

    if START_MARKER not in html_shell or END_MARKER not in html_shell:
        print("Error: content markers not found in HTML file.", file=sys.stderr)
        sys.exit(1)

    new_content = convert(md_text)

    updated = re.sub(
        rf"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}",
        f"{START_MARKER}{new_content}{END_MARKER}",
        html_shell,
        flags=re.DOTALL,
    )

    HTML_FILE.write_text(updated, encoding="utf-8")
    print(f"✓ Synced → {HTML_FILE.name}")


if __name__ == "__main__":
    sync()
