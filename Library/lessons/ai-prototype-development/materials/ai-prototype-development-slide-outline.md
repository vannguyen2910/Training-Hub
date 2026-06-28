# Slide Deck Outline — Build the Pattern First

> **Source of truth:** `ai-prototype-development-lesson.md`
> All content changes (activities, concepts, prompts) must be made there first, then reflected here.
> This file contains only slide-specific concerns: layout types, visual hints, kickers, and structure.

> **How to use this file**
> Paste both this file and `ai-prototype-development-lesson.md` into your AI tool with the instruction below to generate a new slide deck.
> Your AI tool will read `CLAUDE.md` and `_Config/slide-design/RULES.md` automatically and follow Winnie's design system.

---

## Prompt to use

```
Using the outline in this file, create an HTML slide deck for Build the Framework First.

Follow the rules in _Config/rules/SLIDE_DECK_RULES.md exactly.
Save the file to Library/lessons/ai-prototype-development/materials/deck.html.
Copy tokens.css and deck-stage.js locally into Library/lessons/ai-prototype-development/ so the deck is self-contained.

VISUAL DESIGN DIRECTION — apply globally to every slide:

- Prefer diagrams, flows, and visual metaphors over bullet lists. If content can be shown
  as a shape, flow, or diagram — do that instead of listing text.
- Use inline SVG for all diagrams. Keep them flat, clean, and minimal —
  use only token colours (--sienna, --ochre, --sage, --ink, --paper).
- For the prototype pattern layers diagram, draw a vertical stack of three labelled blocks
  (component inventory → interaction pattern → state map) with a bold right arrow
  pointing to a phone frame — showing the prototype pattern becomes the prototype.
- For the screen-by-screen vs pattern-first comparison, use a clean two-column split:
  left column shows three disconnected phone frames drifting apart (--ink-ghost),
  right column shows the same three frames snapping into a grid from shared blocks (--sienna).
- For Entry Point A flow, draw a left-to-right pipeline: System qualities → Token decisions →
  Component inventory → Product context → Framework document.
- For the "Already have components" sub-paths, use a three-branch fork diagram: "In your design tool" · "In code" · "In both"
  converging at a single "Framework document" output node.
- Milestone/activity slides (.milestone) should feel like a full-bleed pause moment — no extra
  content, just the kicker, timer, and the one thing students are doing.
- The pre-flight checklist slide should render the table as a clean grid, not raw markdown.
- Every slide should have one dominant visual or diagram. If the layout is mostly text,
  add a supporting SVG shape or icon to anchor the eye.
- Avoid centred bullet lists. Use .process or .numbered layouts with visual numbering.
```

---

## Session metadata

| Field | Value |
|---|---|
| Session title | Build the Pattern First |
| Subtitle | How to use AI and your design system to prototype smarter — not screen by screen |
| Instructor | Winnie Nguyen |
| Program | UX Class |
| Year | 2026 |
| Duration | 90 min |
| Previous session | Design Once. Use Everywhere. (Atomic Design) |
| Next session | TBD |
| Cover photo | Unsplash — clean architectural blueprint, scaffolding, or structural framework. Search: "blueprint framework minimal" or "scaffolding architecture overhead" or "structural grid construction". Avoid: finished buildings, abstract tech, laptops. |

---

## Slide structure

> **90-minute version — 43 slides.**
> Arc: Celebrate what you built → what is an AI-assisted prototype → the problem with screen-by-screen → the pattern-first solution →
> the two layers (one per slide) → Atomic Design → pattern mapping → two paths (broken out by step and sub-path) →
> full-screen examples at key moments (prototype pattern, AI output, drift audit, browser build) →
> checkpoint → build reference → build → reflect.
> Phase 4 (20 min hands-on) has no new slides — the build reference slide stays on screen.

---

## 1. Where we left off

---

### COVER
- Year: 2026
- Day label: AI Prototype Development
- Title: Build the Pattern\n*First.*
- Subtitle: How to use AI and your design system to prototype smarter — not screen by screen
- Author: Winnie Nguyen
- Right panel photo: Unsplash — clean architectural blueprint, scaffolding detail, or structural grid; or a designer's hands sketching a wireframe layout on paper; or a close-up of a Figma components panel on screen. Precise, structured, and human — not abstract or corporate. Search terms: "blueprint framework minimal" or "wireframe sketch overhead" or "Figma design system screen".

