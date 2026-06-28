---
title: "Build the Pattern First"
subtitle: "How to use AI and your design system to prototype smarter — not screen by screen"
type: lesson
program: ux-class
tags: [prototype, AI, figma, design-system, pattern-first, system-thinking]
level: intermediate
duration: "1.5 hrs"
date: 2026-06-16
draft: true
slides: ""
previous-session: "Design Once. Use Everywhere. (Atomic Design)"
next-session: ""
---

## Overview

In the previous session, students built a design system — tokens, atoms, molecules, organisms, templates, and at least one page. They know *how to build systematically*. This session answers *how to prototype that system* — using AI as a collaborator, not just a generator.

The most common mistake designers make when prototyping is starting with a screen. They open Figma (or a coding tool), pick a screen, and start filling it in. Then they do the next screen. Then they realise screens don't connect. Components diverge. States are missing. AI output is inconsistent because every prompt starts from scratch.

**Template-first flips this.** Before touching any screen, you define two things:
1. What components exist — including all their states (empty, loading, error, filled) — from your design system
2. How users move through the product (interaction pattern)

Once that prototype pattern exists, AI can build from it. Students take their prototype pattern and use an AI coding tool to generate a working, browser-viewable prototype — no screen-by-screen design required.

**Why "pattern"?**

The word "pattern" isn't arbitrary — it comes from software engineering. In object-oriented programming, the *Prototype Design Pattern* is a technique where instead of building new objects from scratch every time, you define one prototype object and clone it. Each clone starts identical, then gets customised for its specific use. The principle: define once, reuse many times, customise at the edges.

That's exactly what this lesson does for prototyping. Your component inventory is the prototype. Every screen AI builds is a clone — assembled from the same defined parts, not invented from scratch. Designers who've worked with engineers will find this familiar. Designers who haven't now have the vocabulary to talk about it.

**What is an AI-assisted prototype?**

An AI-assisted prototype (also called a GenAI prototype) is a working, browser-viewable prototype where the screens are *generated* by AI — not designed one by one in a design tool. Instead of placing every element by hand, the designer defines the rules: what components exist, what states they can have, and how screens connect. The AI coding tool reads those rules and assembles the screens from them.

The output is real code — HTML or React — running in a browser. Not a clickable Figma file. Not a mockup. A prototype that a developer, stakeholder, or user can open on any device, interact with, and share via a link.

What makes it "AI-assisted" (not just "AI-generated") is that the designer stays in control of the decisions. You define the system. You set the constraints. You review every screen and correct what's wrong. The AI handles the assembly. The result is faster than building by hand, and more accurate than asking AI to design from a blank brief — because the brief is already written. It's called your prototype pattern.

A realistic expectation: NN/G research (2025) found that AI prototyping tools "follow general directions but lack the sophistication to weigh design tradeoffs." Output is often good at a distance — assembled, interactive, running in the browser — but misses subtleties: spacing, grouping, visual hierarchy, contrast. It will also default to generic visual styles if you don't give it your tokens and your component system. That's exactly what the first two steps of Phase 4 prevent.

Adobe Design's experiment (2026) found the opposite of what most people expect: working closer to the build process made collaboration *more* intensive, not less. Design judgment, taste, and craft didn't disappear — they became more essential because decisions were made in the moment the experience was actually taking shape.

This lesson focuses on the **coded prototype path**: using an AI coding tool to generate HTML or React from the prototype pattern. The prototype pattern is the instruction manual. AI does the assembly.

It also accommodates two starting points. Students who are building their design system for the first time follow **Starting fresh** — generating a prototype pattern from principles up. Students who already have a design system in Figma or code follow **Already have components** — auditing and documenting what already exists. Both entry points produce the same output: a prototype pattern AI can build from.

> **This lesson builds directly on your Atomic Design output.** Students who completed their Figma Template and at least one Page are ready to go. Students who didn't complete it will use a provided starter template — but the lesson will make you want to finish it.

---

## Learning Objectives

By the end of this session, students will be able to:

