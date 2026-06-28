---
title: "Design Once. Use Everywhere."
subtitle: "How to build a design system that scales — from your first sketch to every screen"
type: lesson
program: ux-class
tags: [design-system, atomic-design, components, system-thinking, design-framework, intermediate, figma]
level: intermediate
duration: "45 min"
date: 2026-05-15
draft: true
slides: ""
previous-session: "Concept validation (user/stakeholder feedback)"
next-session: "AI-assisted prototype development (Cursor / Claude)"
---

## Overview

In the previous session, students validated a concept with real users or stakeholders. They know *what* to build. This session answers *how* to build it — systematically, at scale, in a way that holds together across every screen, every team member, and every iteration.

Atomic Design is a methodology created by Brad Frost that gives designers a mental model and practical framework for building UI from the ground up. In this lesson it is not treated as an abstract component organisation technique. It is treated as the methodology for **translating a validated concept into a buildable design framework** — one that encodes the product's visual language, defines its reusable parts, and produces screens that can be handed directly to a developer or an AI tool.

The previous session told you what users responded to. This session turns that into something you can actually build from.

Every design decision in this lesson connects directly to the validated concept. Tokens encode the product's personality — the trust, the energy, the approachability that came through in user feedback. Atoms are the building blocks that carry that personality into every screen. Molecules and Organisms are the functional patterns users will actually interact with. Templates validate that the structure works. Pages prove that the concept survives contact with reality.

**The end goal of this session is tangible:** students leave with a completed Template and at least one Page built directly from their own validated concept. Atoms, Molecules, and Organisms are the construction process. Templates and Pages are the output — the proof that the design framework works, and the foundation that every design decision going forward is made against.

> **Looking ahead:** In the next session, students will use AI tools (Cursor or Claude) to build working prototypes directly from the Templates they create here. The Template is not just a deliverable for this session — it is the structural input for the prototype build. Treat the naming, the Organism structure, and the layout with that in mind.

By the end of this lesson, students will be able to think about every UI element they touch in terms of its role within a larger system — not just "this is a button" but "this is an Atom that carries my product's visual language, belongs to three Molecules, and appears on every screen of the Template I built from my validated concept."

---

## Learning Objectives

By the end of this session, students will be able to:

1. **Apply** — the 5-step process (find screens → sketch zones → map to interaction patterns → define tokens → build components) before opening Figma
2. **Distinguish** — the reading direction (top-down, from sketch) from the build direction (bottom-up, from tokens) — and why you need both
3. **Translate** — design principles from validated user feedback into specific token decisions
4. **Build** — the Atomic hierarchy (tokens → atoms → molecules → organisms) from the needs identified in the discovery phase, not from scratch
5. **Assemble** — Organisms into Templates that represent real screen structures
6. **Produce** — a complete Template and at least one Page as the tangible output of the session — the structural input for the next AI-assisted prototype session

---

## Materials Needed

