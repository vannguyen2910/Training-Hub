#!/usr/bin/env python3
"""
build.py — Knowledge Library Static Generator
Winnie Nguyen · UX Mentoring Hub

Run from inside 01_Library/:
    python3 build.py

What it does:
  1. Reads library-data.js to get all material metadata
  2. For each material with a bundle folder, reads index.md and learnings.md
  3. Generates a self-contained index.html detail page in that bundle folder
  4. Updates library-data.js to add a `page` field pointing to the HTML file

index.md sections rendered as visual blocks:
  ## Key Concepts      → concept cards grid
  ## Session Structure → phase timeline (parsed from markdown table)
  ## Tools & Materials → checklist
  ## Practice Activities → activity cards

script.md is rendered as a "Teaching Script" tab inside Learnings.
"""

import os
import re
import json
import calendar
import html as html_lib
from pathlib import Path

# ─────────────────────────────────────────────────────────────────────────────
# PATHS
# ─────────────────────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent
LIBRARY_DATA_PATH = SCRIPT_DIR / "library-data.js"

TYPE_DIRS = {
    "lesson":    "lessons",
    "framework": "frameworks",
    "slides":    "slides",
    "guide":     "guides",
}

# ─────────────────────────────────────────────────────────────────────────────
# PARSE library-data.js
# ─────────────────────────────────────────────────────────────────────────────

def parse_library_data():
    text = LIBRARY_DATA_PATH.read_text(encoding="utf-8")
    m = re.search(r'window\.LIBRARY_DATA\s*=\s*(\[.*\])\s*;', text, re.DOTALL)
    if not m:
        raise ValueError("Could not find LIBRARY_DATA array in library-data.js")
    array_text = m.group(1)
    array_text = re.sub(r'//[^\n]*', '', array_text)
    array_text = re.sub(r'([{,]\s*)([a-zA-Z_]\w*)\s*:', r'\1"\2":', array_text)
    array_text = re.sub(r',\s*([}\]])', r'\1', array_text)
    return json.loads(array_text)


def write_library_data(materials):
    original = LIBRARY_DATA_PATH.read_text(encoding="utf-8")
    lines = ["window.LIBRARY_DATA = [\n\n"]
    for i, m in enumerate(materials):
        lines.append("  {\n")
        lines.append(f'    id: {m["id"]},\n')
        lines.append(f'    type: "{m["type"]}",\n')
        lines.append(f'    program: "{m["program"]}",\n')
        lines.append(f'    title: "{m["title"]}",\n')
        lines.append(f'    description: "{m["description"]}",\n')
        lines.append(f'    audience: "{m["audience"]}",\n')
        lines.append(f'    duration: "{m["duration"]}",\n')
        tags_js = "[" + ", ".join(f'"{t}"' for t in m["tags"]) + "]"
        lines.append(f'    tags: {tags_js},\n')
        obj_js = "[\n" + "".join(f'      "{o}",\n' for o in m["objectives"]) + "    ]"
        lines.append(f'    objectives: {obj_js},\n')
        pre_js = "[" + ", ".join(f'"{p}"' for p in m["prerequisites"]) + "]"
        lines.append(f'    prerequisites: {pre_js},\n')
        lines.append(f'    date: "{m["date"]}",\n')
        lines.append(f'    file: "{m.get("file", "")}",\n')
        if m.get("page"):
            lines.append(f'    page: "{m["page"]}",\n')
        if m.get("crossRef"):
            cr_parts = ", ".join(
                '{ id: ' + str(cr["id"]) + ', rel: "' + cr["rel"] + '" }'
                for cr in m["crossRef"]
            )
            lines.append(f'    crossRef: [{cr_parts}]\n')
        else:
            lines.append('    crossRef: []\n')
        comma = "," if i < len(materials) - 1 else ""
        lines.append(f"  }}{comma}\n\n")
    lines.append("];\n")
    new_text = "".join(lines)
    header_match = re.match(r'(//.*?═+\n.*?═+\n)', original, re.DOTALL)
    if header_match:
        new_text = header_match.group(1) + "\n" + new_text
    LIBRARY_DATA_PATH.write_text(new_text, encoding="utf-8")


# ─────────────────────────────────────────────────────────────────────────────
# INLINE MARKDOWN (shared)
# ─────────────────────────────────────────────────────────────────────────────

def inline(s):
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'__(.+?)__', r'<strong>\1</strong>', s)
    s = re.sub(r'\*(.+?)\*', r'<em>\1</em>', s)
    s = re.sub(r'_(.+?)_', r'<em>\1</em>', s)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank">\1</a>', s)
    return s


# ─────────────────────────────────────────────────────────────────────────────
# FULL MARKDOWN RENDERER (for script.md and learnings.md)
# ─────────────────────────────────────────────────────────────────────────────

def render_markdown(text):
    if not text:
        return ""
    lines = text.split("\n")
    html_lines = []
    in_ul = False
    in_ol = False
    in_code = False
    in_table = False
    table_rows = []
    code_buf = []

    def close_list():
        nonlocal in_ul, in_ol
        if in_ul:
            html_lines.append("</ul>")
            in_ul = False
        if in_ol:
            html_lines.append("</ol>")
            in_ol = False

    def close_table():
        nonlocal in_table, table_rows
        if in_table and table_rows:
            html_lines.append('<table class="md-table">')
            for ri, row in enumerate(table_rows):
                if ri == 1 and all(re.match(r'^[-:]+$', c.strip()) for c in row if c.strip()):
                    continue
                tag = "th" if ri == 0 else "td"
                html_lines.append("<tr>" + "".join(f"<{tag}>{c.strip()}</{tag}>" for c in row) + "</tr>")
            html_lines.append("</table>")
            in_table = False
            table_rows = []

    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            if in_code:
                lang = ""
                html_lines.append(f'<pre><code>' + "\n".join(code_buf) + '</code></pre>')
                code_buf = []
                in_code = False
            else:
                close_list()
                close_table()
                in_code = True
            i += 1
            continue
        if in_code:
            code_buf.append(line)
            i += 1
            continue
        if "|" in line and line.strip().startswith("|"):
            close_list()
            in_table = True
            cells = [c for c in line.split("|")[1:-1]]
            table_rows.append([inline(c) for c in cells])
            i += 1
            continue
        else:
            if in_table:
                close_table()
        if re.match(r'^---+$', line.strip()):
            close_list()
            html_lines.append('<hr>')
            i += 1
            continue
        hm = re.match(r'^(#{1,6})\s+(.+)', line)
        if hm:
            close_list()
            level = len(hm.group(1))
            html_lines.append(f'<h{level}>{inline(hm.group(2))}</h{level}>')
            i += 1
            continue
        if line.startswith("> "):
            close_list()
            html_lines.append(f'<blockquote>{inline(line[2:])}</blockquote>')
            i += 1
            continue
        ul_m = re.match(r'^(\s*)[-*+]\s+(.+)', line)
        if ul_m:
            close_table()
            if not in_ul:
                close_list()
                html_lines.append('<ul>')
                in_ul = True
            html_lines.append(f'<li>{inline(ul_m.group(2))}</li>')
            i += 1
            continue
        ol_m = re.match(r'^\d+\.\s+(.+)', line)
        if ol_m:
            close_table()
            if not in_ol:
                close_list()
                html_lines.append('<ol>')
                in_ol = True
            html_lines.append(f'<li>{inline(ol_m.group(1))}</li>')
            i += 1
            continue
        if line.strip() == "":
            close_list()
            close_table()
            html_lines.append("")
            i += 1
            continue
        close_list()
        close_table()
        html_lines.append(f'<p>{inline(line)}</p>')
        i += 1

    close_list()
    close_table()
    return "\n".join(html_lines)


