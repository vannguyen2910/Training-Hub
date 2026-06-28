# Slide Deck Outline — Solution Validation & User Testing

> **Source of truth:** `solution-validation-user-testing-lesson.md`
> All content changes (activities, phases, timing, concepts) must be made there first, then reflected here.
> This file contains only slide-specific concerns: layout types, visual hints, kickers, and structure.

> **How to use this file**
> Paste both this file and `solution-validation-user-testing-lesson.md` into your AI tool with the instruction below to generate a new slide deck.

---

## Prompt to use

```
Using the outline in this file, create an HTML slide deck for Solution Validation & User Testing.

Follow the rules in _Config/rules/SLIDE_DECK_RULES.md exactly.
Save the file to Library/lessons/solution-validation-user-testing/materials/deck.html.

VISUAL DESIGN DIRECTION — apply globally to every slide:
- Prefer diagrams, frameworks, and tables over bullet lists.
- Use inline SVG for all diagrams. Clean, flat shapes using only token colours.
- For the testing spectrum table, use a horizontal gradient bar from low effort (--sage) to high rigour (--sienna), with method labels above.
- For the Feedback Capture Grid, draw a 2×2 quadrant with Likes / Criticisms / Questions / Ideas labels.
- For the severity matrix, draw a 2×2 grid with Impact on Y-axis and Frequency on X-axis, with dot examples placed in quadrants.
- For the importance × feasibility matrix, draw the same 2×2 with Fix Now / Plan / Quick Win / Defer labels.
- Activity / milestone slides feel like full-bleed moments — kicker, time, title, prompt only.
- Part intro slides use a solid --sienna full-bleed background with part number and name only.
- Every slide should have one dominant visual element.
- Avoid centred bullet lists — use .numbered or .process layouts with visual numbering.
```

---

## Session metadata

| Field | Value |
|---|---|
| Session title | Solution Validation & User Testing |
| Session number | Session 7 |
| Instructor | Winnie Nguyen |
| Program | UX Class |
| Year | 2026 |
| Previous session | Build the Pattern First (AI Prototype Development) |
| Next session | Reflection & Next Steps |
| Cover photo | Designer watching a user interact with a prototype on screen — observer in background, warm focused atmosphere |

---

## Slide structure

> **90-minute version — 28 slides.**
> Arc: Validation mindset → Method selection → Test planning (with AI) → Facilitation → Synthesis → Assignments.

---

## 1. Introduction

---

### COVER
- Year: 2026
- Day label: Session 7
- Title: Solution Validation\n*& User Testing*
- Subtitle: Your prototype is a hypothesis. Testing is how you find out if it's right.
- Author: Winnie Nguyen
- Right panel photo: Designer observing a user testing session — warm, focused, research mood.

---

### DIAGRAM — Agenda
- Kicker: What we're covering today
- Title: Five phases.\nOne loop closed.
- 5 agenda items:
  1. **Validation mindset** — What are you actually testing for?
  2. **Choose your method** — Right tool for the right question
  3. **Write your test plan** — Goals, tasks, scenarios, criteria
  4. **Run the session** — Facilitation and think-aloud
  5. **Synthesise & prioritise** — From observations to decisions
- 🎨 Visual hint: 5 numbered cards in a horizontal or vertical list. Each card has a number circle (--sienna), bold phase name, italic sub-description. Clean, scannable.

---

## 2. Validation Mindset

---

### STATEMENT — Part intro
- Kicker: Part 1
- Title: VALIDATION MINDSET
- 🎨 Visual hint: Full-bleed --sienna background. "Part 1" small muted text bottom-left. "VALIDATION MINDSET" in large bold display type. No other content.

---

### STATEMENT — The prototype is a hypothesis
- Kicker: Before we test
- Title: A prototype is not\na deliverable.\n*It's a hypothesis.*
- Lead: Showing people your prototype and asking "what do you think?" produces opinions. Testing starts with a question — and lets evidence answer it. The difference is the difference between guessing and knowing.
- Formula callout: *"We believe [this design] will help [this user] do [this task] because [reason]. We'll know we're right when [signal]."*
- 🎨 Visual hint: Two panels. LEFT: speech bubble with "What do you think?" — muted, grey, labelled "Opinion". RIGHT: clipboard with hypothesis formula — --sienna tint, labelled "Evidence". Bold ≠ symbol between them.