---

### SECTION
- Section num: 01
- Title: Where we\nleft off
- Sub: Building on your design system from last session
- 🎨 Visual: White background, section number "01" faint top-left, title centred. Nothing else.

---

### STATEMENT — Celebrate what you built
- Kicker: Look what you made
- Title: Last session, you built\nsomething *real.*
- Lead: Tokens. Atoms. Molecules. Organisms. A Template. A Page. That's a whole design system — yours. Most people skip this part. You didn't. And today, that matters.
- 🎨 Visual: Six icons in a row — token → atom → molecule → organism → template → page — each with a checkmark above.

---

### STATEMENT — The bridge from last session
- Kicker: So… what now?
- Title: Your design system is\nnot the finish line.\nIt's the *starting gun.*
- Lead: You made every visual decision that matters. Now comes the fun part: turning it into a prototype that actually moves. AI is going to help. But first — you need to give it something to work from. That's what today is about.
- 🎨 Visual: Two labelled boxes — "Design system" → arrow → "Working prototype." Label under arrow: "AI builds the bridge."

---

### STATEMENT — What is an AI-assisted prototype?
- Kicker: Let's be specific
- Title: Not a Figma file.\nNot a mockup.\n*A prototype that actually runs.*
- Lead: An AI-assisted prototype is a working, browser-viewable prototype where screens are generated by AI — not placed by hand. You define the rules: what components exist, what states they can have, how screens connect. The AI reads those rules and builds the screens from them. The output is real code — HTML or React — running in a browser. You can open it on any device, share it as a link, and test it with a real user.
- Clarify what "AI-assisted" means:
  - **You define the system.** Component inventory, states, interaction pattern — all yours.
  - **AI does the assembly.** It builds the screens from your rules. Not from a blank brief.
  - **You review every output.** AI gets close but misses nuance — spacing, grouping, hierarchy. That's expected. Your eye fixes it.
  - **The pattern is the brief.** Without it, AI fills gaps with assumptions and generic styles. With it, AI builds your product.
- Research note (for presenter): NN/G (2025) — "AI prototyping tools follow general directions but lack the sophistication to weigh design tradeoffs." Adobe Design (2026) — "The fundamentals of design don't change with vibe coding. Empathy, judgment, taste, and craft become more essential."
- 🎨 Visual: Three steps in a row — "Prototype pattern" → "AI" → "Running in browser." Simple icons, left to right.

---

### DIAGRAM — Traditional vs AI-assisted prototype
- Kicker: Why this session exists
- Title: Traditional prototype\nvs *AI-assisted prototype.*\nWhat's actually different?
- Lead: Traditional prototyping means designing every screen by hand — one at a time, from scratch, in your design tool. It gets the job done for 3 screens. It falls apart at 10. AI-assisted flips the process: you define the system once (the prototype pattern), and AI assembles the screens from it. You stop being the assembler. You become the architect. The shift isn't about using a new tool — it's about changing what you spend your time on.
- 2-column comparison:
  - **Traditional prototype** — You design each screen manually. Every state, every interaction, every component placed by hand. Changes require updating every screen. AI can't build from it because there's no single source of truth. Time-consuming. Doesn't scale.
  - **AI-assisted prototype** — You define the prototype pattern once: what components exist (with states) and how screens connect. AI reads the prototype pattern and generates the prototype. Changes update from the prototype pattern — not from each screen. Fast. Consistent. Scales to 30 screens as easily as 3.
- 🎨 Visual: Two columns. Left: 3 phone frames slightly misaligned, label "every screen = a new decision." Right: 3 identical phone frames built from one source, label "one pattern → many screens."

---

## 2. The problem with screen-by-screen

---

### SECTION
- Section num: 02
- Title: The problem with\nscreen-by-screen
- Sub: Why starting with a screen is the wrong move
- 🎨 Visual: Dark background (--ink), title in white, centred. No decoration.

---

### STATEMENT — What goes wrong
- Kicker: The most common mistake
- Title: Screen by screen.\n*Everything drifts.*
- Lead: Here's what usually happens. Open your design tool. Start with the home screen. Then the detail screen. Then the settings screen. By screen three, the button looks slightly different. The spacing changed. When you hand it to AI, every prompt starts from zero. Nothing connects. AI doesn't know what you meant — because you haven't told it yet.
- 🎨 Visual: Three phone frames drifting apart, each slightly different. Labels point to inconsistencies: "button changed," "spacing off," "new component."

