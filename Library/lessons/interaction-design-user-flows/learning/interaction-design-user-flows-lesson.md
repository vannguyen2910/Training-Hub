# Interaction Design & User Flows

**Type:** Lesson
**Session:** 5 of 8
**Duration:** 90–120 minutes
**Audience:** Intermediate
**Methods:** Task Flows · User Flows · State Design · B2B Interaction Patterns · Handoff Annotation
**Builds on:** Session 3 — Information Architecture (user flow shape language, happy path, decision branches, swimlanes)

---

## What this session adds

Session 3 established the structural foundation: how to map a user flow using shape language, how to walk the happy path, and how to add decision branches and error states. That work should be in hand before this session.

Session 5 goes deeper into three things that structure alone doesn't cover:

1. **The difference between a task flow and a user flow** — and why choosing the wrong one produces the wrong artefact
2. **Designing for states as a method** — not just a checklist item before handoff, but a design decision that shapes how a product feels under real conditions
3. **Interaction patterns specific to B2B products** — navigation, forms, and data tables behave differently when the user is a professional working at volume, not a consumer making occasional decisions

By the end of the session, every flow the mentee produces should be reviewable against their JTBD Map — so the question is always whether each step helps the user complete their job, or just satisfies the system.

---

## Key Concepts

### Task Flows vs User Flows — When to Use Each

Two terms used interchangeably in most teams. They are not the same thing, and using the wrong one produces work that misleads rather than informs.

**Task flow**
A linear sequence of steps that a single type of user follows to complete one specific task. No branching. No error paths. No alternative routes. It represents the intended path — what *should* happen when everything works.

Use a task flow when:
- You need to communicate the core sequence to a stakeholder without overwhelming them with branches
- You're scoping what needs to be built for one specific scenario
- You're reviewing the overall structure of a flow before designing edge cases

A task flow answers: *what are the steps, in order, to complete this task?*

**User flow**
A branching diagram that includes the full decision tree — happy path, error paths, edge cases, system responses, empty states, and alternative routes. It represents what *actually happens* across all the ways a user might move through a product.

Use a user flow when:
- You're designing for real usage, not just the ideal scenario
- You're handing work to engineering — they need to know what happens in every branch
- You're reviewing a flow for completeness before prototyping

A user flow answers: *what happens at every point in this task, including when things go wrong?*

| | Task Flow | User Flow |
|---|---|---|
| **Structure** | Linear — one path | Branching — multiple paths |
| **Includes errors?** | No | Yes |
| **Use for** | Alignment, scoping, stakeholder review | Design, engineering handoff, edge case mapping |
| **Risk if misused** | You design only the happy path — edge cases surface in development | Too complex for early alignment conversations |
| **Shape language** | Rectangles + arrows, start/end pills | Full vocabulary: diamonds, parallelograms, swimlanes |

**The sequencing rule:** Draw the task flow first to align on scope. Then expand it into a user flow before handing it off. Never skip the task flow — it's what makes the user flow legible.

---

### Designing for States

Most designers design the default state — the screen as it looks when everything has loaded, the user is logged in, and data is present. That state is the least interesting one in terms of experience quality.

The states that shape how a product actually feels are the ones that happen when things are in transition or haven't gone to plan.

**The five states every screen or component needs**

**1. Default**
The screen as it appears when everything is working and data is present. This is where most design effort goes. It should still be designed intentionally — not just "the normal version."

Design decisions at default state: hierarchy, information density, primary action prominence, labelling.

**2. Loading**
The screen's state while data is being fetched, a process is running, or a transition is happening. Loading states are frequently skipped in design and discovered in development. That's late and expensive.

A good loading state:
- Matches the structure of the loaded content (skeleton loaders, not generic spinners, for content-heavy screens)
- Communicates progress when the wait is more than 2–3 seconds
- Does not block the user from doing other things unless it genuinely must

Design decisions at loading state: skeleton vs spinner vs progress bar, timeout handling, retry behaviour.

**3. Empty**
The screen's state when a user arrives with no data — a new account, no search results, no items in a list. Empty states are the product's first impression for new users and a signal of how well the design anticipates user journeys.

A good empty state:
- Tells users what they're looking at (context, not just whitespace)
- Tells users what to do next (a clear first action)
- Does not use the same copy as an error state