# ─────────────────────────────────────────────────────────────────────────────
# OVERVIEW SECTION PARSERS (index.md → visual blocks)
# ─────────────────────────────────────────────────────────────────────────────

def parse_overview_sections(text):
    """Split index.md into named sections by ## headings."""
    sections = {}
    current = None
    buf = []
    for line in text.split("\n"):
        h2 = re.match(r'^##\s+(.+)', line)
        if h2:
            if current is not None:
                sections[current] = "\n".join(buf).strip()
            current = h2.group(1).strip()
            buf = []
        elif current is not None:
            buf.append(line)
    if current is not None:
        sections[current] = "\n".join(buf).strip()
    return sections


def render_key_concepts(text):
    """## Key Concepts → grid of concept cards."""
    blocks = re.split(r'(?=^###\s)', text, flags=re.MULTILINE)
    cards = ""
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        m = re.match(r'^###\s+(.+?)\n([\s\S]*)', block)
        if m:
            name = m.group(1).strip()
            body = m.group(2).strip()
            cards += f'''<div class="concept-card">
              <div class="concept-name">{inline(name)}</div>
              <p class="concept-body">{inline(body)}</p>
            </div>'''
    return f'<div class="concept-grid">{cards}</div>' if cards else ""


# Phase type → CSS class
PHASE_TYPE_CLASS = {
    "warm-up":          "type-warmup",
    "concept":          "type-concept",
    "explain + demo":   "type-explain",
    "activity":         "type-activity",
    "bridge":           "type-bridge",
    "explain + practice": "type-explain",
    "wrap-up":          "type-wrapup",
    "discussion":       "type-discussion",
}


def render_session_structure(text):
    """## Session Structure markdown table → visual phase timeline."""
    rows = []
    for line in text.strip().split("\n"):
        if "|" not in line:
            continue
        cells = [c.strip() for c in line.split("|") if c.strip()]
        if not cells:
            continue
        # Skip separator row
        if all(re.match(r'^[-:]+$', c) for c in cells):
            continue
        # Skip header row
        if cells[0].lower() == "time":
            continue
        rows.append(cells)

    blocks = ""
    for row in rows:
        if len(row) < 4:
            continue
        time, segment, type_str, duration = row[0], row[1], row[2], row[3]
        cls = PHASE_TYPE_CLASS.get(type_str.lower(), "type-other")
        blocks += f'''<div class="phase-block">
          <div class="phase-time">{time}</div>
          <div class="phase-content">
            <div class="phase-name">{segment}</div>
            <div class="phase-meta">
              <span class="phase-type {cls}">{type_str}</span>
              <span class="phase-duration">{duration}</span>
            </div>
          </div>
        </div>'''
    return f'<div class="phase-timeline">{blocks}</div>' if blocks else ""


def render_tools(text):
    """## Tools & Materials list → visual checklist."""
    items = ""
    for line in text.strip().split("\n"):
        m = re.match(r'^[-*+]\s+(.+)', line)
        if m:
            items += f'<li><span class="check-icon">✓</span><span>{inline(m.group(1))}</span></li>'
    return f'<ul class="tools-list">{items}</ul>' if items else ""


def render_activities(text):
    """## Practice Activities H3 blocks → activity cards."""
    blocks = re.split(r'(?=^###\s)', text, flags=re.MULTILINE)
    cards = ""
    count = 0
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        m = re.match(r'^###\s+(.+?)\n([\s\S]*)', block)
        if m:
            count += 1
            name = m.group(1).strip()
            body = m.group(2).strip()
            cards += f'''<div class="activity-card">
              <div class="activity-label">Activity {count}</div>
              <div class="activity-name">{inline(name)}</div>
              <p class="activity-body">{inline(body)}</p>
            </div>'''
    return f'<div class="activity-cards">{cards}</div>' if cards else ""


def render_overview(index_md_text):
    """
    Render index.md as a series of visual sections.
    Falls back to raw markdown render if no recognised sections found.
    """
    # Strip top-level title and frontmatter lines
    text = re.sub(r'^#\s+.+\n', '', index_md_text, count=1)
    text = re.sub(r'^\*\*(?:Type|Duration|Audience|Methods covered|Methods|Tags):\*\*.*\n', '',
                  text, flags=re.MULTILINE)
    text = re.sub(r'^---\n', '', text, count=1)

    sections = parse_overview_sections(text.strip())

    if not sections:
        return f'<div class="md-body">{render_markdown(text)}</div>'

    SECTION_RENDERERS = {
        "Key Concepts":       render_key_concepts,
        "Session Structure":  render_session_structure,
        "Tools & Materials":  render_tools,
        "Practice Activities": render_activities,
    }

    SECTION_ICONS = {
        "Key Concepts":        "💡",
        "Session Structure":   "🗺️",
        "Tools & Materials":   "🛠",
        "Practice Activities": "✏️",
    }

    html = ""
    for section_name, content in sections.items():
        if not content.strip():
            continue
        renderer = SECTION_RENDERERS.get(section_name)
        icon = SECTION_ICONS.get(section_name, "")
        rendered = renderer(content) if renderer else f'<div class="md-body">{render_markdown(content)}</div>'
        html += f'''<section class="overview-section">
          <h2 class="section-title">{icon} {section_name}</h2>
          {rendered}
        </section>'''

    return html


# ─────────────────────────────────────────────────────────────────────────────
# LEARNINGS PARSER
# ─────────────────────────────────────────────────────────────────────────────

