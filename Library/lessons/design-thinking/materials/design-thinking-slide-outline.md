# Slide Deck Outline — Design Thinking for UX Designer

> **Source of truth:** `design-thinking-lesson.md`
> All content changes (activities, concepts, examples) must be made there first, then reflected here.
> This file contains only slide-specific concerns: layout types, visual hints, kickers, and structure.

> **How to use this file**
> Paste both this file and `design-thinking-lesson.md` into your AI tool with the instruction below to generate a new slide deck.

---

## Prompt to use

```
Using the outline in this file, create an HTML slide deck for Design Thinking for UX Designer.

Follow the rules in _Config/rules/SLIDE_DECK_RULES.md exactly.
Save the file to Library/lessons/design-thinking/materials/deck.html.

VISUAL DESIGN DIRECTION — apply globally to every slide:
- Prefer simple diagrams, icons, and visual metaphors over bullet lists.
- Use inline SVG for all diagrams and illustrations. Clean, flat shapes using only token colours.
- For the 5-stage cycle, draw a horizontal pipeline with 5 numbered circles connected by arrows.
- For the "pattern most teams follow" diagram, fade out stages 1 and 2, highlight stage 3 in colour.
- For the "without vs with process" comparison, use a clean two-column split with a hairline divider.
- Stage intro slides use a solid --ochre full-bleed background with stage number and name only.
- Activity / milestone slides feel like a full-bleed moment — kicker, time, title, and prompt only.
- Every slide should have one dominant visual element. If a layout is mostly text, add a supporting SVG shape to anchor the eye.
- Avoid centred bullet lists. If items must be listed, use .numbered or .process layout with visual numbering, not a plain <ul>.
```

---

## Session metadata

| Field | Value |
|---|---|
| Session title | Design Thinking for UX Designer |
| Session number | Session 1 |
| Instructor | Winnie Nguyen |
| Program | UX Class |
| Year | 2026 |
| Previous session | — |
| Next session | Customer Understanding |
| Cover photo | Designer's hands sketching wireframe notes on paper — warm, hand-drawn, human feel |

---

## Slide structure

> **90-minute version — 26 slides.**
> Arc: Hook → Problem → Mindset → Framework → 5 Stages → Activity → Assignments → Close.

---

## 1. Introduction

---

### COVER
- Year: 2026
- Day label: Session 1
- Title: Design Thinking\n*for UX Designer*
- Subtitle: From solving requirements to solving real problems
- Author: Winnie Nguyen
- Right panel photo: Designer's hands sketching on paper with wireframe notes and coloured highlights. Warm, human, process-focused.

---

### MILESTONE — Opening Activity
- Kicker: Let's start here
- Num: 10
- Title: Minutes
- Sub: What's one moment you struggled when starting a new initiative? Take 2 minutes to think of a real example — then we'll share.

---

## 2. The Problem

---

### STATEMENT — Issues designers face
- Kicker: Sound familiar?
- Title: We're designing\nfor *requirements,*\nnot for people.
- Lead: Three patterns that keep showing up: designing from stakeholder requirements without questioning them, jumping to high-fidelity the moment a brief arrives, and working in isolation from users and other teams. The brief feels like the problem. It's not.
- 🎨 Visual hint: Three side-by-side cards with muted icons or light illustrations. Card 1: business brief icon — "Designing from requirements only." Card 2: Figma icon — "Jumping to hi-fi." Card 3: single person icon — "Working in silos." Below all three: italic caption — *"But does it really make the people happy?"*

---

### STATEMENT — The real gap
- Kicker: The problem isn't skills
- Title: The problem is not\nlack of design skill.\nIt's lack of\n*design thinking.*
- Lead: From A to B — the gap between no knowledge and knowing the problem and possible solutions. The messy middle is where design thinking lives.
- 🎨 Visual hint: A-to-B diagram. Left circle: A · "No knowledge". Right circle: B · "Knows the problem + possible solutions". Centre: tangled mess of lines that resolves into a single clean path. --ink background, --ochre highlights on A and B circles.

---

## 3. Mindset

---

### STATEMENT — What is Design Thinking
- Kicker: Theory
- Title: Design Thinking
- Lead: is a *human-centered problem-solving* method that helps teams understand user needs, challenge assumptions, and create innovative solutions.
- 🎨 Visual hint: Dark --ink background. Title in large --ochre display type. Definition in white body type. "human-centered problem-solving" in --sienna bold. Minimal full-bleed dark slide.

