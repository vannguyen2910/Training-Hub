# Mentoring Program — Claude Rules

## Lesson file sync rule

Every lesson in `Library/lessons/` has two paired files:
- `*-lesson.md` — the source of truth for all content (activities, phases, timing, concepts)
- `*-slide-outline.md` — reflects the lesson structure as slide specs (layout types, visual hints, kickers)

**When either file is updated, always check and update the other.**

Specifically:

| What changed in lesson.md | What to update in slide-outline.md |
|---|---|
| Phase timing (e.g. "15 min" → "20 min") | MILESTONE slide `Num:` value + arc description + slide structure note |
| Phase added or removed | Add/remove the corresponding slide section; update total slide count in the structure note |
| New checkpoint or transition inserted | Add a STATEMENT or MILESTONE slide at the matching position in the outline |
| Section reordered (e.g. concept extension moved) | Reorder the corresponding slides in the outline |
| Slide count changes for any reason | Update the `## Slide structure` header line (e.g. "17 slides" → "18 slides") |

| What changed in slide-outline.md | What to update in lesson.md |
|---|---|
| Slide timing or Num value changed | Update the matching phase timing in the Session Structure table |
| Slide added or removed | Check if the lesson phase needs a matching structural change |
| Kicker or title copy changed | Check if the lesson phase heading or key message should match |

**Always apply both files in the same response.** Never leave one out of sync with the other.

---

## General lesson conventions

- All specific AI tool names (Claude, Cursor, ChatGPT, Copilot, etc.) should be replaced with generic labels: "AI chat tool", "AI coding tool", "your AI tool". Do not introduce tool names when editing lesson content.
- The `*-slide-outline.md` file contains only slide-specific concerns (layout, visual hints, kickers). Do not add full lesson prose to it.
- The `*-lesson.md` file is the source of truth. If content in the two files conflicts, the lesson file wins.