MONTH_ORDER = {m: i for i, m in enumerate(calendar.month_abbr) if m}
MONTH_ORDER.update({m: i for i, m in enumerate(calendar.month_name) if m})


def parse_month_year(header):
    m = re.search(r'(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|'
                  r'Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|'
                  r'Dec(?:ember)?)\s+(\d{4})', header, re.I)
    if m:
        mon = m.group(1).capitalize()[:3]
        year = int(m.group(2))
        return (year, MONTH_ORDER.get(mon, 0))
    return (0, 0)


def parse_learnings(text):
    if not text:
        return {}
    sections = {}
    current = None
    buf = []
    for line in text.split("\n"):
        h2 = re.match(r'^##\s+(.+)', line)
        if h2:
            if current and buf:
                sections[current] = "\n".join(buf).strip()
            current = h2.group(1).strip()
            buf = []
        else:
            if current:
                buf.append(line)
    if current and buf:
        sections[current] = "\n".join(buf).strip()

    if sections.get("Teaching Notes"):
        notes_text = sections["Teaching Notes"]
        note_blocks = re.split(r'(?=^###\s)', notes_text, flags=re.MULTILINE)
        note_blocks = [b.strip() for b in note_blocks if b.strip()]

        def note_sort_key(block):
            m = re.match(r'^###\s+(.+)', block)
            if m:
                return parse_month_year(m.group(1))
            return (0, 0)

        note_blocks.sort(key=note_sort_key, reverse=True)
        sections["Teaching Notes"] = "\n\n".join(note_blocks)

    return sections


# ─────────────────────────────────────────────────────────────────────────────
# RELATED & CROSSREF HELPERS
# ─────────────────────────────────────────────────────────────────────────────

REL_LABELS = {
    "requires":  "Prerequisite",
    "uses":      "Uses",
    "extends":   "Goes deeper",
    "companion": "Pair with",
}

REL_CLASSES = {
    "requires":  "rel-requires",
    "uses":      "rel-uses",
    "extends":   "rel-extends",
    "companion": "rel-companion",
}

TYPE_LABELS = {
    "lesson":    "Lesson",
    "framework": "Framework",
    "slides":    "Slides",
    "guide":     "Guide",
}

PROGRAM_LABELS = {
    "ux-class": "UX Class",
    "private":  "Private",
    "both":     "Both",
}


def find_by_id(mid, all_materials):
    return next((m for m in all_materials if m["id"] == mid), None)


def find_related(material, all_materials, limit=4):
    my_tags = set(material.get("tags", []))
    xref_ids = {cr["id"] for cr in material.get("crossRef", [])}
    scored = []
    for m in all_materials:
        if m["id"] == material["id"] or m["id"] in xref_ids:
            continue
        shared = len(my_tags & set(m.get("tags", [])))
        if shared:
            scored.append((shared, m))
    scored.sort(key=lambda x: -x[0])
    return [m for _, m in scored[:limit]]


def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text.strip())
    text = re.sub(r'-+', '-', text)
    text = re.sub(r'-(in|for|of|the|a|an|and|or|to|with)$', '', text)
    return text


def mat_link_from_root(m, library_root="../../"):
    page = m.get("page")
    if page:
        return library_root + page
    return library_root + "index.html" + f"?open={m['id']}"


# ─────────────────────────────────────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────────────────────────────────────

