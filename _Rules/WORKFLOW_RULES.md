# 🔄 Workflow Rules

**Last Updated:** 2026-04-30
**Author:** Winnie Nguyen
**Purpose:** Rules for recurring workflow situations that sit between content creation — sourcing old material, adapting private work, handling ambiguity, and keeping content findable.

---

## Quick Navigation

- [Rule WF-1: Source → Library Migration](#rule-wf-1-source--library-migration)
- [Rule WF-2: Private → Class Adaptation](#rule-wf-2-private--class-adaptation)
- [Rule WF-3: Claude Ambiguity Handling](#rule-wf-3-claude-ambiguity-handling)
- [Rule WF-4: Content Tagging Vocabulary](#rule-wf-4-content-tagging-vocabulary)

---

## Rule WF-1: Source → Library Migration

**Status:** Active | **Priority:** High

### When to migrate

Pull a file from `Source/` into `Library/` when **all three** of these are true:

1. The content is still conceptually accurate (the framework, method, or principle holds)
2. You would actually use it again in a current session or class
3. It would take more effort to rewrite from scratch than to modernize the existing file

If only 1 or 2 apply — leave it in `Source/`. Don't migrate content just because it exists.

### Migration steps

1. **Copy, don't move** — always leave the original in `Source/` untouched
2. **Rename to current convention** — lowercase-hyphens, clear title (e.g. `how-might-we-framing.md`)
3. **Update structure** — apply the current lesson or slide template (see `_Templates/`)
4. **Modernize content:**
   - Replace outdated examples with current ones
   - Add the "AI in Practice" section (Rule LP-4 in `MENTORING_RULES.md`)
   - Update metadata frontmatter (`date`, `level`, `tags`, `draft: true`)
5. **Tag the Source original** — add this line at the top of the Source file:

   ```
   <!-- MIGRATED → Library/[path/to/new-file] on YYYY-MM-DD -->
   ```

6. **File in Library** under the correct subfolder:
   - Lessons → `Library/lessons/[lesson-name]/learning/`
   - Slide decks → `Library/slides/[slide-name]/learning/`
   - Guides / frameworks → `Library/guides/` or `Library/frameworks/`

### What not to migrate

- Raw student work or feedback from old cohorts
- Outdated tool tutorials (e.g. old Sketch, old Figma workflows that no longer apply)
- Files with no clear home in the current folder structure

---

## Rule WF-2: Private → Class Adaptation

**Status:** Active | **Priority:** High

### When this applies

Any time content from a private mentee session (Anh Truong, Vy Duong, or any future private student) is used as the basis for a class lesson, slide deck, or guide.

### Adaptation checklist

Before using private content in class materials:

**Strip personal context:**
- [ ] Remove all student names (replace with "a student", "one mentee", or a fictional persona)
- [ ] Remove specific portfolio or project details that could identify the student
- [ ] Remove any feedback that was personal or situation-specific

**Generalize the content:**
- [ ] Reframe examples so they apply to any student, not just one person's situation
- [ ] Broaden the problem statement (e.g. "struggling with problem framing" → "common challenge in early-stage research")
- [ ] Replace specific project references with generic scenarios or anonymized case studies

**Track the origin:**
- Add this line in the metadata frontmatter of the new class file:

  ```yaml
  source: adapted-from-private-session
  ```

- This is for your own reference only — it never appears in published output

**Never publish:**
- Session recaps (`session-*.md`) must always stay `draft: true`
- Session notes are private records, not source material to be shared directly

### File location after adaptation

Adapted content lives in `Library/` under the appropriate subfolder — **not** in `Sessions/`. Sessions are for private notes only.

---

## Rule WF-3: Claude Ambiguity Handling

**Status:** Active | **Priority:** High

### Default behaviour

**When in doubt, stop and ask.** Claude should not assume or guess when a situation is ambiguous — especially for structural, organizational, or irreversible decisions.

### Always ask before:

- Creating a new folder or changing the folder structure
- Moving or renaming files (especially anything outside the outputs directory)
- Deleting any file (even temporary ones)
- Choosing between two plausible interpretations of a request
- Deciding which program a piece of content belongs to (`ux-class` vs `private-training`)
- Picking a level (`beginner` / `intermediate` / `advanced`) without clear context

### How to ask

When asking, Claude should:

1. **State the ambiguity clearly** — explain what's unclear and why it matters
2. **Offer 2–3 concrete options** — not open-ended questions
3. **Give a recommendation** — label one option as "Recommended" with a reason
4. **Keep it short** — one question per ambiguous point, not a list of five

Example of good ambiguity handling:
> "I'm not sure whether this lesson should go in `Library/lessons/` or stay in `Sessions/anh-truong/`. My recommendation: `Library/lessons/` — it reads like a reusable class resource, not a private recap. Shall I save it there?"

Example of bad ambiguity handling:
> Silently choosing a folder and proceeding.

### When Claude can proceed without asking

- Small wording, formatting, or grammar decisions
- Choosing between synonymous file names that both follow naming conventions
- Applying existing rules (e.g. slide layout, token colors) where the rule is unambiguous

---

## Rule WF-4: Content Tagging Vocabulary

**Status:** Active | **Priority:** Medium

### Why this matters

Tags in frontmatter metadata are only useful if they're consistent. Without a controlled vocabulary, the same concept gets labelled differently across files (`research`, `ux-research`, `UX Research`) and search becomes unreliable.

### Approved tag list

Use only tags from this list. If you need a new tag, add it here first.

**UX Methods & Practice**

| Tag | Use for |
|-----|---------|
| `ux-research` | User research methods, interviews, surveys |
| `synthesis` | Affinity mapping, insights, themes |
| `problem-framing` | HMW, problem statements, reframing |
| `ideation` | Brainstorming, divergent thinking |
| `prototyping` | Low-fi, mid-fi, hi-fi prototyping |
| `usability-testing` | Testing methods, moderation, analysis |
| `design-critique` | Giving and receiving critique |
| `information-architecture` | IA, navigation, card sorting |
| `interaction-design` | IxD, flows, microinteractions |
| `visual-design` | UI, typography, color, layout |
| `design-systems` | Component libraries, tokens, patterns |

**Thinking & Mindset**

| Tag | Use for |
|-----|---------|
| `design-thinking` | Design thinking process, mindsets |
| `systems-thinking` | Big-picture thinking, relationships |
| `critical-thinking` | Analysis, evaluation, reasoning |
| `storytelling` | Presenting work, narrative structure |

**AI & Tools**

| Tag | Use for |
|-----|---------|
| `ai-in-ux` | Using AI tools in UX practice |
| `prompt-engineering` | Writing and refining AI prompts |
| `ai-ethics` | Ethical considerations around AI use |
| `figma` | Figma-specific content |
| `miro` | Miro-specific content |

**Audience & Level**

| Tag | Use for |
|-----|---------|
| `beginner` | No prior UX experience assumed |
| `intermediate` | Some UX experience required |
| `advanced` | Experienced practitioners |
| `ux-class` | Content for the Internal UIUX class |
| `private-training` | Content for private mentees (Anh, Vy, etc.) |

**Content Type**

| Tag | Use for |
|-----|---------|
| `workshop` | Group activities, facilitated sessions |
| `lecture` | Primarily instructional content |
| `case-study` | Real or illustrative project examples |
| `template` | Reusable formats and frameworks |
| `assessment` | Quizzes, reflections, evaluations |

### Tagging rules

- Use **2–5 tags** per file — enough to be findable, not so many they lose meaning
- Always include one **audience tag** (`ux-class` or `private-training`) and one **level tag** (`beginner`, `intermediate`, `advanced`)
- Use lowercase only — no spaces, no capitals
- Combine tags for specificity: `ux-research` + `synthesis` + `beginner` is clear; `research` alone is not

### Example frontmatter

```yaml
---
title: "How to Run a User Interview"
type: lesson
program: ux-class
tags: [ux-research, beginner, ux-class, workshop]
level: beginner
duration: "90 min"
date: 2026-04-30
draft: true
---
```

### Adding new tags

If approved content needs a tag not on this list:
1. Add the tag to this file under the correct category
2. Use it in the new file
3. Optionally backfill existing files that would benefit from it

---

## Rules Summary

| Rule | What It Covers | When to Apply |
|------|----------------|---------------|
| **WF-1** | Bringing old Source content into Library | When reusing archive material |
| **WF-2** | Adapting private session content for class use | When private → class crossover happens |
| **WF-3** | How Claude handles ambiguous situations | Every time Claude faces uncertainty |
| **WF-4** | Consistent tag vocabulary for all content | When writing frontmatter in any file |

---

**Last updated:** 2026-04-30
**Next review:** 2026-07-30