---

### DIAGRAM — Product Designer capability pyramid
- Kicker: Where process fits
- Title: 90% of discussion\nhappens at the bottom.\n*Growth happens at the top.*
- Lead: Most hiring and development conversations focus on tools, visual design, and UX. But the layers that drive senior-level impact — design process, communication, ownership, strategy — get far less attention.
- 🎨 Visual hint: Layered triangle SVG (bottom to top): Tools · Visual Design · UX Design · Collaboration · Communication · Design Process · Ownership · Strategy · Mentorship · Advocacy. Base layers in --ink-muted (labelled ENGAGEMENT). Top layers in --sienna fill (labelled LEADERSHIP). Annotation: "90% of discussion" arrow pointing to base. Credit: @Artiom Dashinsky.

---

### DIAGRAM — Without vs With process
- Kicker: Why process matters
- Title: Process is what\nmakes decisions\n*defensible.*
- 🎨 Visual hint: Two-column split with hairline centre divider. LEFT (muted/grey): WITHOUT — solution before problem, brief as truth, invisible assumptions, expensive late pivots. RIGHT (--sienna fill): WITH — decisions grounded in evidence, assumptions surfaced early, fewer surprises at launch. Column labels bold: "WITHOUT DESIGN PROCESS" / "WITH DESIGN PROCESS".

---

## 4. The Framework

---

### PROCESS — The 5-Stage Cycle
- Kicker: The Framework
- Title: The 5-Stage Cycle
- 5 stages (horizontal pipeline cards):
  1. **EMPATHISE** — What is actually going on with users, not what we assume?
  2. **DEFINE** — What is the real problem worth solving?
  3. **IDEATE** — What are all the possible ways to solve it?
  4. **PROTOTYPE** — What is the fastest way to make this testable?
  5. **TEST** — Were we right? What do we need to change?
- Footer note: *Non-linear: move freely between stages as insights emerge*
- 🎨 Visual hint: Five bordered cards in a horizontal row, numbered 01–05. Stage name bold. Question text below in muted body type. Arrows connecting cards.

---

### STATEMENT — The pattern most teams follow
- Kicker: The reality
- Title: Most teams skip\nstages 1 and 2.
- Lead: Empathise and Define aren't skipped because designers don't know them. They're skipped because nobody asked for them. The brief arrives. The team starts at Ideate. The problem was never validated.
- Key quote: *"A brief is not a problem definition."*
- 🎨 Visual hint: Same 5-card pipeline. Cards 01 (EMPATHISE) and 02 (DEFINE) visually faded/greyed out. Card 03 (IDEATE) highlighted in --sienna with label: "← teams start here". Cards 04 and 05 normal. Quote in large italic below the pipeline.

---

### NUMBERED — What good process looks like
- Kicker: The right path
- Title: Five stages.\nFive outputs.
- 5 numbered items:
  1. **Understand users first** — Research Brief · Interviews · Assumption Map
  2. **Frame the real problem** — Insight statements · Problem statement · JTBD
  3. **Organise for users** — Evidence-based sitemap · Task flows
  4. **Build to answer questions** — Wireframes · Prototype · Decision Log
  5. **Find out if you were right** — Test synthesis · Iterated prototype
- 🎨 Visual hint: 5 cards in a 2+3 grid. Each card has a numbered circle (--sienna), bold heading, italic output list below.

---

## 5. Stage 1 — Empathise

---

### STATEMENT — Stage intro
- Kicker: Stage 1
- Title: EMPATHISE
- 🎨 Visual hint: Full-bleed --ochre background. "Stage 1" in small muted body text bottom-left. "EMPATHISE" in large bold display type. No other content.

---

### DIAGRAM — Empathise modes
- Kicker: Before any solution thinking
- Title: Understand people —\nnot just their *actions.*
- Lead: Four modes of empathic research: Observe, Interview, Immerse, Engage. These work together — not as a checklist.
- 🎨 Visual hint: Four overlapping circles (soft pastel fills). Labels: Observe · Interview · Immerse · Engage. Overlapping areas suggest these modes compound.

---