---

### DIAGRAM — What are you testing?
- Kicker: Part 1 · Three questions
- Title: Different questions\nneed different tests.
- Lead: Identify which question your prototype needs to answer before designing the test.
- 3 cards:
  - **Usability** — Can users complete the task? Where do they get stuck? → Moderated task-based test
  - **Desirability** — Do users want what this offers? Does it feel right? → Concept test or post-task debrief
  - **Comprehension** — Do users understand what this is and what to do? → Five-second test or think-aloud on lo-fi
- 🎨 Visual hint: 3 cards in a row. Each card: icon (task checklist / heart / lightbulb), bold label, one-line description, arrow pointing to recommended method. Cards in --paper with --sienna icon circles.

---

### STATEMENT — Real case
- Kicker: Real case · Go1
- Title: 48 hours.\nReal users.\n*Before a line of code.*
- Lead: At Go1, the team used Maze (unmoderated testing tool) and Intercom (customer platform) to validate a solution with real customers in 48 hours. They defined the happy path → published a Maze link → filtered a customer segment in Intercom → analysed drop-off before building anything. This isn't a replacement for moderated testing. It's proof that validation doesn't require a lab or a long recruitment process — just a clear question and access to real users.
- 🎨 Visual hint: Simple flow diagram. Three nodes connected by arrows: PROTOTYPE → MAZE LINK → INTERCOM SEGMENT → FINDINGS IN 48H. Each node as a rounded box. Arrow labels: "publish" / "send to segment" / "analyse". Minimal, clean.

---

## 3. Choose Your Method

---

### STATEMENT — Part intro
- Kicker: Part 2
- Title: CHOOSE YOUR METHOD
- 🎨 Visual hint: Full-bleed --sienna background. "Part 2" small muted text bottom-left. "CHOOSE YOUR METHOD" in large bold display type.

---

### DIAGRAM — Testing spectrum
- Kicker: Part 2 · The spectrum
- Title: Right method for\nthe right question.
- Lead: No single method is best. The right one depends on what you're trying to learn and how much time you have.
- Table:
  - Headers: Method | What it answers | Fidelity needed | Effort
  - Row 1: Hallway test | Does this make sense at a glance? | Low-fi | Very low
  - Row 2: Five-second test | First impression + what users remember | Any | Low
  - Row 3: Moderated usability test | Can users complete tasks? Where do they struggle? | Mid–high-fi | Medium
  - Row 4: Unmoderated test (Maze, Lyssna) | Task completion + drop-off at scale | Mid–high-fi | Low–medium
  - Row 5: Concept test | Do users understand and want this idea? | Low-fi or none | Low
  - Row 6: A/B test | Which version performs better? | Live product | High
- 🎨 Visual hint: Clean table, styled headers (--sienna). Rows 3–4 highlighted in --ochre tint (most relevant at prototype stage). "Most relevant now" label beside highlighted rows.

---

### DIAGRAM — Moderated vs Unmoderated
- Kicker: Part 2 · Key decision
- Title: Why vs What.
- Lead: The choice between moderated and unmoderated comes down to one question.
- Two panels side by side:
  - LEFT — MODERATED: Gives you the *why*. You observe, follow up, probe. Slower. Requires scheduling. Best when you need to understand behaviour and motivation.
  - RIGHT — UNMODERATED: Gives you the *what* at scale. Faster, cheaper. Task completion rates, drop-off, click patterns. Best for validating specific flows.
- Note below: *The 5-user rule applies to moderated qualitative testing only. Unmoderated and A/B tests need larger samples.*
- 🎨 Visual hint: Two large cards side by side. LEFT (--sage tint): "WHY" in large display type, sub-description below. RIGHT (--ochre tint): "WHAT" in large display type, sub-description below. Simple, bold contrast.