def get_css():
    return """
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --accent: #3B5B8C;
      --accent-light: #EEF2F8;
      --bg: #F9F7F4;
      --surface: #FFFFFF;
      --text: #1A1A1A;
      --muted: #6B7280;
      --border: #E5E0D8;
      --font-serif: 'DM Serif Display', Georgia, serif;
      --font-sans: 'Instrument Sans', system-ui, sans-serif;
      --radius: 10px;
      --shadow: 0 1px 3px rgba(0,0,0,.07), 0 4px 16px rgba(0,0,0,.05);
    }

    body {
      font-family: var(--font-sans);
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
      min-height: 100vh;
    }

    /* ── NAV ── */
    .nav {
      position: sticky; top: 0; z-index: 100;
      background: rgba(249,247,244,.95);
      backdrop-filter: blur(8px);
      border-bottom: 1px solid var(--border);
      padding: 0 2rem;
      display: flex; align-items: center; gap: 1.5rem;
      height: 56px;
    }
    .nav-back {
      display: flex; align-items: center; gap: .5rem;
      color: var(--accent); text-decoration: none;
      font-size: .875rem; font-weight: 500; flex-shrink: 0;
    }
    .nav-back:hover { opacity: .75; }
    .nav-back svg { width: 16px; height: 16px; }
    .nav-title {
      font-family: var(--font-serif);
      font-size: 1rem; color: var(--text);
      flex: 1;
      white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
    }
    .nav-type-badge {
      font-size: .7rem; font-weight: 600; letter-spacing: .06em; text-transform: uppercase;
      padding: .25rem .6rem; border-radius: 99px;
      background: var(--accent-light); color: var(--accent); flex-shrink: 0;
    }

    /* ── HERO ── */
    .hero {
      background: var(--accent);
      color: white;
      padding: 3rem 2rem 2.5rem;
    }
    .hero-inner { max-width: 1100px; margin: 0 auto; }
    .hero-meta {
      display: flex; align-items: center; gap: .75rem;
      margin-bottom: 1rem; flex-wrap: wrap;
    }
    .badge {
      font-size: .7rem; font-weight: 600; letter-spacing: .06em; text-transform: uppercase;
      padding: .25rem .65rem; border-radius: 99px;
    }
    .badge-type     { background: rgba(255,255,255,.15); color: white; }
    .badge-program  { background: rgba(255,255,255,.1);  color: rgba(255,255,255,.85); }
    .badge-audience { background: rgba(255,255,255,.1);  color: rgba(255,255,255,.85); }
    .hero h1 {
      font-family: var(--font-serif);
      font-size: clamp(1.75rem, 4vw, 2.5rem);
      line-height: 1.2; margin-bottom: .75rem;
    }
    .hero-desc {
      font-size: 1.05rem; opacity: .85;
      max-width: 620px; margin-bottom: 1.5rem; line-height: 1.6;
    }
    .hero-stats {
      display: flex; gap: 0; flex-wrap: wrap;
      border-top: 1px solid rgba(255,255,255,.2);
      padding-top: 1.25rem; margin-top: .25rem;
    }
    .hero-stat {
      font-size: .8rem; opacity: .75;
      padding-right: 2rem; margin-right: 2rem;
      border-right: 1px solid rgba(255,255,255,.2);
    }
    .hero-stat:last-child { border-right: none; padding-right: 0; margin-right: 0; }
    .hero-stat strong { opacity: 1; display: block; font-size: 1rem; margin-bottom: .1rem; }

    /* ── LAYOUT ── */
    .layout {
      max-width: 1100px; margin: 0 auto;
      padding: 3rem 2rem 4rem;
      display: grid;
      grid-template-columns: 1fr 308px;
      gap: 3.5rem;
      align-items: start;
    }
    /* Critical: prevents grid children from overflowing their columns */
    .content, .sidebar { min-width: 0; }
    @media (max-width: 800px) { .layout { grid-template-columns: 1fr; } }

    /* ── CONTENT SECTIONS ── */
    .overview-section { margin-bottom: 3rem; }
    .overview-section:last-child { margin-bottom: 0; }
    .section-title {
      font-family: var(--font-serif);
      font-size: 1.25rem; color: var(--text);
      margin-bottom: 1.25rem;
      padding-bottom: .6rem;
      border-bottom: 2px solid var(--border);
    }

    /* ── OBJECTIVES ── */
    .objectives-list { list-style: none; display: flex; flex-direction: column; gap: .5rem; }
    .objectives-list li { display: flex; gap: .75rem; align-items: flex-start; font-size: .95rem; }
    .obj-num {
      flex-shrink: 0; width: 22px; height: 22px;
      background: var(--accent); color: white;
      border-radius: 50%; font-size: .72rem; font-weight: 700;
      display: flex; align-items: center; justify-content: center;
      margin-top: 2px;
    }

    /* ── TAGS ── */
    .tag-row { display: flex; flex-wrap: wrap; gap: .4rem; }
    .tag {
      font-size: .75rem; font-weight: 500;
      padding: .2rem .6rem; border-radius: 99px;
      background: var(--accent-light); color: var(--accent);
    }

    /* ── CONCEPT CARDS ── */
    .concept-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1rem;
    }
    @media (max-width: 500px) { .concept-grid { grid-template-columns: 1fr; } }
    .concept-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.1rem 1.25rem;
      box-shadow: var(--shadow);
    }
    .concept-name {
      font-family: var(--font-serif);
      font-size: 1rem; color: var(--accent);
      margin-bottom: .4rem;
    }
    .concept-body { font-size: .875rem; color: #374151; line-height: 1.55; }

    /* ── PHASE TIMELINE ── */
    .phase-timeline { display: flex; flex-direction: column; gap: .5rem; }
    .phase-block {
      display: flex; align-items: center; gap: 1rem;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: .75rem 1rem;
    }
    .phase-time {
      font-size: .75rem; font-weight: 700; font-family: monospace;
      color: var(--muted); flex-shrink: 0; width: 42px;
    }
    .phase-content { flex: 1; display: flex; align-items: center; gap: .75rem; flex-wrap: wrap; }
    .phase-name { font-size: .9rem; font-weight: 600; flex: 1; min-width: 120px; }
    .phase-meta { display: flex; align-items: center; gap: .5rem; flex-shrink: 0; }
    .phase-type {
      font-size: .68rem; font-weight: 700; letter-spacing: .04em; text-transform: uppercase;
      padding: .2rem .55rem; border-radius: 4px;
    }
    .type-warmup     { background: #FEF3C7; color: #92400E; }
    .type-concept    { background: #DBEAFE; color: #1E40AF; }
    .type-explain    { background: #EDE9FE; color: #4C1D95; }
    .type-activity   { background: #D1FAE5; color: #065F46; }
    .type-bridge     { background: #F3F4F6; color: #4B5563; }
    .type-wrapup     { background: #DBEAFE; color: #1E40AF; }
    .type-discussion { background: #F3F4F6; color: #4B5563; }
    .type-other      { background: #F3F4F6; color: #4B5563; }
    .phase-duration  { font-size: .78rem; color: var(--muted); white-space: nowrap; }

    /* ── TOOLS CHECKLIST ── */
    .tools-list { list-style: none; display: flex; flex-direction: column; gap: .5rem; }
    .tools-list li { display: flex; align-items: flex-start; gap: .65rem; font-size: .9rem; }
    .check-icon {
      flex-shrink: 0; width: 20px; height: 20px;
      background: var(--accent-light); color: var(--accent);
      border-radius: 50%; font-size: .7rem; font-weight: 700;
      display: flex; align-items: center; justify-content: center;
      margin-top: 1px;
    }

    /* ── ACTIVITY CARDS ── */
    .activity-cards { display: flex; flex-direction: column; gap: .875rem; }
    .activity-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-left: 4px solid var(--accent);
      border-radius: 0 var(--radius) var(--radius) 0;
      padding: 1rem 1.25rem;
    }
    .activity-label {
      font-size: .7rem; font-weight: 700; letter-spacing: .06em; text-transform: uppercase;
      color: var(--accent); margin-bottom: .25rem;
    }
    .activity-name { font-size: .95rem; font-weight: 700; margin-bottom: .4rem; }
    .activity-body { font-size: .875rem; color: #374151; line-height: 1.55; }

    /* ── MARKDOWN BODY (script + learnings) ── */
    .md-body h1, .md-body h2 {
      font-family: var(--font-serif);
      margin: 1.75rem 0 .6rem; line-height: 1.25;
    }
    .md-body h1 { font-size: 1.5rem; }
    .md-body h2 { font-size: 1.2rem; color: var(--accent); }
    .md-body h3 { font-size: 1rem; font-weight: 700; margin: 1.25rem 0 .4rem; color: #1f2937; }
    .md-body h4 { font-size: .9rem; font-weight: 700; margin: 1rem 0 .3rem; }
    .md-body p  { margin: .5rem 0; font-size: .95rem; }
    .md-body ul, .md-body ol { margin: .5rem 0 .5rem 1.4rem; }
    .md-body li { margin: .25rem 0; font-size: .95rem; }
    .md-body blockquote {
      border-left: 3px solid var(--accent);
      margin: 1rem 0; padding: .5rem 1rem;
      background: var(--accent-light);
      border-radius: 0 6px 6px 0;
      font-style: italic; color: #374151;
    }
    .md-body code {
      background: #F3F4F6; border-radius: 4px;
      padding: .1rem .35rem; font-size: .85em;
      font-family: 'Fira Code', monospace;
    }
    .md-body pre {
      background: #1E293B; color: #E2E8F0;
      border-radius: 8px; padding: 1rem 1.25rem;
      overflow-x: auto; margin: 1rem 0;
    }
    .md-body pre code { background: none; color: inherit; padding: 0; font-size: .85rem; }
    .md-body hr { border: none; border-top: 1px solid var(--border); margin: 1.5rem 0; }
    .md-body a  { color: var(--accent); }
    .md-body .md-table { width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: .875rem; }
    .md-body .md-table th, .md-body .md-table td {
      border: 1px solid var(--border); padding: .5rem .75rem; text-align: left;
    }
    .md-body .md-table th { background: var(--accent-light); font-weight: 600; }
    .md-body .md-table tr:nth-child(even) { background: #FAFAF9; }

    /* ── LEARNINGS TABS ── */
    .learnings-tabs { display: flex; gap: .25rem; margin-bottom: 1.25rem; flex-wrap: wrap; }
    .tab-btn {
      font-family: var(--font-sans);
      font-size: .8rem; font-weight: 600;
      padding: .35rem .85rem;
      border: 1.5px solid var(--border);
      border-radius: 99px;
      background: transparent; color: var(--muted);
      cursor: pointer; transition: all .15s;
    }
    .tab-btn:hover { border-color: var(--accent); color: var(--accent); }
    .tab-btn.active { background: var(--accent); border-color: var(--accent); color: white; }
    .tab-panel { display: none; }
    .tab-panel.active { display: block; }

    /* ── SIDEBAR ── */
    .sidebar {
      display: flex; flex-direction: column; gap: 1.25rem;
      position: sticky; top: 72px;
      max-height: calc(100vh - 88px);
      overflow-y: auto;
    }
    .sidebar-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.25rem;
      box-shadow: var(--shadow);
    }
    .sidebar-card h3 {
      font-size: .75rem; font-weight: 700;
      text-transform: uppercase; letter-spacing: .08em;
      color: var(--muted); margin-bottom: .875rem;
    }
    .prereq-list { list-style: none; display: flex; flex-direction: column; gap: .4rem; }
    .prereq-list li { font-size: .875rem; display: flex; gap: .5rem; align-items: flex-start; }
    .prereq-list li::before { content: "→"; color: var(--accent); flex-shrink: 0; }

    /* CrossRef */
    .crossref-card {
      display: flex; align-items: flex-start; gap: .75rem;
      padding: .65rem .75rem;
      border-radius: 7px; margin-bottom: .5rem;
      text-decoration: none; color: var(--text);
      border: 1px solid var(--border); transition: box-shadow .15s;
    }
    .crossref-card:hover { box-shadow: 0 2px 8px rgba(0,0,0,.08); }
    .crossref-card:last-child { margin-bottom: 0; }
    .rel-badge {
      font-size: .65rem; font-weight: 700; letter-spacing: .05em; text-transform: uppercase;
      padding: .15rem .45rem; border-radius: 4px; white-space: nowrap; flex-shrink: 0;
      margin-top: 2px;
    }
    .rel-requires  .rel-badge { background: #FEF3C7; color: #92400E; }
    .rel-uses      .rel-badge { background: #DBEAFE; color: #1E40AF; }
    .rel-extends   .rel-badge { background: #D1FAE5; color: #065F46; }
    .rel-companion .rel-badge { background: #EDE9FE; color: #4C1D95; }
    .crossref-title { font-size: .85rem; font-weight: 500; line-height: 1.3; }
    .crossref-type  { font-size: .75rem; color: var(--muted); margin-top: .1rem; }

    /* Related */
    .related-card {
      display: block; padding: .65rem .75rem;
      border: 1px solid var(--border); border-radius: 7px;
      margin-bottom: .5rem; text-decoration: none; color: var(--text);
      transition: box-shadow .15s;
    }
    .related-card:hover { box-shadow: 0 2px 8px rgba(0,0,0,.08); }
    .related-card:last-child { margin-bottom: 0; }
    .related-title { font-size: .85rem; font-weight: 500; }
    .related-meta  { font-size: .75rem; color: var(--muted); margin-top: .1rem; }

    /* ── SLIDE DECK CARD ── */
    .slide-deck-card {
      background: linear-gradient(135deg, #EEF2F8 0%, #E4EBF5 100%);
      border-color: var(--accent-light);
    }
    .slide-deck-link {
      display: flex; align-items: center; gap: .6rem;
      padding: .65rem .75rem;
      background: white;
      border: 1px solid var(--border);
      border-radius: 7px;
      text-decoration: none; color: var(--text);
      margin-top: .5rem;
      transition: box-shadow .15s, transform .15s;
    }
    .slide-deck-link:hover {
      box-shadow: 0 3px 12px rgba(59,91,140,.15);
      transform: translateY(-1px);
    }
    .slide-icon {
      font-size: .7rem; color: white;
      background: var(--accent); border-radius: 50%;
      width: 22px; height: 22px; flex-shrink: 0;
      display: flex; align-items: center; justify-content: center;
    }
    .slide-deck-name {
      font-size: .83rem; font-weight: 500; flex: 1; line-height: 1.3;
    }
    .slide-open-label {
      font-size: .75rem; color: var(--accent);
      font-weight: 600; white-space: nowrap; flex-shrink: 0;
    }

    /* ── FOOTER ── */
    footer {
      text-align: center; padding: 2rem;
      font-size: .8rem; color: var(--muted);
      border-top: 1px solid var(--border);
    }
"""


