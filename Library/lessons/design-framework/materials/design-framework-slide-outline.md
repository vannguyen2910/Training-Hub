# Slide Deck Outline — Build AI Prototype

> **Source of truth:** `lesson.md`
> All content changes (activities, concepts, examples) must be made there first, then reflected here.
> This file contains only slide-specific concerns: layout types, visual hints, kickers, and structure.

> **How to use this file**
> Paste both this file and `lesson.md` into Claude with the instruction below to generate a new slide deck.
> Claude will read `CLAUDE.md` and `_Config/slide-design/RULES.md` automatically and follow Winnie's design system.

---

## Prompt to use

```
Using the outline in this file, create an HTML slide deck for Building a Design Framework from a Validated Concept.

Follow the rules in _Config/rules/SLIDE_DECK_RULES.md exactly.
Save the file to Library/lessons/design-framework/materials/deck.html.
Copy tokens.css and deck-stage.js locally into Library/lessons/design-framework/ so the deck is self-contained.

VISUAL DESIGN DIRECTION — apply globally to every slide:

- Prefer simple diagrams, icons, and visual metaphors over bullet lists. If content can be shown
  as a shape, flow, or diagram — do that instead of listing text.
- Use inline SVG for all diagrams and illustrations. Keep them clean and minimal —
  flat shapes, no gradients, use only token colours (--sienna, --ochre, --sage, --ink, --paper).
- For the 5-level hierarchy, draw a left-to-right horizontal pipeline with circles that grow
  progressively larger from Atom to Page — showing scale accumulating upward.
- For the Molecule anatomy diagram, deconstruct a search bar left-to-right: icon + input + button
  connected by "+" symbols in --sienna, with a right-arrow pointing to the assembled Molecule.
- For the token stack diagram, draw a vertical layered stack: Tokens at the base (--ochre fill),
  then Atoms, Molecules, Organisms stacked above — like a foundation pyramid.
- For the naming convention, render component names in --font-mono on a dark --ink background
  to look like a real Figma Assets panel.
- For comparisons (Template vs Page, messy vs organised), use a clean two-column split with a
  hairline centre divider and colour-coded column labels.
- Activity slides (.milestone) should feel like a full-bleed moment — no extra content,
  just the kicker, number, title, and prompt.
- Every slide should have one dominant visual element. If the layout is mostly text,
  add a supporting SVG shape or icon to anchor the eye.
- Avoid centred bullet lists. If items must be listed, use the .numbered or .process layout
  with visual numbering, not a plain <ul>.
```

---

## Session metadata

| Field | Value |
|---|---|
| Session title | Building a Design Framework from a Validated Concept |
| Methodology | Atomic Design |
| Instructor | Winnie Nguyen |
| Program | UX Class |
| Year | 2026 |
| Previous session | Concept validation (user / stakeholder feedback) |
| Next session | AI-assisted prototype development (Cursor / Claude) |
| Cover photo | Unsplash — modular architecture, LEGO bricks macro, or blueprint/construction detail (search: "blueprint structure minimal" or "building blocks macro") |

---

## Slide structure

> **45-minute version — 16 slides.**
> Question-by-question arc: Where we left off → What happens without a system → The bigger picture → What is Atomic? Why? → How to set up using Atomic.
> Deep-dive reference material (Atom/Molecule/Organism breakdowns, 8pt grid, Figma mapping) is in `lesson.md` for verbal delivery — not in the deck.

---

## 1. Where we left off

---

### COVER
- Year: 2026
- Day label: Design Framework
- Title: Design Once.\n*Use Everywhere.*
- Subtitle: How to build a design system that scales — from your first sketch to every screen
- Author: Winnie Nguyen
- Right panel photo: Unsplash — UX design system or UI component library feel: a designer's desk with wireframe printouts, sticky notes, and a laptop showing Figma; or a close-up of a phone screen with clean UI components visible; or a flat-lay of design artefacts (sketches, colour swatches, component cards). Warm, human, and design-focused — not abstract or corporate. Search terms: "UX design workspace", "UI design system", "designer desk Figma".

---