1. **Explain** why pattern-first prototyping is faster and more consistent than screen-by-screen
2. **Define** a prototype pattern: component inventory (with states) and interaction pattern
3. **Use an AI tool** to analyse their design system and generate a prototype blueprint
4. **Use an AI coding tool** to generate a working prototype from their prototype pattern
5. **Build** at least 1 working screen in the browser with navigation to at least 1 other state

---

## Materials Needed

- Students' Figma files from the Atomic Design session (Templates + at least one Page)
- Starter Figma template (provided for students without completed work)
- Access to an AI chat tool (ChatGPT, Gemini, Claude, or any tool you're comfortable with)
- Access to an AI coding tool (for the coded path — Cursor, GitHub Copilot, or similar)
- Prompt library handout (see below)

---

## Pre-Class Preparation

**For students:**

Before class, check your Figma file against this list. How far you get tells you which entry point you are:

| Level | What to check | Ready? |
|---|---|---|
| Atoms & Molecules | Key components have variants (at minimum: default + one other state) | ☐ |
| Organisms | At least 2 Organisms assembled from your molecules (e.g. nav bar, form, card list) | ☐ |
| Templates | At least 1 Template frame exists per screen in your concept (skeleton layout, no real content) | ☐ |
| Pages | At least 1 Page exists — a Template filled with real text, real images, realistic data | ☐ |

- **All four checked** → Already have components. Bring your Figma file and (if you have one) your codebase.
- **Partially checked or nothing** → Starting fresh. Download the starter template from the class Notion page.
- Make sure you have access to an AI chat tool — use whichever you're most comfortable with
- **Connect your MCP before class.** Set up the connection between your design tool and your AI coding tool (e.g. Figma MCP → Cursor, or similar). This must be working before Phase 4 — troubleshooting it mid-session costs too much time. If you're unsure how, follow the setup guide on the class Notion page.

**For the instructor:**
- Prepare a live demo using your own Figma template (a simple 3-screen flow works well: onboarding → home → detail)
- Have a pre-built coded prototype ready as a "reveal" for the coded path demo
- Load the prompt library into your AI tool before class so you can demo without typing

---

## Session Structure (90 min)

| Phase | Activity | Time |
|---|---|---|
| 1 | Mindset reframe — why pattern-first beats screen-by-screen | 10 min |
| 2 | Generate the prototype pattern — two paths based on what students already have | 20 min |
| — | **Checkpoint: Before you build** | 2 min |
| 4 | Hands-on build — AI coded prototype | 33 min |
| 5 | Share & reflect | 10 min |
| — | **Buffer** | 5 min |

**Entry points at a glance:**

| | Starting fresh | Already have components |
|---|---|---|
| **Who** | Starting fresh, or partial system | Already have Figma system, codebase, or both |
| **AI tool** | AI chat tool | AI chat tool (Figma) · AI coding tool (code) · Both (drift audit) |
| **Activity** | Build prototype pattern from system qualities up | Audit and document what already exists |
| **Output** | Framework document generated from principles | Framework document extracted from existing system |

---

### Phase 1 — Mindset Reframe (10 min)

**The problem with screen-by-screen prototyping**

Open with a demonstration, not a slide. Take a simple 3-screen flow (e.g. Login → Dashboard → Detail). Show what happens when you prototype it screen by screen:
- Each screen is a separate design decision
- Components drift (the button on screen 1 is slightly different from screen 3)
- When the design changes, every screen needs updating
- When you hand it to an AI tool, each prompt starts from zero

Then show the pattern-first alternative:
- Start with the component inventory (what exists)
- Map the interactions (how screens connect)
- Define states (what can change on a component)
- Now every screen is just an *arrangement* of things that already exist

**Key message:** Your design system is not the output of Atomic Design. It is the *input* to your prototype. The Template you built is a blueprint. AI just builds from blueprints.

NN/G research confirms this directly: "longer prompts with clear, detailed design requirements consistently yield better results" with AI coding tools. The prototype pattern *is* that detailed context. Without it, AI fills gaps with assumptions — generic layouts, default styles, misread patterns. With it, AI builds from a complete brief rather than guessing.

**Discussion prompt (2 min — neighbour exercise):** "Turn to the person next to you: if AI could read your entire design file right now and build a prototype, what would it need to know that isn't visible in your designs? 60 seconds. Then share one answer with the class."

Collect 2–3 answers quickly. Common ones: what clicks lead where, what empty/loading/error states look like, what the user is trying to do. These map directly to the two layers of a prototype pattern:

- "What clicks lead where" → **interaction pattern**
- "What components exist and what looks they can have" → **component inventory (with states)**

**In Phase 2, you will build this document.** Everything students just named in the discussion is what they're about to make explicit — for themselves, and for their AI tool.

---

### Phase 2 — Generate the Framework (20 min)

> **Structure:** Class demo (5 min) → Students run their own prompts (10 min) → Regroup and share outputs (5 min)

**Class demo — 5 min**

Before students touch their own files, run Starting fresh live using your own Figma template. Show the complete sequence: system qualities → token decisions → component inventory → product context → prototype pattern. Students don't need to follow along yet — they're watching the rhythm of the prompts and seeing what the output looks like. Point out the moment product context enters and what changes.

---

**Students run their own prompts — 10 min**

Students choose their entry point and run the prompts below. Cap this at 10 minutes. Students with large inventories will want to keep going — tell them the goal is a working prototype pattern, not an exhaustive one. They can complete it in homework.

**What a prototype pattern is**

Regardless of entry point, every student produces the same output by the end of this phase: a **prototype pattern** — a structured description of their design system that AI can build from. It has two layers:

1. **Component inventory** — all components with their variants and states included (default, hover, loading, empty, error, success)
2. **Interaction pattern** — how screens connect and under what conditions

States are part of the component inventory — not a separate layer. When you list a component, you list all the looks it can have right there alongside it.

**Interaction pattern types**

Every screen in a prototype is doing one of a small number of things. Knowing the type helps you map the correct components and transitions:

| Type | What it does | Example screens |
|---|---|---|
| **Read** | User views content — no state change | Dashboard, detail page, profile, feed |
| **Edit** | User modifies existing content | Settings, edit profile, update item |
| **Add** | User creates something new | New post, add to cart, create account |
| **Confirm** | User reviews and approves an action | Order summary, delete confirmation, submit form |
| **Navigate** | User moves between sections | Tab bar, menu, back/forward |
| **Search / Filter** | User queries or narrows a list | Search results, filter panel, sort |
| **Onboard** | User is guided through first-time setup | Welcome screen, tutorial steps, permissions |

Most prototypes use 3–4 of these. When you map your interaction pattern, label each screen with its type — it tells AI exactly what kind of flow to build, what components it needs, and what transitions are required.

How students get there depends on what they already have.

---

#### Starting fresh (no existing system, or partial)

The risk when starting fresh is jumping straight to product context — "I'm building a food delivery app" — and generating UI that looks right but doesn't have a principled system underneath it. Instead, start with how the system should *feel*, then let product context come second.

**Step 1 — Define system qualities, not product (3 min)**

Students describe the qualities they want the system to have — without naming the product:

> "I want to design a system that is [calm / energetic], [minimal / rich], [serious / playful], with [fast / deliberate] interactions. Generate design principles and token decisions — colour scale, type scale, spacing rhythm — from these qualities. Don't assume any specific product."

Your AI tool returns a principled token structure tied to the qualities, not to a product category.

**Step 2 — Generate the Atomic component inventory (4 min)**

From those principles, your AI tool generates a component list that any product built on this system would need:

> "Based on these design principles, what Atomic components does this system need? List atoms, molecules, and organisms with their required states. Keep it product-agnostic — just what the system requires."

**Step 3 — Apply product context (3 min)**

Only now do students bring in their specific concept:

> "My product is [X] for [Y users]. I have this prototype pattern: [paste]. Which components map to my 3–4 screens? What needs adapting? What's missing?"

**Step 4 — Interaction pattern (5 min)**

> "My prototype has these screens: [list]. The user's goal is [goal]. Map the interactions — what does each screen link to, and under what conditions?"

States are already captured in Step 2 as part of the component inventory. Students don't need a separate state map prompt.

**Instructor note:** Walk through Steps 1–2 live before students start. Show them how the AI tool generates a system that could apply to multiple products — then in Step 3, watch it narrow to their specific concept. This is the AI-as-collaborator moment: students see that the system predates the product.

---

#### Already have components (design tool, code, or both)

Having a design system doesn't mean AI can use it. The activity here is the same skill as Starting fresh — make the implicit explicit — but the direction is reversed: extract and document what already exists rather than generate from scratch.

Students choose one of three sub-paths based on what they have:

---

**Components in your design tool**

Most AI chat tools can't read Figma directly. Students bridge the gap by exporting their component names and token values as text and pasting them into their AI tool:

> "Here is my existing Figma design system: [paste component names, variants, and token values]. Document this as a prototype pattern: component inventory with states, and flag anything inconsistent or missing for a prototype."

The AI tool returns the prototype pattern and surfaces gaps the student didn't know existed — duplicate components, missing states, inconsistent naming.

**What to paste into your AI tool:** component names from the Figma layers panel, variant names, and colour/text token names. Students don't need to export assets — text descriptions are enough.

---

> **For designers who already have a codebase.** If you haven't written code before and don't have a component folder, skip straight to the Checkpoint. This path is here for when you need it — not for day one.

**Components in code**

This is the most direct path. An AI coding tool can read component files without any manual export. Students open their AI coding tool, point it at the component library folder, and run:

> "Read my component library and generate a prototype pattern: component inventory with variants and states, interaction patterns, and flag anything incomplete or inconsistent."

The AI coding tool generates the prototype pattern from the actual code. Students review and correct. The Phase 2 exercise collapses into a single prompt — leaving more time for the pre-flight check and build.

---

> **For designers with components in both places.** This path assumes you have an active codebase and a design tool system simultaneously. If you're still building either one, come back to this path when both exist — it won't be relevant on day one.

**Components in both your design tool and code**

The most common real-world scenario, and the most instructive. Students run a **drift audit** — comparing what exists in Figma against what exists in code:

> "Here is my Figma component list: [paste]. Here is my coded component list: [paste]. What exists in Figma but not in code? What exists in code but not in Figma? What's named differently between the two?"

The drift the AI tool surfaces is the gap that exists in almost every real design system. Students then decide: which version is the source of truth for the prototype? Figma or code? That decision becomes the first line of their prototype pattern.

**Instructor note for Already have components:** Students who already have a system sometimes feel this phase is too easy — they paste a list and the AI does the work. Redirect them: "The AI generated the prototype pattern. Now read it carefully. Is this actually your system, or is it the AI's best guess? What would you correct?" The review is the skill, not the generation.

---

**Regroup — 5 min**

Ask 2–3 students to share their prototype pattern on screen for 30 seconds each. You're not reviewing quality — you're normalising what the output looks like. "Does yours roughly look like this? Good. If not, don't worry — we'll use Phase 3 to fill the gaps."

**Convergence point:** by the end of Phase 2, every student — regardless of entry point — has a prototype pattern with a component inventory (states included) and an interaction pattern. Phase 3 applies to everyone equally.

---

---

### Checkpoint — Before You Build (2 min)

Before Phase 4 starts, every student answers three questions out loud (or in writing):

1. **Do I have a prototype pattern?** — component inventory and interaction pattern. If no: finish Phase 2 first.
2. **Do I know which 2–3 screens I'm building?** — not all of them. Pick the core flow only.
3. **Is my MCP connection set up?** — your AI coding tool should already be connected to your design file. If not, raise your hand now.

This is a 2-minute pause, not a discussion. Students who can't answer question 1 finish Phase 2 first. Everyone else moves to Phase 4.

---

### Phase 4 — Hands-On Build (33 min)

> **Prerequisite:** MCP connection between design tool and AI coding tool must be set up before this phase. See Pre-Class Preparation.

**Step 1 — Scope the build (2 min)**
Pick 2–3 screens from your interaction pattern. Don't try to build everything. The goal is to prove the pattern works — not to finish the prototype.

**Step 2 — Sync your design tokens (3 min)**
> "Read my design file via MCP. Extract the design tokens — colour values, typography styles, and spacing. Generate a CSS variables file from these tokens so every screen uses the exact values from my design system."

This runs once. All screens built after this step use your actual design colours and type, not AI defaults. NN/G found that without explicit token guidance, AI tools default to generic visual styles — often resembling common component libraries with neutral colour palettes and minimalist styling that looks interchangeable across products. Token sync is what makes the output look like *your* product, not a template.

**Step 3 — Generate the component inventory (5 min)**
> "Read my design file. Generate a component inventory: list every component with its name, purpose, and all its states (default, hover, loading, error, etc.). Flag anything that looks incomplete or inconsistent."

Students review the output. Correct names or states that are wrong. This becomes the source of truth for the build.

**Step 4 — Generate the interaction pattern (3 min)**
> "Based on the component inventory, map the interaction pattern for my prototype: which screens exist, what connects them, and what triggers each transition. Use the component inventory as your reference."

**Step 5 — Build one screen at a time (20 min)**
> "Build [Screen name] using the component inventory and interaction pattern. Use the design tokens from the CSS variables file. Output React [or plain HTML]. Match component names exactly as listed in the inventory."

After each screen: compare it to your design file. Note what's wrong or missing. Correct before moving to the next screen.

> "This is what you built: [describe]. Here is what should be different: [list corrections]. Update the output."

**Minimum output:** 1 screen running in browser with navigation to at least 1 other state

**What to expect from AI output (set this expectation before students start):**
First screens will be technically assembled but rough — spacing may be off, groupings may not match the design, hierarchy may feel flat. This is normal and documented. NN/G research found that even with detailed prompts, AI output "missed subtle but important details related to spacing, grouping, and hierarchy." The review step is exactly where designer judgment enters. Tell students: the first output isn't the result — it's the starting point.

**Instructor support during hands-on:**
- Circulate and check students are correcting after each screen — not just generating and moving on
- Key coaching question: "Does this match your design? What would you correct before building the next screen?"
- If students feel discouraged by imperfect output: "This is normal — NN/G found AI gets close but misses nuance. Your eye is what makes it right. That's not a bug — that's the job."
- If students skip the review: "The review is where you get AI accuracy. Generation without review is just guessing."
- If MCP connection fails: students fall back to pasting the prototype pattern as markdown text into the AI tool — they still run steps 3–5, just without live file reading

### Phase 5 — Share & Reflect (10 min)

Ask 2–3 students to share their screen for 2 minutes:
- What did you build?
- What did the AI do that surprised you?
- What would have taken longer without the prototype pattern?

**Closing thought for the instructor to land:**

> Screen-by-screen prototyping scales to 3 screens. Template-first prototyping scales to 300. The designers who get hired in the next 5 years won't be the ones who can design faster — they'll be the ones who can *define the system clearly enough that AI can build from it*. That's what you practised today.

---

## Concept Extension — Stitching Prototypes

> **Run this as a separate standalone session for intermediate cohorts.** Do not try to fit it into the same 90-minute session as the pattern-first lesson — it will crowd out the hands-on build time that freshers need most. A dedicated session file should be created for this content.
>
> It can be briefly mentioned during Phase 1 as a third reason why pattern-first matters — one sentence is enough ("Later, you'll see how this same prototype pattern lets you stitch multiple team prototypes into a single journey"). Full teaching belongs in its own session.
>
> For students who finish Phase 4 early, you may share the Nathan Curtis article link as optional reading.

> This concept can be introduced during Phase 1 as a third reason why pattern-first matters, taught as a standalone extension for students who finish Phase 4 early, or expanded into its own session for advanced cohorts.

### What is a Stitched Prototype?

> "A stitch prototype is a collection of prototypes from multiple products, woven together to interactively demo a threaded, complete digital journey."
> — Nathan Curtis, EightShapes

A stitched prototype is not a single Figma file with all your screens. It is a navigable experience assembled from multiple design artefacts — Figma frames, screenshots, coded screens, even lo-fi sketches — connected at the seams so a user (or stakeholder) can walk the complete journey end-to-end.

The individual parts may have been built by different teams, in different tools, at different fidelity levels. Stitching doesn't require them to be consistent. It requires them to be connected.

---

### Why Stitch?

**1. Products span multiple flows and personas — your prototype usually doesn't.**
A student's 3–4 screens might cover a customer journey. But what about the banker who processes the same application? The broker who submitted it? Stitching lets you prototype across personas without duplicating the design system.

**2. Stakeholders see fragments. Stitching shows them the whole.**
Individual team demos are expert demos. "Here's our screen, here's what it does." A stitched prototype is a user demo. "Here's what the customer experiences, from the moment they start to the moment they're done." Those are completely different conversations — and the second one is the one that aligns stakeholders and surfaces the real gaps.

**3. Transitions are where the real design problems hide.**
Screen 2 and Screen 3 look fine in isolation. But what happens between them? Who triggers the transition? What data carries over? What does the user see while they wait? Stitching forces you to design the seams, not just the screens.

---

### How to Stitch

**Step 1 — Define the journey thread**
Before touching any file, write one sentence: *"The user's goal across all screens is [goal]."* This is the thread. Every screen in the stitch must serve this thread. If it doesn't, it doesn't belong — or the thread needs to be longer.

**Step 2 — Gather artefacts, don't rebuild them**
Collect what exists: Figma frames, exported PNGs, coded screens, even annotated wireframes. A stitch prototype is not a redesign. Gather, don't rebuild. If a screen is missing, note it as a gap — don't fill it now.

**Step 3 — Build an index**
Create a homepage for your stitch — a single page that lists every screen in the journey with its current status (complete, in progress, missing). This is the bird's-eye view. Stakeholders can drop in from any point. Designers can see where the gaps are.

**Step 4 — Add the seams**
Connect each screen to the next with navigation links. This is the actual stitching. Seams don't need to be perfect — a clickable button that leads to the next screen is enough. Don't get lost perfecting transitions; get the path walkable.

**Step 5 — Demo the journey, not the screens**
Present the stitch as a user would experience it — start to finish, in character. Don't narrate the design decisions. Narrate the user's goal. "She opens the app wanting to find a home loan. She does this. She sees this. She gets here." One minute. Then stop and invite discussion.

> **Resist fixing seams.** A stitch prototype reveals inconsistency — it is not an audit tool. If you see a button that's slightly wrong or spacing that's off, note it and move on. Turning a stitch session into a design review kills the collaboration that makes stitching work. — Nathan Curtis

---

### How AI Fits

Stitching is where AI becomes genuinely powerful — not at the component level, but at the journey level.

**AI chat tool — identify missing seams**
> "Here is my interaction pattern: [paste]. Here are the screens I've built: [list]. What transitions are undesigned? What does the user see between Screen 2 and Screen 3 that hasn't been prototyped?"

**AI chat tool — generate the index page**
> "Here are my prototype screens: [list each with a one-sentence description and status: complete/in progress/missing]. Generate a simple HTML index page that lists them with their status, links to each, and shows the overall journey flow."

**AI coding tool — build the HTML stitch shell**
For coded prototypes, an AI coding tool can build the navigation shell that connects Figma exports or coded screens into a single navigable experience:
> "I have these screens as separate HTML files: [list]. Build a navigation wrapper that stitches them into a single prototype — a homepage index, back/forward navigation, and a progress indicator showing where the user is in the journey."

---

### Real-World Example

> *Use this with students if relevant — you don't need to show the screens.*

At NAB, five design squads were building separate pieces of a mortgage platform — income verification, document management, credit assessment, settlement, and more. Each squad had its own Figma file, its own prototype, its own demo. No one was showing the banker's complete journey from application to approval.

A stitched E2E prototype was built across all five squads — one shared canvas, navigable end-to-end. The impact: 90% E2E journey coverage, 4 personas aligned, 2–3× more explicit design decisions. The key was not rebuilding anyone's work — just connecting it. The seams were visible. That was fine. The journey was now visible too. That was everything.

---

### The Stitch Mindset

Three things to teach students before they stitch:

1. **It's a throwaway artefact.** A stitched prototype exists to communicate the journey while the product is being built. The day the product ships, the stitch is retired. Don't treat it like a deliverable — treat it like a communication tool with an expiry date.

2. **The goal is the journey, not the screens.** Individual screens will be imperfect. Inconsistencies will be visible. That's the point — stitching surfaces what polished individual demos hide.

3. **One minute hooks the room.** A complete end-to-end demo should take no more than 60 seconds. Walk the user goal, not the design decisions. If you can't tell the story in a minute, the journey isn't clear enough yet.

---

### Resources

- **Nathan Curtis — [Stitching Prototypes](https://medium.com/eightshapes-llc/stitching-a-journey-together-in-a-prototype-d3b86d26ebb)** *(EightShapes, 2015)* — the original article, saved in your Notion Knowledge Sharing library. The Marriott International case study is the clearest illustration of the concept. Assign as pre-reading if you teach this as a standalone session.
- **EightShapes reference** — [eightshapes.com/articles/stitching-a-journey-together-in-a-prototype](https://eightshapes.com/articles/stitching-a-journey-together-in-a-prototype/)

---

## Homework

**Template-first prototype completion**

Extend your prototype from today:
- Add at least 2 more screens to your interaction pattern
- Ensure every component in the new screens comes from your existing design system (no new components without updating the inventory)
- Document one thing AI got wrong and how you corrected it

Submit: a live/repo link or code repository link + a 3-sentence reflection on the AI collaboration experience

---

## Prompt Library Reference

### Starting fresh

| Goal | Prompt |
|---|---|
| Define system qualities | "I want a system that is [calm/energetic], [minimal/rich], [serious/playful]. Generate design principles and style decisions — colour palette, typography, spacing. No product name yet." |
| Generate component inventory | "Based on these design principles: [paste]. What UI components does this system need? List small pieces like buttons and inputs, medium pieces like forms and cards, and bigger sections like nav bars. Include all the states each component needs. Keep it general — not tied to any specific product yet." |
| Apply product context | "My product is [X] for [Y users]. I have this prototype pattern: [paste]. Which components fit my screens? What needs changing? What's missing?" |
| Interaction pattern | "My prototype has these screens: [list]. The user's goal is [goal]. Show me how each screen connects to the others — what does a tap or action lead to? What happens if something goes wrong?" |

### Already have components

| Goal | Prompt |
|---|---|
| Audit Figma system | "Here is my Figma design system: [paste component names, variants, tokens]. Document this as a prototype pattern and flag anything inconsistent or missing." |
| AI coding tool: read codebase | "Read my component library and generate a prototype pattern: component inventory with variants and states. Flag anything incomplete or inconsistent." |
| Drift audit (Figma + code) | "Figma components: [paste]. Coded components: [paste]. What exists in one but not the other? What's named differently? Which should be the source of truth?" |
| Review AI-generated prototype pattern | "You generated this prototype pattern from my system: [paste]. Here is what I know is wrong or missing: [list]. Update the prototype pattern to reflect this." |

### Build Phase — Both Entry Points

| Goal | Prompt |
|---|---|
| Start coded prototype | "Build a prototype from this prototype pattern: [paste]. Use [React/HTML]. Match these naming conventions: [list]." |
| Review AI output | "Does this [code/design] match my interaction pattern? What's missing or inconsistent?" |
| Unstick mid-build | "I'm building [screen]. Available components: [list]. How do I assemble this screen without creating anything new?" |
| Correct AI mistakes | "This output has these problems: [list]. Here is the correct behaviour: [describe]. Fix only these issues." |

---

## Instructor Notes

**Handling mixed completion from Atomic Design:**
Students who didn't complete the Template from the previous session may feel behind. Frame it positively: "This lesson will show you exactly why the Template matters. Use the starter file today, and you'll want to go back and finish your own."

**The most common failure mode:**
Students treat Phase 4 as "free design time" and start inventing new things. The prototype pattern is a constraint, not a suggestion. If a student needs a component that isn't in their inventory, that's a signal — either they missed it in Phase 2, or their concept has shifted. Either way, it's a design decision to make consciously, not accidentally.

**On AI outputs that are wrong:**
When an AI tool generates something incorrect, that's curriculum. Stop the class, show it, and ask: "What did we not tell the AI clearly enough?" This reinforces that AI quality depends on how well you define the prototype pattern — which is exactly the skill this lesson builds.

**Timing notes:**
- Starting fresh students often run long in Phase 2 if they have large component inventories. Cap the prompting at 10 minutes and tell them to finish the prototype pattern in homework.
- Already have components students (especially B2, coded path) will finish Phase 2 significantly faster. Direct them to spend the extra time reviewing the AI's output critically — "what would you correct?" — rather than moving ahead to Phase 3 early.
- Phase 4 always feels too short. Reassure students: the goal is to prove the prototype pattern works, not to finish the prototype.

---

## Recommended Resources

These are resources I'd genuinely point students to — not a complete list, but the ones that make the biggest difference for this specific lesson.

---

### Mindset & Framework Thinking

**[Atomic Design by Brad Frost](https://atomicdesign.bradfrost.com/)** *(free online)*
Still the clearest articulation of why systems beat screens. Students coming from the previous session will have seen this — point them to Chapter 4 specifically, which covers moving from design system to deliverable. This is the conceptual bridge into today's lesson.

**[The Component Gallery](https://component.gallery/)** *(free)*
A curated reference of how real design systems name and structure their components. Useful in Phase 2 when students are auditing their component inventory — if they're unsure what to call something or whether they're missing a component type, this is a faster reference than googling.

---

### Figma Prototype Path

**[Figma Variables documentation](https://help.figma.com/hc/en-us/articles/15339657135383)** *(official docs)*
The authoritative source on Variables — the most important Figma feature for pattern-first prototyping. The section on "modes" is what makes design tokens from the Atomic Design session actually work inside a prototype. Worth reading before class, not during.

**[Smart Animate guide — DesignCourse on YouTube](https://www.youtube.com/watch?v=6Id4INKEwb8)**
The clearest practical walkthrough of Smart Animate I've found. Under 15 minutes. Recommend this to Path A students who haven't used it before — watch it the night before the session, not during.

---

### Coded Prototype Path

**[shadcn/ui](https://ui.shadcn.com/)** *(free, open source)*
The best real-world example of a design system that directly becomes code components. When students ask "what does a coded design system actually look like?", show them this. Recommend this as a reference for what students are building toward — not a template to copy.

**[v0 by Vercel](https://v0.dev/)** *(free tier available)*
A browser-based AI tool for generating UI components from descriptions. More constrained than a full AI coding environment — you describe a component, it generates it, you copy it — but that constraint is useful for students just starting out with AI-generated code. A good stepping stone before moving to a full AI coding tool.

**Your AI coding tool's documentation**
Whatever tool students choose — Cursor, GitHub Copilot, Windsurf, or others — point them to the section on context and codebase indexing. The reason pattern-first works so well with AI coding tools is that they can read your whole project, but only if it's structured clearly. The prototype pattern from Phase 2 is what makes the AI's suggestions accurate rather than generic.

---

### AI Collaboration

**Your AI tool's prompting guide**
Every major AI tool publishes guidance on how to get better results from prompts. The prompt library in this lesson is a starting point, not the ceiling. Encourage students to read the guide for whichever tool they use — specifically the sections on specifying output format and giving the AI a role to play. Both techniques are directly applicable to the prompts in Phase 2.

**[AI-assisted design-to-code workflows — Lenny's Newsletter](https://www.lennysnewsletter.com/)** *(search "AI design prototype")*
Lenny's newsletter has published practitioner walkthroughs of AI-assisted design-to-code workflows across multiple tools. The quality varies, but the best ones are honest about what breaks and why — which is more useful for students than polished demos that make everything look easy.

---

### What I'd Actually Assign

If I had to pick one resource per path:

- **Everyone:** Brad Frost Chapter 4 — before class, 20 minutes
- **Figma prototype students:** Figma Variables docs — skim before class, reference during
- **Coded prototype students:** shadcn/ui homepage — just look at it, understand what a coded design system produces, then come to class ready to build toward that

Everything else is optional depth. Students who finish the hands-on early can explore v0 or their AI tool's prompting guide. Students who struggle should focus on the prototype pattern, not the tools.

---

## Connection to Curriculum

| Session | Role in this lesson |
|---|---|
| Problem Understanding | Defines the user goal that drives the interaction pattern |
| Synthesis & Problem Definition | Defines what success looks like — used to evaluate prototype completeness |
| Design Framework (Atomic Design) | Produces the component inventory and Template that this lesson builds from |
| **This session** | Translates the design system into a working prototype using AI |
| Next session | TBD |
