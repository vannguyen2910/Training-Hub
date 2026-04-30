# Session 4 · Information Architecture

**Winnie Nguyen** — Senior Product Designer at NAB

---

## Session 3 Recap

**Last session: Synthesis & Problem Definition**

What you learned:
- How to turn raw interview notes into themes using Affinity Mapping
- How to write Insight Statements: Observation + Implication
- How to frame design opportunities with How Might We
- How to write a Problem Statement grounded in user research

Your assignment was to:
- Run affinity mapping on all interview notes
- Write 3 insight statements using the formula
- Share your problem statement with one stakeholder and note their response

> Today we take that problem statement and ask: how does the product need to be *organised* to solve it?

---

## What We're Building Today

Turn your problem statement into a structural design decision.

1. **Inherited vs Evidence-Based IA** — understand what you're actually working with
2. **Card Sorting** — how to learn what users expect before you build
3. **Sitemaps** — make the current structure visible so you can change it
4. **User Flows** — map what a user actually does, step by step, before touching a screen

---

## Mindset Shift

> **A polished screen in the wrong flow is still a broken design.**

| Before | After |
|--------|-------|
| "I'll figure out the structure as I wireframe." | "I map the structure first. Wireframes come after the flow is clear." |

---

## Part 1 — What is Information Architecture?

IA is how content is organised, labelled, and connected so users can find what they need — without thinking too hard.

It decides:
- What lives where
- What things are called
- How navigation is structured

> Most designers inherit an IA from whoever came before — and never question it.

---

## Inherited vs Evidence-Based IA

| | Inherited IA | Evidence-Based IA |
|---|---|---|
| **Source** | POs, stakeholders, legacy systems | User research, card sorting |
| **Organising logic** | Business structure, team ownership | Users' mental models and task sequences |
| **Risk** | "It makes sense to us" bias | Requires method discipline |

**The signal:** If your navigation mirrors the org chart — it's inherited.

---

## Part 2 — Card Sorting

**What it is**
Users arrange content cards into groups that feel natural to them. You observe the result.

**When to use it**
- Before building navigation — when you don't know how to group content
- When users complain they can't find things
- When you've inherited a structure and want to test it

**Why it matters**
It gives you evidence to defend structural decisions — not just intuition.

---

## Two Types of Card Sort

**Open card sort**
- Users create their own categories and name them
- Use when: you have no existing structure
- Reveals: the user's mental model directly

**Closed card sort**
- Users sort cards into categories you've already defined
- Use when: you want to validate an existing structure
- Reveals: whether your labels match user expectations

> 3–5 people surfaces structural assumptions worth questioning. You don't need 20.


---

## Part 3 — Sitemaps

**What it is**
A structural diagram of every page or screen in a product — showing hierarchy and connection. Not a wireframe. No layouts, no UI.

**When to use it**
- At the start of any redesign — before changing anything
- After card sorting — to rebuild structure from evidence
- When onboarding to a new product

**Why it matters**
You can't redesign what you haven't made visible. A sitemap makes structural problems undeniable.

---

## Two Sitemaps to Draw

**Inherited sitemap**
- Drawn from the current live product
- Documents reality as it is right now
- Start here — take screenshots, map every screen, draw the hierarchy

**Evidence-based sitemap**
- Rebuilt from card sorting results and your JTBD Map
- Organises content around user tasks, not business categories
- This is the goal

> Every box should be nameable without referring to which team built it. If you can't — that's an IA problem.


---

## Part 4 — User Flows

**What it is**
A diagram of the steps a user takes to complete one specific task — from entry point to final outcome.

Not a wireframe. A structural map of decisions, actions, and system responses along a task path.

**When to use it**
- Before wireframing — map the structure before designing any screen
- When reviewing an existing product — document what users actually have to do
- When identifying friction — where users drop off or get lost

---

## Why User Flows Matter

> Most design problems live in the flow — not in individual screens.

Without a user flow:
- You design screens without knowing what comes before or after
- Error states and edge cases are discovered in development — not design
- Stakeholders debate screen details without agreeing on task structure

