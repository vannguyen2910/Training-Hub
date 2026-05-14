# 📋 Automation Rules & Folder Organization

**Last Updated:** 2026-05-08  
**Purpose:** Central reference for how Claude should organize and handle content creation

---

## Rule 1: New Slide Deck Creation 🎯
**Status:** Active

When you request a new slide deck, Claude will automatically save it here:
```
📁 Library/slides/[slide-deck-name]/
   ├── learning/     (main slide content goes here)
   └── assets/       (images, files, resources)
```

**Example paths:**
- `Library/slides/product-thinking-101/learning/`
- `Library/slides/ux-research-methods-intro/learning/`

**What triggers this:** Any request like:
- "Create a slide deck for..."
- "Make slides about..."
- "Design a presentation for..."

**File naming convention:** Use lowercase-hyphens (no spaces)
- ✅ `product-thinking-intro.pptx`
- ❌ `Product Thinking Intro.pptx`

---

## Rule 2: Design Consistency 🎨
**Status:** Active

When creating slide decks, Claude will reference the **Templates folder** to ensure visual consistency:
```
📁 Templates/
   ├── design-system/
   ├── color-palette.md
   ├── typography-guide.md
   └── slide-templates/
```

**What this means:**
- Check Templates for existing design standards before creating new slides
- Reuse color schemes, typography, and layouts from Templates
- If templates don't exist for a specific deck, create them in Templates first
- Maintain consistent branding across all slides

**Design checklist before finalizing slides:**
- [ ] Colors match approved palette from Templates
- [ ] Typography follows established font standards
- [ ] Layout structure aligns with slide-templates
- [ ] Assets stored in corresponding `assets/` folder

---

## Rule 3: Updating These Rules ✏️
**How to modify this file:**

1. **Location:** `/Users/winnie.nguyen/Library/CloudStorage/GoogleDrive-nguyenphuctuongvan@gmail.com/My Drive/03_Mentoring/AUTOMATION_RULES.md`

2. **To request changes:** Just tell Claude:
   - "Update Rule 1 to..."
   - "Add a new automation rule for..."
   - "Change the slide folder location to..."

3. **I will update this file directly** and save the changes so you can reference it anytime

---

## Rule 6: Inbox Processing 📥
**Status:** Active

The `Inbox/` folder is a **temporary processing zone**. Nothing stays there permanently.

**What triggers this:** Any request like:
- "Process my inbox"
- "Process [filename] from Inbox"
- "Clear my inbox"

**Processing steps Claude follows for each item:**

1. **Read the item** — understand what it is (raw notes, draft content, asset, etc.)
2. **Triage** — determine the artifact type and intended audience using the routing logic from Rule 4
3. **Brief if a build is needed** — if the item will become HTML, a slide deck, or a lesson, apply Rule 5 (content brief first) before building
4. **Move the source file** — relocate the raw input to its permanent home (see routing table below)
5. **Create the structured artifact** — save the finished output to the correct Library folder
6. **Confirm completion** — tell you what was moved where and what was created

**Routing table:**

| Item type | Source file moved to | Structured artifact created in |
|-----------|---------------------|-------------------------------|
| Raw lesson notes | `Source/` | `Library/lessons/[name]/` |
| Rough slide content | `Source/` | Brief → `Library/slides/[name]/` |
| Private session notes | `Sessions/[mentee]/` | — (private, no published artifact) |
| Framework or guide draft | `Source/` | `Library/guides/` or `Library/frameworks/` |
| Reusable template | `_Templates/` | — |
| Asset (image, export) | `Assets/` | — |
| Ambiguous item | Stop and triage (Rule 4) | Confirmed by you before moving |

**What Claude never does:**
- Leave a processed item in `Inbox/` after it has been routed
- Move a file without telling you where it went
- Build an artifact without a brief if the item requires one (Rule 5 still applies)
- Delete anything from `Inbox/` — items are always moved, never deleted

---

## Rule 5: Content Brief Before Building 📝
**Status:** Active

