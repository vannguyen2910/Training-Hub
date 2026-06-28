# 📥 Inbox

This is a **temporary processing zone**. Nothing lives here permanently.

Drop raw files, rough notes, unstructured content, or anything you're not sure where to put.
Claude will process each item, move the source file to the right folder, and create the structured artifact in the correct location.

---

## How to use

1. Drop your file or paste your content here
2. Tell Claude: "Process my inbox" or "Process [filename]"
3. Claude will triage, brief (if a build is needed), and route — then clear the item out

## What happens to each item

| Item type | Source file moved to | Structured artifact created in |
|-----------|---------------------|-------------------------------|
| Raw lesson notes | `Source/` | `Library/lessons/[name]/` |
| Rough slide content | `Source/` | Brief → `Library/slides/[name]/` |
| Private session notes | `Sessions/[mentee]/` | — |
| Framework or guide draft | `Source/` | `Library/guides/` or `Library/frameworks/` |
| Reusable template | `_Templates/` | — |
| Asset (image, export) | `Assets/` | — |
| Unsure | Ask Claude to triage | Confirmed by you |

## Rules

- **Nothing stays here permanently.** Every item must be processed and moved.
- **Do not save finished work here.** Inbox is for inputs, not outputs.
- **If you're unsure what to do with it** — drop it here and let Claude triage it (Rule WF-4 + Rule WF-6).
