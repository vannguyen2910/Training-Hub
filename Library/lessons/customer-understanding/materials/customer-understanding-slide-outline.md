# Slide Deck Outline — Customer Understanding

> **Source of truth:** `customer-understanding-lesson.md`
> All content changes (activities, concepts, examples) must be made there first, then reflected here.
> This file contains only slide-specific concerns: layout types, visual hints, kickers, and structure.

> **How to use this file**
> Paste both this file and `customer-understanding-lesson.md` into your AI tool with the instruction below to generate a new slide deck.

---

## Prompt to use

```
Using the outline in this file, create an HTML slide deck for Customer Understanding.

Follow the rules in _Config/rules/SLIDE_DECK_RULES.md exactly.
Save the file to Library/lessons/customer-understanding/materials/deck.html.

VISUAL DESIGN DIRECTION — apply globally to every slide:
- Prefer diagrams, frameworks, and annotated tables over bullet lists.
- Use inline SVG for all diagrams. Clean, flat shapes using only token colours.
- For friction type diagrams, use 3 overlapping circles with labels (cognitive, interaction, emotional).
- For the Assumption Map, draw a 2×2 matrix with quadrant labels and example sticky notes.
- For the chain diagram (assumption → research question → interview questions), draw a horizontal left-to-right pipeline with labelled nodes.
- For the interview fundamentals, use 5 numbered cards in a horizontal row.
- Activity / milestone slides feel like full-bleed moments — kicker, time, title, prompt only.
- Part intro slides use a solid --sienna full-bleed background with part number and name only.
- Every slide should have one dominant visual element.
- Avoid centred bullet lists — use .numbered or .process layouts with visual numbering.
```

---

## Session metadata

| Field | Value |
|---|---|
| Session title | Customer Understanding |
| Session number | Session 2 |
| Instructor | Winnie Nguyen |
| Program | UX Class |
| Year | 2026 |
| Previous session | Design Thinking for UX Designer |
| Next session | — |
| Cover photo | Person listening intently in a conversation — notebook open, warm human feel |

---

## Slide structure

> **90-minute version — 29 slides.**
> Arc: Mindset shift → Friction Metrics → Assumptions → Research Questions → User Interview → Assignments.

---

## 1. Introduction

---

### COVER
- Year: 2026
- Day label: Session 2
- Title: Customer\n*Understanding*
- Subtitle: From assumptions to evidence — talk to real people before you design
- Author: Winnie Nguyen
- Right panel photo: Person in conversation — notebook open, leaning forward, listening. Warm, human, research-focused.

---

### DIAGRAM — Agenda
- Kicker: What we're building today
- Title: Five parts.\nOne capability.
- 5 agenda items:
  1. **Friction metric** — Where do users struggle?
  2. **Assumptions** — Surface what you believe
  3. **Research questions** — Define what to learn
  4. **User interview** — Go talk with real people
  5. **Synthesis** — Make sense of findings
- 🎨 Visual hint: 5 numbered cards in a vertical or horizontal list. Each card has a number circle (--sienna), bold part name, italic sub-description. Clean, scannable.

---

## 2. Mindset

---

### STATEMENT — Mindset shift
- Kicker: Before we start
- Title: You are not\n*your user.*
- Lead: You've read the brief. You know the product. You may have years of industry experience. None of that makes you a reliable proxy for the people who use the product. The gap between what you assume and what users actually experience is where the most important design insights live.
- 🎨 Visual hint: Two panels side-by-side. LEFT: designer's face/silhouette (--sienna tint, confident posture). RIGHT: user's face/silhouette (--ochre tint, different context). Large ≠ symbol between them in --ink. Simple, bold.

---

## 3. Part 1 — Friction Metrics

---

### STATEMENT — Part intro
- Kicker: Part 1
- Title: FRICTION METRICS
- 🎨 Visual hint: Full-bleed --sienna background. "Part 1" small muted text bottom-left. "FRICTION METRICS" in large bold display type. No other content.

---