---

### MILESTONE — Pick Your Method
- Kicker: Activity · Part 2
- Num: 5
- Title: Minutes
- Sub: Look at your prototype. What's the one thing you most want to know? Pick moderated or unmoderated — and write one sentence justifying the choice. Share back.

---

## 4. Write Your Test Plan

---

### STATEMENT — Part intro
- Kicker: Part 3
- Title: WRITE YOUR TEST PLAN
- 🎨 Visual hint: Full-bleed --sienna background. "Part 3" small muted text bottom-left. "WRITE YOUR TEST PLAN" in large bold display type.

---

### NUMBERED — Test plan components
- Kicker: Part 3 · What goes in
- Title: Five components.\nOne page.
- 5 components:
  1. **Goal** — What question does this test answer? One sentence. Link to the hypothesis.
  2. **Participant profile** — Who are you testing with? Key characteristics that matter for this prototype.
  3. **Tasks** — Specific actions participants attempt. Realistic and neutral — no hints.
  4. **Scenarios** — Context that sets up the task without giving away the answer.
  5. **Success criteria** — How will you know the task was completed? Define before the session, not after.
- 🎨 Visual hint: 5 numbered cards in a vertical list, each with number circle (--sienna), bold component name, one-line description + italic example.

---

### DIAGRAM — Good vs bad tasks
- Kicker: Part 3 · Write it right
- Title: Neutral language.\n*No hints.*
- Lead: The difference between a good task and a bad one is neutrality and realism.
- Bad examples (3 rows, red ✗):
  - "Click the Buy Now button to purchase the item." — Gives away where to click.
  - "Would you use this checkout flow?" — Asks for opinion, not behaviour.
  - "Imagine you want to buy something. What would you do?" — Too vague, no context.
- Good examples (3 rows, green ✓):
  - "You've decided to buy a gift for a friend. Show me how you'd complete the purchase."
  - "You need to update your billing address before your next payment. How would you do that?"
  - "You've just joined a new team. Set up your profile so teammates can find you."
- 🎨 Visual hint: Two-column layout. LEFT column: BAD (muted grey, ✗ icon). RIGHT column: GOOD (--sienna tint, ✓ icon). Each task as a short text card. Column divider hairline.

---

### NUMBERED — AI in Practice
- Kicker: Part 3 · AI in Practice
- Title: Generate a test script\nin under 5 minutes.
- Lead: Use an AI tool to draft your test plan, then edit what it gets wrong.
- Prompt card (dark background):
  *"I'm testing a prototype of [product]. The main user flow is: [describe]. Write a test plan with: 1 goal, 1 participant profile, 3 realistic task scenarios with success criteria. Use neutral language — no hints about where to click."*
- Critical thinking checklist:
  - Are the tasks neutral, or do they give away the answer?
  - Did AI understand who the real user is?
  - Are success criteria measurable?
  - What context did AI not have?
- 🎨 Visual hint: Two sections. TOP: dark --ink card with AI prompt in monospace italic. BOTTOM: 4-item checklist with checkbox icons (--sienna). Clean split.

---

### MILESTONE — Write Your Test Plan
- Kicker: Activity · Part 3
- Num: 10
- Title: Minutes
- Sub: Paste your prototype flow into your AI tool. Generate a draft test plan. Edit: cut any leading language, fix success criteria, adjust the participant profile to match your real user. You leave with a test plan you can use this week.

---

## 5. Run the Session

---

### STATEMENT — Part intro
- Kicker: Part 4
- Title: RUN THE SESSION
- 🎨 Visual hint: Full-bleed --sienna background. "Part 4" small muted text bottom-left. "RUN THE SESSION" in large bold display type.

---

### STATEMENT — The moderator's role
- Kicker: Part 4 · Your job
- Title: Watch.\nListen.\n*Don't help.*
- Lead: The moment you help a user who is struggling, you've lost the data. A user who gets stuck is giving you exactly the information you need. The discipline is to resist the instinct to rescue them and instead ask a neutral prompt.
- 3 neutral prompts (callout cards):
  - "What are you thinking right now?"
  - "What would you do next if I weren't here?"
  - "What were you expecting to happen?"
