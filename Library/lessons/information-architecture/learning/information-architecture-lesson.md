# Information Architecture

**Type:** Lesson
**Duration:** 90–120 minutes
**Audience:** Intermediate
**Methods:** Card Sorting · Sitemaps · Tree Testing · User Flows

---

## Key Concepts

### What is Information Architecture?
IA is the discipline of deciding how content is organised, labelled, and connected so that users can find what they need without thinking too hard. It determines what lives where, what things are called, and how navigation is structured. Most designers inherit an IA from whoever designed before them — and rarely question it.

---

### Inherited IA vs Evidence-Based IA

The most important distinction in this lesson. Most product structures were built by product owners, engineers, or business stakeholders who organised things the way the *business* thinks — by feature, team, or product line. Users don't organise information that way.

| | Inherited IA | Evidence-Based IA |
|---|---|---|
| **Source** | POs, stakeholders, briefs, legacy systems | User research, card sorting, tree testing |
| **Organising logic** | Business structure, feature ownership, system architecture | Users' mental models, language, and task sequences |
| **What it solves** | Internal alignment, delivery scope | User findability, navigation confidence |
| **Risk** | "It makes sense to us" bias | Requires time and method discipline |

A navigation that mirrors the org chart is almost always inherited IA. A navigation built from card sorting and tested with tree testing is evidence-based.

---

### Card Sorting

**What it is**
A method for learning how users mentally group and label content. Users are given cards representing content items and asked to arrange them into groups that feel natural to them.

**When to use it**
- Before building or redesigning navigation — when you don't yet know how content should be grouped
- When users complain they can't find things, but you're not sure which categories or labels are wrong
- When you've inherited a navigation structure and want to know if it matches how users actually think

**Why to use it**
Most navigation structures reflect internal business logic, not user logic. Card sorting reveals the gap. It gives you evidence to defend structural decisions to stakeholders — not just intuition.

**How to use it**
Two formats depending on your question:

- **Open card sort** — users create their own categories and name them. Use this when you don't yet have a navigation structure. Best for discovery. Reveals the user's mental model directly.
- **Closed card sort** — users sort cards into categories you've already defined. Use this to validate an existing structure. Reveals whether your labels match users' expectations.

Run with 15–20 participants for reliable patterns. For a quick in-session test, even 3–5 people surfaces structural assumptions worth questioning. Look for clustering agreement, not perfect consensus — divergence is data too.

Tools: FigJam, Miro (physical sticky notes), Optimal Workshop, or Maze for async runs.

---

### Sitemaps

**What it is**
A structural diagram showing the hierarchy and relationship between all pages or screens in a product. A sitemap is not a wireframe — it shows *what exists and how it connects*, not what anything looks like.

**When to use it**
- At the start of a redesign, to document the current structure before changing anything
- After card sorting, to redesign the structure based on user evidence
- When onboarding onto a new product — to build a shared understanding of the current state

**Why to use it**
Without a sitemap, structural problems stay invisible. You can't redesign what you haven't made explicit. A sitemap also makes it possible to have an honest conversation with stakeholders about whether the current structure serves users — or the business.

**How to use it**
Draw two versions when doing IA work:

- **Inherited sitemap** — drawn from the current live product. Documents reality as it is. Start here. Take screenshots, map every screen, and draw the hierarchy.
- **Evidence-based sitemap** — rebuilt from card sorting results and JTBD insights. Organises content around user tasks, not business categories. This is the goal.

Every box in the sitemap should be nameable and have a clear parent. If you can't define what belongs in a section without referring to the team that built it — that's an IA problem.

---


### User Flows

**What it is**
A diagram of the steps a user takes to complete a specific task — from their entry point to their final outcome. A user flow is not a wireframe. It's a structural map of *decisions, actions, and system responses* that happen along a task path.

**When to use it**
- Before wireframing — to map out the structure of a flow before designing any screen
- When reviewing an existing product — to document what a user currently has to do to complete a task
- When identifying friction — steps where users drop off, get confused, or take the wrong path

**Why user flows matter in the design process**
Most design problems live in the flow, not in individual screens. A screen can look polished and still sit in the wrong place in a broken flow. User flows force you to think through the full task — every decision point, every error state, every branch — before committing those decisions to pixels.

Without a user flow:
- You design screens before knowing what should come before or after them
- Edge cases (error states, empty states, permission gates) get discovered in development — not design
- Stakeholders debate screen-level details without ever agreeing on the task structure

A user flow is also the most useful artefact for handing work to engineering. It tells developers not just what to build, but *when* and *under what conditions* each screen appears.

**The anatomy of a user flow**

A user flow is built from a small set of standard shapes. Using consistent shapes matters — it makes flows readable to anyone on the team without explanation.

| Shape | What it represents | When to use |
|---|---|---|
| **Rounded rectangle / Pill** | Start and end points | Entry points (app opens, user lands on page) and final outcomes (task complete, exit) |
| **Rectangle** | User action or screen | Any step where the user does something: taps a button, fills a field, views a screen |
| **Diamond** | Decision point | A yes/no or either/or branch: "Is the user logged in?", "Did the payment succeed?" |
| **Parallelogram** | System input/output | What the system does automatically: sends an email, loads data, validates a field |
| **Arrow** | Flow direction | Connects all shapes. Label branches on decision diamonds (Yes / No, Success / Error) |

**Swimlanes**
When a flow involves more than one actor — the user, the system, and sometimes a third party like a payment provider or admin — swimlanes organise who does what. Each horizontal lane belongs to one actor. Actions are placed in the lane of whoever is responsible for that step.