### DIAGRAM — What is friction?
- Kicker: Define the problem
- Title: Friction is the\n*cost of using* your product.
- Lead: Three types of friction — cognitive, interaction, and emotional. Each type reveals a different kind of failure in the experience.
- 3 friction types:
  - **Cognitive friction** — Mental effort to understand or decide. Spotted when: users pause, re-read, or choose wrong on first attempt.
  - **Interaction friction** — Physical effort to complete an action. Spotted when: users tap wrong, re-enter data, or abandon mid-flow.
  - **Emotional friction** — Anxiety, confusion, or frustration. Spotted when: users hesitate, express doubt, or give up and call support.
- 🎨 Visual hint: Three overlapping circles (Venn diagram style). Labels: Cognitive (blue-tinted) · Interaction (orange-tinted) · Emotional (pink-tinted). Below each circle: one bullet for how to spot it. Overlapping areas show that friction types compound.

---

### NUMBERED — When / Why / How
- Kicker: Part 1 · Framework
- Title: Run a friction analysis\nbefore any redesign.
- When: At the start of any project involving an existing product, before any major redesign.
- Why: Makes the invisible visible. Every team member has an opinion — a friction analysis makes those opinions testable. Creates a baseline to measure improvement.
- How — two steps:
  - **Step 1:** Analyse the current experience (friction analysis table: screen / user action / friction type / detail / severity 1–5)
  - **Step 2:** Map the proposed experience against the same steps — which frictions does your design reduce?
- 🎨 Visual hint: Three cards in a row (When · Why · How). Each card with an icon placeholder and 2–3 lines of explanation. Below: small table preview showing column headers for both friction tables.

---

### DIAGRAM — Friction Analysis: Current Experience
- Kicker: Part 1 · Current state
- Title: Where does the\ncurrent experience\n*fail users?*
- Table (current experience):
  - Headers: Screen or step | User action | Friction type | Friction detail | Severity (1–5)
  - Row 1: Login screen | Enter credentials | Cognitive | Two-factor auth flow is unclear — users don't know what to expect next | 3
  - Row 2: Application form step 3 | Upload document | Interaction | File format requirements not shown until after upload fails | 4
  - Row 3: Confirmation screen | Review and submit | Emotional | No indication of what happens after submission — no timeline, no contact option | 5
- 🎨 Visual hint: Clean table with styled headers (--sienna header row, alternating --paper / --ink-ghost rows). Severity shown as coloured dots: 1–2 green, 3 yellow, 4–5 red. Compact but readable.

---

### DIAGRAM — Friction Analysis: Proposed Experience
- Kicker: Part 1 · Proposed state
- Title: Does your design\nactually *reduce* friction?
- Table (proposed experience):
  - Headers: Screen or step | User action | Proposed change | Friction type reduced | Notes
  - Row 1: Login screen | Enter credentials | Added inline explanation of 2FA steps | Cognitive | Eliminates the "what just happened?" moment
  - Row 2: Application form step 3 | Upload document | Show format requirements before upload field | Interaction | Reduces failed attempts and re-uploads
- Key point below table: This is the test. If your redesign doesn't reduce friction in the current state — you need to ask why.
- 🎨 Visual hint: Same table style as current experience table. Proposed change column in --sage tint (green, positive). Notes column in --ink-muted italic.

---

### STATEMENT — NAB case study
- Kicker: Real case
- Title: 27 taps.\n*60% friction reduction.*
- Lead: A home loan application at NAB's prior experience involved 27 separate taps to complete a single interaction model. A friction analysis of the current state identified the specific interaction frictions at each step. The redesigned flow reduced friction at those points — resulting in a 60% measurable reduction. The improvement didn't come from visual redesign. It came from mapping friction systematically and removing it step by step.
- 🎨 Visual hint: Two panels. LEFT: a row of 27 small numbered circles (--ink, small, dense — the "27 taps" visualised). RIGHT: the same row, but with ~17 circles highlighted in --sienna and the rest faded — showing 60% reduction. Label: "Before → After". Clean, dramatic.

---

### MILESTONE — A Simple Friction Review
- Kicker: Activity · Part 1
- Num: 10
- Title: Minutes
- Sub: Open your screen flows. Choose one key flow. For each step, add a sticky: 🟡 Cognitive, 🔴 Interaction, or 🔵 Emotional. Write each sticky as: "[User action] causes [friction type] because [specific issue]." Share back your highest-severity friction point.