### NUMBERED — Discovery Activities
- Kicker: Stage 1 · Discovery
- Title: Discovery Activities
- Lead: Understand users, their context, and their real experience before any solution thinking begins.
- 6 activities in 2-column grid:
  - **Desk research** — Competitor review, market reports, analytics. Done before primary research.
  - **User survey** — Quantitative snapshot. Supplement interviews, don't replace them.
  - **User interviews** — Open questions, probing techniques.
  - **Shadowing / observation** — Observe without interfering. Surface workarounds users don't mention.
  - **Stakeholder interviews** — Business context and constraints. Not a substitute for user research.
  - **Support ticket / NPS analysis** — Mine for patterns before talking to users directly.
- 🎨 Visual hint: 2×3 grid of cards (blue-tinted). Each card has a small icon placeholder, bold activity name, 1-sentence description.

---

### NUMBERED — Synthesis Activities
- Kicker: Stage 1 · Synthesis
- Title: Synthesis Activities
- Lead: Turn raw observations into a clear picture.
- 3 activities:
  - **Empathy mapping** — SAY / THINK / DO / FEEL. Forces distinction between observation and inference.
  - **Assumption Map** — Move entries from Unknown to Confirmed or Unconfirmed. Surface what the team believes without evidence.
  - **Research Log update** — Add an entry after every user conversation: quote, behaviour, context.
- 🎨 Visual hint: 3 cards in a row (lavender tint). Each card with a small diagram: Empathy Map 2×2, Assumption Map 2-column table, Research Log as rows.

---

## 6. Stage 2 — Define

---

### STATEMENT — Stage intro
- Kicker: Stage 2
- Title: DEFINE
- Lead: What is the real problem worth solving?
- 🎨 Visual hint: Full-bleed --ochre background. "Stage 2" small text bottom-left. "DEFINE" large bold display. Sub-question in body type.

---

### NUMBERED — Define Activities
- Kicker: Stage 2 · Define
- Title: Define Activities
- Lead: Turn raw research into a clear, validated problem statement the whole team can align on and design against.
- 4 activities in 2×2 grid:
  - **Lean UX Canvas** — Problem, user, solution hypothesis, metrics, assumptions in one view.
  - **Jobs-to-Be-Done mapping** — Functional, emotional, and social jobs. Most design misses emotional and social.
  - **How Might We (HMW)** — Convert each insight into a design opportunity. Not too broad, not too narrow.
  - **Current-state journey mapping** — Map the experience as it actually is, not as it should be.
- 🎨 Visual hint: 2×2 grid of cards (green-tinted). Each card with small icon (canvas grid, concentric ovals for JTBD, HMW? bold text, dotted journey line) + name + 1-sentence description.

---

## 7. Stages 3–5 Overview

---

### STATEMENT — Stage intro (Ideate)
- Kicker: Stage 3
- Title: IDEATE
- 🎨 Visual hint: Full-bleed --ochre background. Stage number and title only.

---

### NUMBERED — Ideate: Generate Activities
- Kicker: Stage 3 · Generate
- Title: Generate Activities
- Lead: Explore as many possible solutions as possible before committing to one. Quantity first, quality later.
- 4 activities:
  - **Crazy 8s** — 8 sketches in 8 minutes. Forces volume, kills perfectionism.
  - **HMW ideation** — Generate 5–10 ideas per HMW question. The question is the useful constraint.
  - **Brainwriting** — Silent, parallel idea generation. Prevents loudest-voice bias.
  - **Ideate Workshop** — Crazy 8s + HMW back-to-back = 50+ ideas to dot-vote from.
- 🎨 Visual hint: 4 cards in a row (warm cream tint). Equation layout below: Crazy 8s + HMW + Brainwriting = Ideate Workshop.

---

### NUMBERED — Ideate: Select Activities
- Kicker: Stage 3 · Select
- Title: Select Activities
- Lead: After exploring multiple directions — choose based on evidence.
- 4 activities:
  - **Impact vs effort matrix** — Plot by user value vs build cost. Top-left quadrant first.
  - **Concept sketching** — Develop top 2–3 directions into fuller sketches with a narrative.
  - **Storyboarding** — Narrative of how the concept plays out in the user's real context.
  - **Proposed process map** — Map the experience as it should feel after the solution is built.
- 🎨 Visual hint: 4 cards in a row (pink/coral tint). Small icons: 2×2 matrix, pencil sketch, storyboard frames, upward arc line.

---

### STATEMENT — Stage intro (Prototype)
- Kicker: Stage 4
- Title: PROTOTYPE
- 🎨 Visual hint: Full-bleed --ochre background. Stage number and title only.