# ─────────────────────────────────────────────────────────────────────────────
# HTML GENERATOR
# ─────────────────────────────────────────────────────────────────────────────

def learning_dir(bundle_path):
    """Return the directory where source .md files live.
    Prefers bundle_path/learning/ if it exists, otherwise falls back to bundle root."""
    ld = bundle_path / "learning"
    return ld if ld.is_dir() else bundle_path


def generate_detail_page(material, all_materials, bundle_path):

    src = learning_dir(bundle_path)
    index_md_path     = src / "index.md"
    learnings_md_path = src / "learnings.md"
    script_md_path    = src / "script.md"

    library_root  = "../../"
    library_index = library_root + "index.html"

    def mat_link(m):
        return mat_link_from_root(m, library_root)

    # ── Overview content ───────────────────────────────────────────────────
    overview_html = ""
    if index_md_path.exists():
        overview_html = render_overview(index_md_path.read_text(encoding="utf-8"))

    # ── Learnings sections ─────────────────────────────────────────────────
    learnings_sections = {}
    if learnings_md_path.exists():
        learnings_sections = parse_learnings(learnings_md_path.read_text(encoding="utf-8"))

    # ── Teaching Script ────────────────────────────────────────────────────
    # Look for script.md first, then any other .md in learning/ or bundle root
    RESERVED = {"index.md", "learnings.md"}
    script_html = ""
    script_source = None
    if script_md_path.exists():
        script_source = script_md_path
    else:
        extras = sorted(
            p for p in src.glob("*.md")
            if p.name not in RESERVED
        )
        if extras:
            script_source = extras[0]   # first alphabetically
    if script_source:
        script_html = render_markdown(script_source.read_text(encoding="utf-8"))

    # ── Slide deck detection ───────────────────────────────────────────────
    # Any .html in the bundle root that is NOT the detail page or index.html
    detail_filename = slugify(material["title"]) + ".html"
    SKIP_HTML = {detail_filename, "index.html"}
    slide_files = sorted(
        p for p in bundle_path.glob("*.html")
        if p.name not in SKIP_HTML
    )

    # ── CrossRef sidebar ───────────────────────────────────────────────────
    crossrefs = []
    for cr in material.get("crossRef", []):
        ref_m = find_by_id(cr["id"], all_materials)
        if ref_m:
            crossrefs.append((cr["rel"], ref_m))

    related = find_related(material, all_materials)

    prog_label = PROGRAM_LABELS.get(material.get("program", ""), material.get("program", ""))
    type_label = TYPE_LABELS.get(material.get("type", ""), material.get("type", "").title())

    # ── Objectives ─────────────────────────────────────────────────────────
    obj_html = ""
    if material.get("objectives"):
        items = "".join(
            f'<li><span class="obj-num">{i+1}</span><span>{o}</span></li>'
            for i, o in enumerate(material["objectives"])
        )
        obj_html = f'<ul class="objectives-list">{items}</ul>'

    # ── Slide deck sidebar card ────────────────────────────────────────────
    slides_sidebar_html = ""
    if slide_files:
        deck_items = ""
        for sf in slide_files:
            pretty = sf.stem.replace("-", " ").replace("_", " ").title()
            deck_items += f'''
            <a href="{sf.name}" target="_blank" class="slide-deck-link">
              <span class="slide-icon">▶</span>
              <span class="slide-deck-name">{pretty}</span>
              <span class="slide-open-label">Open →</span>
            </a>'''
        slides_sidebar_html = f'<div class="sidebar-card slide-deck-card"><h3>🎯 Slide Deck</h3>{deck_items}</div>'

    # ── Tags (sidebar) ─────────────────────────────────────────────────────
    tags_sidebar_html = ""
    if material.get("tags"):
        pills = "".join(f'<span class="tag">{t}</span>' for t in material["tags"])
        tags_sidebar_html = f'<div class="sidebar-card"><h3>Tags</h3><div class="tag-row">{pills}</div></div>'

    # ── Prerequisites ──────────────────────────────────────────────────────
    if material.get("prerequisites"):
        items = "".join(f'<li>{p}</li>' for p in material["prerequisites"])
        prereq_html = f'<ul class="prereq-list">{items}</ul>'
    else:
        prereq_html = '<p style="font-size:.875rem;color:var(--muted)">None — open to all.</p>'

    # ── CrossRef block ─────────────────────────────────────────────────────
    crossref_html = ""
    if crossrefs:
        cards = "".join(f'''
        <a href="{mat_link(m)}" class="crossref-card {REL_CLASSES.get(rel,'')}">
          <span class="rel-badge">{REL_LABELS.get(rel, rel)}</span>
          <span>
            <div class="crossref-title">{m["title"]}</div>
            <div class="crossref-type">{TYPE_LABELS.get(m["type"], m["type"].title())}</div>
          </span>
        </a>''' for rel, m in crossrefs)
        crossref_html = f'<div class="sidebar-card"><h3>Building on</h3>{cards}</div>'

    # ── Related block ──────────────────────────────────────────────────────
    related_html = ""
    if related:
        cards = "".join(f'''
        <a href="{mat_link(m)}" class="related-card">
          <div class="related-title">{m["title"]}</div>
          <div class="related-meta">{TYPE_LABELS.get(m["type"], m["type"].title())} · {m.get("audience","")}</div>
        </a>''' for m in related)
        related_html = f'<div class="sidebar-card"><h3>Related materials</h3>{cards}</div>'

    # ── Learnings tabs ─────────────────────────────────────────────────────
    learnings_html = ""
    tab_defs = []

    if script_html:
        tab_defs.append(("Teaching Script", "teaching-script", f'<div class="md-body">{script_html}</div>'))

    for section_name in ["References", "Resources & Tools", "Teaching Notes", "Student Examples"]:
        content = learnings_sections.get(section_name, "")
        if content:
            sid = section_name.lower().replace(" ", "-").replace("&", "and")
            tab_defs.append((section_name, sid, f'<div class="md-body">{render_markdown(content)}</div>'))

    if tab_defs:
        tabs   = ""
        panels = ""
        for i, (label, sid, panel_html) in enumerate(tab_defs):
            active = " active" if i == 0 else ""
            tabs   += f'<button class="tab-btn{active}" data-tab="{sid}">{label}</button>'
            panels += f'<div class="tab-panel{active}" id="tab-{sid}">{panel_html}</div>'
        learnings_html = f'''
        <section class="overview-section">
          <h2 class="section-title">Learnings</h2>
          <div class="learnings-tabs">{tabs}</div>
          {panels}
        </section>'''

    # ─────────────────────────────────────────────────────────────────────
    # FULL PAGE
    # ─────────────────────────────────────────────────────────────────────

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{material["title"]} — Winnie Nguyen</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Instrument+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
{get_css()}
  </style>