---

## 4. Part 2 — Assumptions

---

### STATEMENT — Part intro
- Kicker: Part 2
- Title: ASSUMPTIONS
- 🎨 Visual hint: Full-bleed --sienna background. "Part 2" small muted text bottom-left. "ASSUMPTIONS" in large bold display type. No other content.

---

### NUMBERED — What is an assumption?
- Kicker: Part 2 · Types
- Title: Four types of\nassumptions.
- Lead: Assumptions are everything your team believes without evidence. There are four types — and each one carries a different kind of risk if it's wrong.
- 4 types in 2×2 grid:
  - **User** — Who they are, what they care about, how they behave. *Example: "Users check this feature at least once a week."*
  - **Problem** — The nature, severity, and prevalence of the problem. *Example: "Users struggle because there are too many options."*
  - **Solution** — Whether the proposed fix actually addresses the problem. *Example: "A comparison table will help users choose faster."*
  - **Business** — Market viability, pricing, regulatory factors. *Example: "Users will pay for this if bundled with the existing plan."*
- 🎨 Visual hint: 2×2 grid of cards. Each card with a coloured icon circle (user outline / problem warning / solution lightbulb / business chart) + bold type label + one italic example. Clean card borders.

---

### STATEMENT — The assumption formula
- Kicker: Part 2 · Write it right
- Title: Write assumptions\nyou can *actually test.*
- Lead: Every assumption should be written in this format — so it becomes a hypothesis, not an opinion.
- Formula callout: *"We believe [WHO] will [WHAT] because [WHY]. We'll know we're right when [SIGNAL]."*
- Weak vs strong example:
  - WEAK: "We think users want a faster checkout."
  - STRONG: "We believe returning customers will use one-click checkout in over 40% of sessions because reducing checkout steps was the top complaint in last quarter's NPS. We'll know when post-launch checkout completion exceeds 80%."
- 🎨 Visual hint: Two cards stacked vertically. WEAK card: muted/grey, cross icon, single short line of text. STRONG card: --sienna border, checkmark icon, full formatted assumption with [WHO] [WHAT] [WHY] [SIGNAL] labelled as inline annotations. The contrast should be visual and obvious.

---

### DIAGRAM — The Assumption Map
- Kicker: Part 2 · Prioritise
- Title: Not all assumptions\nare equal.
- Lead: The Assumption Map places assumptions on a 2×2 grid: importance vs evidence. The top-left quadrant — high importance, low evidence — is where you start.
- Quadrant labels:
  - Top-left: **TEST FIRST** — High importance · Low evidence. These matter most and you know the least.
  - Top-right: **PROCEED** — High importance · High evidence. Validated. Continue with confidence.
  - Bottom-left: **MONITOR** — Low importance · Low evidence. May not be worth testing yet.
  - Bottom-right: **FILE** — Low importance · High evidence. Known and low-risk.
- 🎨 Visual hint: Clean 2×2 matrix SVG. Y-axis: IMPORTANCE (low → high). X-axis: EVIDENCE (low → high). Each quadrant labelled with action word + description. Top-left quadrant in --sienna tint with a "START HERE" indicator arrow. Faint sticky note icons placed in each quadrant.

---

### NUMBERED — When to run an Assumption Map
- Kicker: Part 2 · When
- Title: Five moments to\nrun it.
- 5 occasions:
  1. At the start of a new project — before any research begins
  2. When the team is stuck and disagreeing about direction
  3. When a stakeholder changes the brief
  4. When a prototype test produces unexpected results
  5. After any major research synthesis session
- 🎨 Visual hint: 5 numbered cards in a vertical list (left-to-right alternating layout, or clean numbered column). Each card with number circle (--sienna) + occasion title + 1-line description.

---

### MILESTONE — Create Assumptions with AI
- Kicker: Activity · Part 2
- Num: 10
- Title: Minutes
- Sub: Paste your project into your AI tool. Generate 10 assumptions across all 4 types using the formula. Place 4–5 on your Assumption Map. Share back: which assumption is top-left — high stakes, unproven?

---

## 5. Part 3 — Research Questions

---