Before Claude writes any HTML, assembles any slide deck, or produces any design artifact, it must first generate a **markdown content brief** and wait for approval.

**What triggers this:** Any request like:
- "Create a slide deck for..."
- "Build an HTML page for..."
- "Design a lesson on..."
- "Make a workshop about..."

**Why this rule exists:**
- A full HTML slide deck costs 3,000–8,000 tokens. A brief costs 200–400.
- Structural or flow problems caught at brief stage cost nothing to fix; caught after a full build, they require a full rebuild.
- Markdown is fast to scan, cheap to edit, and easy to approve in one reply.

**The gate:** Claude produces the brief → you approve or edit it → Claude builds. Claude never skips this step.

**Brief format Claude will always use:**

```markdown
---
title: "Artifact title"
type: slide-deck | html-page | lesson | guide
audience: ux-class | private-training
level: beginner | intermediate | advanced
duration: e.g. "90 min" (if applicable)
---

## Purpose
One sentence: what this artifact helps the student do or understand.

## Structure
1. Section name — what it covers (1 line)
2. Section name — what it covers
3. ...

## Key decisions
- Tone, framing, or anything you'd want to review before Claude builds
```

**After you approve:**
- Reply "looks good", "go ahead", or make inline edits and say "updated, build it"
- Claude proceeds to the full build using the approved brief as the spec

**Brief file location:** Claude saves the brief to the same destination folder as the planned artifact, with a `-brief.md` suffix (e.g. `design-thinking-101-brief.md`), so you can reference it later or reuse it.

---

## Rule 4: Unknown Artifact Triage 📂
**Status:** Active

When you share an artifact without a clear destination folder, Claude will **stop and triage** rather than guess.

**What triggers this:** Any message like:
- "Here's [artifact], not sure where it goes"
- "I made this, where should I save it?"
- "Can you file this for me?"

**How Claude will respond:**

1. **State what's ambiguous** — explain which signals are unclear (content type, audience, reusability)
2. **Offer 2–3 concrete folder options** — never open-ended questions
3. **Give a recommendation** — one option labelled "Recommended" with a short reason
4. **Wait for your confirmation** before creating or moving any file

**Example response format:**
> "This looks like a reusable framework guide, not a private session recap. My recommendation: `Library/guides/` — it would apply to any student, not just one mentee. Alternatively: `Source/` if it's still a rough draft. Which do you prefer?"

**Routing logic Claude will use:**

| Signal | Likely destination |
|--------|--------------------|
| Reusable across students | `Library/` (lessons, slides, guides, or frameworks subfolder) |
| Specific to one private mentee | `Sessions/[mentee-name]/` |
| Raw / unprocessed / incomplete | `Source/` |
| Visual template or design file | `_Templates/` |
| Finished asset (image, export) | `Assets/` |

**Speed tip:** Include the artifact type in your message (slide deck, lesson plan, guide, session recap, template) — it eliminates most ambiguity immediately.

---

## Quick Reference Table

| Trigger | Action | Output Folder |
|---------|--------|---------------|
| "Create slide deck / HTML / lesson / design" | Generate brief first, wait for approval, then build | Brief saved alongside artifact with `-brief.md` suffix |
| "Create slide deck" (after brief approved) | Generate and organize | `Library/slides/[name]/learning/` |
| Check before finalizing | Reference Templates folder | `_Templates/` |
| "Process my inbox" / "Process [file]" | Read → triage → brief (if build needed) → move source → create artifact → report | Source to permanent folder; artifact to Library |
| "Not sure where this goes" | Triage with options + recommendation | Confirmed by you |
| Need to adjust rules | Edit this file | `_Rules/AUTOMATION_RULES.md` |

---

**📍 How to find this file:**
- In your Mentoring folder: `03_Mentoring/AUTOMATION_RULES.md`
- Or search: "AUTOMATION_RULES.md"
- It's always in the root of your 03_Mentoring folder

**💡 Pro tip:** This file is your source of truth. Claude will check it before creating slides, so keeping it updated ensures consistent behavior!