</head>
<body>

  <nav class="nav">
    <a href="{library_index}" class="nav-back">
      <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M10 3L5 8l5 5"/>
      </svg>
      Library
    </a>
    <span class="nav-title">{material["title"]}</span>
    <span class="nav-type-badge">{type_label}</span>
  </nav>

  <header class="hero">
    <div class="hero-inner">
      <div class="hero-meta">
        <span class="badge badge-type">{type_label}</span>
        <span class="badge badge-program">{prog_label}</span>
        <span class="badge badge-audience">{material.get("audience","")}</span>
      </div>
      <h1>{material["title"]}</h1>
      <p class="hero-desc">{material.get("description","")}</p>
      <div class="hero-stats">
        <div class="hero-stat"><strong>{material.get("duration","")}</strong>Duration</div>
        <div class="hero-stat"><strong>{material.get("date","")}</strong>Last updated</div>
        <div class="hero-stat"><strong>{len(material.get("objectives",[]))}</strong>Objectives</div>
      </div>
    </div>
  </header>

  <div class="layout">
    <main class="content">

      <section class="overview-section">
        <h2 class="section-title">Learning Objectives</h2>
        {obj_html}
      </section>

      {overview_html}

      {learnings_html}

    </main>

    <aside class="sidebar">

      {slides_sidebar_html}

      {tags_sidebar_html}

      <div class="sidebar-card">
        <h3>Prerequisites</h3>
        {prereq_html}
      </div>

      {crossref_html}

      {related_html}

    </aside>
  </div>

  <footer>
    <p>Winnie Nguyen · UX Mentoring Hub · {material.get("date","")}</p>
    <p style="margin-top:.25rem">
      <a href="{library_index}" style="color:var(--accent)">← Back to Library</a>
    </p>
  </footer>

  <script>
    document.querySelectorAll('.tab-btn').forEach(btn => {{
      btn.addEventListener('click', () => {{
        const target = btn.dataset.tab;
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
        btn.classList.add('active');
        const panel = document.getElementById('tab-' + target);
        if (panel) panel.classList.add('active');
      }});
    }});
  </script>