### STATEMENT — Part intro
- Kicker: Part 3
- Title: RESEARCH QUESTIONS
- 🎨 Visual hint: Full-bleed --sienna background. "Part 3" small muted text bottom-left. "RESEARCH QUESTIONS" in large bold display type. No other content.

---

### DIAGRAM — The chain: assumption → interview
- Kicker: Part 3 · The method
- Title: From assumption\nto interview guide.
- Lead: A research question bridges your assumption and your interview. It defines what you need to learn. Interview questions are the prompts you use to find the answer.
- Chain diagram (3 nodes, left to right):
  - Node 1: **ASSUMPTION** — "We believe returning users will abandon the checkout when asked for 2FA because it interrupts the flow."
  - Node 2: **RESEARCH QUESTION** — "How do users experience authentication steps during time-sensitive purchases?"
  - Node 3: **INTERVIEW QUESTIONS** — "Tell me about a time you tried to buy something quickly online. What made you continue or stop?" / "How did you feel when you hit a verification step mid-checkout?"
- 🎨 Visual hint: Horizontal pipeline. Three boxes connected by arrows. Left box: muted/assumption colour. Centre box: --ochre tint. Right box: --sienna tint with multiple sub-lines showing the 2 interview questions. Node labels above each box.

---

### NUMBERED — Good vs bad research questions
- Kicker: Part 3 · What works
- Title: Research questions\nare not feedback forms.
- Lead: Good research questions investigate reality. Bad ones fish for validation.
- Bad examples (3 cards, muted/red cross):
  - "What do users think of our new checkout redesign?" — Feedback-fishing, not research.
  - "Do users prefer the current or proposed navigation?" — Preference testing, not understanding.
  - "Would users use a feature that lets them do X?" — Hypothetical behaviour produces unreliable answers.
- Good examples (3 cards, --sienna/green check):
  - "How do users currently manage [specific task] without our product?"
  - "What causes users to stop mid-flow in a checkout process?"
  - "What information do users look for before committing to a plan?"
- 🎨 Visual hint: Two columns. LEFT: BAD (muted headers, red ✕ icon, italic text). RIGHT: GOOD (--sienna headers, green ✓ icon). Clean contrast. Column divider hairline.

---

### STATEMENT — Urban Farming case study
- Kicker: Real case
- Title: The answer wasn't\nwhat we expected.
- Lead: A team researching urban farming assumed the main barrier was space and equipment cost. Their research question: "What prevents people interested in urban farming from getting started?" After interviewing 6 participants, the real barrier was knowledge and confidence — not cost or space at all. The product direction changed entirely because the research question was open enough to capture the real answer.
- Key takeaway: *If your research question already contains your solution — you've skipped the learning.*
- 🎨 Visual hint: Two thought-bubble panels side-by-side. LEFT: "We assumed..." with small icons for money and space (cost/constraint imagery). RIGHT: "Users said..." with a speech bubble and knowledge/confidence icons. Bold "≠" between them. Caption: "The research question was open enough to catch the truth."

---

### MILESTONE — Prepare Research Questions
- Kicker: Activity · Part 3
- Num: 10
- Title: Minutes
- Sub: Take your top-left assumption. Write one research question (neutral, no solution language). Use your AI tool to generate 8 open-ended interview questions. Cut to 5–6 strong ones. Come back with your research question and your best 3 interview questions.

---

## 6. Part 4 — User Interview

---

### STATEMENT — Part intro
- Kicker: Part 4
- Title: USER INTERVIEW
- 🎨 Visual hint: Full-bleed --sienna background. "Part 4" small muted text bottom-left. "USER INTERVIEW" in large bold display type. No other content.

---

### NUMBERED — Interview Fundamentals
- Kicker: Part 4 · Five behaviours
- Title: Five fundamentals.
- Lead: These behaviours separate interviews that generate insight from interviews that confirm what you already think.
- 5 fundamentals (numbered cards in a row):
  1. **Ask open questions** — "Tell me about a time when..." invites stories. Closed questions invite yes/no. Open questions are always more useful.
  2. **Follow the story** — When something unexpected comes up, follow it — even if it's off-script. The most important insights usually arrive unannounced.
  3. **Stay curious** — Approach every answer as though you've never heard this situation before. Users can tell whether you're genuinely interested.
  4. **Listen more than you speak** — If you're talking more than 20% of the time, something is wrong. Silence is productive.
  5. **Observe, don't just hear** — A 5-second pause before pressing a button is data. Watch what users do as well as what they say.