**Also:** A user flow is the most useful handover artefact for engineering. It tells developers not just *what* to build — but *when* and *under what conditions* each screen appears.

---

## The Shapes

| Shape | What it represents | Example |
|---|---|---|
| **Pill / Rounded rectangle** | Start and end points | "App opens", "Task complete" |
| **Rectangle** | User action or screen | Taps a button, fills a form, views a screen |
| **Diamond** | Decision point | "Is user logged in?" / "Did payment succeed?" |
| **Parallelogram** | System action | Sends email, loads data, validates a field |
| **Arrow** | Flow direction | Label branches: Yes / No, Success / Error |

> Consistent shapes make your flow readable to anyone on the team — no explanation needed.

---

## Swimlanes

When more than one actor is involved, swimlanes separate who does what.

Each horizontal lane = one actor. Actions go in the lane of whoever is responsible.

```
┌──────────────────────────────────────────────┐
│  USER      │  Taps "Pay" → Enters card        │
├──────────────────────────────────────────────┤
│  SYSTEM    │  Validates → Sends to gateway    │
├──────────────────────────────────────────────┤
│  3RD PARTY │  Gateway processes → Returns     │
└──────────────────────────────────────────────┘
```

Use swimlanes for:
- Checkout flows (payment provider involved)
- Onboarding (system triggers emails or state changes)
- Admin features (a second user type acts on the primary user's data)

---

## How to Draw a User Flow

1. **Name the task** — be specific. Not "checkout." "Complete a purchase as a returning user with a saved card."
2. **Define entry and end points** — draw Start and End pills before anything else
3. **Map the happy path first** — the ideal sequence when everything works
4. **Add error and edge case branches** — declined card, not logged in, empty state — every branch needs a destination
5. **Add swimlanes** if the system acts independently of the user
6. **Review for completeness** — every diamond needs two labelled outgoing arrows. No orphaned shapes.

---

## What a Good Flow Reveals

- Steps that exist because of how the system was built — not because users need them
- Decision points where users do work the system could handle automatically
- Flows longer than necessary because content is in the wrong IA location
- Missing states: empty, error, loading, success

> If a core task takes more than 7 steps — the IA is likely the problem, not the screen design.

---

## JTBD → Flow

Use your JTBD Map to evaluate every step.

**Ask for each step:** Does this help the user move toward their job — or is it friction the system created for its own reasons?

| JTBD Insight | Flow Implication |
|---|---|
| Users need to confirm quickly before losing a slot | No upsell screens in the critical path |
| Users feel anxious about irreversible actions | Add a review step before final commit |
| Users want to look competent when sharing work | Surface "share" at task-completion, not buried in settings |

---

## 🤖 AI in Practice — User Flows

**Try this prompt:**

```
I'm mapping the current user flow for [describe the task]
in [describe your product briefly].

Here are the steps I've identified:
[paste your list of steps]

Help me:
1. Identify which steps exist because of system constraints,
   not because users need them
2. Suggest where decision diamonds should be placed
3. Flag missing steps — especially error states
   or edge cases I may have overlooked
```

**Watch out for:** AI doesn't know your system's real constraints. It may suggest removing steps that are technically necessary. Verify against your engineering reality.

**Reflect:** Which missing state did AI flag that you hadn't considered?

---

## Activity · 20 min

> Pick one real project. Choose the core task a user needs to complete. Walk through it yourself — screen by screen — and map every step using the correct shapes and swimlanes.

Start with the happy path. Then add one error branch.

---

## Your Assignment — Before Session 5

1. Complete the full current-state user flow for your chosen task in FigJam or Miro — correct shapes, correct swimlanes
2. Annotate every step: **U** (user), **S** (system), or **3P** (third party)
3. Highlight in red every step that exists because of a system or IA constraint — not because it serves the user
4. Pick the single highest-friction step. Write one paragraph: why does it exist, what would need to change to remove it, and what would you test to validate that change?

---

*"Organise for users — not for the org chart."*