### STATEMENT — The bridge from last session
- Kicker: Where we left off
- Title: You know *what*\nto build.\nNow build it *right.*
- Lead: Last session, real people told you what worked about your concept. That's a big deal — don't waste it. This session is about turning that feedback into a design system that actually holds together, no matter how many screens you add or how many times things change.
- 🎨 Visual hint: Two nodes connected by a bold arrow. Left: speech bubble icon + "Validated concept" (--ochre fill). Right: clean phone frame + "Design framework" (--sienna border). Minimal — no clutter.

---

## 2. What happens without a design system

---

### STATEMENT — The drift
- Kicker: You've seen this before
- Title: Without a system,\nthe concept *drifts.*
- Lead: You open a Figma file and there are 12 slightly different buttons. Three versions of the same card. A colour that's almost right but not quite the same as the one two screens over. Nobody planned that — it just happened, one screen at a time. This is how a concept that users loved slowly becomes something nobody recognises.
- 🎨 Visual hint: A Figma-style canvas as SVG — overlapping rectangles, frames labelled "Frame 47", "Button copy (2)", "Card FINAL v3" at random angles (--ink-ghost, --ink-muted). At the centre, a faint outline of a clean phone frame barely visible under the clutter. The concept is still in there somewhere, buried.

---

## 3. The bigger picture

---

### DIAGRAM — Experience architecture
- Kicker: Why a design system matters
- Title: Every screen\nshares the same\n*building blocks.*
- Lead: Think about any app you use — banking, shopping, social media. The screens all look different, but underneath they're all built from the same types of pieces: forms, buttons, cards, navigation bars. A design framework is how you build those pieces once — and use them everywhere.
- 4 levels (outer to inner):
  - **Level 1 · User journey** — Everything a user does to reach one goal, across multiple screens. *"Laura applies for a loan."* / *"Laura updates her profile."*
  - **Level 2 · User story** — One specific step inside that journey. *"Laura fills in her income details."* / *"Laura changes her phone number."*
  - **Level 3 · Interaction pattern** — The type of thing the user is doing: adding information, making a choice, confirming something. *"Adding" / "Editing" / "Confirming"*
  - **Level 4 · Components** — The actual UI pieces that make it happen. *Form fields, buttons, dropdowns, error messages.*
- Key insight: Two completely different journeys — applying for a loan and updating a profile — both end up needing the exact same form fields and buttons at Level 4. Build those components once, and they already work for every journey that needs them.
- Mention verbally: This is how big design systems like GOV.UK, IBM Carbon, and Atlassian are organised — journeys at the top, shared components at the base.
- 🎨 Visual hint: Concentric circles as SVG. Four rings labelled outer to inner: "User journeys" (--ink), "User stories" (--ink-muted), "Interaction patterns" (--ochre), "Components" (--sienna, innermost, solid). Two journey arcs drawn as curved coloured paths on the outer ring — Arc 1 (--ochre path) "Apply for loan", Arc 2 (--sienna-tint path) "Update profile" — both converging as they move inward, merging at Level 3 and Level 4. The inner circles feel solid and shared; the outer ring feels wide and varied. This diagram is the entire slide.

---

## 4. What is Atomic Design? Why?

---

### PROCESS — The Atomic hierarchy
- Kicker: Meet Atomic Design — Brad Frost, 2013
- Title: A design system\nis built in *layers.*
- Layers (bottom to top):
  0. **Tokens** — Instead of typing the same colour code on every screen, you give it a name — like `brand-blue` — and use that name everywhere. Change the name's value once, and everything updates. Tokens are your colour, spacing, text size, and corner radius values.
  1. **Atoms** — The smallest pieces: a single button, an icon, a text input. You can't break them down any further without losing what they are.
  2. **Molecules** — Two or more Atoms working together as one thing. A search bar is a Molecule — it's an input (Atom) + a button (Atom) side by side.
  3. **Organisms** — A whole section of a screen. A navigation bar, a product card, a comment section.
  --- system / product boundary ---
  4. **Templates** — The layout of a screen, without real content. Like a skeleton — you can see how everything is arranged before you fill it in.
  5. **Pages** — The same screen filled with real photos, real text, real data. This is what users actually see.
