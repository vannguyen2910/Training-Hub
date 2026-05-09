# Session 3 · Synthesis & Problem Definition

**Winnie Nguyen** — Senior Product Designer at NAB

---

## Session 2 Recap

**Last session: Customer Understanding**

What you learned:
- How to surface and challenge assumptions
- How to write a user interview discussion guide
- How to run structured user interviews
- How to log raw notes without interpretation

Your assignment was to:
- Run user interviews on your live project
- Log raw notes in your Research Log within 24 hours
- Start mapping Jobs-to-Be-Done from what you heard
- Begin your Design Decision Log

> Today we take those raw notes and turn them into something actionable.

---

## The Pipeline

Raw notes don't become a design direction on their own. There's a sequence — and each step feeds the next.

| Step | Method | Input | Output |
|------|--------|-------|--------|
| 1 | Affinity Mapping | Raw observations | Themes that reveal patterns |
| 2 | Insight Statements | Themes | The "so what" behind each pattern |
| 3 | How Might We | Insights | Design opportunities to explore |
| 4 | Problem Statement | HMW questions | One problem the whole team can act on |

You can't write a strong problem statement without insights. You can't find insights without clustering first. Start at the top and work down.

---

## Mindset Shift

> **Research without synthesis is just noise.**
>
> You have the raw data. This session is about making it mean something.

| Before | After |
|--------|-------|
| "I have interview notes… let me start designing." | "I have interview notes. Now I'll find the patterns, name the insights, define the real problem." |

**And one more shift — how you run synthesis matters as much as whether you run it:**

| Solo synthesis | Workshop synthesis |
|----------------|-------------------|
| You analyse alone, then present a report | The room builds meaning together |
| Stakeholders receive findings | Stakeholders co-own the findings |
| Buy-in happens later — if at all | Alignment is a byproduct of the process |
| One perspective on the data | Multiple lenses catch what one person misses |

> Running synthesis as a workshop isn't just more collaborative — it's more accurate. The PM notices something you normalised. The engineer flags something infeasible before it becomes a problem statement. The stakeholder stops pushing back on the output because they helped create it.

---

## Setting Up Your Workshop

Before you run the pipeline, you need the right people in the room.

### Who to invite

- **Product Manager** — needs to align the roadmap to what users actually said
- **Engineer** — spots technical constraints that affect what's feasible
- **Fellow designer** — second set of eyes on what's a pattern vs. an outlier
- **Stakeholder or lead** — makes prioritisation decisions; better if they've seen the data themselves

> Keep it to 4–6 people. More than that and clustering becomes a committee.

### Room setup

1. **Share raw notes in advance** — give participants 15 min to read before the session, not during
2. **One tool, one board** — FigJam or Miro, set up with all raw observations already on stickies
3. **No titles in the room** — everyone clusters as equals; seniority distorts patterns

### Your role as facilitator

You are **not** the one with the answers. You are the one holding the process.

- Open with the research question: *"We're here to find out what the data is telling us — not to confirm what we already think."*
- Protect silent clustering time — resist the urge to explain notes
- Name disagreements as useful: *"That tension is data too."*
- Time-box each step ruthlessly
- Close by asking: *"What surprised you most?"* — surprises are where the real insights live

---

## Step 1 — Affinity Mapping

*Your first move in the room. Raw notes go in, themes come out.*

### What is Affinity Mapping?

A method for clustering raw research observations into themes — so patterns emerge instead of staying buried in your notes.

**01 · One note, one observation**
Each quote, behaviour, or data point lives on its own sticky. No grouping yet.

**02 · Move notes that feel related**
Group silently first — don't discuss, just feel. Let the clusters find themselves.

**03 · Name the cluster**
Write a header that captures what unites that group. That header is your theme.

### How to run it

1. Dump everything — one observation per sticky note (FigJam, Miro, or physical)
2. Read each note — don't sort yet, just absorb the full weight of the data
3. Start moving — cluster notes that feel related, without labelling first
4. Name each cluster — the header should answer: "what unites these notes?"
5. Stand back — look for super-themes, outliers, and surprises

> 🤖 **AI Task:** Paste your raw notes into Claude and ask: "Cluster these into themes. What patterns are emerging?" Compare AI groupings to your own.

---

### 🤖 AI in Practice — Affinity Mapping

**Try this prompt:**

```
Here are my raw interview notes:
[paste your notes]

Cluster these into themes.
Give each theme a short name
and explain what connects
the notes in it.
```

**Watch out for:** AI groups by keywords, not meaning. It may lump a usability problem and an emotional reaction into the same cluster. Always split and rename clusters yourself.

**Reflect:** Did AI surface a theme you hadn't noticed? Did it miss one that only made sense from being in the room?

*Rule: try it with AI first, then verify with your own judgment before using the output.*

---

### Activity 1 · 10 min

> Walk me through the findings from your interviews. What surprised you the most?

---

## Step 2 — Insight Statements

*You have themes. Now name what each one means — not just what happened, but why it matters.*

### What is an Insight Statement?

**Insight = Observation + Implication**

| | |
|--|--|
| **Observation** | What you saw or heard — a direct quote, a behaviour, a pattern from the research |
| **Implication** | The "so what" — why this matters for your design decisions |

**Example:**

*Observation:* "Users kept abandoning the checkout flow after the payment step — even when the transaction went through."

*Implication:* "This means the app fails to confirm the transaction clearly — users don't know it worked, which breaks trust at the most critical moment."

---