---

## 3. The pattern-first solution

---

### SECTION
- Section num: 03
- Title: The pattern-first\nsolution
- Sub: A better way to think before you build
- 🎨 Visual: --sienna background, title in white, centred. Warm contrast to the dark section before it.

---

### STATEMENT — Why build the template before the screens?
- Kicker: Here's what you gain
- Title: Build the template first.\n*Here's why it's faster.*
- Lead: It feels slower to plan before you build. But it isn't. Here's what actually happens when you define your prototype pattern before touching any screen.
- 4 benefits:
  1. **Nothing drifts.** Every screen uses the same components because they're all listed in one place. No more "why does this button look different on screen 3?"
  2. **AI gets consistent results.** When your AI coding tool has a complete component list and interaction pattern, it doesn't have to guess. Every screen it builds comes from the same source.
  3. **Changes are easy.** Need to update a component? Change it in the template. Every screen that uses it updates automatically — you don't hunt through 10 separate screens.
  4. **You build faster after planning.** The first screen takes 5 minutes. The next one takes 2. Because the hard decisions are already made.
- 🎨 Visual: Four cards in a 2×2 grid. Each: number (1–4) + one-line benefit heading.

---

### STATEMENT — What is a prototype pattern?
- Kicker: Let's break it down
- Title: A prototype pattern is just\n*a really clear set\nof instructions.*
- Lead: Think of it like a recipe. You don't start cooking and figure out the ingredients as you go. You list everything first. A prototype pattern is the same thing — it lists your components (with all the looks they can have) and how your screens connect before any building starts. AI loves a good recipe.
- 🎨 Visual: Left: short bulleted list — "components, states, screens." Arrow right. Right: phone frame. Label on arrow: "AI follows the recipe."

---

### DIAGRAM — Layer 1: Component inventory
- Kicker: The first layer
- Title: What pieces do you have —\nand what can they *look like?*
- Lead:
  - A list of every UI piece in your system — buttons, inputs, cards, nav bars
  - Every component includes all its states: default, hover, loading, disabled, error
  - If it's not on the list, AI doesn't know it exists
  - Think of it like telling LEGO which bricks are in the box, and what colour each can be
- 🎨 Visual: A simple two-column table — component names in column 1, states listed in column 2. e.g. Button | default / hover / loading / disabled.

---

### DIAGRAM — Layer 2: Interaction pattern
- Kicker: The second layer
- Title: Where does each\nscreen *lead?*
- Lead:
  - A diagram of your screens and the paths between them
  - Each path is labelled: what triggers the move — a tap, a form submit, an error
  - This is the map AI follows when connecting your screens
  - No map, no navigation
- 🎨 Visual: Three labelled boxes connected by arrows — Home → "tap Start" → Active → "tap Done" → Summary. Left to right.

---

### DIAGRAM — Interaction pattern types
- Kicker: Every screen is doing one of these
- Title: Read. Edit. Add.\nConfirm. *And a few others.*
- Lead: Every screen in your prototype fits into one of a small number of interaction types. Knowing the type tells AI what components are needed, what states to include, and what transitions to build. Label each screen in your pattern with its type before you start building.
- 7 types (rendered as a card grid):
  - **Read** — User views content, no state change. Examples: Dashboard, detail page, feed, profile.
  - **Edit** — User modifies existing content. Examples: Edit profile, update settings, rename item.
  - **Add** — User creates something new. Examples: New post, create account, add to cart.
  - **Confirm** — User reviews and approves an action. Examples: Order summary, delete confirmation, submit form.
  - **Navigate** — User moves between sections. Examples: Tab bar, side menu, breadcrumb.
  - **Search / Filter** — User queries or narrows a list. Examples: Search results, filter panel, sort.
  - **Onboard** — User guided through first-time setup. Examples: Welcome, tutorial steps, permissions.
- Instructor note: Most student prototypes use 3–4 types. Ask students to call out which types their core flow uses before they start Phase 4.
- 🎨 Visual: Seven cards in a grid. Each: type name in bold + one example screen underneath. Consistent neutral style — no colour variation.

---

