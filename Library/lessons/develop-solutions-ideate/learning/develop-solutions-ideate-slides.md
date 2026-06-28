# Session 5 · Develop Solutions & Ideate

**Winnie Nguyen**

---

## Last Session Recap

**Last session: Information Architecture**

What you learned:
- How to distinguish inherited IA from evidence-based IA
- How to use card sorting to understand how users mentally group content
- How to draw a current-state and evidence-based sitemap
- How to map a user flow and identify friction caused by structural decisions

Your assignment was to:
- Map the current-state user flow for one core task in your live project
- Annotate each step as User, System, or Third Party
- Identify the single highest-friction step and write a rationale for why it exists

> Today we shift from understanding structure to generating solutions.

---

## What We're Building Today

Move from problem to idea to decision — without jumping to screens.

1. **Opportunity Tree** — map the space between your problem and your solutions
2. **Flow Review** — revisit your user flow to find where and what to improve
3. **Crazy 8s** — a technique to generate more ideas than you think you need
4. **Concept Sketching** — make the best ideas visible, legible, and discussable
5. **Concept Validation** — check which concepts are strong enough to develop further
6. **Prioritisation** — choose what to build, and why

---

## Mindset Shift

> **The best solution is almost never the first one.**

| Before | After |
|--------|-------|
| "I have the problem. Let me design a solution." | "I have the problem. Let me map the opportunity space — then generate solutions across it." |

The most common failure in ideation: converging before you've explored widely enough.

---

## The Rule

**No evaluation while generating.**

Write every idea down. The bad ideas are fuel for the good ones.

> "Yes, and..." — not "Yes, but..."

You will evaluate. That's what prioritisation is for. For now, the only failure is stopping too soon.

---

## Part 1 — Opportunity Tree Mapping

*Before you generate solutions, get clear on what opportunities exist.*

---

## What is an Opportunity Tree?

A visual framework that connects a product outcome to the user opportunities that could achieve it — and then to the solutions that could address each opportunity.

```
OUTCOME (your problem statement)
    │
    ├── Opportunity A
    │       ├── Solution A1
    │       └── Solution A2
    │
    ├── Opportunity B
    │       └── Solution B1
    │
    └── Opportunity C
            ├── Solution C1
            └── Solution C2
```

Developed by Teresa Torres — *Continuous Discovery Habits*

---

## Three Levels

**Outcome**
The goal you're designing toward. Your problem statement. One root node.

**Opportunities**
User needs, pain points, and desires that — if addressed — would move the user toward the outcome. Not solutions. The *spaces* where a solution could live.

**Solutions**
Specific ideas that address a given opportunity. They live under opportunities — not directly under the outcome.

> This ordering matters. It prevents teams from jumping to solutions before they've understood the full landscape.

---

## Why It Matters

Without the tree, most teams do one of two things:

**Brainstorm against the problem directly**
→ A cluster of loosely related ideas with no structure for evaluating them

**Default to one opportunity**
→ Usually the first one that comes to mind — leaving the rest of the problem space unexplored

The tree makes the structure of a problem visible. It shows you what you're solving for at each branch — and makes gaps obvious.

---

## Opportunities Are Not Solutions

| Looks like an opportunity | Actually a solution |
|---|---|
| "Users need a better notification system" | "Add push notifications with customisable frequency" |
| "Users need to track their progress" | "Build a dashboard with progress charts" |
| "Users need faster access to their data" | "Add a search bar to the home screen" |

**How to write an opportunity:**
> *"Users struggle to [need or goal] because [barrier or gap]"*

That formulation keeps the opportunity grounded in the user — not in a feature idea.

---

## How to Build the Tree

1. **Start with your outcome** — write your problem statement at the top
2. **Map the opportunities** — what are all the user needs, pain points, or desires inside this problem? Aim for 5–8
3. **Don't solve yet** — go wide on opportunities before you touch solutions
4. **Branch solutions from opportunities** — 2–3 specific ideas per opportunity
5. **Read the shape** — where are the dense branches? Where are the gaps?

> The shape of the tree tells you where your thinking is underdeveloped.

---

## Strong vs Weak Opportunities

| Weak | Strong |
|---|---|
| One branch dominates — all solutions attached there | Multiple branches with roughly balanced solution candidates |
| Opportunities written as features | Opportunities written as user needs |
| Tree built by one person | Tree built with the team — different people name different opportunities |