Design decisions at empty state: first-use onboarding integration, call to action, tone.

**4. Error**
The screen's state when something has failed — a submission error, a validation failure, a system error, a permission restriction. Error states are the moment users most need clarity, and the moment most products are least clear.

A good error state:
- States what went wrong in plain language (not error codes, not "something went wrong")
- Tells the user what to do — specifically
- Preserves the user's input where possible (don't clear a form on submit error)
- Distinguishes between user errors (fixable by the user) and system errors (not fixable by the user)

Design decisions at error state: inline vs modal vs toast notification, error message tone, recovery path.

**5. Success**
The screen's state when a task is completed. Frequently overlooked — designers confirm the action happened but don't consider what the user should do next. Success states are transition moments: the task is done, what's the next job?

A good success state:
- Confirms what happened (specifically, not generically — "Your report was exported to PDF" not "Done")
- Offers a clear next action relevant to the user's likely next job
- Does not require the user to navigate back manually to continue working

Design decisions at success state: persistence (toast that disappears vs persistent confirmation), next-action prompt, return-to-flow logic.

**How to use this in practice**

For every screen in a flow, draw all five states before considering the design done. The test: if you couldn't show the engineering team what the loading state looks like, the screen is not ready for handoff.

| State | The question it answers |
|---|---|
| Default | What does this look like when everything is working? |
| Loading | What does the user see while they wait? |
| Empty | What does the user see the first time, or when there's no data? |
| Error | What does the user see when something fails — and what do they do next? |
| Success | What does the user see when they've completed the task — and what do they do next? |

---

### Interaction Patterns for B2B Products

B2B products serve professionals working at volume, under time pressure, often with specific domain expertise. The interaction patterns that work for consumer products frequently fail in B2B contexts because the assumptions are wrong.

**Navigation**

B2B products typically have complex navigation structures — multiple modules, role-based access, and deep hierarchies. Three patterns are most common:

- **Persistent sidebar navigation** — all top-level modules always visible. Good for products where users switch contexts frequently (e.g. a CRM switching between Contacts, Deals, and Reports). Requires discipline: every item in the sidebar should represent a real job a user regularly needs to do.

- **Top navigation with sub-navigation** — top bar for modules, secondary bar for sub-sections. Good for products with a strong hierarchy (one primary task area at a time). Risk: the sub-navigation disappears when the user moves to a new top-level section, breaking their orientation.

- **Progressive disclosure navigation** — only the currently relevant options are shown. Good for workflow-driven products where users follow a defined path (e.g. an onboarding wizard, a configuration flow). Risk: users lose the sense of where they are in the overall product.

**What to watch for in B2B nav:**
- Role-based visibility — what does an admin see vs a standard user? This is almost always underspecified in early designs.
- Contextual navigation — when a user is deep inside a record (e.g. a specific deal in a CRM), the navigation should indicate their location and make it easy to return.
- Breadcrumbs — essential in products with deeply nested content. Often skipped in design and missed until a usability test reveals users can't find their way back.

**Forms**

B2B forms are usually longer, more complex, and more consequential than consumer forms. Three patterns apply:

- **Single-page forms** — all fields visible at once. Best for short forms (under 8–10 fields) or when users need to see all fields before starting (to gather information before they begin). Risk: cognitive overload on complex forms.

- **Multi-step forms (wizards)** — fields grouped into stages with a progress indicator. Best for complex processes where fields in later steps depend on inputs in earlier steps (e.g. configuring a product, onboarding a new account). Risk: users can't see what's coming, which creates anxiety about the commitment they're making. Always show a progress indicator.

- **Inline editing** — fields within a record that become editable on click, without navigating to a separate edit page. Best for records users need to update frequently (e.g. contact details in a CRM). Risk: unclear edit affordance — users don't know what's editable until they try to click it. Use consistent hover states.

**What to watch for in B2B forms:**
- Validation timing — validate on blur (when a user leaves a field), not on submit. Submitting a long form only to find 12 errors is one of the most common B2B UX failures.
- Required vs optional fields — mark required fields explicitly. In B2B, incomplete submissions often have downstream consequences (broken integrations, missing data for reports).
- Autosave — for long or complex forms, autosave is not a nice-to-have. Users are interrupted. They switch contexts. They close tabs. Progress should not be lost.

**Data Tables**