### STATEMENT — Two layers, one document
- Kicker: Put it all together
- Title: Two layers.\n*One document.\nAI builds from it.*
- Lead: Component inventory (with states inside) + Interaction pattern = your prototype pattern. That's it. This is what you hand to AI — or what AI reads from your code files. The better it is, the more accurate the output. You built most of this already in the last session. Today you make it explicit.
- 🎨 Visual: Two stacked rows — "Component inventory" + "Interaction pattern" — with a bold arrow pointing right to a phone frame outline.

---

### DIAGRAM — Your Atomic Design output is already most of the prototype pattern
- Kicker: Here's the good news
- Title: You already built\n*most of this.*
- Lead: The components you made last session — atoms, molecules, organisms — those are your component inventory. The templates you made are your screens for the interaction pattern. Most of the prototype pattern already exists in your design system. Today you make it explicit so your AI coding tool can read it.
- 🎨 Visual: Two columns with horizontal arrows connecting each row. Left: Atoms + Molecules → Organisms → Templates. Right: Component inventory → Interaction pattern → Screens.

---

### FULLSCREEN EXAMPLE — What a prototype pattern looks like
- Kicker: This is what you're making
- Layout: full-bleed document preview, no slide chrome
- 🎨 Visual: Full-screen document. Two clearly labelled sections — "Component Inventory" (table: component + states per row) and "Interaction Pattern" (screen flow list). Clean mono font, plain background.

---

### STATEMENT — Two paths
- Kicker: Which one is you?
- Title: Starting fresh — or\nalready have *something?*
- Lead: Some of you are starting fresh or have a partial system. Some of you already have components in your design tool or working code files. Both are fine. Both end up in the same place: a prototype pattern AI can build from. Read the two paths and pick the one that fits.
- 🎨 Visual: Two cards side by side — "Starting fresh" and "Already have components." A single arrow below both pointing down to "Prototype pattern."

---

## 4. Generate the prototype pattern (Phase 2)

---

### SECTION
- Section num: 04
- Title: Build your\nprototype pattern
- Sub: Pick your path. Same finish line.
- 🎨 Visual: --ochre background, title in --ink, centred. Signals it's time to work.

---

### PROCESS — Starting fresh: Step 1
- Kicker: Starting fresh · Step 1 of 4
- Title: Don't name the product yet.\nDescribe how it *feels.*
- Lead: The biggest mistake when starting fresh is jumping straight to "I'm building a food delivery app." That gets you generic food delivery UI. Instead, start with the feeling: calm, minimal, fast. No product name yet. Let the system have a personality before it has a purpose.
- Prompt to show: "I want a system that is [calm / energetic], [minimal / rich], [serious / playful], with [fast / deliberate] interactions. Generate design principles and basic style decisions — colour palette, typography, and spacing. No product name yet."
- 🎨 Visual: Prompt text on the left → arrow → AI output on the right (colour swatch, type sample, spacing rhythm).

---

### PROCESS — Starting fresh: Steps 2 & 3
- Kicker: Starting fresh · Steps 2 & 3 of 4
- Title: Build the list.\n*Then add your product.*
- Lead:
  - Step 2: from your design principles, ask AI to generate a component list — no product name yet
  - Any product built on this system would need these same pieces
  - Step 3: now bring in your specific concept — this is the moment AI narrows from "any product" to yours
- 2 steps:
  1. **Step 2** — "Based on these design principles, what UI components does this system need? List small pieces like buttons and inputs, medium pieces like forms and cards, and bigger sections like nav bars. Include the states each one needs. Keep it general — not tied to any specific product yet."
  2. **Step 3** — "My product is [X] for [Y users]. I have this prototype pattern: [paste]. Which components fit my 3–4 screens? What needs changing? What's missing?"
- 🎨 Visual: Three steps in a row — "Design principles" → "Component list" → "Your product." Dashed line before step 3 labelled "product context enters here."

---

### PROCESS — Starting fresh: Step 4
- Kicker: Starting fresh · Step 4 of 4
- Title: Last step: map\nhow your screens *connect.*
- Lead: You have your components (with their states already included) and your product context. One prompt left: map how screens connect. What does each screen lead to? What triggers the move? After this, your prototype pattern is ready.
- Prompt to show: "My prototype has these screens: [list]. The user's goal is [goal]. Show me how each screen connects to the others — what does a tap or action lead to? What happens if something goes wrong?"
- 🎨 Visual: Screen flow with a branch — main path: Home → "Tap Start" → Active → "Tap Done" → Summary. Error branch: "Submit fails" → Error screen → back to form. Labelled "Interaction pattern."