---

## Activity 1 · 15 min

**Round 1 · 5 min — Map the opportunities**
Write your problem statement at the top. Generate as many opportunities as you can — user needs and pain points inside this problem. Aim for at least 5. No solutions yet.

**Round 2 · 7 min — Branch solutions**
Pick your 3 strongest opportunities. Write 2–3 specific solution ideas underneath each one.

**Round 3 · 3 min — Read the tree**
Which opportunity has the most solutions? Which has the fewest? Is there an opportunity with no solution — and why?

> Debrief: Which branch surprised you? Did the tree surface an opportunity you hadn't considered?

---

## Before We Move On — Revisit Your Flow

*Your Opportunity Tree lives in user space. Your user flow lives in product space. Now make them talk to each other.*

---

## Why Revisit the Flow Now?

Last session you mapped a current-state user flow and identified your **highest-friction step**.

That friction is not random — it points directly to a user need that the current design isn't meeting.

Before generating solutions, we need to answer two questions:

1. **Which part of the flow are we trying to improve?**
2. **What does a better flow look like from the user's perspective?**

> Without this step, your Crazy 8s ideas will be disconnected from the real experience — and harder to evaluate.

---

## Connect the Flow to the Tree

Look at your current-state user flow alongside your Opportunity Tree.

| In the flow | On the tree |
|---|---|
| A step the user struggles with | → An opportunity |
| A handoff that breaks down | → An opportunity |
| A step that takes too long | → An opportunity |
| A step with no clear outcome | → An opportunity |

**Every friction point in the flow is a candidate opportunity on the tree.**

If your tree has opportunities that don't connect to any step in the flow — ask why. Either the flow is incomplete, or the opportunity is weaker than you think.

---

## Two Directions to Consider

**Option A — Improve an existing flow**
Keep the overall structure but redesign the friction point. The user still takes the same path — but a specific step works better.

**Option B — Propose a new flow**
The friction is structural. The current sequence doesn't work. You need to rethink the order, remove steps, or introduce a new entry point entirely.

> Neither is better by default. The right choice depends on where the friction lives in your tree.

---

## Activity 1B · 10 min — Flow Review

**Round 1 · 5 min — Map friction to opportunities**
Open your current-state user flow from the IA session. For each friction point you annotated, find the matching opportunity on your tree. Draw a line or note the connection.

Ask: Is there friction in the flow that has no opportunity on the tree? Add it now.

**Round 2 · 5 min — Decide your direction**
Choose one of the following and write it down:

- *"I need to improve [specific step] in the current flow because [opportunity it fails to address]."*
- *"The current flow doesn't work for [reason]. The new flow should [proposed change]."*

> This is your anchor for Crazy 8s. Everything you sketch next should connect back to this sentence.

---

## Part 2 — Crazy 8s

*You have a map of the opportunity space and a clear flow direction. Now go wide on solutions — fast.*

---

## What is Crazy 8s?

A technique from the Google Design Sprint. 8 different concepts in 8 minutes — roughly one minute each.

**How to run it:**
1. Fold A4 paper into 8 equal panels
2. Timer on — 8 minutes total
3. Sketch one idea per panel — label each with 2–3 words
4. No erasing, no perfecting — move when the time is up
5. Share back: pick your two most interesting panels and explain why

**What counts as a sketch:**
Boxes, arrows, labels, one sentence of context. Make the idea visible enough to discuss. Stick figures are fine.

---

## Strong vs Weak Crazy 8s

| Weak | Strong |
|---|---|
| 8 variations of the same idea | 8 directions that each take a different approach |
| Detailed, polished panels | Rough sketches readable in 15 seconds |
| Skipping panels — "this one is good enough" | Filling every panel, even when it's hard |
| All ideas assume the same solution shape | At least one panel breaks the dominant assumption |

---

## Try It on Your Own

*No time to run Crazy 8s in full today — but it's worth doing before next session.*

Before you start sketching concepts, do one round of Crazy 8s using the direction from your Flow Review:

1. Fold an A4 sheet into 8 panels
2. Set a timer for 8 minutes
3. Sketch one idea per panel — label each
4. Circle the two most interesting panels
5. Use those two as the basis for your concept sketches

> The constraint is the point. Force yourself to fill all 8 panels before judging any of them.

