# Slide Deck Outline — Session 3 · Synthesis & Problem Definition

> **Source of truth:** `Synthesis & Problem Definition.md`
> All content changes (activities, examples, concepts) must be made there first, then reflected here.
> This file contains only slide-specific concerns: layout types, visual hints, kickers, and structure.

> **How to use this file**
> Paste both this file and `Synthesis & Problem Definition.md` into Claude with the instruction below to generate a new slide deck.
> Claude will read `CLAUDE.md` and `_Config/slide-design/RULES.md` automatically and follow Winnie's design system.

---

## Prompt to use

```
Using the outline in this file, create an HTML slide deck for Session 3 · Synthesis & Problem Definition.

Follow the rules in Training_Hub/slide-deck-design/RULES.md exactly.
Save the file to synthesis-problem-definition-in-ux/session-3-synthesis.html.
Copy tokens.css and deck-stage.js locally into that same folder so the deck is self-contained.

VISUAL DESIGN DIRECTION — apply globally to every slide:

- Prefer simple diagrams, icons, and visual metaphors over bullet lists. If content can be shown
  as a shape, flow, or diagram — do that instead of listing text.
- Use inline SVG for all diagrams and illustrations. Keep them clean and minimal —
  flat shapes, no gradients, use only token colours (--sienna, --ochre, --sage, --ink, --paper).
- For process steps, draw a horizontal flow with numbered circles connected by arrows,
  not a plain list.
- For comparisons (weak vs strong), use a two-column visual split with a clear dividing line
  and colour-coded labels — not a table.
- For formulas or equations (e.g. Observation + Implication = Insight), render them large
  as a typographic visual with the operator symbols styled distinctly, not as a sentence.
- For the affinity mapping cluster diagram, draw a visual scatter of sticky-note shapes
  grouped into labelled clusters — not a list of steps.
- Activity slides (.milestone) should feel like a full-bleed moment — no extra content,
  just the number, title, and prompt. No diagrams needed.
- Every slide should have one dominant visual element. If the layout is mostly text,
  add a supporting icon or shape to anchor the eye.
- Avoid centred bullet lists. If items must be listed, use the .numbered or .process layout
  with visual numbering, not a plain <ul>.
```

---

## Session metadata

| Field | Value |
|---|---|
| Session number | 3 |
| Title | Synthesis & Problem Definition |
| Instructor | Winnie Nguyen |
| Year | 2026 |
| Cover photo | Unsplash photo of a research wall / sticky notes / workshop |

---

## Slide structure

### COVER
- Year: 2026
- Day label: Session 03
- Title: Synthesis &\nProblem Definition
- Subtitle: Turning raw research into a problem worth solving
- Author: Winnie Nguyen

---

### SECTION DIVIDER — Recap
- Num: 00
- Title: Session 2\nRecap
- Sub: What you brought into today

---

### STATEMENT — Session 2 recap
- Kicker: Last session · Customer Understanding
- Title: You learned how to\n*listen* without\ninterpreting.
- Lead: You surfaced assumptions, wrote discussion guides, ran interviews, and logged raw notes without editorialising.

---

### NUMBERED — What your assignment was
- Kicker: Your homework
- Title: What you did\nbefore today
- 4 items:
  1. Run user interviews on your live project
  2. Log raw notes in your Research Log within 24 hours
  3. Start mapping Jobs-to-Be-Done from what you heard
  4. Begin your Design Decision Log

---

### STATEMENT — Bridge
- Kicker: Today's shift
- Title: Now we make\nthe data *mean*\nsomething.
- Lead: Research without synthesis is just noise.

---

### SECTION DIVIDER — The Pipeline
- Num: 01
- Title: The\nPipeline
- Sub: Four moves from raw data to a problem worth solving

---