The most common and most underdesigned component in B2B products. A data table in a professional context needs to do real work: filtering, sorting, bulk actions, and column customisation are not enhancements — they are the baseline expectation.

- **Sorting** — every column with meaningful order should be sortable. The current sort column and direction should be visually indicated.
- **Filtering** — for tables with more than ~20 rows, filtering is required. Filter state should persist (don't reset filters when the user returns to the table).
- **Pagination vs infinite scroll** — pagination is almost always preferable in B2B. Users need to know how many records exist, where they are in the list, and how to return to a specific position. Infinite scroll loses all of this.
- **Bulk actions** — when users need to update many records at once, bulk selection with contextual actions (archive, export, assign, delete) reduces a painful repetitive task to a single operation.
- **Empty and filtered-empty states** — a table with no results needs two distinct designs: the true empty state (no records exist yet) and the filtered-empty state (records exist, but none match the current filters). These are different problems and need different copy and actions.
- **Row actions** — actions on individual rows (edit, delete, view) should be visible on hover, not always visible (to avoid visual noise at scale) and not buried in a three-dot menu that users can't discover.

---

### How to Annotate Flows for Handoff Clarity

An annotated flow is the contract between design and engineering. Annotations are not commentary — they are specifications. They answer questions before engineers need to ask them.

**What annotations should cover**

For every screen in a flow:

- **State being shown** — label which of the five states this frame represents (Default / Loading / Empty / Error / Success)
- **Trigger** — what action or event brings the user to this screen (button tap, page load, system redirect, timer expiry)
- **Conditions** — any logic the screen depends on (user role, data state, permission level, previous action). Example: "This screen is only shown if the user has admin access and the organisation has fewer than 50 seats."
- **System actions** — anything the system does at this point that the user doesn't initiate (sends an email, logs an event, updates a record). These are the things developers need to implement that don't appear in the visual design.
- **Error handling** — what happens at this step if the system fails. Don't leave this to developer interpretation.
- **Edge cases** — any known variations from the default behaviour (e.g. "If the user's name is longer than 30 characters, truncate with ellipsis in this label")

**Annotation format**

Number each annotation on the frame. Keep the annotation text brief and specific — one fact per note. Use a consistent visual convention: a numbered callout circle on the design element, matched to a numbered note in a side panel or legend.

Avoid annotations that describe what the user can already see. Annotations should describe *why* the design is the way it is, and *what the system needs to do* — not what the designer already drew.

```
✗ "Button is blue"              → describes what's visible, not useful
✓ "Primary CTA. Disabled until all required fields are valid."

✗ "Table shows list of users"   → describes what's visible, not useful
✓ "Sorted by Last Active descending by default. Sort preference persists per user session."
```

**Handoff checklist**

Before sharing a flow with engineering:

- [ ] Every screen has its state labelled
- [ ] Every decision point has both branches designed (not just the success branch)
- [ ] All five states exist for every component that can load, fail, or be empty
- [ ] System actions are explicitly annotated (not assumed)
- [ ] Error states have specific error copy — not placeholder text
- [ ] Role or permission conditions are documented where they apply

---

## Tools & Materials

- FigJam or Miro — for mapping task flows and user flows
- Figma — for annotated screens and state design
- JTBD Map from Session 2 — used to select critical paths and evaluate each flow step
- A product you're currently working on — bring a real project, not a hypothetical

---

## Practice Activities

### Activity 1 — Map 2–3 Critical User Journeys as Annotated Task Flows

**Goal:** Translate the product's most important user jobs into documented task flows, ready for expansion into full user flows.

**Steps:**

1. **Select your critical paths** — Open your JTBD Map. Identify the 2–3 functional jobs that are most central to why users use the product. These are the paths you'll map. If you don't have a JTBD Map yet, ask: "What are the 2–3 things a user absolutely must be able to do for this product to be worth using at all?"

2. **Draw each task flow** — For each job, map the task flow: entry point → steps → outcome. Linear only at this stage. Use the shape language from Session 3 (pill for start/end, rectangles for steps, arrows for sequence). Name each step as a user action, not a screen name.

3. **Expand to user flows** — For each task flow, add branching: decision diamonds, error paths, and system actions. Every diamond needs two labelled outgoing arrows. Every path needs an end point — nothing should be unresolved.

4. **Annotate each flow** — Add annotations following the handoff format: state labels, triggers, conditions, system actions, error handling. Number each annotation and match to a legend.

**Debrief prompts:**
- Which path had the most decision points? Is that complexity serving the user — or the system?
- Where did you discover steps you hadn't planned for?
- Which annotations required you to make a design decision you hadn't made yet?

---

### Activity 2 — Identify and Design Edge Cases and Error States

**Goal:** For each critical path, surface the failure modes that are easiest to miss in early design — and design them explicitly.

**Steps:**

1. **Walk the flow as an adversarial user** — go through each critical path and ask at every step: "What could go wrong here?" Categorise each failure:
   - **User error** — wrong input, missed required field, invalid format
   - **System error** — server failure, timeout, integration failure
   - **Permission error** — user doesn't have access to this resource
   - **Data error** — expected data is missing, malformed, or stale

2. **Design the error state for each** — for each failure you identified, design the screen or component state that handles it. Specific error message (no placeholder text), clear recovery action, preserved user input where possible.

3. **Design the empty states** — for every list, table, or content area in your flows, design both the true empty state (no data yet) and the filtered-empty state (data exists but none matches current filters).

4. **Check for missing states** — review every component in your flows against the five-state framework: Default / Loading / Empty / Error / Success. Any component missing a state is a gap.

**Debrief prompts:**
- Which errors were hardest to write copy for? What does that reveal about the design decision behind them?
- Which empty states need a first-action prompt — and what is that action?
- Which error states could the system prevent with better validation earlier in the flow?

---

### Activity 3 — Review Flows Against the JTBD Map

**Goal:** Evaluate whether each flow actually helps users complete their job — or adds friction that serves the system, not the user.

**Steps:**

1. **Pull up the JTBD Map** — you need the functional job, emotional job, and social job for each critical path you've mapped.

2. **Step through each flow against the job** — for every step in the flow, ask:
   - Does this step help the user make progress toward their functional job?
   - Does this step create or relieve the emotional friction identified in the JTBD Map?
   - Does this step serve the user — or does it exist because of how the system was built?

3. **Flag the friction points** — mark any step where the answer to one of the questions above is "no" or "I'm not sure." These are candidates for redesign.

4. **Write a one-line rationale for each flagged step** — either "this step exists because [system constraint] — to remove it we would need to [change]" or "this step exists because [user need] — it should stay."

**Debrief prompts:**
- How many steps in each flow exist because of system constraints rather than user needs?
- Which emotional job is hardest to serve through the flow's current structure?
- If you could remove one step from each critical path, which would it be — and what would need to change structurally to make that possible?

---

## Assignment (before next session)

**Deliver annotated task flows for your product's 2–3 critical paths, with edge cases and error states designed.**

1. Map 2–3 task flows → expand each into a full user flow with branches, error paths, and system actions
2. Design all five states for every key screen in each flow (Default, Loading, Empty, Error, Success)
3. Annotate each flow following the handoff format — state labels, triggers, conditions, system actions, error handling
4. Review each flow against your JTBD Map and write a one-sentence assessment: "This flow helps users complete [functional job] by [what it does well]. The biggest remaining friction point is [what still needs work]."

**🤖 AI in Practice prompt:**
> *"I've mapped a user flow for [task name] in [product type]. Here are the steps: [paste your flow as a numbered list]. Help me: 1. Identify which steps are likely caused by system or IA constraints rather than user needs. 2. List the error states and edge cases I'm most likely to have missed. 3. Write specific, plain-language error messages for each error state — the message should tell the user what went wrong and what to do next. 4. Flag any of the five states (default, loading, empty, error, success) that I haven't designed for each key component."*

---

## Related Notion Resources

- [Design Activities by DT Stage — Reference](https://www.notion.so/3248a6b135db810385bdf06991f4f87a) — Prototype stage: interactive Figma, annotated wireframes, task flow documentation
- [Session 3 — Information Architecture](https://www.notion.so/3528a6b135db8118a6aeced23d64b1ee) — User flow shape language, swimlanes, and Assignment 2 (end-to-end flow)
- [Sessions](https://www.notion.so/3238a6b135db81f2a02bfedc222ae3c1) — Program tracker — Session 5

---

*Lesson: Interaction Design & User Flows · Session 5 of 8 · UX Mentoring Program*