- 🎨 Visual hint: Large statement text on left. Three speech bubble cards on right (--ochre tint) with the neutral prompts in italic. Clean, spacious layout.

---

### NUMBERED — Six facilitation principles
- Kicker: Part 4 · How to run it
- Title: Six principles.
- 6 principles (numbered cards):
  1. **Ask before you show** — Context questions before the prototype. Build rapport and a baseline.
  2. **Test on the right people** — Not colleagues. Real potential users. Consider extreme users.
  3. **Ask, don't tell** — When users ask questions, turn it back. "What would you do if I wasn't here?"
  4. **Stay neutral** — Don't sell the design. Don't explain intent. Let the prototype speak.
  5. **Adapt when needed** — If a task prompt confuses everyone, rephrase. Rigid scripts that produce no data are worse than flexible ones.
  6. **Let users contribute** — When users say "I wish this did X" — ask them to describe it. Their suggestions reveal the underlying need.
- 🎨 Visual hint: 6 cards in a 2×3 grid. Each card: number circle (--sienna), bold principle title, 1–2 line description.

---

### MILESTONE — Live Role-Play
- Kicker: Activity · Part 4
- Num: 10
- Title: Minutes
- Sub: One student moderates. One student plays a participant on a peer's prototype. The group observes and fills in the Feedback Capture Grid in real time. Debrief: what was hard to resist? What did observers catch that the moderator missed?

---

## 6. Synthesise & Prioritise

---

### STATEMENT — Part intro
- Kicker: Part 5
- Title: SYNTHESISE &\nPRIORITISE
- 🎨 Visual hint: Full-bleed --sienna background. "Part 5" small muted text bottom-left. "SYNTHESISE & PRIORITISE" in large bold display type.

---

### DIAGRAM — Feedback Capture Grid
- Kicker: Part 5 · Capture first
- Title: Separate observations\nfrom interpretations.
- Lead: The Feedback Capture Grid organises raw observations into four quadrants. Fill it in during or immediately after the session — before interpretation happens.
- 4 quadrants:
  - TOP LEFT — **Likes ✓** — What worked. What users responded positively to.
  - TOP RIGHT — **Criticisms ✗** — What didn't work. Where users got stuck, confused, or frustrated.
  - BOTTOM LEFT — **Questions ?** — Questions the session raised — from users or from the team.
  - BOTTOM RIGHT — **Ideas 💡** — Ideas the session sparked — from user suggestions or observer insights.
- Key rule below: *In Criticisms: write what the user DID — not what you think it means. "User spent 40 seconds on payment screen without clicking" is an observation. "The payment screen is confusing" is an interpretation. Keep them separate.*
- 🎨 Visual hint: Clean 2×2 grid SVG. Each quadrant with a distinct background tint (--sage / --sienna-light / --paper / --ochre-light). Quadrant label + icon in each corner. Rule note in small italic below the grid.

---

### DIAGRAM — From observation to finding
- Kicker: Part 5 · Translate
- Title: What users did →\n*what it means.*
- Lead: Move from raw observations to findings using this formula.
- Formula: *"[User] did [X]" → "Users struggle to [Y] because [Z]"*
- Example:
  - Observation: "3 of 5 participants tried to tap the logo to go home."
  - Finding: "Users expect the logo to be a home button — the current navigation doesn't have a clear home action."
- 🎨 Visual hint: Two-step pipeline. LEFT box (--paper, observation): raw note in italic. Arrow in --sienna. RIGHT box (--sienna tint, finding): translated finding in bold. Formula label above the arrow.

---