- Students' concept sketches from the previous session (hand-drawn or digital)
- Students' validation feedback notes — at minimum 3 words/phrases from user or stakeholder response
- Figma (with a shared class file for group sessions; students' own project files for private sessions)
- FigJam board or whiteboard for Phase 1 discovery activities
- Reference: Brad Frost's [Atomic Design book](https://atomicdesign.bradfrost.com/) (free online)
- Reference: Muzli article "Building Design Systems with Atomic Design" (saved in your Notion research library)
- Reference: "Xây dựng Design System với Atomic Design – An" (Vietnamese resource, also in Notion)

---

## Pre-Class Preparation

Ask students to do the following before the session:

1. **Bring your validated concept.** Review the feedback you received from users or stakeholders in the previous session. Come with at least three words or phrases that describe how users responded to your concept — the feeling, the tone, the thing they responded to. These will become the inputs for your design token decisions.
2. **Screenshot 2–3 screens from an app in your concept's category.** If you're building a fintech product, look at how GoPay or Momo handles its UI. If you're building a marketplace, look at Shopee or Chợ Tốt. Don't copy — audit. Notice which elements repeat, how spacing behaves, what the visual personality is.
3. **Optional read:** Skim the introduction and Chapter 1 of Brad Frost's Atomic Design (link above). No need to read all of it — just enough to have a first impression to discuss.

---

## Session Plan

| Act | Block | Topic | Duration |
|---|---|---|---|
| 1 · Why | Opening | Bridge from last session → the drift → experience architecture | 8 min |
| 2 · What | Map | 5-step process map | 2 min |
| 3 · Read | Teaching | Steps 1–2: find screens + sketch zones | 4 min |
| 3 · Read | Activity 1 | Steps 1–2 Sprint — students work from their own sketch | 8 min |
| 4 · Bridge | Teaching | Step 3: map zones to interaction patterns (Organism reveal) | 5 min |
| 4 · Build | Teaching | Steps 4–5: tokens + Atomic build → system/product framing | 11 min |
| 5 · Payoff | Close | Homework → prototype teaser | 7 min |

**Total: 45 min**

> **Story logic:** Act 1 makes students feel the problem and understand the stakes before showing any solution. Act 2 gives the full map so every subsequent slide feels like progress. Act 3 is hands-on first — students discover from their sketch before any Atomic theory lands. Act 4 opens with Step 3 (the bridge moment: zones = interaction patterns = Organisms), then builds the full hierarchy bottom-up. Act 5 closes the loop with homework as the natural next step.
>
> **For verbal delivery:** Individual Atom/Molecule/Organism breakdowns, 8pt grid, Figma component mapping, and naming convention detail are in the Core Content section below — deliver verbally alongside the Atomic hierarchy slide.

---

## Core Content

### The 5-Step Process — Overview

Before teaching any Atomic Design theory, show students the complete process they will follow in this session and in their homework. Seeing the full map first removes the anxiety of "where do I even start?" — which is the most common reason students open Figma with a concept sketch and immediately start drawing screens without a system.

The process is a single linear flow — no phases, no branching:

```
Step 1 — Find your screens       (from your sketch: pick the 2–3 that were validated)
Step 2 — Sketch your zones       (strip the screen to grey rectangles, name each one)
Step 3 — Map to interaction patterns  (connect zone names to design system vocabulary)
Step 4 — Define or adopt tokens  (build your own OR pick an existing system to override)
Step 5 — Build Atomic components (Atoms → Molecules → Organisms → Template → Page)
```

**The critical insight:** Steps 1–3 are reading work — you are extracting what you need to build from a sketch that already exists. Steps 4–5 are building work — you build purposefully because Steps 1–3 told you exactly what to build. Most students skip the reading and go straight to Figma, building components without knowing what screens they serve. The result is a component library that doesn't match the actual product. Steps 1–3 are the compass. Steps 4–5 are the construction.

**Step 3 is the bridge.** When students name their zones in Step 2 ("navigation", "search area", "action bar"), they are doing something they don't realise yet: they are mapping interaction patterns. In Step 3, they connect those plain-language names to the design system vocabulary — Navigating, Searching, Confirming. And those patterns are Organisms in Atomic Design. This is the reveal moment. Deliver it as recognition, not new information.

---

### Steps 1–3 — Read the Sketch

#### Step 1 — Find Your Screens

Open your concept sketch from the previous session. You are not redesigning anything. You are reading what you already made.

Ask: what are the 2–3 screens that represent the core of this concept? Not every screen — just the ones that are essential to what was validated. If users validated a checkout flow, those screens are home, product detail, and checkout. If they validated a social feed, those screens are the feed, the post, and the profile.

These become your **Pages** — the destination you are building toward. Everything else in the process exists to make these screens hold together.

#### Step 2 — Sketch Your Zones

**What is a skeleton?**
A skeleton is a stripped-down layout of one key screen — every image replaced with a grey box, every heading replaced with a horizontal line, every button replaced with a plain rectangle. No colour, no real text, no visual detail. What remains is the bare structure: which zones exist, how they're arranged, and what spatial relationships hold the screen together.

Think of it like the frame of a building before the walls go up. You can see exactly how many rooms there are, how big each one is, and how they connect — without any furniture or decoration getting in the way.

**Why do this, not just look at the sketch?**
A concept sketch is full of content decisions (this product photo here, this heading copy there) that make it hard to see the structure underneath. Stripping it to a skeleton forces you to separate *layout* from *content* — and layout is what the design framework actually needs to encode.

**How to do it:**
Open your key screen from Step 1. Create a new blank frame the same size. Using only rectangles, redraw the zones — not the content inside them. Label each rectangle with what it *is*, not what it contains:

```
┌─────────────────────┐
│  navigation area    │  ← a grey bar at the top
├─────────────────────┤
│                     │
│  content feed       │  ← the main scrollable zone
│                     │
├─────────────────────┤
│  primary action     │  ← a sticky bar at the bottom
└─────────────────────┘
```

This labelled grey-box layout is your **Template** — the structural blueprint of the screen. It's the same concept as a wireframe, but its explicit purpose here is to reveal Organisms, not just plan layout.

**Why this step matters before building anything:** if you skip it, you will build Organisms before you know what screen they belong to, Atoms before you know what Molecules they serve, and tokens before you know what visual decisions the screens actually require.

#### Step 3 — Map Zones to Interaction Patterns

This is the bridge step — and the most important one in the process.

Look at the zone list from Step 2. Each zone has a plain name: "navigation", "content feed", "action bar". Now ask a different question: what is the user *doing* in each zone?

- "navigation" → the user is **Navigating**
- "content feed" → the user is **Searching** or **Selecting**
- "action bar" → the user is **Confirming** or **Adding**

These are **interaction patterns** — a design system vocabulary for describing what a user is trying to accomplish, independent of the visual design. Common patterns: Navigating, Searching, Filtering, Adding, Selecting, Editing, Confirming, Notifying, Sharing.

**Why this matters:** interaction patterns are how mature design systems organise their components. A search pattern always needs the same building blocks — input, icon, trigger, results list — regardless of whether it's used on the home screen or a checkout screen. Define the pattern once, and every screen that needs it pulls from the same components.

**The Organism reveal:** In Atomic Design, each of these interaction pattern zones is called an **Organism** — a self-contained, reusable section of the UI. When you named your zones in Step 2, you were already defining your Organisms. Deliver this as recognition: *"Those zones you named in your skeleton? In Atomic Design, those are called Organisms. You already know what you need to build."*

**How to do Step 3:** Take your zone list from Step 2. Beside each zone name, write the interaction pattern it maps to. Then write the Atomic `o/` name:

| Zone (Step 2) | Interaction pattern (Step 3) | Organism name |
|---|---|---|
| navigation | Navigating | `o/navigation` |
| content feed | Searching + Selecting | `o/content-feed` |
| action bar | Confirming | `o/action-bar` |

This table is your **build list** for Steps 4 and 5. You are no longer building blind.

---

### Experience Architecture — Why the System Scales

Before diving into Phase 2, show students why building a design system matters beyond one product, one screen, or one journey. This is the framing that separates "I made a component library" from "I built a design framework."

**The four-level model:**

| Level | Name | Example |
|---|---|---|
| 1 | User journey | Laura applies for a new loan |
| 2 | User story | Laura provides her income details |
| 3 | Interaction pattern | Adding |
| 4 | Components | Form fields, buttons, validation messages |

**The key insight to deliver verbally:**
Take two completely different user journeys — "applying for a loan" and "updating a profile." Different goals, different screens, different stories. But at Level 3, both require an "Adding" pattern. At Level 4, both use the same form fields and buttons. The journeys diverge at the top and converge at the bottom. A component built for one journey is automatically available to every other journey that needs the same pattern.

This is how mature design systems are structured in practice. GOV.UK Design System organises their work around service patterns ("apply for something", "pay for something") that map directly to reusable components. IBM Carbon and Atlassian follow the same logic — journeys at the top, shared components at the base.

**How it connects to Atomic Design:**
The four levels map directly onto the Atomic hierarchy:

| Experience architecture | Atomic Design |
|---|---|
| Components (Level 4) | Atoms + Molecules |
| Interaction patterns (Level 3) | Organisms |
| User stories (Level 2) | Templates |
| User journeys (Level 1) | Pages (and beyond) |

Atomic Design is the methodology for building Levels 4 and 3. The experience architecture is the reason Levels 1 and 2 hold together.

---

### Steps 4–5 — Build the System

Steps 4 and 5 are where Atomic Design comes in. Now that Steps 1–3 have told you exactly what you are building — your zone list, your interaction patterns, your Organism names — you use the Atomic hierarchy to build purposefully rather than arbitrarily.

#### Step 4 — Define or Adopt Design Tokens

Before any components, establish your token foundation. You have two paths:

**Path A — Build your own tokens.** Sit with your validation feedback. Extract 3–5 words or phrases that describe what the concept needs to feel like: "trustworthy and clear", "fast and familiar", "playful but focused". These are your **design principles** — not aesthetic preferences but design arguments. Every token decision should be traceable to at least one.

**Path B — Adopt an existing system.** If you're under time pressure or building a prototype, start from Material Design 3, Ant Design, or Radix UI and override the tokens that matter for your concept's personality: primary colour, border radius, and base spacing. The system gives you everything else.

Either path is valid. Tokens are named values for colour, spacing, typography, border radius, and shadow — the translation of your concept's personality into design decisions.

**"Trustworthy"** → `color/primary` is a deep, calm blue. Not bright. Not thin. Stable.
**"Fast"** → `space/sm = 8px`, `space/md = 16px`. No generous padding. Tight and direct.
**"Approachable"** → `radius/md = 8px`. Rounded, not sharp. Buttons feel tappable, not clinical.

In Figma, tokens live as Variables and Styles. Define at minimum: 3 colour tokens, 2 typography tokens, 2 spacing tokens. Use a consistent naming convention: `color/primary/default`, `text/body/regular`, `space/sm`.

**The rule:** if a token decision cannot be traced back to your concept's personality — or to the adopted system you chose — it is a personal preference, not a framework decision. Challenge yourself on every value.

#### Step 5 — Build Atomic Components (Atoms → Molecules → Organisms → Template → Page)

Step 5 is the full build. Everything below is the construction sequence — work through it in order. Each level depends on the one below it.

##### 5a — Build Atoms from Tokens

Atoms are the smallest possible UI elements — individual pieces that cannot be broken down further without losing their function. A button, a text label, an icon, an input field.

Build only the Atoms you actually need, based on what your Organisms (from Step 3) require. If your Organisms include `o/navigation` and `o/search-header`, you need: icon, label, input, button. Build those. Do not build Atoms speculatively.

Every Atom must use only token values — no hardcoded colours, no arbitrary spacing. If an Atom needs `#2563EB`, there must be a token named `color/primary/default` that holds that value. The Atom references the token. Not the other way around.

Use Figma Variants to hold all states of an Atom (default, hover, disabled, error) in a single component set.

##### 5b — Build Molecules

Molecules combine Atoms into one functional unit with one clear job. A search bar is a Molecule: icon + input + button, assembled into a unit whose sole job is to accept a search query.

Build the Molecules your Organisms need. Each Molecule must use your Atom component instances as nested elements — not copies, not detachments. When you edit an Atom, every Molecule using it updates. That cascading update is the system doing work on your behalf.

**The test:** a Molecule has one job. If it appears to do two things, it is probably an Organism.

##### 5c — Build Organisms

Organisms are the self-contained UI sections you named in Step 3 (your interaction pattern zones). Now you build them — from the Molecules and Atoms you built in Steps 6 and 7.

Each Organism must be complete and independent enough to appear on a different screen without requiring contextual explanation. `o/navigation` should work on the home screen, the search results screen, and the checkout screen without modification.

**The reusability test:** can this section be dropped unchanged onto a completely different screen and still make sense? If yes — it is an Organism. If it needs surrounding context — it is still a Molecule.

##### 5d — Assemble Templates

Take the template skeletons from Step 2 and replace the grey placeholder zones with your real Organism component instances. Do not add real content yet. The Template is about structure — proving that the Organisms fit together, that the layout decisions from Step 2 actually work with real components.

A completed Template answers: *does the structure work?* It uses placeholder text and image blocks, not real data.

##### 5e — Fill to Pages

Duplicate the Template. Fill it with real content — real product names, real images (or placeholder descriptions), real prices, real user names. This is your Page.

Watch for what breaks: text that overflows, images with wrong ratios, empty states you haven't designed. Every breakage is a design decision you deferred. Note them — they are the next iteration's starting point.

A completed Page answers: *does the framework survive contact with reality?*

---

---

> **Reference material — Phase 2 deep dive.** The sections below provide detailed teaching notes on each Atomic level, Figma mapping, tokens, and naming. Use these during Core Content delivery of Phase 2 (Steps 4–10). They supplement the step-by-step process above with the rules, tests, and Figma specifics students need to build correctly.

---

### The Atomic Design Framework — Level Reference

Atomic Design was introduced by Brad Frost in 2013, drawing a direct analogy from chemistry. Just as all physical matter is made of atoms that combine into molecules, which combine into organisms, which combine into living systems — all UI is made of small elements that combine into progressively larger and more complex structures. The naming is not decorative. It is literal.

The framework defines five levels, built from the smallest to the largest.

#### Atoms

Atoms are the smallest possible UI elements. They cannot be broken down further without losing their function. A button is an Atom. A text label is an Atom. An icon, an input field, a colour swatch, a font style — all Atoms. They are the raw materials of the system.

In Figma, Atoms are your base components: components with no other components nested inside them. Use **Variants** to hold all states of an Atom — default, hover, focused, disabled, error — within a single component set rather than creating separate components for each state.

**The defining rule:** an Atom defines one unit of behaviour or style. If an element appears to do two separate things, it is likely a Molecule in disguise.

#### Molecules

Molecules are two or more Atoms combined to form a simple, functional unit with one clear job. A search bar is a Molecule: it is made of an input field, an icon, and a button — three Atoms — assembled into one functional unit whose single job is to accept a search query. A form field (label + input + error message) is a Molecule. A card header (avatar + name + timestamp) is a Molecule.

In Figma, Molecules are components that contain other component instances nested inside them. This is the key technical distinction: when you edit an Atom, every Molecule built on it updates automatically. The hierarchy is doing work on your behalf.

**The test:** a Molecule has one clear job. If it seems to do two separate things, it may already be an Organism.

#### Organisms

Organisms are complex, self-contained sections of the UI made from groups of Molecules — and sometimes Atoms directly. They are the first level that can truly stand alone. A navigation bar is an Organism. A product card grid is an Organism. A login form, a comment thread, a checkout summary — all Organisms.

**The test:** could this section be dropped unchanged onto a completely different screen and still make sense on its own? If yes, it is an Organism. If it needs surrounding context to make sense, it is probably still a Molecule.

**The power:** Organisms are the first level where you gain true reusability. Change an Organism once and every screen that uses it updates. This is where the system starts to return the investment of building it correctly.

#### Templates

Templates are arrangements of Organisms placed within a page layout — structure without real content. A Template uses placeholder boxes, wireframe-level fidelity, and generic labels to show the layout decisions before any specific content has been placed. A checkout page Template. A dashboard Template. A product detail page Template. The content is absent; the structure is the point.

Templates answer one question: *does the structure work?*

#### Pages

Pages are the high-fidelity version of a Template, filled with real content — real photos, real product names, real prices, real user data from an actual account. Pages reveal whether the system holds up under real conditions: long text that breaks a layout, a missing image, an empty state that was never designed, a product name in Vietnamese that is twice the length of the English placeholder.

Pages answer a different question: *does the system survive contact with reality?*

#### The Direction Flip

The most important insight in Atomic Design is directional. Designers build bottom-up — defining Atoms before Molecules, Molecules before Organisms, Organisms before Templates, Templates before Pages. But users experience the product top-down. They open a Page, navigate through Organisms, interact with Molecules, and tap Atoms — without ever thinking in those terms.

Good system designers hold both directions simultaneously: building from the small while always designing for the whole.

---

### Atomic Design in Figma (2026)

Brad Frost described Atomic Design as a methodology, not a tool. Since 2013, Figma has become the industry standard, and its component architecture maps cleanly onto the Atomic hierarchy:

| Atomic Level | Figma Equivalent |
|---|---|
| Atoms | Base components — no nested sub-components; states held in Variants |
| Molecules | Components with nested Atom instances |
| Organisms | Complex components or component sets with nested Molecules |
| Templates | Low-fidelity frames with placeholder content |
| Pages | High-fidelity frames with real data |

#### Design Tokens — The Layer Beneath Atoms

Before building a single Atom, define your **design tokens**: named values for colour, spacing, typography, border radius, and shadow that every component in the system will reference. In Figma, tokens live as Variables and Styles.

Tokens are the DNA of a design system — and for a validated concept, they are the most direct translation of user feedback into design decisions. The words users used to describe your concept are token decisions in disguise. "Trustworthy" is a `color/primary` decision. "Approachable" is a `border-radius` decision. "Clean and focused" is a `spacing` decision. Before you define a token value, ask: *does this encode what users responded to?*

Change a token and every Atom built on it updates across the entire product automatically. Without tokens, even a well-organised component library becomes inconsistent the moment someone changes a colour — because that change has to be hunted down manually in every component that used it.

The stack looks like this: Tokens are the foundation. Atoms are built on tokens. Molecules are built on Atoms. Organisms are built on Molecules. The system compounds — upward and downward. Every good token decision propagates up through every screen. Every bad one does too.

#### Component Variants

Figma's Component Variants let a single Atom hold all of its states in one component set. This keeps the Atom layer clean and prevents a button from fragmenting into five separate, unrelated components. When the button's padding needs to change, it changes once — across all states, everywhere it is used in the product.

---

### Naming & Organisation

A design system without a consistent naming convention is difficult to navigate and impossible to hand off. The standard convention uses level prefix, element type, and variant:

```
[level] / [element-type] / [variant]
```

Where `a/` = Atom, `m/` = Molecule, `o/` = Organism. For example: `a/button/primary`, `a/button/disabled`, `m/search-bar/default`, `m/form-field/error`, `o/navigation/mobile`.

The `/` separator is not cosmetic — Figma uses it to create automatic folder grouping in the Assets panel. `a/button/primary` and `a/button/disabled` both appear inside a `button` folder, inside an `a` group. No manual sorting required.

#### The 8pt Grid

All spacing values in an Atomic system should be multiples of 8: 8, 16, 24, 32, 48, 64px. This creates visual rhythm and eliminates arbitrary spacing decisions from every component you build. Atoms built on 8pt values align naturally inside Molecules. Molecules align naturally inside Organisms. The grid is invisible infrastructure — users never see it, but they feel its absence when it is missing.

In Figma, set spacing tokens to 8pt multiples and apply them via Auto-Layout padding and gap values. When every component uses token-driven 8pt spacing, components snap together without friction — and developers can implement them predictably.

#### Documentation

A design system without documentation is a system only its creator understands. For every Organism and above, document at minimum: what it is, when to use it, and what it contains. Use Figma's component description field for inline notes, and Notion, Storybook, or Zeroheight for the broader system guide.

Without documentation, the system will be broken the first time someone who was not in the room when it was designed tries to use it.

---

### Key Takeaways

**Read first. Then build.** You cannot build purposefully without first discovering what you need. Steps 1–3 are reading work — from sketch to zones to interaction patterns. Steps 4–5 are building work. Skipping Steps 1–3 is why most component libraries don't match the actual product.

**Your sketch already contains your framework.** The concept sketch from the previous session is not a starting point for visual design — it is the source of your template skeleton, your Organism list, and your build priorities. Read it as a structural document first.

**Tokens encode the concept. Every other decision inherits from them.** The words users used in feedback are token decisions in disguise. Before setting a token value, ask: can I trace this decision back to what was validated?

**Templates and Pages are the output. Everything else is the process.** Atoms, Molecules, and Organisms are construction work. The Template is where you validate structure. The Page is where you validate reality. If you leave without both, the system exists only as components in an assets panel — not as design decisions applied to real screens.

**Design decisions compound — in both directions.** Build Atoms well and every Molecule, Organism, and screen inherits good decisions. Build Atoms badly — wrong spacing, hardcoded colours, no token — and every level inherits those mistakes. The system amplifies whatever you put into the foundation.

**Your Templates are structural contracts, not one-off screens.** A Template built from real Organisms can become any page that needs the same structure. The same Template can serve a product listing, search results, or category page — by changing only the Page content inside it. That is the compounding value.

> *"Find the screen. Sketch the zones. Map the patterns. Build from tokens. Ship to the Page. The five steps are the path."*

---

## Practice Dataset

For students who don't bring their own project: use a 3–4 screen flow from a Vietnamese app they know well — Grab, Shopee, or Zalo. Suggest they screenshot 3 screens from a single flow (e.g. Grab: home → select destination → confirm ride) and import them into Figma as reference images to audit.

Alternatively, provide a pre-built "messy" Figma frame — 4 screens with inconsistent components, no naming, no token use — and ask them to map the Atomic hierarchy and identify what's broken.

---

## Industry Case Studies

Use these during the Core Concept or Debrief to ground the theory in real decisions made by real teams. Each company faced a version of the same crisis — growth outpaced structure — and Atomic Design was part of how they responded.

---

### Airbnb — Design Language System (DLS)

**The problem before**
Airbnb scaled from a small startup to a global platform with dozens of product designers working simultaneously across web, iOS, Android, host tools, and Airbnb for Work. Each team was making independent design decisions. The result: buttons that looked slightly different per platform, card layouts that varied by team, spacing decisions made from scratch on every new screen. When a designer joined a new squad, they had no shared reference — just a folder of past screens to reverse-engineer.

The hidden cost was not just visual inconsistency. Every time a designer needed a button, they rebuilt it. Every time an engineer needed to implement a card, they asked a designer. The system was burning hours on decisions that should have been made once.

**Why they changed**
The tipping point was cross-platform parity. Airbnb's product needed to feel like one experience whether you were booking on desktop, iOS, or Android. With separate teams building separately, parity was impossible to maintain manually. They also faced a growing design-engineering gap — designers in Sketch, engineers in React Native, and nothing reliably connecting the two.

**What they built**
Airbnb created the Design Language System (DLS) — a set of shared components, tokens, and guidelines built on Atomic principles. Atoms (icons, colours, typography) were defined once and shared across platforms. Molecules and Organisms were implemented as React Native components that rendered correctly on both iOS and Android from a single codebase. They also built React Sketch.app, an internal tool that could render live React components directly inside Sketch — closing the gap between design files and production code.

**The outcome**
Design decisions made at the Atom level cascaded automatically across every platform. Updating the primary button colour meant updating one token — not hunting through dozens of files across three platforms. Teams could move faster because the foundational decisions were no longer up for debate.

---

### Shopify — Polaris

**The problem before**
The Shopify admin interface had grown organically for years. New features were added by different teams at different times, each making reasonable local decisions. The overall result was a patchwork: some pages used one button style, others used a slightly different one; form layouts varied; error messages were worded and positioned inconsistently. For merchants using Shopify daily, the experience was functional but subtly exhausting — small inconsistencies that add up to cognitive friction.

The problem became critical when Shopify opened its platform to third-party developers. Thousands of app developers started building on top of Shopify's admin, and each built their own components. Merchants installing third-party apps encountered interfaces that looked nothing like Shopify. The platform felt fractured.

**Why they changed**
Shopify needed a system that could be used not just internally, but by the entire external developer ecosystem. The design system had to be documentable, distributable, and implementable by engineers who had never spoken to a Shopify designer. That required a level of specificity and structure that the existing ad-hoc approach could never provide.

**What they built**
Polaris launched in 2017 as Shopify's open-source design system. It is structured on Atomic principles: design tokens at the foundation (colour, spacing, typography, shadow), then Components (Atoms and Molecules like buttons, inputs, cards), then Patterns (Organisms and Templates like data tables, page layouts, navigation structures). Every component ships with React code, design specs, usage guidelines, and explicit do/don't examples. Third-party developers building Shopify apps use Polaris components — which means merchants experience a coherent interface even when they install apps from fifty different developers.

**The outcome**
Polaris is now one of the most widely-used open-source design systems in the world. Internally, it reduced design-engineering handoff time significantly. Externally, it gave Shopify's app ecosystem a consistent visual identity without requiring central oversight of every app.

---

### IBM — Carbon Design System

**The problem before**
IBM is not one product — it is hundreds. Watson, IBM Cloud, IBM Security, IBM Maximo, Cognos, and dozens more enterprise software products, many of which were acquired rather than built internally. Each product had its own design language, its own component library, its own interaction patterns. An enterprise client using IBM Cloud and IBM Security in the same workday was moving between two completely different visual worlds.

The accessibility problem was equally serious. Enterprise software is subject to WCAG compliance requirements, and with each product team managing its own components, accessibility standards were applied inconsistently. Some components passed. Some did not. Auditing hundreds of products independently was not scalable.

**Why they changed**
IBM launched its Enterprise Design Thinking initiative to bring design discipline to a company historically dominated by engineering culture. The design systems effort was part of that — a recognition that at IBM's scale, consistency cannot be achieved through guidelines alone. It requires shared infrastructure. Carbon was built to be that infrastructure: one system that all IBM product teams could pull from, ensuring that every token, every component, and every pattern met the same quality and accessibility bar before it reached a product team.

**What they built**
Carbon Design System is one of the most explicitly Atomic design systems in the industry. Its documentation describes the hierarchy directly: Design Tokens at the foundation (over 400 tokens covering colour, spacing, motion, and more), then Elements (Atoms — individual UI primitives), then Components (Molecules and Organisms), then Patterns (recurring multi-component layouts), then Layouts (page-level Templates). Every component ships accessibility-tested, with WCAG 2.1 AA compliance documented explicitly.

**The outcome**
Carbon is now used across all IBM software products and is open-source. When a new IBM product team starts, they do not design their Atoms from scratch — they inherit them from Carbon. An accessibility fix to a token in Carbon propagates across every product using it. IBM estimates that Carbon saves thousands of design and development hours per year across the organisation.

---

### Atlassian — Atlassian Design System (ADS)

**The problem before**
Atlassian grew through acquisition. Jira (enterprise project management), Confluence (team wiki), Trello (visual task boards), Bitbucket (code repositories), and Statuspage were each built by separate teams with separate design languages. When Atlassian acquired Trello in 2017, the problem became impossible to ignore: users who worked across multiple Atlassian products every day were experiencing jarring context switches. Jira felt dense and information-heavy. Trello felt light and card-based. Confluence felt like a document editor. They were designed for different audiences, by different teams, at different times.

The internal problem was equally pressing. Each product team was maintaining its own component library. When Atlassian wanted to ship a new interaction pattern (say, a new type of in-app notification), every team had to implement it separately. There was no shared infrastructure to push changes through.

**Why they changed**
Atlassian's strategic direction required the products to feel like one connected platform — Atlassian Cloud. Users should be able to move between Jira, Confluence, and Trello and feel continuity, not disconnection. That continuity had to be built from shared foundations, not retrofitted onto separately-evolved codebases. A unified Atomic Design system was the only viable path.

**What they built**
The Atlassian Design System (ADS) established shared tokens, a component library, and interaction guidelines that apply across all Atlassian products. The system uses Atomic principles: a foundation layer of tokens (colour roles, spacing scale, typography), a component layer (individual UI primitives built from those tokens), and a patterns layer (recurring multi-component compositions like empty states, inline edit, and loading skeletons). All components are built in React and available as an open npm package.

**The outcome**
Products that were once visually disconnected now share the same button, the same form field, the same notification component. When ADS ships an update to a component, all products using it inherit the change. The team also documented a formal process for proposing new components to ADS — so that if one product team solves a new design problem, their solution can become part of the shared system rather than staying siloed.

---

### Spotify — Encore

**The problem before**
Spotify runs on a squad model — small, autonomous product teams that own their area of the product end to end. The squad model is good for speed and ownership, but it is structurally hostile to design consistency. By the time Spotify had 200+ designers and hundreds of engineers working across Desktop, Mobile, Web, the Creator tools, and Podcast Studio, each squad had accumulated its own set of local design decisions. The result was a product that looked mostly coherent on the surface but was held together by coincidence and good individual taste, not by shared infrastructure.

The maintainability cost was enormous. When Spotify wanted to update its primary purple to a slightly different shade, the change had to be tracked down across dozens of separate implementations in dozens of separate codebases. There was no single source of truth to update.

**Why they changed**
Spotify's scale made the squad model's design debt untenable. More importantly, the product was expanding into new surfaces — smart speakers, car screens, embedded players, wearables — that required components to be defined at an abstract enough level to be rendered correctly across contexts. A button needed to exist as a concept before it existed as pixels, so that each surface could render it appropriately. That required Atomic thinking: define the token and the component first, then let each surface implement the rendering.

**What they built**
Encore is Spotify's design system, built explicitly on Atomic foundations. It separates concerns across three layers: Foundations (tokens — colour, typography, spacing, motion), Components (reusable UI building blocks), and Patterns (higher-order compositions for recurring problems). Encore ships to web, iOS, Android, and TV surfaces from shared source definitions, with platform-specific rendering handled by each platform's implementation layer.

**The outcome**
A colour token change in Encore's foundation propagates to every Spotify surface simultaneously. New product surfaces can onboard to Encore without rebuilding their component foundation from scratch. The design and engineering teams share a single vocabulary — when a designer says "primary button," every engineer knows exactly which component that maps to in every codebase.

---

### How AI is changing Atomic Design implementation today

These companies faced their Atomic Design challenges before AI was available as a practical tool. The teams that built these systems did it largely by hand — manually auditing inconsistencies, writing documentation, enforcing naming conventions through code reviews, and running design critiques to catch component drift. Today, AI is changing several of those workflows significantly.

**Detecting inconsistency at scale**
The most immediate AI application is automated auditing. Tools can now scan a Figma file or a codebase and identify every place where a component was built as a one-off instead of using a shared component, every place where a colour was hardcoded instead of using a token, and every place where spacing deviates from the 8pt grid. IBM uses internal AI tooling to check Carbon compliance across product codebases before release. Shopify has integrated AI-assisted linting into its development workflow to flag Polaris violations before they reach production.

**Generating components from intent**
Tools like GitHub Copilot, Vercel's v0, and Locofy can take a design brief — "a product card with image, title, price, and a primary CTA button" — and generate production-ready code using the team's existing Atomic component library. Instead of an engineer translating a Figma frame manually into components, they describe what they need and the AI assembles it from the correct Atoms and Molecules. The quality depends entirely on how well the design system is defined — which is why good Atomic Design practice makes AI assistance more effective, not less necessary.

**Writing documentation automatically**
One of the most time-consuming parts of maintaining a design system is documentation. AI can now generate first drafts of component descriptions, usage guidelines, and do/don't examples from the component's code and design spec. Atlassian has experimented with using AI to maintain ADS documentation as components evolve, reducing the lag between a component being updated and its documentation catching up.

**Figma's own AI features**
Figma introduced AI-assisted features that are directly relevant to Atomic Design practice: the ability to detect visually similar components that should be unified, the ability to suggest an existing library component when a designer starts drawing something that already exists, and auto-naming for layers and frames based on their visual content. These features nudge designers toward reusing Atoms and Molecules rather than creating one-offs — which is exactly the behaviour Atomic Design is trying to build.

**The important caveat**
AI accelerates Atomic Design implementation — it does not replace the thinking. An AI tool can tell you that you have 47 slightly different button variants in your Figma file. It cannot tell you which one should become the canonical Atom, or whether the variation exists for a good reason or as an accident. The design judgment — what should be a token, where the boundary between Molecule and Organism lies, what to do with legacy components that can't be refactored immediately — still requires a designer who understands the system. AI makes the execution faster. It does not make the decisions.

---

Full instructions for each activity. Use the Run-of-Show for timing and facilitation context.

---

### 🗺️ Activity 1 — Steps 1–2 Sprint: Sketch to Zones
**Type:** In-class · FigJam or paper
**Time:** 8 min
**Format:** Solo (each student works from their own validated concept sketch)

**What it is:**
Students work through Steps 1–2 of the process using their own concept sketch. The output is a named zone skeleton — structure visible, content stripped away. Step 3 (mapping zones to interaction patterns) follows immediately after as a taught moment, building directly on what students produced here.

**Setup (before class):**
- Ask students to have their concept sketch accessible (photo of hand-drawn, or digital file)
- Prepare a FigJam board with one blank area per student, or have students use paper
- Template: a blank phone frame (or desktop frame) drawn large enough to label zones

**Instructions for students:**

1. **(2 min) — Step 1: Find your screens.** Look at your concept sketch. Circle the 2–3 screens that are essential to what was validated. Write their names: "home", "product detail", "checkout". These are your Pages — the destination.

2. **(4 min) — Step 2: Sketch your zones.** Pick your most important screen. In the blank frame, strip out all content and redraw only the layout zones as grey rectangles. Label each zone with what it *is*, not what it contains: "navigation area", "content feed", "action bar". This is your Template skeleton.

3. **(2 min) — Share.** Each student reads out their zone list. Winnie listens for: are these genuinely separate sections, or are two zones actually one?

> **After the activity:** lead immediately into Step 3 — ask students what a user is *doing* in each zone. Their answers are the interaction patterns. Walk through the mapping together as a class.

**Facilitator watch-fors:**
- Students who list 8+ Organisms have either a very complex concept or are naming things at the Molecule level — help them consolidate
- Students who can only name 1–2 Organisms may be thinking too broadly — prompt: "could the navigation stand alone on a completely different screen? If yes, that's already one Organism"
- The sketch does not need to be detailed — a rough concept sketch is enough. If a student has only 1 screen, that is fine: one Template, multiple Organisms

**For private mentees (Anh / Vy):**
This activity is their real project audit. The skeleton they draw becomes the actual Template they build in homework. Spend extra time on the Organism naming — the names they choose here should be used consistently in every subsequent Figma file and handoff.

---

### ⚡ Activity 2 — Principles to Tokens
**Type:** In-class · No Figma needed
**Time:** 8 min
**Format:** Solo then pair-share

**What it is:**
The bridge between Phase 1 and Phase 2. Students translate their validated user feedback (words, phrases, emotional responses) into specific token decisions. This is the moment where the concept stops being a sketch and starts becoming a design language.

**Setup:**
No setup needed. Students need only their feedback notes from the previous session.

**Instructions for students:**

1. **(2 min)** Write down 3 words or phrases from your validation feedback — things users said, emotions that came through, qualities stakeholders pointed to. Examples: "felt trustworthy", "looked too corporate", "easy to scan", "needed more energy".

2. **(4 min)** For each phrase, make one token decision:

| Feedback phrase | Token | Decision |
|---|---|---|
| "felt trustworthy" | `color/primary` | Deep blue — `#1D4ED8`. Not bright. Stable. |
| "too corporate" | `radius/md` | Increase to `8px`. Soften the edges. |
| "easy to scan" | `space/section` | `32px` between sections. Breathing room. |

3. **(2 min)** Pair with the person next to you. Share one token decision. Does it actually encode the feedback phrase — or is it just a personal preference dressed up as a principle?

**Debrief question:**
"Could you defend every token decision you just made in a design critique — with a sentence that starts with 'This token encodes...'? If not, it needs more thinking."

**For private mentees (Anh / Vy):**
This becomes the token specification for their actual project. Push further: what does the `color/neutral` token say about the product? What does the `radius/sm` token say? Every value is a decision, not a default.

---

### 🔧 Activity 3 — Atomic Build Sprint
**Type:** In-class · Figma
**Time:** 12 min
**Format:** Solo

**What it is:**
Students build one complete Atom-to-Organism chain for the highest-priority Organism from their Activity 1 list. Not the full system — just one chain, done correctly. The goal is to feel how the layers connect in practice, not to finish everything.

**Setup (before class):**
- Shared Figma file with one blank page per student
- Each page has: a Variables section (for tokens), a Components section (for Atoms and Molecules), an Organisms section, and a Template frame

**Instructions for students:**

1. **(2 min)** Open your Activity 1 Organism list. Pick the one Organism your concept most depends on — the one that, if it were built well, would make everything else easier.

2. **(3 min)** In the Variables section, create 2 tokens that your Organism needs: one colour token, one spacing token. Name them using the convention.

3. **(4 min)** Build one Atom using only those tokens. Then combine it with one or two other Atoms into a Molecule that this Organism needs.

4. **(3 min)** Drop the Molecule instances into the Organism frame. Does the Organism look like the zone you sketched in Activity 1? If not — what's different, and why?

**Facilitator watch-fors:**
- Students hardcoding values instead of referencing tokens — stop and redirect immediately. This is the most common failure mode and it compounds.
- Students who finish early: ask them to add a second state to their Atom (disabled, error) using Variants. This teaches how states live at the Atom level, not the Molecule level.
- Students who are stuck on naming: the name comes from the job. "What does this Molecule do?" → one verb phrase → that's the name.

**For private mentees (Anh / Vy):**
This is the start of their real component library. Keep the file. The Organisms from this activity become the direct inputs for the homework and eventually the prototype session.

---

### 🔎 Activity 4 — Atomic Audit (Optional / Early Finishers)
**Type:** In-class · Figma or FigJam
**Time:** 30 min (main session activity)
**Format:** Pairs for group class · Solo for private sessions

**What it is:**
Students deconstruct an existing UI layer by layer into the five Atomic levels — then flip it: they assemble those Organisms into a Template frame and drop real content into it to produce a Page. The deconstructon is how you read a system. The assembly is how you *use* one. Both halves are in this activity.

**Setup (before class):**
- Have a shared Figma or FigJam file ready with a dedicated frame per student or pair
- If using the practice dataset, pre-import 3 Grab / Shopee / Zalo screens as reference images
- Prepare a simple annotation key: 5 coloured sticky labels, one per Atomic level (Atom = yellow, Molecule = green, Organism = blue, Template = purple, Page = orange)
- Pre-create a blank Template frame beside each student's working area — a phone-sized frame with nothing in it, ready to receive Organisms

**Instructions for students:**

1. **(5 min) — Atoms.** Look at one screen only. List every element that cannot be broken down further — buttons, text styles, icons, input fields, colour swatches. Tag each one with your Atom sticky colour.

2. **(8 min) — Molecules & Organisms.** Look for elements that consistently appear together as one functional unit (Molecules: search bar, form field, card header). Then identify the self-contained sections (Organisms: navigation bar, product card grid, login form). Ask yourself: could this section be dropped unchanged onto a completely different screen and still make sense?

3. **(7 min) — Build the Template.** In your blank frame, arrange your Organisms as layout zones — no real content, just structure. Label each zone by Organism name: "navigation organism", "product grid organism", "CTA organism". This is your Template. It answers: *does the structure work?*

4. **(5 min) — Build the Page.** Duplicate the Template frame. Fill it with real content — real product names, real photos, real prices (or realistic stand-ins). This is your Page. It answers: *does the system hold up under real conditions?* Watch for what breaks: long text, missing images, empty states you forgot to design.

5. **(5 min) — Share back.** Each pair presents their Template and Page side by side: what changed between the two, and one edge case they discovered when real content arrived.

**Facilitator watch-fors:**
- Molecule/Organism confusion is common — ask: *"Can this section exist completely alone on a different screen?"* Yes → Organism. Needs context → Molecule.
- Students who only find Atoms are not looking hard enough — prompt: *"Find two or more of those Atoms that always appear together."*
- Expect the discomfort moment when building the Page: students discover their Template doesn't handle real content gracefully. This is the point. Don't rescue them — let them name what broke.
- Early finishers: ask them to build a second Page variation (e.g. empty state, error state) using the same Template. This reveals whether the Template is truly reusable or was only designed for the happy path.

**For private mentees (Anh / Vy):**
Use their actual current project file instead of the sample dataset. The Template and Page they build in this activity become the direct input for a future session where they use AI tools to generate a working prototype from those Templates. Frame it explicitly: *"The Template you build today is the foundation we'll hand to AI in our next advanced session."*

---

### 🔬 Activity 5 — System Smell Hunt (Optional Take-Home)
**Type:** In-class or take-home · Figma
**Time:** 15–20 min (or assign as take-home after session)
**Format:** Solo or pairs

**What it is:**
Students examine a set of 4 screens with deliberate design inconsistencies and identify every "system smell" — places where the Atomic hierarchy was ignored, components were built as one-offs, or tokens were never applied. This is the reverse of Activity 1: instead of mapping the hierarchy, students find where it breaks.

**Setup:**
Create a simple "broken" Figma frame before class — 4 screens with these intentional problems:
- 3 slightly different button styles (same button, built 3 separate times instead of one component)
- 2 card components — one with 16px padding, one with 14px
- A navigation bar rebuilt from scratch on each screen (not a shared component instance)
- Typography not linked to styles — random font sizes instead of tokens
- Bonus: one icon used in 2 different sizes across screens for no reason

Alternatively, import screenshots from your `Day7-Atomic - Design System in trend.pdf` source material (which documents similar design debt examples).

**Instructions for students:**

1. Open the "broken" Figma file (or their own project if they're ready for it)
2. Create a running list of every inconsistency they can find. Classify each one:
   - **Atom broken** — a base element used inconsistently (e.g. button appears in 3 different sizes)
   - **Molecule broken** — a combination built differently per screen (e.g. form field label above on one screen, left-aligned on another)
   - **Organism broken** — a section rebuilt from scratch instead of reused (e.g. navigation rebuilt fresh on every screen)
   - **Token missing** — a style decision that should be a token but is hardcoded (e.g. `#2563EB` written directly instead of a colour variable)
3. For each inconsistency, write one sentence: *"If this were fixed, what would improve in the product or the workflow?"*

**Debrief questions:**
- How many smells did you find? (The sample file has at least 8)
- Which type was most common — Atom, Molecule, Organism, or Token?
- What's the real-world cost of each type? (Extra design time? Developer confusion? Inconsistent user experience? All three?)

**For private mentees (Anh / Vy):**
Use their actual project file instead of the sample. Frame it not as "finding problems" but as "building a prioritised fix list." At the end, rank the top 3 smells by impact on the product and turn them into action items for the next session.

---

## AI in Practice

### 🤖 Try this with AI

> Paste this prompt into Claude or ChatGPT:
> *"I'm building a mobile app for [describe your app in one sentence]. I've identified the following UI elements: [paste your list of elements]. Help me organise these into an Atomic Design hierarchy — Atoms, Molecules, and Organisms. For each Molecule and Organism, tell me which Atoms it should contain. Also suggest a Figma naming convention I can use."*

### 🧠 Critical thinking prompt

After seeing the AI output, discuss as a class:
- Did the AI correctly identify which elements are truly Atoms vs. Molecules? Where did it get confused?
- Did the AI's naming convention match the one we used in class — or invent something different? Which is clearer?
- What context did the AI not have that you had? (e.g. platform — mobile vs. web, Vietnamese user behaviour, the actual visual design)

### ✍️ Prompt engineering tip

The more specific you are about your app type and platform, the better the AI's organisation suggestions will be. Instead of *"a social app"*, try *"a Vietnamese social commerce app for buying from individual sellers, primarily used on Android phones."* Specificity gives the AI enough context to make sensible hierarchy decisions rather than giving you a generic textbook answer.

### ⚖️ Ethics consideration

AI tools can generate component libraries and design system structures quickly — but they reflect the design patterns of the training data, which skews heavily toward English-language, Western-market products (Google, Airbnb, Spotify). When building a design system for a Vietnamese or Southeast Asian product, be critical about whether the AI's suggested hierarchy actually matches your users' mental models and interaction patterns. A chat interface for Vietnamese users may have very different organism-level structures than one designed for US users.

---

## Assessment

### Quick knowledge check

Run verbally or in a shared FigJam at the close of the Core Concept section (2–3 min):

1. You're designing a search results page. Name one Atom, one Molecule, and one Organism you'd find on it.
2. What's the difference between a Template and a Page in Atomic Design?
3. A designer changes the primary button colour token in Figma. Which levels of the Atomic hierarchy update automatically — and which ones don't?
4. A colleague says: *"I don't need Atomic Design, I just make sure all my buttons look the same."* What's the gap in that thinking?

---

### Homework 1 — Atomic Map
**Due:** Before next session
**Time estimate:** 30–45 min
**Type:** Analysis · Figma annotation

Open one of your existing Figma project files. Pick one complete screen you've worked on.

In a duplicate of that frame:
1. Add annotation stickies or labels to identify every Atom, Molecule, and Organism you can find
2. Highlight one element that was clearly designed as a one-off (not part of a system)
3. Write two sentences below the frame: what you would change, and what would concretely improve in the product if you changed it

**For group class:** Share your annotated frame in the class Figma file before the next session. Be ready to spend 3 minutes walking the group through your top finding.

**For private mentees (Anh / Vy):** Share the annotated frame link with Winnie before your next 1-on-1. The first 15 minutes of that session will be a review together — and the top inconsistency you found becomes a real fix on your live project.

**What Winnie is looking for:**
- Can you tell Molecules from Organisms correctly — without second-guessing?
- Is your observation about the inconsistency specific? ("This button was built at 14px font size instead of using the `--text-sm` token" beats "this looks a bit off")
- Do you understand *why* the inconsistency matters systemically, not just visually?

---

### Homework 2 — Complete the 5-Step Process
**Due:** Before next session
**Time estimate:** 90–120 min
**Type:** Creation · Figma

> In class you completed Steps 1–2 (find screens + sketch zones) and did the Step 3 mapping. This homework completes Steps 4–5 for your own concept.

The full Atomic chain — from tokens to a complete Page. This is the session's main deliverable. By the end you will have built a real, working design system fragment and a screen that proves it holds up.

**Steps 1–3 — If you haven't done them yet (from Activity 1)**

**Step 1 — Identify key screens (5 min)**
From your concept sketch: name the 2–3 screens essential to what was validated. These are your Pages — the destination.

**Step 2 — Sketch your zones (10 min)**
Pick your most important screen. Draw the layout skeleton in a blank Figma frame — grey rectangles for zones, labelled by what they *are*, not what they contain.

**Step 3 — Map zones to interaction patterns (5 min)**
For each zone, write the interaction pattern it maps to (Navigating, Searching, Adding, Confirming, etc.). Then give each zone an `o/` name. This is your build list.

---

**Steps 4–5 — Build the system**

**Step 4 — Define or adopt tokens (15 min)**

*Option A — Build your own:* From your validation feedback, write 3–5 principles that define what the concept needs to feel like. In Figma Variables or Styles, create:
- At least 3 colour tokens (primary, secondary, neutral)
- At least 2 typography tokens (heading, body)
- At least 2 spacing tokens (`space/sm = 8`, `space/md = 16`)
- Every token traceable to one of your principles

*Option B — Adopt and override:* Choose Material Design 3, Ant Design, or Radix UI as your base. Override at minimum: primary colour, border radius, and section spacing to match your concept's personality. Document why you overrode each one.

**Step 5 — Build Atomic components (60–75 min)**

*5a — Build 5 Atoms (20 min)*
Using only your tokens — no hardcoded values:
- 1 Button (min 2 variants: Default + Disabled)
- 1 Input field
- 1 Icon component
- 1 Text/Label
- 1 Badge or Tag

Name using `a/button/default`, `a/input/default`, etc.

*5b — Build 2 Molecules (15 min)*
Combine Atoms into 2 Molecules. Each must use Atom instances (not copies), have one clear job, and be named `m/[name]`.

*5c — Build 2+ Organisms from your Step 3 list (15 min)*
Build the Organisms you mapped in Step 3. Each must be self-contained and reusable. Named `o/[name]`.

*5d — Assemble the Template (10 min)*
In a phone or desktop frame, arrange your Organisms into your skeleton layout from Step 2. Placeholder content only — structure is the point.

*5e — Fill to a Page (10 min)*
Duplicate the Template. Fill with real content. Note what breaks — these are deferred design decisions, not mistakes.

**Document as you go (10 min)**
One sentence per Molecule, Organism, and Template frame: what it is and when to use it.

**Deliverable:**
- Figma link shared with Winnie (private) or class channel (group)
- Must contain: tokens, 5 Atoms, 2 Molecules, 2+ Organisms, 1 Template, 1 Page
- Come ready to explain: one token decision traceable to your concept, and one thing that broke on the Page

**What Winnie is looking for:**
- Do Steps 1–3 clearly show in the file — is there a skeleton, a zone-to-pattern mapping, evidence of reading before building?
- Are tokens driving styles — or were values hardcoded?
- Do Molecules nest Atom instances, not copies?
- Does the Template feel like a real screen structure?
- What broke on the Page, and what does that tell you about your concept?

> **Your Template is the input for the next session.** You will hand it to AI (Cursor or Claude) to generate a working prototype. Clean naming and consistent structure matter — not just for aesthetics, but because the AI will read your component names to understand what to build.

---

## Further Resources

- **Brad Frost — Atomic Design (book, free online):** https://atomicdesign.bradfrost.com/ — The original and still the clearest articulation of the methodology
- **Muzli — "Building Design Systems with Atomic Design"** (saved in your Notion) — Good visual examples of the 5 levels applied to real products
- **"Xây dựng Design System với Atomic Design – An"** (saved in your Notion, Vietnamese) — Useful for students who prefer Vietnamese reading material
- **Airbnb Design — "5 tips for maintaining a design system"** (saved in your Notion) — Real-world perspective from a product design team at scale
- **Google Material Design 3:** https://m3.material.io/ — A live, public example of a design system built on Atomic principles; useful to explore how Google implements the hierarchy in practice
- **Figma Variables documentation:** https://help.figma.com/hc/en-us/articles/15339657135383 — How to implement design tokens in Figma (the practical 2026 starting point)

---

*Created by Winnie Nguyen · UX Class · Last updated May 2026*
