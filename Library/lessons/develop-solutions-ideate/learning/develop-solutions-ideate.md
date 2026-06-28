# Session 4 · Develop Solutions & Ideate

**Winnie Nguyen**

**Type:** Lesson · **Duration:** 60–90 min · **Audience:** Mixed
**Methods:** Opportunity Tree Mapping · Flow Review · Crazy 8s · Concept Sketching · Concept Validation · Prioritisation

---

## Key Concepts

### The Ideation Mindset
Ideation is a mode, not a step. It requires deliberately suspending judgment long enough to generate quantity — because the best solution is almost never the first one. The most common failure in ideation is evaluating too early and converging before you've explored widely enough.

### Diverge Before You Converge
The double diamond is the underlying logic: you expand first (more ideas, more directions), then compress (fewer, better). Skipping the expansion phase produces solutions that are obvious, safe, and rarely right. The value of ideation is not the ideas — it's the distance you travel from your starting assumption.

### Opportunity Tree Mapping
A structured method for moving from a problem statement to opportunities to solutions — without jumping directly from insight to screen. Developed by Teresa Torres, the Opportunity Tree makes the connection between user needs and design directions explicit and navigable. It prevents teams from latching onto one solution before they've understood the full landscape of opportunity.

### Brainstorming & Crazy 8s
Rapid idea generation under time pressure. Quantity over quality. Crazy 8s is a constraint-based format that forces 8 ideas in 8 minutes — breaking the pattern of over-investing in the first idea that sounds good.

### Concept Sketching
Visual thinking before committing to pixels. A concept sketch communicates intent — what a solution is, how it's structured, and why it's different from the obvious approach — faster than any written description. You don't need to draw well. You need to make the idea visible enough to discuss and critique.

Concept sketching is not only a post-workshop step. It can be triggered by a HMW question, a research insight, an analogy, or a constraint — any starting point where a direction needs to be made visible. Sketching two concepts for the same opportunity, rather than one, surfaces the assumption underneath each direction and makes the design decision explicit.

### Concept Validation
A structured check that a concept's logic holds before committing to a prototype. Three tests: legibility (can someone cold read it?), rationale (does the "this works because..." hold without qualifying?), and traceability (does it connect to a specific opportunity in the tree?). The assumption audit — listing and rating each assumption the concept makes — surfaces what the prototype needs to test.

### Prioritisation
Not all ideas deserve the same time. After generating widely, you need a structured way to evaluate which concepts are worth developing further. The effort–impact matrix separates high-leverage ideas from low-leverage ones — without personal bias driving the decision.

---

## Session Structure

| Time | Segment | Type | Duration |
|------|---------|------|----------|
| 00:00 | Open & Frame | Warm-up | 10 min |
| 00:10 | Last Session Recap + The Ideation Mindset | Concept | 10 min |
| 00:20 | Opportunity Tree Mapping + Flow Review | Explain + Activity | 25 min |
| 00:45 | Crazy 8s — Introduction | Explain only | 5 min |
| 00:50 | Concept Sketching — Entry points, demo, activity | Explain + Demo + Activity | 15 min |
| 01:05 | Concept Validation — 30-second test, rationale, assumption audit | Explain + Activity | 10 min |
| 01:15 | Prioritisation — Choosing What to Develop | Explain + Activity | 10 min |
| 01:25 | Wrap-up + Assignment | Close | 5 min |

---

## Tools & Materials