---

### FULLSCREEN EXAMPLE — What AI gives you back (starting fresh)
- Kicker: This is what AI gives you back
- Layout: full-bleed chat interface mockup, no slide chrome
- 🎨 Visual: Full-screen chat view. User prompt visible, AI response formatted as structured sections (Design Principles, Colour scale, Type scale, Spacing). Clean, no extra decoration.

---

### STATEMENT — Already have components intro
- Kicker: Already have components
- Title: Having components is good.\nBut can AI *read* them?
- Lead: If your design system lives in your design tool or in code, most of the prototype pattern already exists — it's just invisible. Your job isn't to build from scratch. It's to make the invisible visible. Three paths, depending on what you have.
- 🎨 Visual: Locked file icon → arrow labelled "make it explicit" → open document icon. Labels: "Your existing system" and "Prototype pattern."

---

### PROCESS — Already have components: In your design tool
- Kicker: Already have components · In your design tool
- Title: Export the names.\nAI fills in the gaps.
- Lead:
  - Most AI tools can't read design files directly — but they can read text
  - Export your component names and style values as a list, then paste them in
  - AI converts it to a prototype pattern and flags anything inconsistent or missing
- Prompt to show: "Here is my existing design system: [paste component names, variants, style values]. Document this as a prototype pattern: component inventory with states, and flag anything inconsistent or missing for a prototype."
- 🎨 Visual: Component list on the left → arrow "paste as text" → AI output card on the right with one gap flag highlighted.

---

### PROCESS — Already have components: In code *(optional — skip if no codebase)*
- Kicker: Already have components · In code · advanced
- Title: Point AI at your\ncomponents.\nIt reads them *directly.*
- Lead:
  - The fastest path — no manual export needed
  - Point your AI coding tool at your component folder and run one prompt
  - AI reads the files and generates the prototype pattern
  - Your job: review what it found and correct what's wrong — the review is the skill
- Prompt to show: "Read my component library and generate a prototype pattern: component inventory with variants and states, interaction patterns, and flag anything incomplete or inconsistent."
- 🎨 Visual: Folder icon → arrow "AI reads files" → prototype pattern output card.

---

### PROCESS — Already have components: In both *(optional — skip if no codebase)*
- Kicker: Already have components · In both · advanced
- Title: Two systems, one question:\n*which one is right?*
- Lead:
  - When your design system lives in both your design tool and in code, they're probably not the same
  - A component might be named "ButtonPrimary" in your design tool and "btn-primary" in code
  - A state might exist in one but not the other — this is called drift
  - Run the drift audit prompt and decide: which is the source of truth?
- Prompt to show: "Here is my design tool component list: [paste]. Here is my coded component list: [paste]. What exists in one but not the other? What's named differently?"
- 🎨 Visual: Two lists side by side — design tool components, code components — with mismatches highlighted between them. Arrow below to "source of truth decided."

---

### FULLSCREEN EXAMPLE — What a drift audit output looks like *(optional)*
- Kicker: AI spots what you missed
- Layout: full-bleed chat interface mockup, no slide chrome
- 🎨 Visual: Full-screen chat. AI response shows three sections: "Design tool only," "Code only," "Named differently." Clean list per section, mismatch rows lightly highlighted.

---

### MILESTONE — Activity: Generate your prototype pattern
- Kicker: Activity 01 · your turn
- Num: 10
- Title: Minutes
- Sub: Pick your path — starting fresh or already have components. Run the prompts from the prompt library. You're building one thing: a prototype pattern with a component inventory (states included) and an interaction pattern. That document is what AI builds from.

---

## 5. Build (Phase 4)

---

### SECTION
- Section num: 05
- Title: Build
- Sub: Pattern in hand. Time to make something real.
- 🎨 Visual: Dark background (--ink), single word "Build" centred in white. Nothing else.

---

### PROCESS — Build steps (MCP workflow)
- Kicker: How the build works
- Title: Design tool → MCP\n→ Pattern → *Screen by screen.*
- Lead:
  - Your design tool is already connected via MCP — your AI coding tool reads components directly
  - You're not pasting text — you're pointing AI at the source
  - Build one screen at a time and check the output before moving forward
  - That review loop is what makes the results accurate