```
┌─────────────────────────────────────────────────────┐
│  USER      │  → Taps "Pay" → Enters card details    │
├─────────────────────────────────────────────────────┤
│  SYSTEM    │  → Validates card → Sends to gateway   │
├─────────────────────────────────────────────────────┤
│  3RD PARTY │  → Payment gateway → Returns response  │
└─────────────────────────────────────────────────────┘
```

Swimlanes are especially useful for:
- Checkout flows where a payment provider is involved
- Onboarding flows where the system sends emails or triggers state changes
- Admin-facing features where a second user type (admin) acts on something the primary user initiated

**How to draw a user flow**

1. **Name the task** — be specific. Not "checkout" but "complete a purchase as a returning user with a saved card." The more specific the task, the cleaner the flow.
2. **Define the entry point** — where does this task begin? Direct link, navigation tap, search result, notification?
3. **Map the happy path first** — the ideal sequence of steps when everything works. Use rectangles for actions, diamonds for decisions, parallelograms for system steps.
4. **Add branches for errors and edge cases** — what happens if the card declines? What if the user is not logged in? What if the content hasn't loaded yet? Each branch needs a destination — never leave a line unresolved.
5. **Add swimlanes if multiple actors are involved** — separate user actions from system actions and third-party actions into their own lanes.
6. **Review for completeness** — every diamond must have at least two outgoing arrows, labelled. Every path must end somewhere. No orphaned shapes.

**What a well-drawn flow reveals**
- Steps that exist only because of how the system was built, not because users need them
- Decision points that ask users to do work the system could do automatically
- Flows that are longer than necessary because content is in the wrong place in the IA
- Missing states: what happens at empty state, error state, loading state?

**How JTBD shapes user flows**
Jobs-to-Be-Done gives you the lens for evaluating a flow. For each step in the flow, ask: does this step help the user progress toward their job — or is it friction the system is adding for its own reasons?

If the functional job is "confirm my booking before I lose the slot," every step in the flow that delays confirmation is a structural problem. JTBD makes those problems visible — and defensible to stakeholders.

| JTBD Insight | Flow Implication |
|---|---|
| Users' primary job is confirming quickly before the slot expires | Reduce steps between intent and confirmation — no upsell screens in the critical path |
| Users feel anxious about irreversible decisions | Add a review step before final commit; make "go back" always visible |
| Users want to look competent when sharing work | Surface "share" at task-completion moments, not buried in settings |

---

## Tools & Materials

- One of your own projects (bring a working product or prototype to the session)
- FigJam or Miro — for drawing the user flow
- Screenshots of the relevant screens in the flow
- JTBD Map from Session 2 (used to choose which task to map)

---

## Practice Activity — Map the Current User Flow

Pick one real project you're working on. Choose one core task — the most important thing a user needs to do in this product. Map the flow exactly as it exists today: not how it should work, but how it actually works right now.

**Steps:**

1. **Choose your task** — pick one core user job from your JTBD Map. Make it specific: not "browse products" but "find and save a product for later." This will be the scope of your flow.

2. **Define your entry point and end point** — where does the user start this task? Where are they when the task is complete? Draw a Start pill and an End pill before anything else.

3. **Walk through the flow step by step** — open your product (or prototype) and complete the task yourself, narrating every step aloud. Write each step on a sticky note as you go. Don't skip steps — include every tap, every screen load, every decision the user has to make.

4. **Assign shapes to each step:**
   - Rectangles for user actions and screens
   - Diamonds for decision points (login check, empty state, error condition)
   - Parallelograms for system actions (email sent, data saved, validation triggered)

5. **Add swimlanes if needed** — if the system does things independently of the user (sends a confirmation, refreshes data), separate the User lane from the System lane.

6. **Add the error paths** — for each diamond, follow both the Yes and No branches. Where does the user go if something fails? If you don't know — that's a gap in the design.

7. **Count the decision points** — how many times does a user have to make a choice before completing the task? Each decision point is a potential drop-off. Note which ones exist because of IA decisions (content is in the wrong place) vs interaction design decisions (the flow itself is poorly sequenced).

**Debrief prompts:**
- Which steps surprised you — ones you didn't realise existed until you walked through it?
- Which steps are there because of how the system was built, not because users need them?
- Which decision points could the system resolve automatically, removing a step entirely?
- Where does the flow break down if the user takes a wrong turn?

---

## Assignment (before next session)

**Build the current-state flow and identify one structural fix.**

1. Complete the user flow for your chosen task in FigJam or Miro using the correct shapes and swimlanes
2. Annotate every step with one of: **U** (user does this), **S** (system does this), or **3P** (third party does this)
3. Highlight in red every step that exists because of an IA or system constraint — not because it serves the user
4. Pick the single highest-friction step and write a short rationale: why does this step exist, what would need to change structurally to remove it, and what would you need to test to validate the change?

**🤖 AI in Practice prompt:**
> *"I'm a UX designer mapping the current user flow for [describe the task in one sentence] in [describe your product briefly]. Here are the steps I've identified: [paste your list of steps]. Help me: 1. Identify which steps are likely caused by system or IA constraints rather than user needs. 2. Suggest where decision diamonds should be placed. 3. Flag any steps that appear to be missing — especially error states or edge cases I might have overlooked."*

---

## Related Notion Resources

- [Design Activities by DT Stage — Reference](https://www.notion.so/3248a6b135db810385bdf06991f4f87a) — Card sorting and tree testing in context of the full DT cycle
- [Session 1 Playback — Design Thinking in Practice](https://www.notion.so/3318a6b135db81a2a1ebf83b4ec081a5) — "Organise for users — Evidence-based sitemap, Task flows"
- [Progress Tracker](https://www.notion.so/3238a6b135db816db041d2cfbc58fa8c) — Evidence-based sitemap is the S4 artifact

---

*Lesson: Information Architecture · Part of the 8-session UX Mentoring Program*