---

### NUMBERED — Prototype Activities
- Kicker: Stage 4 · Build fast
- Title: Prototype Activities
- Lead: The fastest way to make an idea testable. Not a product — an argument.
- 3 activities:
  - **Wireframes** — Structural layout. No colour, no brand, no distraction.
  - **Interactive prototype** — States, transitions, navigation. Cover default, loading, empty, error, success states.
  - **POC (Proof of Concept)** — Answers one question: does this idea work? Keep it rough and fast.
- 🎨 Visual hint: 3 cards in a row (orange/peach tint). Small icons: wireframe layout, prototype with cycle arrow, POC with question mark.

---

### STATEMENT — Stage intro (Test)
- Kicker: Stage 5
- Title: TEST
- 🎨 Visual hint: Full-bleed --ochre background. Stage number and title only.

---

### NUMBERED — Test Activities
- Kicker: Stage 5 · Find out
- Title: Testing Session
- Lead: Find out if the design solves the problem — and change what doesn't based on evidence.
- 4 activities:
  - **Internal feedback session** — "I noticed / I wonder / What if." Documents decisions before shipping.
  - **Concept testing** — Show concept to 3 users. Measure comprehension before building.
  - **Moderated / Unmoderated usability testing** — Think-aloud protocol. 5 users reveals ~85% of critical issues.
  - **A/B testing** — Compares two live versions. Answers "which is better?" not "why?"
- 🎨 Visual hint: 4 cards in a row (lavender tint). Icons: feedback speech bubble, question mark circle, eye/observer icon, A|B blocks.

---

## 8. Activity + Assignments + Close

---

### MILESTONE — Draft Your Design Process
- Kicker: Activity · Your turn
- Num: 10
- Title: Minutes
- Sub: Open the shared board. Use your real project. For each stage, write 1 activity and 1 output. Come back with one stage you're confident about — and one where you're stuck.

---

### PRACTICE — AI in Practice
- Kicker: AI in Practice
- Title: Draft your\nDesign Process
- Lead: Use your real project. One step at a time.
- 5-column grid: EMPATHISE · DEFINE · IDEATE · PROTOTYPE · TEST — with blank activity and output rows under each
- AI prompt box: *"I'm a UX designer working on [project description]. My users are [who they are]. For each Design Thinking stage, suggest: 1 key activity, 1 output to produce, 1 sign I'm ready to move forward, and the biggest risk if I skip this stage."*
- 🎨 Visual hint: 5-column table with stage headers as coloured pills. 2 blank rows under each (Activity / Output). AI prompt in dark card below, monospace text.

---

### PRACTICE — Assignments 1 + 2
- Kicker: Before next session
- Title: Set up + document
- Assignment 1 — Set Up Your Design Process:
  - Choose a real project
  - Add at least 1 activity + 1 output per Design Thinking stage
  - Set up in your project management tool
  - Share and agree on a workspace with your team
- Assignment 2 — Complete the Design Brief:
  - Open your Design Brief in Notion
  - Draft your Problem Statement (3 versions using the AI prompt)
  - Describe your primary user in 2–3 sentences
  - List 3 design goals + any known constraints
  - Update after your stakeholder interview
- 🎨 Visual hint: Two-column split. Assignment 1 left, Assignment 2 right. Numbered steps, clean list layout.

---

### PRACTICE — Assignments 3 + 4
- Kicker: Before next session
- Title: Capture + interview
- Assignment 3 — Capture Current Screens:
  - Identify key experiences (Onboarding, Core Task, Checkout, Settings)
  - Screenshot each screen — label each state
  - Arrange in a screen flow layout
  - We'll use these for friction analysis in Session 2
- Assignment 4 — Run a Stakeholder Interview:
  - Prepare a 5–8 question script
  - Focus on: user experience, pain points, constraints, success criteria
  - Record notes immediately after
  - Update your design brief from what you learned
- 🎨 Visual hint: Two-column split. Assignment 3 left, Assignment 4 right. Clean numbered steps.

---

### END — Closing
- Kicker: One thing to carry forward
- Title: "Design Thinking\nis not a checklist.\nIt's a *habit.*"
- Lead: Start with empathy. Define the real problem. Generate before you judge. Build to learn. Test before you ship.
- Sign: — Winnie Nguyen