### DIAGRAM — The Pipeline (4-step flow)
- Kicker: How it works
- Title: Raw notes don't\nbecome direction\non their own.
- 4 steps in a horizontal flow:
  1. **Affinity Mapping** — Input: raw observations → Output: themes
  2. **Insight Statements** — Input: themes → Output: the "so what"
  3. **How Might We** — Input: insights → Output: design opportunities
  4. **Problem Statement** — Input: HMW questions → Output: one problem to solve
- 🎨 Visual hint: Draw a left-to-right horizontal pipeline — 4 nodes connected by arrows. Each node is a rounded rectangle with the method name large and the input/output in small text below. Use --sienna for node borders, --ochre for the arrows. Make the flow feel inevitable — each step feeds directly into the next.

---

### COMPARE — Mindset shift
- Kicker: Mindset shift
- Title: Before vs\nAfter synthesis
- Left column (label: Before):
  - "I have interview notes… let me start designing."
  - Jumping to solutions with unprocessed data
  - Designing based on what felt memorable in the room
- Right column (label: After):
  - "I have interview notes. Now I'll find the patterns, name the insights, define the real problem."
  - Letting the data lead before picking a direction
  - Designing based on what the evidence actually says
- 🎨 Visual hint: Draw a large arrow pointing right across the centre divider to make the shift feel directional and kinetic, not just two columns of text.

---

### COMPARE — Solo vs workshop synthesis
- Kicker: How you run it matters
- Title: Solo synthesis\nvs workshop\nsynthesis
- Left column (label: Solo):
  - You carry all the context
  - Stakeholders receive a report
  - Buy-in happens later — if at all
  - One perspective on the data
- Right column (label: Workshop):
  - Context is distributed across the room
  - Stakeholders co-own the findings
  - Alignment is a byproduct of the process
  - Multiple lenses catch what one person misses
- 🎨 Visual hint: Left column feels closed and individual — single person icon, inward-pointing shapes. Right column feels open and collective — group of person icons, outward-pointing or circular shapes. Use --ink for left, --sage for right.

---

### SECTION DIVIDER — Setting Up Your Workshop
- Num: 02
- Title: Setting Up\nYour Workshop
- Sub: Before you run the pipeline, get the right people in the room

---

### NUMBERED — Who to invite
- Kicker: The room
- Title: Four people\nwho make synthesis\nsmarter
- 4 items:
  1. **Product Manager** — aligns the roadmap to what users actually said
  2. **Engineer** — spots technical constraints before they become design assumptions
  3. **Fellow designer** — second set of eyes on what's a pattern vs. an outlier
  4. **Stakeholder or lead** — makes prioritisation decisions; better if they built the meaning themselves
- Note: Keep it to 4–6 people. More than that and clustering becomes a committee.

---

### NUMBERED — Room setup
- Kicker: Before the session
- Title: Three things\nthat make the\nroom work
- 3 items:
  1. **Share raw notes in advance** — give participants 15 min to read before the session, not during
  2. **One tool, one board** — FigJam or Miro, all raw observations already on stickies before anyone arrives
  3. **No titles in the room** — everyone clusters as equals; seniority distorts patterns
- 🎨 Visual hint: Three horizontal cards stacked with a small icon on the left of each — clock icon, board/grid icon, equals sign icon. Clean and instructional.

---

### NUMBERED — Your role as facilitator
- Kicker: Your role
- Title: You hold the\nprocess, not\nthe answers.
- 5 items:
  1. Open with the research question: "We're here to find out what the data tells us — not confirm what we already think."
  2. Protect silent clustering time — resist the urge to explain notes
  3. Name disagreements as useful: "That tension is data too."
  4. Time-box each step ruthlessly
  5. Close by asking: "What surprised you most?" — surprises are where the real insights live
- 🎨 Visual hint: Show a facilitator figure (simple outline) at the edge of a group, not at the centre. Visual metaphor: holding the space, not dominating it.

---

### SECTION DIVIDER — Step 1
- Num: 03
- Title: Step 1\nAffinity\nMapping
- Sub: Your first move — raw notes go in, themes come out