</body>
</html>
"""


# ─────────────────────────────────────────────────────────────────────────────
# FOLDER SCANNER — auto-register new content from index.html
# ─────────────────────────────────────────────────────────────────────────────

def parse_index_html(html_text):
    """
    Extract library card metadata from a content folder's index.html.
    Relies on the consistent HTML structure produced by this build script.
    Returns a dict of field values (may have empty strings if not found).
    """

    def get(pattern, default=""):
        m = re.search(pattern, html_text, re.DOTALL)
        if m:
            raw = re.sub(r'<[^>]+>', '', m.group(1)).strip()
            return html_lib.unescape(raw)
        return default

    # Core fields
    title       = get(r'<h1>(.*?)</h1>')
    type_label  = get(r'class="nav-type-badge">(.*?)</span>')
    prog_label  = get(r'class="badge badge-program">(.*?)</span>')
    description = get(r'class="hero-desc">(.*?)</p>')
    audience    = get(r'class="badge badge-audience">(.*?)</span>')

    # Duration and date live inside hero-stat blocks
    dur_m  = re.search(r'<strong>(.*?)</strong>\s*Duration',     html_text)
    date_m = re.search(r'<strong>(.*?)</strong>\s*Last updated', html_text)
    duration = html_lib.unescape(dur_m.group(1).strip())  if dur_m  else ""
    date     = html_lib.unescape(date_m.group(1).strip()) if date_m else ""

    # Tags — deduplicated, preserving order
    seen, tags = set(), []
    for t in re.findall(r'class="tag">(.*?)</span>', html_text):
        t = html_lib.unescape(t.strip())
        if t and t not in seen:
            seen.add(t)
            tags.append(t)

    # Objectives — numbered spans inside objectives-list
    obj_matches = re.findall(
        r'class="obj-num">\d+</span><span>(.*?)</span>', html_text
    )
    objectives = [html_lib.unescape(o.strip()) for o in obj_matches]

    # Prerequisites — only if the prereq-list element exists
    prerequisites = []
    prereq_block = re.search(r'class="prereq-list">(.*?)</ul>', html_text, re.DOTALL)
    if prereq_block:
        raw_items = re.findall(r'<li>(.*?)</li>', prereq_block.group(1), re.DOTALL)
        prerequisites = [
            html_lib.unescape(re.sub(r'<[^>]+>', '', p).strip())
            for p in raw_items if p.strip()
        ]

    # Map human-readable labels to data values
    type_map = {"Lesson": "lesson", "Framework": "framework",
                "Guide": "guide",  "Slides":    "slides"}
    prog_map = {"UX Class": "ux-class", "Private": "private", "Both": "both"}

    return {
        "title":         title,
        "type":          type_map.get(type_label, ""),
        "program":       prog_map.get(prog_label, "both"),
        "description":   description,
        "audience":      audience,
        "duration":      duration,
        "date":          date,
        "tags":          tags,
        "objectives":    objectives,
        "prerequisites": prerequisites,
    }


def ensure_scaffold(folder, mat_type):
    """
    For a newly detected folder, create assets/ + learning/ if missing,
    and drop in starter index.md + learnings.md if learning/ is empty.
    Returns True if any scaffolding was created.
    """
    import datetime
    created = False

    assets_dir    = folder / "assets"
    learning_dir_ = folder / "learning"

    if not assets_dir.exists():
        assets_dir.mkdir()
        (assets_dir / ".gitkeep").write_text("")
        created = True

    if not learning_dir_.exists():
        learning_dir_.mkdir()
        created = True

    # Drop starter files only if learning/ has no .md files yet
    existing_mds = list(learning_dir_.glob("*.md"))
    if not existing_mds:
        title      = folder.name.replace("-", " ").title()
        type_label = mat_type.title()
        month_year = datetime.date.today().strftime("%b %Y")
        (learning_dir_ / "index.md").write_text(
            STARTER_INDEX_MD.format(title=title, type_label=type_label),
            encoding="utf-8"
        )
        (learning_dir_ / "learnings.md").write_text(
            STARTER_LEARNINGS_MD.format(month_year=month_year),
            encoding="utf-8"
        )
        created = True

    return created


def scan_new_folders(materials):
    """
    Walk each type directory (lessons/, frameworks/, guides/, slides/).
    For every subfolder that has NO matching entry in library-data.js:
      1. Auto-scaffold assets/ + learning/ if missing.
      2. If an HTML page exists, parse it and register a new entry.

    Matching is done by folder name — if any existing material's page path
    contains the folder name as a segment, it is considered already registered.

    Returns a (possibly empty) list of new material dicts.
    """
    # Collect folder names already covered by existing entries
    known_folders = set()
    for m in materials:
        page = m.get("page", "")
        if page:
            parts = page.replace("\\", "/").split("/")
            if len(parts) >= 2:
                known_folders.add(parts[1])

    next_id      = max((m["id"] for m in materials), default=0) + 1
    new_materials = []

    for mat_type, type_dir in sorted(TYPE_DIRS.items()):
        type_path = SCRIPT_DIR / type_dir
        if not type_path.exists():
            continue

        for folder in sorted(type_path.iterdir()):
            if not folder.is_dir() or folder.name in known_folders:
                continue

            # ── Auto-scaffold missing assets/ + learning/ ─────────────────
            if ensure_scaffold(folder, mat_type):
                print(f"  ✦  Scaffolded {type_dir}/{folder.name}/")
                print(f"             → assets/ + learning/ created")

            # ── Register in library-data if an HTML page exists ───────────
            index_html_path = folder / "index.html"
            if index_html_path.exists():
                html_file = index_html_path
            else:
                candidates = sorted(folder.glob("*.html"))
                if not candidates:
                    continue      # new empty folder — scaffolded, no page yet
                html_file = candidates[0]

            html_text = html_file.read_text(encoding="utf-8")
            meta = parse_index_html(html_text)

            if not meta["title"] or not meta["type"]:
                print(f"  ⚠  {type_dir}/{folder.name}/ — could not parse title/type, skipping")
                continue

            new_mat = {
                "id":            next_id,
                "type":          meta["type"],
                "program":       meta["program"],
                "title":         meta["title"],
                "description":   meta["description"],
                "audience":      meta["audience"],
                "duration":      meta["duration"],
                "tags":          meta["tags"],
                "objectives":    meta["objectives"],
                "prerequisites": meta["prerequisites"],
                "date":          meta["date"],
                "file":          "",
                "page":          f"{type_dir}/{folder.name}/{html_file.name}",
                "crossRef":      [],
            }
            new_materials.append(new_mat)
            known_folders.add(folder.name)
            next_id += 1
            print(f"  ＋  [{meta['type']:9}] {meta['title'][:50]}")
            print(f"             auto-registered from {type_dir}/{folder.name}/")

    return new_materials


# ─────────────────────────────────────────────────────────────────────────────
# SCAFFOLD — create a new content folder with assets/ + learning/ + index.md
# ─────────────────────────────────────────────────────────────────────────────

STARTER_INDEX_MD = """\
# {title}

