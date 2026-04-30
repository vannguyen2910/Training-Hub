# 📚 Complete Mentoring Rules System

**Last Updated:** 2026-04-30  
**Author:** Winnie Nguyen  
**Purpose:** Central rulebook for efficient mentoring content preparation, lesson planning, and session management

---

## 🎯 Quick Navigation

- [Slide Deck Rules](#slide-deck-rules) — Creating slide presentations
- [Lesson Planning Rules](#lesson-planning-rules) — Designing lessons
- [Session Management Rules](#session-management-rules) — Mentee meetings & recaps
- [File Organization Rules](#file-organization-rules) — Folder structure & naming
- [Quality Assurance Rules](#quality-assurance-rules) — Pre-publish checklist
- [Workflow Priority Rules](#workflow-priority-rules) — What to do first

---

## 🎨 Slide Deck Rules

### Rule SD-1: Slide Deck Structure
**Status:** Active | **Priority:** High

When creating a new slide deck:

```
Library/slides/[slide-name]/
├── learning/
│   └── [slide-name].html (main presentation)
├── assets/
│   ├── images/
│   ├── diagrams/
│   └── references/
└── README.md (metadata & notes)
```

**File naming:** Use lowercase-hyphens (no spaces)
- ✅ `product-thinking-101.html`
- ❌ `Product Thinking 101.html`

---

### Rule SD-2: Design System Compliance
**Status:** Active | **Priority:** High

**ALWAYS follow the design rules in `_Templates/slide-deck-design/RULES.md`**

Key requirements:
- Link `../../../_Templates/slide-deck-design/tokens.css` (correct relative path)
- Load `deck-stage.js` from templates folder
- **Use token colors ONLY** — never hardcode hex values:
  - Accent: `--sienna` (purple), `--ochre` (yellow)
  - Text: `--ink`, `--ink-soft`, `--ink-muted`
  - Backgrounds: `--paper`, `--paper-deeper`
- **Font families:** Use `--font-display` (Syne for headings), `--font-body` (Inter), `--font-mono` (JetBrains)
- **Use preset slide layouts** from RULES.md:
  - `.cover` (title slide)
  - `.section-divider` (section headers)
  - `.statement` (centered big idea)
  - `.numbered` (numbered lists)
  - `.compare` (pros/cons)
  - `.process` (workflows)
  - `.quote` (testimonials)
  - `.milestone` (activity slides)
  - `.practice` (assignments)
  - `.end` (closing)

**Do NOT:**
- ❌ Create custom layouts not in RULES.md
- ❌ Use dark ink backgrounds for section dividers (use `--paper-deeper`)
- ❌ Hardcode hex colors
- ❌ Import Google Fonts separately
- ❌ Show slide numbers unless explicitly requested

---

### Rule SD-3: Slide Deck Content Checklist
**Status:** Active | **Priority:** High

Before finalizing any slide deck, ensure:

**Structure:**
- [ ] Title/cover slide with date, program, facilitator name
- [ ] Clear section dividers between major topics
- [ ] Numbered slides for multi-step content
- [ ] Activity/practice slide(s) using `.milestone` layout
- [ ] Closing slide using `.end` layout
- [ ] Logical flow from simple → complex

**Content:**
- [ ] One main idea per slide
- [ ] Minimal text (max 5 bullet points per slide)
- [ ] Action verbs in titles ("Analyze," "Design," "Critique")
- [ ] Images/diagrams support the text, don't distract
- [ ] Activities have clear instructions (not assumptions)

**Design:**
- [ ] Colors consistent with token system
- [ ] Typography hierarchy: headings vs. body vs. labels
- [ ] Animations use stagger pattern (0.05s, 0.15s, 0.25s, 0.32s)
- [ ] `prefers-reduced-motion` included for accessibility
- [ ] All layouts match RULES.md exactly

**Assets:**
- [ ] All images & diagrams in `assets/` subfolder
- [ ] All external links tested & working
- [ ] No local file paths (use relative paths or URLs)
- [ ] Credit sources if using external images

---

### Rule SD-4: AI in Slide Decks
**Status:** Active | **Priority:** Medium

If including AI examples or prompts in slides:

- Use `.practice` cards for prompt examples
- Include 3 elements:
  1. The prompt (in mono font, dark background)
  2. What the AI output was (with critique callout in `--sienna-tint`)
  3. What was missing or wrong (reflection in `--ochre-tint`)
- Add critical thinking questions
- Label: "🤖 Try this prompt" or "⚠️ AI Limitation"

---

## 📖 Lesson Planning Rules

### Rule LP-1: Lesson Structure & Template
**Status:** Active | **Priority:** High

**Always use `_Templates/learning/_template-lesson.md` as starting point**

Required sections in every lesson:

```
---
title: [Clear, action-focused title]
type: lesson
program: ux-class | private-training
tags: [research, synthesis, beginner, design, etc.]
level: beginner | intermediate | advanced
duration: "60 min" | "90 min" | "2 hours"
date: YYYY-MM-DD
draft: true | false (true = work in progress)
slides: [Google Slides URL - optional]
---

1. Overview (what + why)
2. Learning Objectives (3-5 verbs: explain, apply, critique, analyze)
3. Materials Needed
4. Pre-Class Preparation
5. Run-of-Show (timeline breakdown)
   - Open & Frame (hook/provocation)
   - Core Concept (main teaching)
   - Activity (hands-on practice)
   - Debrief & Takeaways
   - Q&A + Close
6. Practice Dataset (optional for self-study)
7. AI in Practice (new section - always include!)
8. Assessment (knowledge check + reflection)
9. Further Resources
```

---

### Rule LP-2: Learning Objectives Format
**Status:** Active | **Priority:** High

Every lesson must have 3–5 learning objectives using **Bloom's verbs**:

**For beginner level:**
- Explain, Define, Identify, Describe

**For intermediate level:**
- Apply, Analyze, Compare, Distinguish, Critique

**For advanced level:**
- Evaluate, Synthesize, Design, Create, Argue

**Format:**
```
By the end of this session, students will be able to:
1. **[Verb]** — [specific outcome]
2. **[Verb]** — [specific outcome]
3. **[Verb]** — [specific outcome]
```

Bad: "Understand design thinking" ❌  
Good: "Apply design thinking to identify problem statements in their own projects" ✅

---

### Rule LP-3: Run-of-Show (Timing)
**Status:** Active | **Priority:** High

Always include a **minute-by-minute breakdown**:

```
[00:00] Open & Frame (5 min) — Hook or warm-up question
[00:05] Core Concept (25 min) — Main teaching content
[00:30] Activity (30 min) — Hands-on practice + facilitator watch-fors
[01:00] Debrief (10 min) — Key takeaways
[01:10] Q&A + Close (5 min) — Final thoughts
```

**Rules:**
- Total must match `duration` field in metadata
- Mark activities with setup → task → facilitator watch-fors
- Include contingency time (if running long, what can flex?)
- Note any pre-recorded videos or external content

---

### Rule LP-4: AI in Lessons (CRITICAL)
**Status:** Active | **Priority:** High

**Every lesson must include an "AI in Practice" section:**

```
## AI in Practice

### 🤖 Try this with AI
> Paste this prompt into Claude or ChatGPT:
> *"[Your specific prompt]*"

### 🧠 Critical thinking prompt
- What did the AI get right?
- What was generic or wrong?
- What context did the AI not have?

### ✍️ Prompt engineering tip
[One concrete, actionable tip for writing better prompts on this topic]

### ⚖️ Ethics consideration
[One relevant ethical issue students should be aware of]
```

This teaches students to be critical consumers + builders of AI tools.

---

### Rule LP-5: Assessment Structure
**Status:** Active | **Priority:** Medium

Include two assessment types in every lesson:

**Quick knowledge check** (5 min, during session):
- 3–5 questions aligned to learning objectives
- Format: multiple choice, fill-in-blank, or quick discussion

**Reflection prompt** (homework):
- Open-ended reflection tied to real work
- Format: 1–2 sentence prompt asking for personal application

Example:
```
### Reflection prompt (homework)
> Think of a recent design decision you made. Reframe it as a 
> problem statement using the Insight → Problem → Question format.
> Share in next session.
```

---

## 👥 Session Management Rules

### Rule SM-1: Session Structure & Tracking
**Status:** Active | **Priority:** High

**After every mentee session, create a session recap using `_template-session.md`**

File location: `Sessions/[student-name]/session-[number].md`

Required in every recap:
- Session summary (2–3 sentences about energy/big moments)
- Topics covered (bullet list)
- Key observations (strengths, areas to develop, blockers)
- Student work reviewed (what you looked at together)
- Feedback given (using Situation → Behaviour → Impact)
- Commitments & next steps (with due dates)
- Trainer reflection (what worked, what to try next time)
- Next session plan (focus, opening questions, materials)

**Mark `draft: true` always** — these are private notes, not published.

---

### Rule SM-2: Feedback Format
**Status:** Active | **Priority:** High

Use **Situation → Behaviour → Impact** for all mentee feedback:

```
Situation: When we reviewed your user interview notes,
Behaviour: You jumped straight to solutions before mapping pain points,
Impact: This meant you missed opportunities to ask deeper questions.

Next time: Try writing 3 key insights BEFORE suggesting any designs.
```

**Avoid:**
- ❌ "Your design is good" (vague)
- ❌ "This is wrong" (demoralizing)

**Use:**
- ✅ Specific observations
- ✅ Actionable next steps
- ✅ Growth mindset language

---

### Rule SM-3: Student Progress Tracking
**Status:** Active | **Priority:** Medium

In each session recap, track progress on:

- **Thinking progression:** Are they asking better questions? Getting more sophisticated?
- **Technical growth:** New tools, methods, or skills applied?
- **Confidence shifts:** What are they more/less confident about than last session?
- **Blockers:** What's slowing them down? (Process? Mindset? Skills?)

This helps you:
- See patterns over time
- Adjust teaching to meet them where they are
- Celebrate growth in next session

---

## 📁 File Organization Rules

### Rule FO-1: Folder Structure (Master)
**Status:** Active | **Priority:** High

```
03_Mentoring/
├── Library/                           ← ACTIVE CONTENT
│   ├── slides/
│   │   └── [slide-name]/
│   │       ├── learning/
│   │       ├── assets/
│   │       └── README.md
│   ├── lessons/
│   │   └── [lesson-name]/
│   │       ├── learning/
│   │       ├── assets/
│   │       └── README.md
│   ├── guides/
│   ├── frameworks/
│   └── README.md
│
├── Sessions/                          ← MENTEE WORK
│   ├── anh-truong/
│   ├── vy-duong/
│   └── [student-name]/
│       ├── session-1.md
│       ├── session-2.md
│       └── portfolio/ (their work)
│
├── Showcase/                          ← PUBLISHED WORK
│   ├── ux-class/ (public materials)
│   └── private/ (private portfolio)
│
├── _Templates/                        ← REFERENCE
│   ├── learning/ (template files)
│   └── slide-deck-design/ (design system)
│
├── _Rules/                            ← THIS FILE
│   └── MENTORING_RULES.md
│
├── Assets/                            ← SHARED MEDIA
│   ├── images/
│   └── pdfs/
│
└── Source/                            ← ARCHIVE (2018-2026)
    ├── my-teaching/
    ├── ux-material/
    └── ux-methodology/
```

---

### Rule FO-2: Naming Conventions
**Status:** Active | **Priority:** High

**Files:**
- Use: lowercase-with-hyphens
- ✅ `product-thinking-101.html`
- ✅ `session-1-recap.md`
- ❌ `Product Thinking 101.html`
- ❌ `Session 1 Recap.md`

**Folders:**
- Same rule: lowercase-with-hyphens
- ✅ `intro-to-ux-research-methods`
- ✅ `how-to-give-design-critique`
- ❌ `Intro to UX Research Methods`

**Dates:**
- Format: `YYYY-MM-DD` in metadata
- Example: `2026-04-30`

---

### Rule FO-3: Metadata in Every File
**Status:** Active | **Priority:** Medium

Every lesson/slide/session must have frontmatter:

```yaml
---
title: "[Clear title]"
type: lesson | slide | guide | session-recap
program: ux-class | private-training
tags: [tag1, tag2, tag3]
date: YYYY-MM-DD
draft: true | false
---
```

This helps you:
- Search & filter by program, level, topic
- See what's ready to publish vs. work-in-progress
- Track creation/update dates

---

## ✅ Quality Assurance Rules

### Rule QA-1: Pre-Publish Slide Deck Checklist
**Status:** Active | **Priority:** High

Before publishing any slide deck:

**Content Quality:**
- [ ] All text is grammatically correct & concise
- [ ] No empty placeholders or "TODO"s left
- [ ] Images are high-quality (no pixelated/blurry)
- [ ] Links are tested & working
- [ ] Credit/attribution included for external assets

**Design Quality:**
- [ ] All colors use token variables (no hardcoded hex)
- [ ] All fonts are correct (Syne/Inter/JetBrains)
- [ ] Animations stagger correctly & don't distract
- [ ] Tested on different screen sizes if possible
- [ ] No `chrome` elements visible unless requested

**Slide Compliance:**
- [ ] Layouts match RULES.md exactly (no custom CSS hacks)
- [ ] Accessibility: `prefers-reduced-motion` included
- [ ] Relative paths used (no local file references)
- [ ] All assets in `assets/` subfolder

**Metadata:**
- [ ] `draft: false` set (if ready to publish)
- [ ] Title is clear & action-focused
- [ ] Tags are relevant
- [ ] Date is current

---

### Rule QA-2: Pre-Publish Lesson Checklist
**Status:** Active | **Priority:** High

Before marking a lesson `draft: false`:

**Completeness:**
- [ ] All required sections filled in (see Rule LP-1)
- [ ] Learning objectives use Bloom's verbs
- [ ] Run-of-show timing matches total duration
- [ ] Activities have clear setup + task + watch-fors
- [ ] "AI in Practice" section included & complete

**Quality:**
- [ ] No typos or grammatical errors
- [ ] Prompts tested (if asking students to try AI)
- [ ] External links working
- [ ] Images/diagrams credited if external

**Alignment:**
- [ ] Assessment questions align to learning objectives
- [ ] Reflection prompt asks for personal application
- [ ] Difficulty matches stated level (beginner/intermediate/advanced)

**Metadata:**
- [ ] `draft: false`
- [ ] `program` set correctly
- [ ] `level` accurate
- [ ] `duration` realistic

---

### Rule QA-3: Session Recap Completeness
**Status:** Active | **Priority:** Medium

Before finalizing a session recap, check:

**Content:**
- [ ] Key observations are specific, not vague
- [ ] Feedback uses Situation → Behaviour → Impact
- [ ] Next steps are clear & time-bound
- [ ] Personal reflection included (what worked for you as facilitator)

**Format:**
- [ ] Markdown is clean & readable
- [ ] Commitments table has due dates
- [ ] Student name & session number clear
- [ ] `draft: true` (these are private)

---

## 🚀 Workflow Priority Rules

### Rule WP-1: When Creating Slide Decks
**Status:** Active | **Priority:** High

**Priority order:**

1. **Design first** → Review `_Templates/slide-deck-design/RULES.md`
2. **Structure second** → Create folder & link template files
3. **Content third** → Write slides using preset layouts
4. **Polish fourth** → Animate, test, fix spacing
5. **QA last** → Run through QA-1 checklist

**Time estimate:** 2–3 hours for a 20-slide deck

---

### Rule WP-2: When Creating Lessons
**Status:** Active | **Priority:** High

**Priority order:**

1. **Define learning objectives** → Use Bloom's verbs
2. **Plan run-of-show** → Minute-by-minute breakdown
3. **Write core content** → Main teaching section
4. **Design activity** → Setup + task + watch-fors
5. **Add AI in Practice** → Critical thinking prompts
6. **Create assessment** → Knowledge check + reflection
7. **Review & polish** → Grammar, flow, clarity
8. **Run QA checklist** → Mark draft status

**Time estimate:** 3–4 hours for a comprehensive lesson

---

### Rule WP-3: After Mentee Sessions
**Status:** Active | **Priority:** High

**Within 24 hours of session:**

1. **Capture key moments** (Session summary)
2. **Log observations** (Strengths, areas to develop, blockers)
3. **Record feedback** (Using S→B→I format)
4. **Document commitments** (With due dates)
5. **Plan next session** (Focus, opening questions, materials)
6. **Reflect on facilitation** (What worked, what to adjust)

This helps you:
- Remember details for next session
- See long-term growth patterns
- Adjust approach based on what's working

---

### Rule WP-4: Content Update Cycles
**Status:** Active | **Priority:** Medium

**After each use of a lesson/slide deck:**

- [ ] Note any timing gaps (did it run long/short?)
- [ ] Fix typos or unclear wording
- [ ] Update examples to stay current
- [ ] Refresh images if outdated
- [ ] Incorporate student feedback
- [ ] Update metadata `date` field

**For published content:** Update once per year minimum

---

## 🔄 Workflow Commands

Use these phrases with Claude to trigger rule application:

**Slides:**
- "Create a slide deck about [topic]" → I'll use SD-1, SD-2, SD-3, WP-1
- "Design a presentation for [audience]" → Same as above
- "Check my slides against design rules" → I'll use QA-1

**Lessons:**
- "Write a lesson for [topic]" → I'll use LP-1 through LP-5, WP-2
- "Create a new training module on [topic]" → Same as above
- "Review this lesson before publishing" → I'll run QA-2

**Sessions:**
- "Create a session recap for [student]" → I'll use SM-1, SM-2, SM-3, WP-3
- "Prepare for [student]'s next session" → I'll reference past recaps + WP-3

**Files:**
- "Organize my mentoring folder" → I'll use FO-1, FO-2, FO-3
- "Check file naming" → I'll use FO-2

---

## 📊 Rules Summary Table

| Rule | What It Covers | Frequency |
|------|---|---|
| **SD-1 to SD-4** | Slide deck structure, design, content, AI | Every new slide deck |
| **LP-1 to LP-5** | Lesson planning, objectives, run-of-show, AI, assessment | Every new lesson |
| **SM-1 to SM-3** | Session tracking, feedback, progress | After each mentee session |
| **FO-1 to FO-3** | Folder structure, naming, metadata | Always |
| **QA-1 to QA-3** | Pre-publish checklist | Before publishing |
| **WP-1 to WP-4** | Workflow priority & cycles | Every time you create |

---

## ❓ When to Reference These Rules

- **Creating new slides?** → Read SD-1 through SD-4
- **Planning a lesson?** → Read LP-1 through LP-5
- **After a mentee session?** → Read SM-1 through SM-3
- **Before publishing anything?** → Read QA-1 through QA-3
- **Unsure about folder structure?** → Read FO-1
- **Lost in the process?** → Read WP-1 through WP-4

---

## 🎯 Key Principles

1. **Design consistency first** — Use the design system, don't customize
2. **Structure before content** — Outline before writing
3. **Learning outcomes matter** — Start with objectives, not topics
4. **AI is standard** — Every lesson includes critical thinking about AI
5. **Assessment is essential** — Measure learning, don't assume
6. **Feedback drives growth** — Be specific, be kind, be actionable
7. **Document everything** — Future you will be grateful

---

**Last updated:** 2026-04-30  
**Next review:** 2026-07-30  
*Winnie's mentoring compass · Use this to stay on course* 🧭