---

## Want to Go Deeper? — Google Design Sprint

*For students who want to run a full ideation workshop with their team.*

The **Google Design Sprint** is a structured 5-day process for answering critical design questions through rapid prototyping and testing. Crazy 8s is one technique inside it.

The sprint compresses months of work into one week:

| Day | Focus |
|---|---|
| Monday | Map the problem and pick a target |
| Tuesday | Sketch competing solutions |
| Wednesday | Decide and storyboard |
| Thursday | Build a realistic prototype |
| Friday | Test with real users |

**Resources to get started:**
- *Sprint* by Jake Knapp (the original book)
- [designsprintkit.withgoogle.com](https://designsprintkit.withgoogle.com) — free templates and facilitation guides
- [The Sprint Stories podcast](https://www.thesprintbook.com/podcast) — real teams, real sprints

> If your team has a big unsolved problem and a week to focus — this is worth running.

---

## Part 3 — Concept Sketching

*Make the most promising ideas visible enough to evaluate and develop.*

---

## What is Concept Sketching?

A single rough illustration of one idea — showing what the solution is, how it's structured, and what makes it different.

Not a wireframe. A thinking tool, not a deliverable.

**What it communicates:**
- The core structure: what are the main components?
- The key interaction: what does the user do, how does the product respond?
- The differentiating logic: what makes this different from the obvious approach?

> If you have to narrate it for it to make sense, it needs more labelling — not more detail.

---

## What the Outcome Looks Like

A finished concept sketch has four parts:

| Part | What it is | Example |
|---|---|---|
| **Key screen or moment** | The one view that makes the concept legible | The farm discovery screen, the pack-selection moment |
| **Component labels** | Named parts of the UI or interaction | "Filter by distance", "Seasonal tag", "Pack contents" |
| **Intent annotations** | Short notes on why things are placed where they are | "Below the fold so user commits to browsing first" |
| **One-sentence rationale** | *"This works because..."* — the logic behind the concept | "This works because it reduces decision fatigue by leading with the theme, not the list" |

It should be readable by someone who wasn't in your head — in under 30 seconds.

---

## How to Sketch a Concept

In real work, you're rarely starting from a workshop. You might be reacting to a research finding, responding to a HMW, sketching on a whiteboard mid-conversation, or developing a direction from a project brief.

1. **Identify your starting point** — a HMW question, a research insight, an analogy, a constraint, or a Crazy 8s panel
2. **Identify the one moment** that makes the concept make sense — the key screen, decision point, or interaction
3. **Sketch that moment** — rough, fast, no erasing
4. **Label everything** — name every component, annotate intent, explain placement
5. **Write one sentence:** *"This works because..."*
6. **Show it to someone cold** — note exactly where they get confused

> If you sketch more than one screen, you're wireframing. One well-labelled sketch is enough to evaluate and discuss.

---

## Strong vs Weak Concept Sketches

| Weak | Strong |
|---|---|
| Polished — time spent on visual quality | Rough — time spent on labelling and logic |
| Shows many screens | Shows the one screen that makes the concept legible |
| Components are unlabelled | Every component is named and annotated |
| No rationale — "it's obvious" | Explicit *"This works because..."* statement |
| Could belong to any product | Only makes sense for this specific opportunity |

---

## How to Use a Concept Sketch

**In a team setting**
Use it as a discussion object — not a proposal. It externalises the idea so the team can react to the concept, not the person pitching it.

**With a stakeholder**
It's legible enough to share without explaining — and rough enough that feedback feels safe to give. A polished sketch closes down conversation; a rough one opens it.

**For yourself**
Making an idea visible forces you to make it specific. The moment you can't label something, you've found the part you haven't thought through yet.

**As a gate before wireframing**
If the concept sketch doesn't hold up — if people can't read it, or the *"This works because..."* doesn't hold — it saves you from wireframing an idea that was never strong enough.

---

## Concept Sketching Doesn't Require a Workshop

Crazy 8s is one path in. But you can reach for a concept sketch from any of these:

| Starting point | What it looks like |
|---|---|
| A HMW question | "How might we help users trust a new vendor?" → sketch two different trust signals |
| A research insight | A user said "I never know if it's fresh" → sketch what proof-of-freshness looks like as a UI element |
| An analogy | "What if this worked like a playlist, not a search?" → sketch that model |
| A constraint | "We can only change the checkout step" → sketch three ways that constraint becomes a feature |
| A Crazy 8s panel | One of several starting points — not the only one |

> Concept sketching is available any time you need to make a direction visible enough to think about — with or without a workshop.

---

## Two Concepts, One Opportunity

Sketch two responses to the same opportunity. Then compare them.

| | Concept A | Concept B |
|---|---|---|
| **Core approach** | What's the fundamental logic? | What's the alternative logic? |
| **Key screen** | The one moment that makes it legible | The one moment that makes it legible |
| **This works because...** | | |
| **What it assumes** | About user behaviour or context | About user behaviour or context |

The comparison surfaces the design decision — you can't see it until both directions exist on paper.

> Use this when you're stuck between two directions, or when a stakeholder says "can we just do both?"

---

## Activity 3 · 10 min — Concept Sketching

**On-site · 10 min**

Pick one opportunity you want to develop. Sketch **one concept** that responds to it.

Label every component. Write *"This works because..."*

Share back: can the person next to you read it without your help? Where does it break down?

> Debrief: What did labelling force you to decide? Where did the sketch stop making sense?

---

## After This Session — Sketch the Second Concept

**Homework · before next session**

Go back to the same opportunity. Sketch a **second concept** that contradicts a key assumption in the first — a different approach entirely, not a variation.

Label it. Write *"This works because..."*

Then compare the two side by side: what's different about the core approach? What does each one assume about the user?

This is what you bring to the validation step — two directions for the same opportunity, ready to test.

---

## Validating Your Concept Sketches

*Before you move to prototyping — check that your concepts are strong enough to develop.*

---

## What Concept Validation Is

Not user testing. Not a prototype. Not a stakeholder sign-off.

It's a structured check that the logic of your concept holds before you invest further.

Three things to test:

1. **Legibility** — can someone else read this without your help?
2. **Rationale** — does the *"this works because..."* statement hold under challenge?
3. **Traceability** — does it connect back to a real opportunity in your tree?

> A concept that fails any of these isn't ready to prototype. It needs more thinking — not more pixels.

---

## The 30-Second Test — Legibility

Show your sketch to someone who wasn't in the session. No introduction, no context.

Ask: *"What does this do? Who is it for?"*

| Their response | What it means |
|---|---|
| Describes it accurately in ~30 seconds | Legible — ready to discuss and develop |
| Gets the product but misses the key interaction | Needs better component labels |
| Confused about who it's for | The opportunity connection is missing from the sketch |
| Needs you to explain it before they respond | Needs more labelling — not more detail |

> If you have to speak before they respond, the sketch is doing too little of the work.

---

## The Rationale Test — Does the Logic Hold?

Say *"This works because..."* aloud — without stopping, without qualifying.

Watch for these words: **but**, **if**, **as long as**, **assuming**

Each one signals an assumption hiding inside the rationale.

| ❌ Weak rationale | ✅ Strong rationale |
|---|---|
| *"This works because users will check the app each morning — if they have notifications on."* | *"This works because it surfaces options at the moment of decision, not before it."* |
| *"This works because people want to know where their food comes from — assuming they care."* | *"This works because it removes the research burden from the user and puts it on the platform."* |

Write the assumption down. It's not a flaw — it's exactly what your prototype should be designed to test.

---

## The Assumption Audit

Every concept makes assumptions. Surface them before someone else does.

For each concept, list: *"This concept assumes that users will / have / know / care about..."*

Then rate each assumption:

| Assumption | Confidence (1–5) | What changes if it's wrong? |
|---|---|---|
| Users notice the availability alert | 3 | Core trigger disappears — the whole flow breaks |
| Users are willing to plan a week ahead | 2 | Pack model doesn't work — switch to on-demand |
| Users trust the farm quality claim | 4 | Minor — can reinforce with photos |

**The lowest-confidence assumption = the riskiest thing about this concept.** Your next step should be designed to test it.

---

## The Opportunity Trace

Draw a line from your concept back to your opportunity tree.

The line should go: **Concept → Opportunity → Outcome**

| What you find | What it means |
|---|---|
| Clean line to a specific opportunity | Concept is grounded — ready to develop further |
| Line goes to the outcome, skipping opportunities | You're solving a product goal, not a user need |
| No clear line exists | The concept solves a problem you haven't mapped — go back to the tree |
| Two concepts trace to the same opportunity | One is probably solving it better — compare directly |

> If you can't draw the line, the concept isn't wrong — but it's floating. Ground it before building it.

---

## Reading Stakeholder Response

Share your rough sketch with a PO or key stakeholder. Watch — don't pitch.

| Their response | What it tells you |
|---|---|
| *"I don't understand what this is"* | Legibility problem — more labels needed, not more explanation |
| *"What happens if...?"* | The concept has something — explore the question they're raising |
| *"That assumes users will..."* | You've found the right conversation — that assumption is the design risk |
| *"Can we ship this?"* | Slow down. Compelling ≠ validated. The sketch is a hypothesis, not a decision |
| Silence | Ask: *"What would have to be true for this to work?"* |

> The most useful response is a challenge to an assumption. That's not resistance — that's design input.

---

## When to Move Forward

A concept is ready to prototype when it passes these four checks:

- [ ] Someone cold can read it in 30 seconds without your help
- [ ] The *"This works because..."* statement holds without qualifying
- [ ] You can name the riskiest assumption — and you know what you'd build to test it
- [ ] It traces back to a specific opportunity on your tree

**If it doesn't pass:** sketch a second version that resolves the failing check — before opening Figma.

> The goal isn't a perfect concept. It's a concept with a clear hypothesis — so the prototype has something to learn from.

---

## Part 4 — Prioritisation

*Not all concepts deserve the same investment. Choose deliberately.*

---

## Why Prioritisation Matters

Without a structured step, teams converge on:
- The idea the most senior person liked
- The one pitched most confidently
- The first one written down

None of these are good reasons to build something.

> Prioritisation separates concept selection from personal preference — and gives you a defensible rationale for what you develop next.

---

## The Effort–Impact Matrix

| Quadrant | What it means | What to do |
|---|---|---|
| **High impact · Low effort** | Quick wins | Prioritise immediately |
| **High impact · High effort** | Strategic bets | Plan for later; validate first |
| **Low impact · Low effort** | Nice-to-haves | Park unless quick to test |
| **Low impact · High effort** | Traps | Drop or defer |

The matrix is a conversation tool. Its value is making trade-offs explicit and shared — not producing an objective ranking.

---

## Dot Voting

When working with a group, dot voting prevents the loudest voice winning.

**Rules:**
- Each person gets 3 dots
- Vote silently — no explaining before voting
- You can stack dots on one concept
- Discuss after voting — the distribution is data

Dot voting + effort–impact matrix = individual signal and structural evaluation.

---

## Activity 4 · 10 min

**Round 1 · 5 min — Place your concepts**
Draw the matrix. Write each concept on a sticky. Place them honestly. Connect each back to the opportunity it came from on your tree.

**Round 2 · 5 min — Make a decision**
Pick one concept to develop into a prototype.

Write: *"I'm developing [concept] because [reason grounded in the opportunity it addresses and its position on the matrix]."*

> Debrief: Did the matrix change what you thought the best option was? Does your chosen concept trace back cleanly to a specific opportunity?

---

## Common Mistakes

| Mistake | The fix |
|---|---|
| Writing solutions as opportunities in the tree | Reframe as a user need, not a feature |
| Skipping the tree — going straight to Crazy 8s | Build the tree first, even roughly |
| All 8 Crazy 8s panels are the same idea | Sketch one idea that actively contradicts your first instinct |
| Only sketching one concept per opportunity | Sketch two — the second one reveals the assumption hiding in the first |
| Moving to Figma before validating the concept | Run the 30-second test and write the assumption audit first |
| Treating stakeholder enthusiasm as validation | Enthusiasm means it's compelling; the assumption audit tells you if it's sound |
| Prioritising by gut | Vote silently before discussing |

---

## Your Assignment — Before Next Session

Come to the next session with **one concept you're ready to prototype**.

1. Sketch your second concept — a different approach to the same opportunity, not a variation of the first
2. Run the 30-second test on both — show each to someone outside the project, no intro, and note where they get confused
3. Choose one concept to move forward with

> The prototype session starts from your chosen concept.

---

*"The goal of ideation is not to find the answer. It's to find enough answers that you can choose the right one."*

---

## Thank You

**Winnie Nguyen**

📧 nguyenphuctuongvan@gmail.com