### DIAGRAM — Severity matrix
- Kicker: Part 5 · Prioritise
- Title: Not all issues\nare equal.
- Lead: Prioritise by multiplying impact × frequency. The highest scores go to the top of the fix list.
- 2×2 matrix:
  - Y-axis: IMPACT (low → high)
  - X-axis: FREQUENCY (low → high)
  - TOP RIGHT (high impact + high frequency): Fix immediately — --sienna dot
  - TOP LEFT (high impact + low frequency): Investigate — --ochre dot
  - BOTTOM RIGHT (low impact + high frequency): Polish — --sage dot
  - BOTTOM LEFT (low impact + low frequency): Monitor — --paper/muted dot
- 🎨 Visual hint: SVG 2×2 matrix. Axes labelled. Each quadrant has a label and action word. Coloured dots scattered as examples. Simple, clean.

---

### DIAGRAM — Importance × Feasibility
- Kicker: Part 5 · Triage
- Title: Fix now or\nplan for later?
- Lead: After severity, evaluate what's worth fixing in this iteration.
- 2×2 matrix:
  - Y-axis: IMPORTANCE (low → high)
  - X-axis: FEASIBILITY (low → high)
  - TOP RIGHT: **Fix now** — High importance + high feasibility
  - TOP LEFT: **Plan next sprint** — High importance + low feasibility
  - BOTTOM RIGHT: **Quick win** — Low importance + high feasibility
  - BOTTOM LEFT: **Defer** — Low importance + low feasibility
- 🎨 Visual hint: Same 2×2 style as severity matrix. Each quadrant colour-coded. "Fix now" in --sienna. Labels bold inside each quadrant.

---

## 7. Close the Loop + Assignments

---

### STATEMENT — Iteration loop
- Kicker: The cycle
- Title: Testing doesn't end.\n*It iterates.*
- Lead: The output of a test session is not a final answer — it's a more informed hypothesis. Fix the highest-severity issues, update the prototype, and test again. Two to three rounds of testing will surface most critical issues before anything goes to development.
- Loop diagram: OBSERVE → SYNTHESISE → PRIORITISE → FIX → RETEST → (back to OBSERVE)
- 🎨 Visual hint: Circular loop diagram with 5 nodes connected by curved arrows (--sienna). Each node: rounded rectangle with label. "You are here" indicator on OBSERVE. Clean, minimal.

---

### PRACTICE — Assignment A: Moderated Usability Test
- Kicker: Assignment A
- Title: Run a Moderated\nUsability Test
- Steps Before:
  - Share prototype link or set up the device in advance
  - Brief participant: "I'm testing the design, not you. Say out loud what you're thinking."
  - Have test plan and Feedback Capture Grid ready
- Steps During:
  - Give each task as a scenario — then let them go. Don't help.
  - Take notes in Criticisms and Questions quadrants as you go
  - Use "What are you thinking right now?" when they go quiet
- Steps After:
  - Complete all four quadrants of the Feedback Capture Grid
  - Write 3–5 findings using observation → finding format
  - Prioritise using impact × frequency
  - Identify one change with the biggest effect on usability
- Deliverable: Feedback Capture Grid + 3–5 findings + one priority recommendation. Bring to Session 8.
- 🎨 Visual hint: Three columns (Before / During / After) with numbered steps. --sienna accent on "Deliverable" label at bottom.

---

### PRACTICE — Assignment B: Additional Test (Optional)
- Kicker: Assignment B · Optional
- Title: Go Again — \nDifferent Method
- Steps:
  - Run an additional test using either moderated or unmoderated testing — whichever you didn't use for Assignment A
  - If unmoderated: choose any tool (Maze, Lyssna, recorded Zoom, written survey) and share your test link with what you're trying to learn
  - If moderated: recruit a second participant — compare their session to the first
- 🎨 Visual hint: Two cards side by side. LEFT: "MODERATED" — icon of two people, one line description. RIGHT: "UNMODERATED" — icon of laptop/tool, one line description. Equal weight, no hierarchy. "Choose one" label above.

---

### END — Closing
- Kicker: One thing to carry forward
- Title: "Testing is not\na final step.\nIt's how design\n*earns its decisions.*"
- Lead: The prototype you built is the beginning of the evidence, not the end of the work. Every finding from a test session brings you closer to something that actually works for real people.
- Sign: — Winnie Nguyen