**Type:** {type_label}
**Duration:**
**Audience:**

---

## Key Concepts

### Concept 1
One-sentence explanation.

### Concept 2
One-sentence explanation.

## Session Structure

| Time  | Segment          | Type    | Duration |
|-------|------------------|---------|----------|
| 0:00  | Warm-up          | Warm-up | 10 min   |
| 0:10  | Core concept     | Concept | 20 min   |
| 0:30  | Practice activity | Activity | 30 min  |
| 1:00  | Wrap-up + Q&A    | Wrap-up | 15 min   |

## Tools & Materials

- Whiteboard or FigJam
- Printed handout (see assets/)

## Practice Activities

### Activity name
Description of what students will do.
"""

STARTER_LEARNINGS_MD = """\
## References

- Source 1
- Source 2

## Teaching Notes

### {month_year}
Notes from this session.

## Student Examples

Examples of strong student work go here.
"""


def scaffold_new(type_key, name_slug):
    """Create a new content folder: type_key/name_slug/ with assets/ + learning/ + starter files."""
    import datetime

    type_dir_name = TYPE_DIRS.get(type_key)
    if not type_dir_name:
        print(f"  ✗  Unknown type '{type_key}'. Choose from: {', '.join(TYPE_DIRS)}")
        return

    folder = SCRIPT_DIR / type_dir_name / name_slug
    if folder.exists():
        print(f"  ✗  Folder already exists: {type_dir_name}/{name_slug}/")
        return

    assets_dir   = folder / "assets"
    learning_dir_ = folder / "learning"
    assets_dir.mkdir(parents=True)
    learning_dir_.mkdir(parents=True)

    title      = name_slug.replace("-", " ").title()
    type_label = type_key.title()
    month_year = datetime.date.today().strftime("%b %Y")

    (learning_dir_ / "index.md").write_text(
        STARTER_INDEX_MD.format(title=title, type_label=type_label),
        encoding="utf-8"
    )
    (learning_dir_ / "learnings.md").write_text(
        STARTER_LEARNINGS_MD.format(month_year=month_year),
        encoding="utf-8"
    )
    (assets_dir / ".gitkeep").write_text("")

    print(f"\n  ✓  Scaffolded {type_dir_name}/{name_slug}/")
    print(f"       assets/          ← drop images here")
    print(f"       learning/        ← edit index.md and learnings.md")
    print(f"\n  Next: fill in learning/index.md, then run:  python3 build.py\n")


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print("\n  📚 Knowledge Library — Static Build\n  " + "─" * 38)
    materials = parse_library_data()
    print(f"  Loaded {len(materials)} materials from library-data.js\n")

    # ── Scan for new folders ───────────────────────────────────────────────
    print("  Scanning for new folders…")
    new_mats = scan_new_folders(materials)
    if new_mats:
        materials.extend(new_mats)
        print(f"\n  ＋  {len(new_mats)} new card(s) auto-registered\n")
    else:
        print("  ○  No new folders found\n")

    generated = 0
    skipped = 0

    for m in materials:
        type_dir = TYPE_DIRS.get(m["type"])
        if not type_dir:
            print(f"  ⚠  Unknown type '{m['type']}' for id {m['id']} — skipping")
            skipped += 1
            continue

        slug = slugify(m["title"])
        bundle_path = SCRIPT_DIR / type_dir / slug

        if not bundle_path.exists():
            print(f"  ○  No bundle: {type_dir}/{slug}/ — skipping id {m['id']}")
            skipped += 1
            continue

        html = generate_detail_page(m, materials, bundle_path)
        filename = f"{slug}.html"
        out_path = bundle_path / filename
        out_path.write_text(html, encoding="utf-8")
        m["page"] = f"{type_dir}/{slug}/{filename}"

        # Remove any stale index.html from previous builds (best-effort)
        stale = bundle_path / "index.html"
        if stale.exists():
            try:
                stale.unlink()
            except OSError:
                pass  # iCloud-synced files may be read-only; skip silently

        RESERVED_NAMES = {"index.md", "learnings.md"}
        src_dir = learning_dir(bundle_path)
        has_content = (src_dir / "index.md").exists()
        extra_mds = [p.name for p in src_dir.glob("*.md") if p.name not in RESERVED_NAMES]
        script_label = extra_mds[0] if extra_mds else "○"
        print(f"  ✓  [{m['type']:9}] {m['title'][:48]}")
        print(f"             index.md={'✓' if has_content else '○'}  script={script_label}  → {m['page']}")

    write_library_data(materials)
    print(f"\n  ✓  library-data.js updated")
    print(f"  Done: {generated + (len(materials) - skipped)} pages built, {skipped} skipped.\n")


if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    if args and args[0] == "--new":
        if len(args) < 3:
            print("\n  Usage:  python3 build.py --new <type> <folder-name>")
            print("  Types:  lesson | framework | guide | slides")
            print("  Example: python3 build.py --new lesson user-journey-mapping\n")
        else:
            scaffold_new(args[1], args[2])
    else:
        main()