- 5 steps:
  1. **Scope** — pick 2–3 screens from your interaction pattern. Start with the most important one.
  2. **Sync tokens** — "Read my design file. Extract design tokens (colours, type, spacing) and generate a CSS variables file."
  3. **Component inventory** — "Read my design file. List every component with its name and all its states. Flag anything missing."
  4. **Interaction pattern** — "Based on the component inventory, map the interaction pattern: which screens exist, what connects them, what triggers each transition."
  5. **Build screen by screen** — "Build [Screen name] using the component inventory, interaction pattern, and token file. Match component names exactly." → Review → Correct → Next screen.
- Minimum output: 1 screen in browser, navigation to 1 other state
- 🎨 Visual: Five numbered steps in a row — Scope → Sync tokens → Component inventory → Interaction pattern → Build screen by screen. Below step 5: a small loop arrow — "Review → Correct → Next screen."

---

### FULLSCREEN EXAMPLE — What a coded prototype looks like in the browser
- Kicker: This is what you're building toward
- Layout: full-bleed browser window mockup, no slide chrome
- 🎨 Visual: Full-screen browser window. A phone-width app (FitTrack) running centred on the page — top bar, workout card, CTA button, bottom nav all visible. Looks like a real running product, not a mockup.

---

### STATEMENT — Build reference (keep on screen)
- Kicker: Keep this visible while you build
- Title: Five prompts.\n*One rule.*
- Lead:
  1. Sync design tokens from your design file via MCP
  2. Generate your component inventory with all states
  3. Generate your interaction pattern
  4. Build each screen one at a time using the inventory and tokens
  5. Review, correct, repeat for each screen
  - **One rule:** if it's not in your component inventory, don't invent it — add it first, then build.
- 🎨 Visual: Full-width card — 5 numbered rows, one step per row. Bottom rule + one bold line: "Not in your inventory → add it first, then build." Large enough to read from the back of the room.

---

### STATEMENT — What AI will and won't do
- Kicker: Set your expectations now
- Title: AI builds it.\n*You make it right.*
- Lead:
  - Your first screen will be assembled, interactive, and running in the browser
  - It will also have problems — spacing off, groupings unclear, hierarchy flat
  - NN/G confirms this: even with detailed prompts, AI output misses nuance
  - That's not a failure — it's what the review step is for
  - Your designer's eye closes the gap between "technically built" and "actually good"
- 3 things to expect:
  1. **Colours and type will look generic at first** — until your token file is applied. If something looks off-brand, check whether the token step ran correctly.
  2. **Spacing and groupings need your eye** — AI places components correctly but doesn't always know what belongs close together. That's a design judgment, not a technical one.
  3. **Each correction makes the next screen better** — the feedback loop is cumulative. A screen you correct well becomes the reference for everything that follows.
- 🎨 Visual: Two phone frames side by side — left has spacing issues marked with callout labels, right shows the same screen corrected with check marks.

---

### MILESTONE — Hands-on build
- Kicker: Activity 03 · build
- Num: 20
- Title: Minutes
- Sub: Build from your prototype pattern using the MCP workflow. One rule: no new components without updating your inventory first. Review every screen before moving to the next one.

---

## 6. Reflect (Phase 5)

---

### SECTION
- Section num: 06
- Title: Reflect
- Sub: Share what you built. Say what surprised you.
- 🎨 Visual: White background, title "Reflect" centred. Calm — no decoration.

---

### STATEMENT — What comes next
- Kicker: This isn't the end
- Title: Your prototype is not\nthe destination.\nIt's the *question.*
- Lead: You built it. Now show it to a real person and see if it holds. Does the prototype pattern survive contact with a user? That's what next session is about. Everything you made today — the system, the prototype pattern, the prototype — was pointing toward that moment.
- 🎨 Visual: Two panels — left: phone frame (prototype), arrow right, right: person looking at a phone. Labels: "You built this" / "They test it next."

---

### END — Closing
- Kicker: One thing to carry forward
- Title: "Define the system.\nGenerate the prototype pattern.\nCheck your components.\nBuild from what exists.\nLet AI *do the rest.*"
- Lead: Five steps from design system to working prototype. The prototype pattern is the proof the system holds.
- Sign: — Winnie Nguyen