- Timer (Crazy 8s must be timed — this is non-negotiable)
- A4 paper folded into 8 panels — or the Crazy 8s template in FigJam
- Pens or markers (no pencils — you can't erase during ideation)
- FigJam or Miro for the Opportunity Tree and effort–impact matrix
- Your problem statement from Session 3

---

## Last Session Recap

**Last session: Information Architecture**

What you learned:
- How to distinguish inherited IA from evidence-based IA
- How to use card sorting to understand how users mentally group content
- How to draw a sitemap — current state and evidence-based
- How to map a user flow and identify friction caused by structural decisions

Your assignment was to:
- Map the current-state user flow for one core task in your live project
- Annotate each step as User, System, or Third Party
- Identify the single highest-friction step and write a rationale for why it exists

> Today we shift from understanding the structure of a problem to generating solutions for it. Bring your problem statement from the Synthesis session — that's the anchor for everything we do today.

---

## The Ideation Mindset

### Why most people ideate badly

Most designers (and most teams) move from problem statement to first idea to refinement — skipping the messy middle entirely. The messy middle is where the interesting solutions live.

| Common mistake | What it costs you |
|---|---|
| Falling in love with idea #1 | You never discover whether idea #5 was better |
| Evaluating while generating | Ideas die before they're useful — killed by the critic before the generator has finished |
| Designing alone | You get one perspective. That's usually one blind spot |
| Jumping straight to screens | You skip the structural thinking that makes screens worth building |

### The rule during ideation

**No evaluation while generating.** Write every idea down. The bad ideas are fuel for the good ones. "Yes, and..." not "Yes, but..."

You will evaluate later — that's what prioritisation is for. For now, the only failure is stopping too soon.

---

## Part 1 — Opportunity Tree Mapping

*Before you generate solutions, get clear on what opportunities exist. Most teams skip this step and pay for it later.*

### What is an Opportunity Tree?

A visual framework — developed by Teresa Torres — that connects a product outcome to the user opportunities that could achieve it, and then to the solutions that could address each opportunity.

The tree has three levels:

```
OUTCOME
(the goal you're designing toward — your problem statement)
    │
    ├── Opportunity A
    │       ├── Solution A1
    │       └── Solution A2
    │
    ├── Opportunity B
    │       ├── Solution B1
    │       └── Solution B2
    │
    └── Opportunity C
            └── Solution C1
```

**Outcome** — the product or user goal you're designing toward. This comes directly from your problem statement.

**Opportunities** — the user needs, pain points, and desires that, if addressed, would move the user toward that outcome. Opportunities are not solutions. They are the spaces where a solution could live.

**Solutions** — specific ideas that address a given opportunity. Solutions live under opportunities, not directly under the outcome. This ordering matters: it prevents teams from jumping to solutions before they've understood the full landscape of what's possible.

---

### Why the Opportunity Tree matters

Without it, most teams do one of two things:

1. **They brainstorm against the problem statement directly** — and produce a cluster of loosely related ideas with no structure for evaluating which ones are addressing the same underlying need.
2. **They default to one opportunity** — usually the first one that comes to mind — and generate solutions only for that, leaving the rest of the problem space unexplored.

The Opportunity Tree makes the structure of a problem visible. It shows you what you're solving for at each branch, and it makes gaps obvious: if one opportunity has five solutions mapped to it and another has none, that's a signal — not an accident.

---

### Opportunities are not solutions

This distinction is where the tree usually breaks down in practice.

| Looks like an opportunity | Actually a solution |
|---|---|
| "Users need a better notification system" | "Add push notifications with customisable frequency" |
| "Users need to track their progress" | "Build a dashboard with progress charts" |
| "Users need faster access to their data" | "Add a search bar to the home screen" |

An opportunity describes a user need — what they are trying to achieve, what is blocking them, or what they feel but can't resolve. A solution describes a specific response to that need. Getting this distinction right is what makes the tree useful.

**How to write an opportunity:**
> *"Users struggle to [need or goal] because [barrier or gap]"*

That formulation keeps the opportunity grounded in the user, not in a feature idea.

---

### How to build the tree

1. **Start with your outcome.** Write your problem statement at the top. This is your root node.
2. **Map the opportunities.** Ask: *"What are all the different user needs, pain points, or desires that relate to this problem?"* Write each one on a sticky. Aim for 5–8 before you evaluate.
3. **Don't solve yet.** Go wide on opportunities first. Resist the pull to jump to solutions — that comes next.
4. **Branch solutions from opportunities.** For each opportunity, generate 2–3 specific ideas that could address it. These are your solution candidates.
5. **Look at the shape of the tree.** Where are the dense branches? Where are the gaps? Which opportunities have no solutions yet? The shape tells you where your thinking is underdeveloped.

---

### Strong vs Weak Opportunity Trees

| Weak | Strong |
|---|---|
| Opportunities that are really just features ("Add a filter") | Opportunities that describe user needs ("Users can't find relevant content quickly enough to act on it") |
| One dominant branch with all solutions attached | Multiple branches with roughly balanced solution candidates |
| Solutions that don't trace back to a specific opportunity | Every solution connected to the opportunity it addresses |
| Tree built by one person in isolation | Tree built with the team — different people name different opportunities |

---

### Activity 1 · 15 min

*Use your problem statement from Session 3 — or the practice scenario below.*

**Practice scenario:**
> "Freelance professionals need a way to follow up with clients after sending a proposal because most forget to respond within 48 hours — causing freelancers to lose projects they would have won."

**Round 1 · 5 min — Map the opportunities.**
Write your problem statement at the top of a FigJam board or blank paper. Generate as many opportunities as you can — user needs and pain points that sit inside this problem. Aim for at least 5. No solutions yet.

**Round 2 · 7 min — Branch solutions.**
Pick your 3 strongest opportunities. For each one, write 2–3 specific solution ideas underneath it.

**Round 3 · 3 min — Read the tree.**
Step back. Which opportunity has the most solutions? Which has the fewest? Is there an opportunity you mapped with no solution — and why?

> Debrief: Did building the tree surface an opportunity you hadn't considered before? Which branch surprised you most?

---

## Part 2 — Brainstorming & Crazy 8s

*You have a map of the opportunity space. Now go wide on solutions — fast.*

### What is Brainstorming?

Structured divergent thinking — generating as many ideas as possible in response to a prompt, without judging or filtering as you go.

The output isn't a solution. It's a range of directions. You're expanding one branch of the Opportunity Tree, not committing to a destination.

**The rules:**

- **Quantity over quality** — your goal is volume. Aim for 20+ ideas in 10 minutes.
- **No evaluation during generation** — write every idea, even the ones you hate. You'll filter later.
- **Build on others** — in a group, "yes, and..." is the only permitted response during generation.
- **Wild ideas welcome** — an extreme idea often contains a useful principle even when the idea itself is impractical.

---

### What is Crazy 8s?

A Design Sprint technique that forces rapid ideation through constraint. You sketch 8 different concepts in 8 minutes — roughly one minute each.

**Why the constraint matters:** Most people invest their best thinking in the first idea that sounds viable. They refine it obsessively while the other 95% of the solution space goes unexplored. Crazy 8s breaks this habit by forcing you to keep moving.

**How to run it:**

1. Fold a sheet of A4 paper into 8 equal panels (three folds)
2. Start the timer — 8 minutes total
3. Sketch one idea per panel — label each with 2–3 words
4. No erasing, no perfecting — move to the next panel when the time is up
5. Share back: pick the two most interesting panels and explain why

**What counts as a sketch:**
Boxes, arrows, labels, and one sentence of context. You're not drawing a screen — you're making an idea visible enough to talk about. Stick figures are fine. "Draw it badly and quickly" is the correct approach.

---

### Strong vs Weak Crazy 8s

| Weak | Strong |
|---|---|
| 8 variations of the same idea | 8 directions that each take a different approach to the problem |
| Detailed, polished panels (means you spent 5 min on one) | Rough sketches that can be understood in 15 seconds |
| Skipping panels because "this one is good enough" | Filling every panel, even when it's hard |
| Ideas that all assume the same solution shape | At least one panel that breaks the dominant assumption |

---

### Activity 2 · 12 min

*Pick one opportunity from your tree — the one with the most tension or the least explored solutions.*

**Round 1 · 8 min — Crazy 8s.**
Take an A4 sheet, fold it into 8 panels. Timer on. Sketch one idea per panel for your chosen opportunity. Label each. No evaluation, no erasing. Keep moving.

**Round 2 · 4 min — Share back.**
Pick your two most interesting panels. Why those two? What did the constraint force you to think of that you wouldn't have otherwise?

> Debrief: How many of your 8 ideas were variations on idea #1? What happened when you ran out of obvious ideas? Do any panels belong on a different branch of your Opportunity Tree?

---

## Part 3 — Concept Sketching

*You have a range of directions. Now make the most promising ones visible enough to evaluate and develop — starting from wherever you are in the process.*

### What is Concept Sketching?

A single rough illustration of one idea — showing what the solution is, how it's structured, and what makes it different. A concept sketch is not a wireframe. It's a thinking tool, not a deliverable.

**What a concept sketch communicates:**

- The core structure: what are the main components of this solution?
- The key interaction: what does the user do, and how does the product respond?
- The differentiating logic: what makes this solution different from the obvious approach?

> A concept sketch should be interpretable by someone who wasn't in the room. If you have to narrate it for it to make sense, it needs more labelling — not more detail.

---

### The Outcome of a Concept Sketch

A finished concept sketch has four parts:

| Part | What it is |
|---|---|
| **Key screen or moment** | The one view that makes the concept legible — not the whole flow |
| **Component labels** | Named parts of the UI or interaction — every element identified |
| **Intent annotations** | Short notes on why things are placed or structured as they are |
| **One-sentence rationale** | *"This works because..."* — the logic behind the concept |

Readable by someone who wasn't in your head. In under 30 seconds.

---

### Entry Points — Concept Sketching Doesn't Require a Workshop

Crazy 8s is one starting point. But concept sketching can be triggered any time you need to make a direction visible:

**From a HMW question**
The most direct path. Take one HMW, sketch two different responses. One obvious — one that contradicts the first assumption. The gap between them is the design decision the team needs to make.

**From a research insight or user quote**
A user said something in an interview that points at a design direction. Sketch what that would look like before it disappears into a research document.

**From an analogy**
"What if this worked like a subscription, not a search?" Sketch that model applied to your product. Analogies are fast concept generators.

**From a constraint**
"We can only change the onboarding step." Sketch three ways that constraint becomes a feature rather than a limitation.

**From a Crazy 8s panel**
The familiar path — but now one entry point among several, not the only one.

---

### Sketching Two Concepts, One Opportunity

Instead of developing one idea, sketch two different responses to the same opportunity side by side.

| | Concept A | Concept B |
|---|---|---|
| **Core approach** | What's the fundamental logic? | What's the alternative logic? |
| **Key screen** | The one moment that makes it legible | The one moment that makes it legible |
| **This works because...** | | |
| **What it assumes** | About user behaviour or context | About user behaviour or context |

**Why this is useful:**
One sketch externalises an idea. Two sketches make the assumption underneath it visible. You can't see the assumption until you've drawn something that doesn't share it. The comparison surfaces the design decision — which is exactly what you need before committing to a direction.

Use this when you're stuck between approaches, or when a stakeholder is asking "can we just do both?" — two sketches answer that question faster than any meeting.

---

### How to Sketch a Concept

1. Identify your starting point — HMW, insight, analogy, constraint, or Crazy 8s panel
2. Draw the **key screen or moment** — the one that makes the solution legible
3. Add labels, not polish — name every component, annotate intent
4. Write one sentence underneath: *"This works because..."*
5. Show it to someone cold — note exactly where they get confused

> If you're sketching more than one screen, you've crossed into wireframing territory. One sketch, well-labelled, is enough to evaluate and discuss.

---

### Strong vs Weak Concept Sketches

| Weak | Strong |
|---|---|
| Polished — time spent on visual quality | Rough — time spent on labelling and logic |
| Shows many screens | Shows the one screen that makes the concept legible |
| Components are unlabelled | Every component is named and annotated |
| No rationale — "it's obvious" | Explicit *"This works because..."* statement |
| Could belong to any product | Only makes sense for this specific opportunity |

---

### How to Use a Concept Sketch

**In a team setting**
Use it as a discussion object — not a proposal. It externalises the idea so the team can react to the concept, not the person pitching it.

**With a stakeholder**
It's legible enough to share without explaining — and rough enough that feedback feels safe to give. A polished sketch closes down conversation; a rough one opens it.

**For yourself**
Making an idea visible forces you to make it specific. The moment you can't label something, you've found the part you haven't thought through yet.

**As a gate before wireframing**
If the concept sketch doesn't hold up — if people can't read it, or the *"This works because..."* doesn't hold — it saves you from wireframing an idea that was never strong enough.

---

### Facilitation Note — Live Demo

Before the activity, sketch live in front of the group. Take one HMW from a student's project — ideally the one with the most debate.

Sketch two concepts on the shared board. Narrate as you go:

- Say out loud what you're labelling first and why — that's where the concept lives
- Pause when the sketch breaks — "I can't draw this part because I haven't decided X yet"
- When writing *"This works because..."* — say it aloud before writing it down. If it sounds thin, the concept needs more thinking, not more drawing

The demo serves two purposes: it models the tool, and it lowers the bar — students who see a rough sketch that makes sense stop trying to draw something impressive.

---

### Activity 3 · 10 min — Concept Sketching (On-site)

Pick one opportunity from your tree — or the strongest direction from your Crazy 8s. Sketch **one concept** that responds to it.

Label every component. Write *"This works because..."*

Share back: have the person next to you read it without your help. Where does it break down?

> Debrief: What did labelling force you to decide? Where did the sketch stop making sense?

---

### After This Session — Sketch the Second Concept (Homework)

Go back to the same opportunity. Sketch a **second concept** that contradicts a key assumption in the first — a genuinely different approach, not a variation.

Label it. Write *"This works because..."*

Then compare the two side by side: what's different about the core approach? What does each one assume about the user?

**Facilitation note:** Make this explicit at the end of session — students should leave knowing that the first sketch is done, but the second sketch is what makes the validation step meaningful. Without two directions, the assumption audit has nothing to compare against.

---

## Part 4 — Concept Validation

*You have sketches. Before moving to prototypes, check that the logic of your concepts holds.*

### What Concept Validation Is

Not user testing. Not a prototype. Not a stakeholder sign-off.

It's a structured check — run before you invest further — that a concept is grounded, legible, and testable. Three things to check:

1. **Legibility** — can someone who wasn't in the room read this without your help?
2. **Rationale** — does the *"this works because..."* statement hold without qualifying?
3. **Traceability** — does it connect back to a specific opportunity in the tree?

A concept that fails any of these isn't ready to prototype. It needs more thinking — not more pixels.

---

### The 30-Second Test — Legibility

Show your sketch cold to someone who wasn't in the session. No introduction. Ask: *"What does this do? Who is it for?"*

| Their response | What it means |
|---|---|
| Describes it accurately in ~30 seconds | Legible — ready to discuss and develop |
| Gets the product but misses the key interaction | Needs better component labels |
| Confused about who it's for | The opportunity connection is missing from the sketch |
| Needs you to explain it before they respond | Needs more labelling — not more detail |

**Facilitation note:** Run this live in the session if time allows — have students swap sketches across the table, no verbal handoff, 30 seconds to read and describe back. The gap between what was intended and what was understood is where the labels need to go.

---

### The Rationale Test

Say *"This works because..."* aloud — without stopping, without qualifying.

Listen for these words: **but**, **if**, **as long as**, **assuming**. Each one signals an assumption hiding inside the rationale.

| ❌ Weak rationale | ✅ Strong rationale |
|---|---|
| *"This works because users will check the app each morning — if they have notifications on."* | *"This works because it surfaces options at the moment of decision, not before it."* |
| *"This works because people want to know where their food comes from — assuming they care."* | *"This works because it removes the research burden from the user and places it on the platform."* |

Every assumption surfaced here is a learning objective for the prototype — not a reason to abandon the concept.

---

### The Assumption Audit

Every concept rests on assumptions about user behaviour, context, or motivation. Surface them before someone else does.

For each concept, list: *"This concept assumes that users will / have / know / care about..."*

Then rate each assumption on confidence (1 = no evidence, 5 = well validated):

| Assumption | Confidence (1–5) | What changes if it's wrong? |
|---|---|---|
| Users notice the availability alert | 3 | Core trigger disappears — the whole flow breaks |
| Users are willing to plan purchases a week ahead | 2 | Pack model doesn't work — switch to on-demand |
| Users trust the quality claim without verification | 4 | Minor — reinforce with photos or farmer profiles |

**The lowest-confidence assumption = the riskiest thing about this concept.** The prototype should be designed to test that assumption before anything else.

---

### The Opportunity Trace

Draw a line from your concept back to your opportunity tree. The line should go: **Concept → Opportunity → Outcome**.

| What you find | What it means |
|---|---|
| Clean line to a specific opportunity | Concept is grounded — ready to develop further |
| Line goes to the outcome, skipping opportunities | Solving a product goal, not a user need — revisit the opportunity |
| No clear line | Concept addresses a problem you haven't mapped — go back to the tree |
| Two concepts trace to the same opportunity | Compare them directly — one is probably solving it better |

> If you can't draw the line, the concept isn't wrong — but it's floating. Ground it before building it.

---

### Reading Stakeholder Response

Share your rough sketch with a PO or key stakeholder — rough is the point. Watch. Don't pitch.

| Their response | What it tells you |
|---|---|
| *"I don't understand what this is"* | Legibility problem — more labels, not more explanation |
| *"What happens if...?"* | The concept has something — explore the question they're raising |
| *"That assumes users will..."* | You've found the right conversation — that assumption is the design risk |
| *"Can we ship this?"* | Slow down. Compelling ≠ validated. The sketch is a hypothesis, not a decision |
| Silence | Ask: *"What would have to be true for this to work?"* |

The most useful response is a challenge to an assumption. That's not resistance — that's design input.

---

### When to Move Forward

A concept is ready to prototype when it passes these four checks:

- [ ] Someone cold can read it in 30 seconds without your help
- [ ] The *"This works because..."* statement holds without qualifying
- [ ] You can name the riskiest assumption — and know what you'd build to test it
- [ ] It traces back to a specific opportunity on your tree

If it doesn't pass: sketch a revised version that resolves the failing check — before opening Figma. The goal isn't a perfect concept. It's a concept with a clear hypothesis so the prototype has something to learn from.

---

## Part 5 — Prioritisation

*You have concepts. Not all of them deserve the same investment. Choose deliberately.*

### Why prioritisation matters

Without a structured evaluation step, teams converge on the idea that the most senior person liked, the one that was pitched most confidently, or the first one written down. None of these are good reasons to build something.

Prioritisation separates concept selection from personal preference — and gives you a defensible rationale for what you develop next.

---

### The Effort–Impact Matrix

The most practical tool for evaluating concepts quickly. Two axes:

- **Impact** — How much value does this solution deliver for the user? Does it solve the core problem, or a peripheral one?
- **Effort** — How much time, complexity, or resource does this solution require to build and validate?

```
HIGH IMPACT
       |
   [Q2]  |  [Q1]
   Hard  |  Quick Wins
   Gains |
─────────────────── EFFORT
   [Q4]  |  [Q3]
   Don't |  Fill-ins
   bother|
       |
LOW IMPACT
```

| Quadrant | What it means | What to do |
|---|---|---|
| **Q1 · High impact, low effort** | Quick wins — do these first | Prioritise immediately |
| **Q2 · High impact, high effort** | Strategic bets — worth the investment if resources allow | Plan for later; validate first |
| **Q3 · Low impact, low effort** | Nice-to-haves — fill in when other work is done | Park unless quick to test |
| **Q4 · Low impact, high effort** | Traps — they consume energy without delivering value | Drop or defer |

**Important:** effort and impact are relative to each other, not absolute. One team's Q1 is another team's Q2. The matrix is a conversation tool — its value is in making trade-offs explicit and shared.

---

### Dot Voting — for group decisions

When working with a team or stakeholder group, dot voting prevents the loudest voice winning. Each participant gets 3 dots (sticky-note dots or votes in FigJam). They place their dots on the concepts they believe have the highest potential — without discussion first.

**Rules:**
- Vote silently — no explaining your choices before voting
- You can put multiple dots on one concept if you feel strongly
- Discuss after voting, not before — the distribution is data

Dot voting combined with the effort–impact matrix gives you both individual signal and structural evaluation.

---

### Activity 4 · 10 min

**Round 1 · 5 min — Place your concepts.**
Draw the effort–impact matrix on a whiteboard, FigJam, or paper. Write each concept on a sticky. Place them where you honestly believe they belong. Connect each sticky back to the opportunity it came from on your tree.

**Round 2 · 5 min — Make a decision.**
Pick one concept to develop into a prototype in the next session.
Write one sentence: *"I'm developing [concept] because [reason grounded in the opportunity it addresses and the matrix]."*

> Debrief: Did placing concepts on the matrix change what you thought the best option was? Does your chosen concept trace back cleanly to a specific opportunity on your tree?

---

## Your Assignment — Before next session

Bring **one validated concept sketch** to the next session. That's it.

1. Refine both concept sketches from today — close the gaps, label what's missing, sharpen the *"This works because..."* so it has no qualifiers
2. Run the assumption audit on each — list the top 3 assumptions, rate confidence 1–5, identify the riskiest
3. Run the 30-second test — show each sketch cold to one person outside the project, no introduction. Write down exactly where they hesitate or ask a question
4. Get one stakeholder response — share both with your PO or a key stakeholder. Note whether the response is confusion, curiosity, or challenge to an assumption
5. Make a decision — choose the concept that passed validation. That's the one you bring

> One validated concept sketch. The prototype session starts from there.

---

## Common Mistakes to Watch For

| Mistake | What it looks like | The fix |
|---|---|---|
| Writing solutions as opportunities in the tree | "Opportunity: Add a progress bar" | Reframe as a user need: "Users don't know how far along they are in the process" |
| Skipping the tree and going straight to Crazy 8s | Solutions generated without knowing which opportunity they address | Build the tree first — even a rough 10-minute version |
| Anchoring on the first idea | All 8 Crazy 8s panels are variations of the same concept | Actively sketch one idea that contradicts your first instinct |
| Only sketching one concept per opportunity | Moving to wireframes based on a single direction without comparison | Sketch two: one obvious, one that challenges the first assumption |
| Skipping the rationale | Sketch produced but no "this works because..." written | Write the sentence before showing anyone — it surfaces gaps the drawing hides |
| Moving to Figma before validating | Opening a wireframe tool while the concept logic is still unresolved | Run the 30-second test and assumption audit first |
| Treating enthusiasm as validation | Stakeholder says "I love it" — student moves to wireframes | Enthusiasm ≠ validated. Ask: "What would have to be true for this to work?" |
| Evaluating during ideation | "That won't work because..." said out loud during Crazy 8s | Name it as a rule violation — defer all critique to the validation and prioritisation steps |
| Prioritising by gut | Choosing the concept you're most excited about without examining the matrix | Vote silently before discussing, use the matrix to structure the decision |

---

## Further Resources

- [Teresa Torres — Continuous Discovery Habits](https://www.producttalk.org/2021/08/product-discovery/) — the source of the Opportunity Solution Tree and continuous discovery practice
- [Sprint by Jake Knapp](https://www.thesprintbook.com/) — the source of Crazy 8s and structured ideation within a 5-day format
- [IDEO Design Kit — Brainstorm Rules](https://www.designkit.org/methods/28) — the canonical rules for effective group ideation
- [How to Sketch for UX Design (YouTube — Google Ventures)](https://www.youtube.com/watch?v=ZtN3yHIWuRY) — practical sketching for non-illustrators
- Notion: Design Activities by DT Stage — Ideation methods in context of the full design thinking cycle

---

*"The goal of ideation is not to find the answer. It's to find enough answers that you can choose the right one."*

---

*Created by Winnie Nguyen · UX Class · Session 4 · May 2026*