- 🎨 Visual hint: Horizontal pipeline — icons for each level (Atoms → Pages) connected by arrows, matching the Brad Frost diagram style. Below: two bracket labels — left bracket spanning Atoms–Organisms labelled **system** (--ink), right bracket spanning Templates–Pages labelled **product** (--sienna). Tokens shown as a foundation row below the pipeline, separated by a dashed line (--ochre). Use `assets/atomic-design-product.jpg` prominently on this slide as the primary visual reference.

---

### NUMBERED — See it in a real product
- Kicker: What it looks like in practice
- Title: Every app you use\nis already built\n*this way.*
- Lead: Atomic Design isn't a new idea invented for class. Every mature product you use — from Shopee to Gmail to your banking app — is built from the same layered system. Here's what it looks like when you can see all the layers at once.
- 🎨 Visual hint (two-panel layout):
  - **Left panel** — `assets/1_U-jFHRJxePDHHBWtd19M8g.png` full-bleed. Caption: "One Page traced back through every level — from typography tokens to the final login screen."
  - **Right panel** — `assets/544936___screen_1.jpg` full-bleed. Caption: "A real design system showing Atoms, Molecules, Organisms, Templates, and Pages side by side."
  - No competing text — let the images do the teaching. Captions are the only copy.

---

## 5. How to set up a design system using Atomic

---

### PROCESS — The 5-step process map
- Kicker: The method
- Title: Five steps.\nOne system.
- Steps (horizontal linear rail):
  1. Find your screens
  2. Sketch your zones
  3. Map to interaction patterns
  4. Define your tokens
  5. Build the system
- 🎨 Visual hint: Single horizontal rail — 5 numbered circles connected by arrows, all in one row. No phase split, no column divider. Steps 1–3 in --ochre tint (reading/discovery), Steps 4–5 in --sienna tint (building). Step 3 acts as the bridge — slightly larger circle or a subtle colour transition to signal "this is where both frameworks connect." A small text tag beneath Step 4: "build your own or pick one →". Reference map — stays visible as students work through each step.

---

### PROCESS — Steps 1–2: Read what you already have
- Kicker: Before you open Figma
- Title: Your concept sketch\nis already a\n*design blueprint.*
- 2 steps:
  1. **Find your screens** — Open your concept sketch. Pick the 2–3 screens that capture the core of what users responded to. Write their names down. These become your destination — the Pages you're building toward.
  2. **Sketch your zones** — Take your most important screen. Strip away all content — no text, no colour, no images. Draw grey rectangles for each section. Give each one a plain name: "navigation", "content area", "action bar". This structure is your Template. Write the list.
- 🎨 Visual hint: Two side-by-side panels connected by a forward arrow. Panel 1: rough concept sketch (loose phone screen, warm --ochre tint). Panel 2: same screen stripped to a skeleton — grey rectangles labelled "nav", "content", "action". Each panel progressively more structured. --ochre accent throughout.

---

### MILESTONE — Activity 1: Steps 1–2 Sprint
- Kicker: Activity 01 · your turn
- Num: 8
- Title: Minutes
- Sub: Open your concept sketch. Pick your 2–3 most important screens. Draw the skeleton for one of them — grey rectangles only. Give every section a plain name. Come back with your list of zones.

---

### STATEMENT — Step 3: The bridge
- Kicker: Step 3 · From zones to patterns
- Title: Those zones?\nThey each have\na *name in design.*
- Lead: Look at the list you just made — "navigation", "content area", "action bar". Now think about what a user is *doing* in each zone. Navigating. Searching. Adding something. Confirming. These aren't just layout zones — they're interaction patterns. And interaction patterns are exactly how design systems organise their Organisms. You already mapped your system without knowing it.
- Interaction pattern examples: Navigating · Searching · Adding · Selecting · Editing · Confirming · Notifying
- 🎨 Visual hint: Two-column mapping diagram. Left: plain zone names from Activity 1 ("navigation area", "search zone", "checkout summary"). Right: interaction pattern labels (Navigating, Searching, Confirming) connected by horizontal arrows. Small label in the top-right corner: "= Organisms in Atomic Design" (--sienna, italic). This is the reveal moment — students recognise their zones already have system-level names.

---