- 🎨 Visual hint: 5 numbered cards in a horizontal row. Each card has a large number (--sienna circle), bold principle title, 2-line description below.

---

### STATEMENT — The golden rule
- Kicker: Part 4 · Remember this
- Title: "The goal is not to\nvalidate your ideas.\nIt's to understand\n*their reality.*"
- Lead: The moment you start presenting your solution or asking "would you use this?" — you've stopped doing user research. Stay curious. Stay neutral. Let users surprise you.
- 🎨 Visual hint: Dark --ink full-bleed background. Large bold italic quote in --ochre display type. Attribution line in small white body type below: *"— User interview golden rule"*

---

### NUMBERED — How AI helps at this stage
- Kicker: Part 4 · AI in Practice
- Title: AI accelerates four\npreparation tasks.
- Lead: AI tools are useful for the preparation phase — not the interview itself.
- 4 tasks:
  1. **Generate assumptions from a brief** — Paste your brief, ask for assumptions across all 4 types. Review critically.
  2. **Write assumption statements** — Use the formula as a prompt template. AI generates structure; you judge importance.
  3. **Draft interview questions** — Give AI your research question, ask for 8–10 open-ended questions. Expect to cut half.
  4. **Synthesise notes after interviews** — Paste notes, ask for themes. Useful first pass — always return to raw notes.
- Limit note: *AI cannot assess which assumptions matter most for your specific project, evaluate whether a question is leading in your context, or replace the judgment that comes from sitting with a real user.*
- 🎨 Visual hint: 4 cards in a 2×2 grid (--sage tint). Each card with a task number, bold heading, 1–2 line description. Below the grid: a "limit" card in muted --ink-ghost with the limitation statement in italic.

---

## 7. Assignments + Close

---

### PRACTICE — Assignment 1: User Interview
- Kicker: Assignment 1
- Title: Conduct a\nUser Interview
- Steps before:
  - Choose a real user — not a friend or colleague who knows your project
  - Use your prepared research + interview questions as your guide
  - Brief the participant and get consent to record
  - Set up a timestamped notes document
- Steps during:
  - Open with a warm-up question about their role and context
  - Ask your prepared questions — follow anything surprising
  - End with: "Is there anything I didn't ask that would be helpful to know?"
- Steps after:
  - Write up notes within 2 hours
  - Identify your 3 most surprising findings
  - Note which assumptions were confirmed, refuted, or need more data
- Deliverable: Notes document + reflection paragraph. Share before next session.
- 🎨 Visual hint: Three columns (Before / During / After) with numbered steps in each. Clean dividers. --sienna accent on "Deliverable" label at bottom.

---

### PRACTICE — Assignment 2: Assumption Mapping
- Kicker: Assignment 2
- Title: Build Your\nAssumption Map
- Steps:
  - List at least 10 assumptions across all 4 types using the formula
  - Place each on the Assumption Map (importance vs evidence)
  - Add a confidence level: Unproven / Partially validated / Validated
  - Identify the 3 assumptions you most need to test
  - Write one research question for each of those 3
  - After your interview — update confidence levels based on what you learned
- AI prompt: *"I'm a UX designer working on [project]. Generate 10 assumptions across all four types. For each one, suggest: 1 research question, and whether desk research, a user interview, or analytics would be the best way to answer it."*
- Deliverable: FigJam or Miro link. Come ready to discuss.
- 🎨 Visual hint: Numbered steps list on left. Assumption Map 2×2 thumbnail on right (preview of completed deliverable). AI prompt in dark card below.

---

### END — Closing
- Kicker: One thing to carry forward
- Title: "The most important\nthing you can do\nfor your design —\nis *talk to a real user.*"
- Lead: Friction metrics tell you where to look. Assumptions tell you what you believe. Research questions tell you what to ask. The interview is where the evidence lives.
- Sign: — Winnie Nguyen
