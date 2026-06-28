---
title: "Module 1 — Think Framework-First"
subtitle: "Why AI prototyping fails without a plan — and how to fix that before you start"
course: AI Prototype Development for Product Designers
module: 01
source-lesson: Library/lessons/ai-prototype-development/materials/ai-prototype-development-lesson.md
last-updated: 2026-06-26
---

## Module Overview

Most designers prototype the wrong way — and don't realise it until it's too late. They open Figma (or an AI tool), pick a screen, and start filling it in. Then the next screen. Then they realise the screens don't connect, components have drifted, and every AI prompt has to start from scratch because nothing is defined.

This module flips that. Before you touch a single screen, you'll learn what a prototype framework is, why it's what AI actually needs to build from, and how thinking framework-first makes everything that follows faster, more consistent, and less frustrating.

**By the end of this module, you'll be able to:**
1. Explain why screen-by-screen prototyping breaks down — and when
2. Describe the three layers of a prototype framework: component inventory, interaction map, and state map
3. Recognise what AI tools need from you before they can build anything useful
4. Decide which 2–3 screens you'll prototype in this course

**What's included:**
- 3 short videos (~10 min each)
- 1 exercise: Define your prototype scope
- No downloads needed for this module — just a notepad

---

## Before You Start

This course assumes you have basic Figma knowledge — you know how to create frames, use components, and connect screens. You don't need a full design system or coding skills. If you have a project you're working on (even a rough one), bring it. Every exercise uses your real project.

---

## Video Breakdown

### Video 1 — The Screen-by-Screen Trap (10 min)
*Why the way most designers prototype is slowing them down.*

Here's the pattern most designers follow when they start prototyping:

> Open Figma → pick a screen → design it → pick another screen → design it → try to connect them → realise they don't match → go back and fix → repeat.

This feels productive. It isn't. Here's what goes wrong:

**Components drift.** The button on screen 1 is slightly different from the button on screen 3. You made a small decision on each screen without realising it, and now they're inconsistent. When a stakeholder asks you to change the button style, you update it in 12 different places.

**AI prompts start from zero.** Every time you ask an AI tool to help you build or generate something, it has no memory of what you built before. You describe the button again. The card again. The nav again. Each prompt produces something slightly different because the AI has no reference point.

**States get missed.** You designed the default state of the login screen. But what does it look like when the password is wrong? When the page is loading? When the user has no internet? These states get discovered by your developer — or your user — not by you.

**Framework-first fixes all three:**

| Problem | Framework-first solution |
|---|---|
| Components drift | Define what components exist once, before building any screen |
| AI starts from zero | Give AI a framework document — it builds from that every time |
| States get missed | Map states before building, not after |

The framework is not extra work. It's the work that makes everything else faster.

---

### Video 2 — What a Prototype Framework Is (10 min)
*Three things AI needs that most designers never write down.*

A prototype framework is a structured description of your design system that AI can build from. It has three layers:

**Layer 1 — Component Inventory**
A list of every UI component in your prototype, with its variants and states. Not what they look like — what they *are* and what they can *do*.

Example:
```
Button
  — Variants: Primary, Secondary, Ghost
  — States: Default, Hover, Loading, Disabled

Input Field
  — Variants: Text, Password, Search
  — States: Empty, Filled, Error, Focused
```

**Layer 2 — Interaction Map**
How your screens connect. What leads to what, and under what conditions.

Example:
```
Login Screen
  — Success → Home Dashboard
  — Error → Login Screen (error state)
  — Forgot Password → Password Reset Screen

Home Dashboard
  — Tap product card → Product Detail Screen
  — Tap nav: Profile → Profile Screen
```

**Layer 3 — State Map**
For each key component or screen, what states need to be designed.

Example:
```
Home Dashboard
  — Loading (skeleton)
  — Loaded (content present)
  — Empty (first-time user, no data yet)
  — Error (failed to load)
```

When you hand these three layers to an AI tool, it stops guessing. It knows what exists, how things connect, and what variations to account for. Your prompts become specific, your output becomes consistent, and your prototype becomes something you can actually hand to a stakeholder or test with a user.

---

### Video 3 — Define Your Scope (10 min)
*Picking the right 2–3 screens before you build anything.*

The most common prototyping mistake is trying to prototype everything. You end up with 12 half-finished screens that don't connect cleanly, no time to test, and a demo that requires 10 minutes of narration to make sense.

For this course, you're building a focused prototype: **2–3 connected screens that demonstrate one user goal.**

**How to choose your screens:**

Start with the user goal — not the product feature. Ask: *"What is the one thing a user is trying to do?"* That goal becomes your prototype's spine. Every screen you include should move the user closer to completing it.

Good examples:
- User goal: "Apply for a home loan" → Screens: Start application → Upload documents → Confirmation
- User goal: "Find and buy a product" → Screens: Browse → Product detail → Checkout
- User goal: "Onboard to a new app" → Screens: Welcome → Sign up → Home

Avoid:
- Picking screens from different user goals (they won't connect naturally)
- Picking more than 3 screens (scope creep kills prototypes)
- Picking your most complex screen first (start with the core flow)

**Your entry point for this course:**

This course follows Entry Point A — you'll build your prototype framework from scratch using AI, starting from how your design should *feel* before worrying about what it looks like. You don't need a complete design system to start. You need a user goal, 2–3 screens, and an AI tool.

---

## Exercise — Define Your Prototype Scope

No template needed for this one. Open a note and answer these four questions:

1. **What is your project?** Describe it in 1–2 sentences. Who is the user? What problem does the product solve?

2. **What is the one user goal your prototype will demonstrate?** Write it as: *"The user wants to [goal]."*

3. **What are the 2–3 screens that cover this goal?** Name them. Don't design them yet — just name them.

4. **What do you NOT know yet?** List 2–3 things about your design system, your user flow, or your screens that you're unsure about. These are what the next modules will help you resolve.

Keep these answers somewhere accessible — you'll reference them in every module that follows.

---

## Knowledge Check

Before moving to Module 2, make sure you can answer these:

1. What breaks down when you prototype screen-by-screen?
2. Name the three layers of a prototype framework.
3. Why does AI need a framework document instead of just a description of your product?
4. What are your 2–3 prototype screens?

---

*Course: AI Prototype Development for Product Designers · Module 01 of 05*
*Created by Winnie Nguyen · Last updated June 2026*