---

### NUMBERED — What is affinity mapping (3-col)
- Kicker: The method
- Title: One method,\nthree moves
- 3 items:
  1. **One note, one observation** — Each quote, behaviour, or data point lives on its own sticky. No grouping yet.
  2. **Move notes that feel related** — Group silently first — don't discuss, just feel. Let the clusters find themselves.
  3. **Name the cluster** — Write a header that captures what unites that group. That header is your theme.
- 🎨 Visual hint: Draw a small inline SVG per card — (1) a single isolated sticky note, (2) several stickies drifting toward each other, (3) a neat cluster with a label above. Flat, minimal, --ochre sticky colour.

---

### PROCESS — How to run affinity mapping (5 steps)
- Kicker: Step by step
- Title: How to run it
- 5 steps:
  1. **Dump everything** — one observation per sticky note (FigJam, Miro, or physical)
  2. **Read each note** — don't sort yet, just absorb the full weight of the data
  3. **Start moving** — cluster notes that feel related, without labelling first
  4. **Name each cluster** — the header should answer: "what unites these notes?"
  5. **Stand back** — look for super-themes, outliers, and surprises
- Step 3 is active
- 🎨 Visual hint: Render as a horizontal flow — numbered circles connected by thin arrows, not a vertical list. Step 3 circle fills with --sienna, others are outlined. Show a small sticky-note icon inside each circle.

---

### MILESTONE — Activity 1
- Kicker: Activity 01
- Num: 10
- Title: Minutes
- Sub: Recipe app dataset is on your FigJam board. 6 min — cluster silently. 4 min — label each cluster. What surprised you? Did any note belong in two places?

---

### SECTION DIVIDER — Step 2
- Num: 04
- Title: Step 2\nInsight\nStatements
- Sub: You have themes — now name what each one means

---

### STATEMENT — What is an insight statement
- Kicker: The definition
- Title: *Observation* +\n*Implication* =\nInsight
- Lead: An observation is what you saw or heard. An implication is why it matters for design. Together they make an insight.
- 🎨 Visual hint: Render the formula as a large typographic equation — three big blocks side by side: [OBSERVATION] + [IMPLICATION] = [INSIGHT]. Style the "+" and "=" as --sienna. Below each block, add a one-line descriptor in small mono text. Make the equation the dominant element on the slide, not the lead text.

---

### COMPARE — Strong vs weak insight
- Kicker: Quality check
- Title: Weak insight\nvs strong insight
- Left column (label: Weak):
  - "Users find the app confusing"
  - "Users want a simpler interface"
  - "Users liked the new feature"
- Right column (label: Strong):
  - "Users can't locate booking status after submission, causing them to call support — a gap in post-action feedback design"
  - "Hospitality managers visit the app 3–5x per shift but navigate 4 screens each time — suggesting a need for a persistent dashboard view"
  - "3 of 4 users completed the flow faster, but all 4 got stuck at the date picker — a specific interaction failure, not a layout issue"

---

### MILESTONE — Activity 2
- Kicker: Activity 02
- Num: 10
- Title: Minutes
- Sub: Pick one moment from your interviews. Write the insight: what did you observe, and what does it mean for the design?

---

### SECTION DIVIDER — Step 3
- Num: 05
- Title: Step 3\nHow Might\nWe
- Sub: Turn insights into questions the team can design toward

---

### NUMBERED — What HMW means (3-col)
- Kicker: Breaking it down
- Title: Three words,\none big idea
- 3 items:
  1. **How** — Assumes it's solvable. Not "can we" or "should we" — it's already a given that it can be done.
  2. **Might** — Leaves the solution open. Invites exploration. No single right answer yet.
  3. **We** — It's a team challenge. Builds shared ownership, not one person's burden to solve alone.

---