### STATEMENT — Step 4: Tokens come from the concept
- Kicker: Step 4 · Build your foundation — or borrow one
- Title: "Trustworthy" is\na colour.\n"Approachable" is\na *corner radius.*
- Lead: Before any components, you need a foundation. You have two paths: define your own tokens from your concept's personality — or adopt an existing design system (Material, Ant Design, Radix) and override the tokens that matter. Either way, every decision should trace back to what users told you. A random colour choice isn't a token — it's a preference.
- Token examples from concept:
  - "felt trustworthy" → `color/primary` → deep blue swatch
  - "too corporate" → `radius/md` → rounded corner diagram
  - "easy to scan" → `space/section` → 32px spacing bar
- Pick-or-build note: Under time pressure? Adopt Material or Ant Design as your base — then override the 3 tokens that define your concept's personality.
- 🎨 Visual hint: Three rows as a compact table — feedback phrase (--ochre pill tag) → arrow → token name in --font-mono → token value as a visual swatch. Small fork diagram at the bottom: "Build your own ↔ Adopt + override" — both paths leading to the same Step 5 arrow.

---

### STATEMENT — The system builds. The product ships.
- Kicker: Step 5 · What you're actually building toward
- Title: The system *builds.*\nThe product *ships.*
- Lead: Step 5 is where everything assembles. Molecules from Atoms. Organisms from Molecules. Then Organisms into your Template skeleton — and the Template filled with real content becomes a Page. Every decision in Steps 1–4 was pointing here. The system is how you build it. The Page is what users see.
- 🎨 Visual hint: Two-column layout with a dashed vertical divider, matching the style of the uploaded slide image.
  - **Left column — SYSTEM** (--ink label):
    - Atom icon + label: **Atom** · small tag below: *"Component"*
    - Molecule icon + label: **Molecule** · small tag below: *"Component"*
    - Organism icon + label: **Organism** · small tag below: *"Interaction Pattern"*
    - Each icon stacked vertically with its dual label — Atomic name above, Experience Architecture name below in --ink-muted smaller text.
  - **Centre** — bold arrow labelled **OUTPUTS** (--sienna) pointing right.
  - **Right column — PRODUCT** (--sienna label):
    - Template phone frame (skeleton, grey zones, dashed border) · label: **Template** · small tag below: *"User Story"*
    - Page phone frame (filled with real content — image, product name, price like "189.000đ", CTA button) · label: **Page** · small tag below: *"User Journey"*
  - Dual labels (Atomic name + Experience Architecture name) are the key teaching element — students see both frameworks collapse into one diagram. Experience Architecture tags in --ink-muted italic, Atomic names in --font-display normal weight.

---

### PRACTICE — Homework
- Kicker: Your turn to build
- Title: Steps 4 and 5\nare yours to *build.*
- Steps to complete:
  - Step 4 — Set your foundation: define your tokens (or adopt an existing design system and override 3 tokens). For each custom token, write one sentence connecting it to what users said.
  - Step 5 — Build the system: 3 Atoms → 2 Molecules → at least 2 Organisms from your zone list → assemble into your Template skeleton → fill with real content to make a Page. Note what breaks.
- Deliverable: Share your Figma link — tokens, Atoms, Molecules, Organisms, a Template frame, and a Page frame.
- 🎨 Visual hint: Two steps on a process rail (circles 4 and 5 matching the process map). Step 5 (Template + Page) in --sienna to signal it's the deliverable. Small tag at the bottom: "Your Template is the input for the next session."

---

### STATEMENT — What comes next
- Kicker: Next session
- Title: Your Template\nis not the end.\nIt's the *input.*
- Lead: In the next session, you'll take the Template you built and give it to an AI tool — Cursor or Claude — which will turn it into a working prototype. The better your system is built, the faster and more accurate that prototype will be. Everything you did today matters more than you think.
- 🎨 Visual hint: Two panels. Left: Figma Template frame (wireframe phone, zone labels visible). Bold arrow right. Right: code window showing `<NavBar />`, `<ContentFeed />`, `<ActionBar />` in --font-mono on --ink background. Labels: "You build (today)" / "AI builds (next session)".

---

### END — Closing
- Kicker: One thing to carry forward
- Title: "Find the screen.\nSketch the zones.\nMap the patterns.\nBuild from tokens.\nShip to the *Page.*"
- Lead: Five steps from sketch to system. The Template and Page prove it works.
- Sign: — Winnie Nguyen