### Strong vs Weak Insight

| Weak | Strong |
|------|--------|
| "Users find the app confusing" | "Users can't locate booking status after submission, which causes them to call support — revealing a gap in post-action feedback design" |
| "Users want a simpler interface" | "Hospitality managers visit the app 3–5x per shift to monitor requests but must navigate 4 screens each time — suggesting a need for a persistent dashboard view" |
| "Users liked the new feature" | "3 of 4 users completed the booking flow faster with the new layout, but all 4 got stuck at the date picker — pointing to a specific interaction failure, not a layout issue" |

---

### 🤖 AI in Practice — Writing Insights

**Try this prompt:**

```
Here is a raw observation from my research:
[paste note]

Help me write this as an insight statement:
what was observed, and what does it imply
for design?
```

**Watch out for:** AI often writes generic implications. If the implication could apply to any product, it's not specific enough — push it further.

**Reflect:** Did the AI version capture the emotional tension from the interview? What did you have to add or correct?

*Rule: try it with AI first, then verify with your own judgment before using the output.*

---

### Activity 2 · 10 min

> Pick one moment from your interviews. Write the insight: what did you observe, and what does it mean for the design?

---

## Step 3 — How Might We

*You have insights. Now turn them into questions the team can design toward — without jumping to solutions.*

### What is "How Might We"?

A framing technique that turns an insight into a design opportunity — without jumping straight to a solution.

**How** — Assumes it's solvable. Not "can we" or "should we" — it's already a given that it can be done.

**Might** — Leaves the solution open. "Might" invites exploration. No single right answer yet.

**We** — It's a team challenge, not one person's burden to solve alone. It builds shared ownership.

---

### From Insight to HMW

**Insight:**
> "Users abandon after checkout even when the transaction succeeds — because there is no clear confirmation — breaking trust at the most critical moment in the flow."

**How Might We...**
- ...make it immediately clear that a transaction was successful, without requiring the user to check?
- ...reduce user anxiety at the moment between action and confirmation?
- ...design a post-payment experience that builds trust instead of doubt?

---

### 🤖 AI in Practice — How Might We

**Try this prompt:**

```
Here is my insight statement:
[paste insight]

Generate 5 'How Might We' questions based on this.
Vary the scope — some broad, some narrow.
```

**Watch out for:** AI HMWs can sound polished but be too vague to act on. Check: can you actually design something to answer each one?

**Reflect:** Which AI question was most useful? Which was most surprising? Did any make you reframe your insight?

*Rule: try it with AI first, then verify with your own judgment before using the output.*

---

### Activity 3 · 8 min

> Take the insight you wrote. Turn it into 3 different "How Might We" questions.

---

## Step 4 — Problem Statement

*Converge. Take everything the room has built and land on one problem worth solving — one that everyone in the room can stand behind.*

### What makes a strong Problem Statement?

**01 · User-centred**
It describes a real person's problem — not a business goal, not a feature request, not a technical constraint.

**02 · Specific, not vague**
"Users struggle to track booking status" beats "users find the product confusing." Precision makes it testable.

**03 · Open to multiple solutions**
A good problem statement doesn't hint at the answer. It opens possibility instead of closing it down.

---

### The Formula

```
[User type]  needs a way to  [goal / need]  because  [insight / barrier]
```

**Example:**
> "First-time online shoppers need a way to know their order was confirmed immediately after payment because the current delay and lack of feedback causes them to abandon — and sometimes re-order — thinking the transaction failed."

**Before you finalise, ask:**
- ✓ Does it describe a person, not a system or a feature?
- ✓ Could you solve this problem in more than one way?
- ✓ Is it grounded in something real you heard from users?

---

### Strong vs Weak Problem Statement

| Weak | Why weak | Strong |
|------|----------|--------|
| "We need to redesign the checkout flow" | Solution, not a problem | "First-time buyers need a way to confirm their order was placed because the current lack of feedback after payment causes them to re-submit, creating duplicate orders" |
| "Users don't trust the app" | Too vague to act on | "New users need a way to verify their account is set up correctly because there is no onboarding confirmation — leading them to contact support before completing their first action" |
| "The app needs better notifications" | Solution, not user-centred | "Frequent users need a way to know when a status change happens without opening the app because they currently miss time-sensitive updates — causing delays and frustration" |

---

### 🤖 AI in Practice — Problem Statement

**Try this prompt:**

```
Here is my research finding:
[paste insight or HMW]

Help me write a problem statement using this formula:
[User] needs a way to [goal]
because [barrier].
```

**Watch out for:** AI often fills the "because" with logical-sounding assumptions. Make sure the barrier comes from what users actually said — not what seems reasonable.

**Reflect:** Would a designer who wasn't in your sessions understand exactly who you're designing for from this statement alone?

*Rule: try it with AI first, then verify with your own judgment before using the output.*

---

### Activity 4 · 15 min

> Draft the problem statement for your project. Use the formula. Ground it in what you actually heard.

---

## Your Assignment — Before Session 4

1. Run affinity mapping on all your interview notes — use FigJam, Miro, or physical sticky notes
2. Write 3 insight statements from your research. Use the Observation + Implication formula for each
3. Share your problem statement with one stakeholder — a PM, engineer, or team lead — and note how they respond

> 🤖 **AI Challenge:** Paste your raw notes into Claude. Ask it to cluster themes. Compare its groupings to yours — where did it help? Where did it miss context only you had?

---

*"After today, you should have one thing: a problem worth solving."*