### STATEMENT — HMW example
- Kicker: In practice
- Title: From insight\nto *opportunity*
- Lead: Insight: "Users abandon after checkout even when the transaction succeeds — because there is no clear confirmation — breaking trust at the most critical moment in the flow."
- HMW list (3 bullets on the slide):
  - How might we make it immediately clear that a transaction was successful, without requiring the user to check?
  - How might we reduce user anxiety at the moment between action and confirmation?
  - How might we design a post-payment experience that builds trust instead of doubt?
- 🎨 Visual hint: Show the insight in a distinct callout box (dark --ink background, --paper text) at the top. Below it, draw a downward arrow into 3 HMW cards arranged horizontally — each card in --paper-deeper with a --sienna "HMW →" label. Visually show the transformation from one insight to multiple opportunities.

---

### MILESTONE — Activity 3
- Kicker: Activity 03
- Num: 8
- Title: Minutes
- Sub: Take the insight you wrote. Turn it into 3 different "How Might We" questions.

---

### SECTION DIVIDER — Step 4
- Num: 06
- Title: Step 4\nProblem\nStatement
- Sub: Converge — one problem the whole team can act on

---

### NUMBERED — What makes a strong problem statement (3-col)
- Kicker: The criteria
- Title: Three things a\ngood problem\nstatement does
- 3 items:
  1. **User-centred** — Describes a real person's problem, not a business goal, a feature request, or a technical constraint.
  2. **Specific, not vague** — "Users struggle to track booking status" beats "users find the product confusing." Precision makes it testable.
  3. **Open to multiple solutions** — Doesn't hint at the answer. Opens possibility instead of closing it down.

---

### STATEMENT — The formula
- Kicker: The formula
- Title: *[User]* needs a way\nto *[goal]* because\n*[barrier]*
- Lead example: "First-time online shoppers need a way to know their order was confirmed immediately after payment because the current delay and lack of feedback causes them to abandon — and sometimes re-order — thinking the transaction failed."
- 🎨 Visual hint: Render the formula as three colour-coded pill/tag blocks in a row — [USER] in --sienna-tint, [GOAL] in --sage-tint, [BARRIER] in --ochre-tint — each with its label above in mono. Below, show the filled-in example sentence with the same colour highlights applied inline to the matching words.

---

### COMPARE — Strong vs weak problem statement
- Kicker: Quality check
- Title: Weak statement\nvs strong statement
- Left column (label: Weak):
  - "We need to redesign the checkout flow" — *Solution, not a problem*
  - "Users don't trust the app" — *Too vague to act on*
  - "The app needs better notifications" — *Solution, not user-centred*
- Right column (label: Strong):
  - "First-time buyers need a way to confirm their order was placed because the current lack of feedback after payment causes them to re-submit, creating duplicate orders"
  - "New users need a way to verify their account is set up correctly because there is no onboarding confirmation — leading them to contact support before completing their first action"
  - "Frequent users need a way to know when a status change happens without opening the app because they currently miss time-sensitive updates — causing delays and frustration"

---

### MILESTONE — Activity 4
- Kicker: Activity 04
- Num: 15
- Title: Minutes
- Sub: Start your problem statement now. Use the formula. You'll finish it before Session 4.

---

### PRACTICE — Assignment (before Session 4)
- Kicker: Your assignment
- Title: Before Session 4
- Card 1 — Affinity Mapping:
  - Run affinity mapping on all your interview notes
  - Use FigJam, Miro, or physical sticky notes
  - Look for super-themes and outliers
- Card 2 — Insight Statements:
  - Write 3 insight statements from your research
  - Use the Observation + Implication formula for each
  - Push the implication until it's product-specific
- Card 3 — Share your problem statement:
  - Share it with one stakeholder — a PM, engineer, or team lead
  - Note how they respond
  - Update the statement if they were confused about who or why
---

### END — Closing
- Kicker: After today, you should have one thing
- Title: A problem\nworth solving.
- Sign: — Winnie Nguyen
