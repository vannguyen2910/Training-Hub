---
title: "Customer Understanding"
subtitle: "From assumptions to evidence — talk to real people before you design"
type: lesson
program: ux-class
tags: [customer-understanding, friction-metrics, assumptions, research-questions, user-interviews, mixed]
level: mixed
duration: "90 min"
date: 2026-06-24
draft: false
slides: ""
previous-session: "Design Thinking for UX Designer"
next-session: ""
---

## Overview

The biggest mistake in UX isn't bad design — it's designing for the wrong person. This session challenges one core assumption students carry into every project: that they already understand their users because they've read the brief, used the product, or worked in the industry for years. They don't.

The session is built around a mindset shift: *you are not your user.* From that foundation, students learn four connected practices that build toward a real user interview. First, friction metrics — a structured way to identify where users struggle in an existing experience. Second, assumption mapping — a method for surfacing what the team believes without evidence, before talking to users. Third, research questions — how to turn unvalidated assumptions into a purposeful interview guide. Fourth, user interview fundamentals — the behaviours that separate a useful interview from a conversation that confirms what you already think.

Each practice section includes a short in-class activity and uses AI tools to speed up the generation phase. The session closes with two assignments: conducting a 60-minute user interview and running a structured assumption map with confidence ratings.

---

## Learning Objectives

By the end of this session, students will be able to:

1. **Identify** friction in an existing experience using three friction types: cognitive, interaction, and emotional
2. **Categorise** team assumptions by type (user, problem, solution, business) and write them in a testable format
3. **Rank** assumptions on an importance-vs-evidence matrix to decide which to test first
4. **Convert** an assumption into a focused research question and a set of 5–8 interview questions
5. **Apply** user interview fundamentals: asking open questions, following the story, and listening more than speaking
6. **Use** an AI tool to accelerate the preparation phase — assumption writing, interview question generation — while critically evaluating what it gets wrong

---

## Materials Needed

- Students' current screens from Assignment 3 (Design Thinking session) — screen flows captured in FigJam or Figma
- Shared FigJam or Miro board with friction analysis template (current + proposed experience tables)
- Assumption Map template — 2×2 grid (importance vs evidence) in FigJam or Notion
- Research Question template — table mapping: assumption → research question → interview questions
- Interview Guide template in Notion (pre-populated with common probing follow-ups)
- Students' real project from the previous session

---

## Pre-Class Preparation

Ask students to do the following before the session:

1. **Complete Assignment 3** from the previous session: screen flows of the current experience in FigJam or Figma. These are the input for the friction analysis activity.
2. **Read one article** about Jobs-to-Be-Done or assumption-based design (linked in Notion). Come with 1 question about something that wasn't clear.
3. **Think about** one user you'd ideally interview for your project. Who are they? What do you not know about them?

---

## Session Plan

| Act | Block | Topic | Duration |
|---|---|---|---|
| 1 · Mindset | Opening | You are not your user — mindset shift | 5 min |
| 2 · Friction | Teaching | What is friction metric? Three types + when/why/how | 10 min |
| 3 · Friction | Examples | Friction analysis tables (current + proposed) + NAB case study | 10 min |
| 4 · Practice | Activity | A Simple Friction Review | 10 min |
| 5 · Assumptions | Teaching | What is an assumption + 4 types + formula | 10 min |
| 6 · Assumptions | Teaching | The Assumption Map + when to run it | 10 min |
| 7 · Practice | Activity | Create assumptions (with AI) | 10 min |
| 8 · Research Qs | Teaching | Research questions: what/how/when + good vs bad examples | 10 min |
| 9 · Interview | Teaching | User interview fundamentals + how AI helps | 10 min |
| 10 · Close | Assignments | Two assignments briefed + wrap-up | 5 min |

**Total: 90 min**

> **Story logic:** The session moves from observation (what do we see in the current experience?) to assumption (what do we believe that we haven't proven?) to inquiry (how do we test it?). Each part builds on the previous one. Friction metrics give students something concrete to question. Assumption mapping turns those questions into hypotheses. Research questions turn hypotheses into interview prompts. The interview section provides the behaviours for actually running the conversation. By the end, students have the full chain from "here's what we see" to "here's how we find out."

---

## Core Content

### The Mindset Shift: You Are Not Your User

The most important thing to remember when doing user research: you are not your user.

You've read the brief. You know the product category. You may have been in this industry for years. None of that makes you a reliable proxy for the people who actually use the product — and the gap between what you assume and what users actually experience is often where the most important design insights live.

The goal of this session is to build the habits that close that gap. Not by doing more research — but by doing targeted research: knowing exactly what to look for, what you believe without evidence, and what questions to ask.

---

### Part 1 — Friction Metrics

#### What is a friction metric?

A friction metric is a measurable indicator of where users struggle in an experience. It quantifies the *cost* of using a product at specific points in the journey — so design decisions can be grounded in evidence about real user difficulty, not team opinion.

There are three types of friction:

**Cognitive friction** — Mental effort required to understand or make a decision.
Examples: unclear navigation labels, too many choices at once, jargon in UI copy, inconsistent patterns between screens.
*How to spot it:* Users pause, re-read, ask "what does this mean?", or make the wrong selection on first attempt.

**Interaction friction** — Physical effort required to complete an action.
Examples: small tap targets, too many steps to complete a task, form fields that reset on error, required information the user doesn't have to hand.
*How to spot it:* Users tap wrong elements, re-enter the same data, abandon mid-flow, or take more steps than necessary to complete a task.

**Emotional friction** — Anxiety, confusion, or frustration caused by the experience.
Examples: unclear error messages, trust issues at payment screens, fear of making an irreversible mistake, feeling overwhelmed by options.
*How to spot it:* Users hesitate, express doubt verbally ("is this safe?"), abandon high-stakes flows, or give up and call support instead.

#### When to run a friction analysis

Run a friction analysis at the start of any project involving an existing product, or before any major redesign. It gives your team a shared, evidence-based picture of where the current experience is failing — before any solution is proposed. Without it, team members often disagree about where the real problems are because everyone is working from different anecdotes and intuitions.

#### Why it matters

Friction analysis makes the invisible visible. Every team member has an opinion about what's broken. A friction analysis makes those opinions testable. It also creates a baseline — once you've measured friction in the current state, you can measure whether the proposed design actually reduces it.

#### How to run one

Use a friction analysis table with two views:

**Current Experience Friction Table** (analyse what exists today):

| Screen or step | User action | Friction type | Friction detail | Severity (1–5) |
|---|---|---|---|---|
| Login screen | Enter credentials | Cognitive | Two-factor auth flow is unclear — users don't know what to expect next | 3 |
| Application form step 3 | Upload document | Interaction | File format requirements not shown until after upload fails | 4 |
| Confirmation screen | Review and submit | Emotional | No indication of what happens after submission — no timeline, no contact option | 5 |

**Proposed Experience Friction Table** (evaluate your proposed design against the same steps):

| Screen or step | User action | Proposed change | Friction type reduced | Notes |
|---|---|---|---|---|
| Login screen | Enter credentials | Added inline explanation of 2FA steps | Cognitive | Eliminates the "what just happened?" moment |
| Application form step 3 | Upload document | Show format requirements before upload field | Interaction | Reduces failed attempts and re-uploads |

#### Real case: NAB Simple Home Loan

A home loan application at NAB's prior experience involved 27 separate taps to complete. Not 27 screens — 27 taps on a single interaction model. A friction analysis of the current state identified the specific interaction frictions at each step. The redesigned flow reduced friction at the identified points. Result: a 60% reduction in measured friction. The improvement didn't come from visual redesign — it came from identifying the specific friction types and removing them systematically.

---

### Part 2 — Assumptions

#### What is an assumption?

An assumption is anything your team believes about users, problems, solutions, or the business — that you haven't yet proven with evidence.

Every design brief contains assumptions. Every sprint planning session is full of them. The problem isn't having assumptions — it's not knowing which ones are true and which ones could kill the product if wrong.

There are four types of assumptions:

**User assumptions** — Who the users are, what they care about, how they behave.
*Example:* "Users check this feature at least once a week."
*Risk if wrong:* The entire product is optimised for a usage pattern that doesn't exist.

**Problem assumptions** — The nature, severity, and prevalence of the problem being solved.
*Example:* "Users struggle to find the right plan because there are too many options."
*Risk if wrong:* The solution doesn't reduce friction because friction wasn't coming from the options — it was coming from unclear plan descriptions.

**Solution assumptions** — Whether the proposed solution actually addresses the problem.
*Example:* "A comparison table will help users choose faster."
*Risk if wrong:* The comparison table adds cognitive load instead of reducing it.

**Business assumptions** — Market viability, competitive dynamics, pricing sensitivity, regulatory factors.
*Example:* "Users are willing to pay for this feature if bundled with the existing plan."
*Risk if wrong:* The business model doesn't hold, regardless of whether the UX is excellent.

#### The assumption formula

Write every assumption in this format:

> *"We believe [WHO] will [WHAT] because [WHY]. We'll know we're right when [SIGNAL]."*

**Weak assumption:** "We think users want a faster checkout."
**Strong assumption:** "We believe returning customers will use one-click checkout in over 40% of sessions because reducing checkout steps was the top complaint in last quarter's NPS responses. We'll know we're right when post-launch checkout completion rates exceed 80%."

The strong version names the user segment, the expected behaviour, the evidence for the belief, and a measurable signal. The weak version is an opinion dressed as a hypothesis.

#### The Assumption Map

The Assumption Map is a 2×2 prioritisation matrix with two axes:

- **Y axis (vertical): Importance** — How critical is this assumption to the project's success? If it's wrong, does everything fall apart?
- **X axis (horizontal): Evidence** — How much evidence do we have that this assumption is true?

This creates four quadrants:

- **High importance + low evidence (top-left):** These are your highest priority assumptions to test. They matter most and you know the least about them. Start here.
- **High importance + high evidence (top-right):** These are validated. Proceed with confidence, but revisit if the project scope changes significantly.
- **Low importance + low evidence (bottom-left):** These may not be worth testing at all, unless they become important later.
- **Low importance + high evidence (bottom-right):** These are known and low-risk. Move on.

#### When to run an assumption map

Run an assumption map at the start of a project (before any research begins), when a project has stalled and the team is disagreeing about direction, when a stakeholder changes the brief, when a prototype test produces unexpected results, and after any major user research synthesis session.

---

### Part 3 — Research Questions

#### What are research questions?

A research question is a specific, investigable question that, when answered, will either confirm or refute one of your assumptions. Research questions are not the same as interview questions — a research question defines what you need to learn; interview questions are the prompts you use to find the answer in a conversation.

The chain works like this:
**Assumption** → **Research question** → **5–8 interview questions**

#### How to write a research question

**What:** A focused, neutral question about behaviour, attitude, or context — not about your solution.
**How:** Not too broad ("How do users feel about banking?") and not too narrow ("Do users prefer blue or green CTA buttons?"). Aimed at understanding reality, not confirming a preference.
**When:** Written before any interview, before any design work, and before any solution is presented to users.

**Why research questions matter:**
Without them, interviews drift. The conversation follows wherever the facilitator's natural curiosity leads — often toward solution feedback rather than problem understanding. Research questions keep the interview anchored to what the team actually needs to learn.

#### Good vs bad research questions

**Bad research questions:**
- "What do users think of our new checkout redesign?" — This is feedback-fishing, not research.
- "Do users prefer the current or proposed navigation?" — This is preference testing, not problem understanding.
- "Would users use a feature that lets them do X?" — Hypothetical behaviour questions produce unreliable answers.

**Good research questions:**
- "How do users currently manage [specific task] without our product?"
- "What causes users to stop mid-flow in a checkout process?"
- "What information do users look for before committing to a plan?"

**Real case: Urban Farming research**
A team researching urban farming practices came in with the assumption that the main barrier to entry was space and equipment cost. Their research question: "What prevents people who are interested in urban farming from getting started?" After interviewing 6 participants, the main barrier turned out to be knowledge and confidence — not cost or space. The product direction changed entirely because the research question was broad enough to capture the real answer.

#### From assumption to interview guide

| Assumption | Research question | Interview questions |
|---|---|---|
| "Users struggle to find the right plan because there are too many options." | "How do users currently navigate plan selection decisions?" | "Walk me through the last time you compared two plans for any service. What did you do first?" / "What made it easy or hard?" / "How did you know you'd made the right choice?" |
| "Users are comfortable submitting documents via mobile." | "What is users' experience with document-heavy tasks on mobile?" | "Tell me about a time you had to upload something important on your phone." / "What made you feel confident or nervous about it?" |

---

### Part 4 — User Interview Fundamentals

#### The five fundamentals

Good user interviews are a discipline, not just a skill. These five behaviours separate interviews that generate real insight from interviews that confirm what you already think:

**1. Ask open questions**
Open questions ("Tell me about a time when...") invite stories. Closed questions ("Do you prefer X or Y?") invite yes/no answers. Closed questions feel efficient but produce data that can't be acted on. The single most important interviewing skill is resisting the urge to close.

**2. Follow the story**
When a user says something unexpected or interesting, stop and follow it — even if it's off your script. The most important insights usually come from moments the interviewer didn't anticipate. Your script is a safety net, not a constraint.

**3. Stay curious**
Approach every answer as though you've never heard this situation before — even if you've heard five identical answers in the last hour. Curiosity changes your body language, your tone, and the questions you follow up with. Users can tell whether you're genuinely interested or just ticking boxes.

**4. Listen more than you speak**
If you're talking more than 20% of the time, something is wrong. Interviewers often fill silence with suggestions, summaries, or agreement noises that subtly guide the user's next answer. Silence is productive. Let it breathe.

**5. Observe, don't just hear**
Watch what the user *does* as well as what they say. Hesitations, re-reads, and physical reactions are data. If a user says "it's fine" but pauses for 5 seconds before pressing a button — the pause is the insight, not the "fine."

#### The golden rule

The goal of a user interview is not to get the user to validate your ideas. It is to understand their reality. The moment you start presenting your solution or asking "would you use this?", you've stopped doing user research.

#### How AI tools help at this stage

AI tools can accelerate four specific tasks in the research preparation phase:

1. **Generating assumptions from a brief** — Paste your brief and ask the AI to generate a list of testable assumptions across all four types. Review critically; the AI will miss context you know.
2. **Writing assumption statements** — Use the formula ("We believe [WHO] will [WHAT] because [WHY]. We'll know when [SIGNAL]") as a prompt template. AI is fast at generating the structure; your judgment determines which ones are actually important.
3. **Drafting interview questions** — Give the AI your research question and ask for 8–10 open-ended interview questions. Expect to cut at least half; AI tends to generate repetitive questions that circle the same point.
4. **Synthesising notes after interviews** — Paste your interview notes and ask for themes. Useful as a first pass — but always return to the raw notes before drawing conclusions.

The limit of AI in research: it cannot assess which assumptions matter most for your specific project, it cannot evaluate whether an interview question is leading or neutral in your context, and it cannot replace the judgment that comes from sitting in a room with a real user.

---

## Activities

### 🔍 Activity — A Simple Friction Review
**Type:** In-class · FigJam or Figma
**Time:** 10 min
**Format:** Solo, using your current screen flows

Open your screen flows from Assignment 3. You'll identify friction in your current experience using the three friction types.

**Instructions:**

1. **(3 min)** Choose one key flow from your screen capture (e.g. onboarding, checkout, core task). Open it in FigJam or Figma.

2. **(5 min)** For each major step in the flow, add a sticky note identifying one friction. Use a colour code:
   - 🟡 **Yellow** = Cognitive friction (understanding / decision difficulty)
   - 🔴 **Red** = Interaction friction (physical effort / too many steps)
   - 🔵 **Blue** = Emotional friction (anxiety / confusion / frustration)

   Write each sticky in this format: *"[User action] causes [friction type] because [specific issue]."*

3. **(2 min)** Share back: your single highest-severity friction point and why you rated it that way.

---

### 💡 Activity — Create Assumptions with AI
**Type:** In-class · AI chat tool + FigJam or Notion
**Time:** 10 min
**Format:** Solo, then small group share

Generate a set of assumptions for your project, then map them by importance and evidence.

**Instructions:**

1. **(3 min)** Open your AI tool and paste this prompt:

   > *"I'm a UX designer working on [project description]. My users are [who they are]. Generate 10 assumptions for this project — cover all four types: user assumptions, problem assumptions, solution assumptions, and business assumptions. Write each one in this format: 'We believe [WHO] will [WHAT] because [WHY]. We'll know when [SIGNAL].'"*

2. **(4 min)** Read the output. Select 4–5 assumptions that feel most relevant. Open your Assumption Map template in FigJam and place each assumption in the correct quadrant:
   - High importance + low evidence → top-left (test these first)
   - High importance + high evidence → top-right
   - Low importance → bottom half

3. **(3 min)** Share back: which assumption lands in the top-left quadrant? Why is it high-stakes and unproven?

> **Critical check:** Review the AI output carefully. Did the AI make your users sound too generic? Did it miss a key user segment, constraint, or competitor behaviour that you know about? Edit at least 2 of the AI-generated assumptions to make them more specific to your real project context.

---

### 📋 Activity — Prepare Research Questions
**Type:** In-class · AI chat tool + Notion
**Time:** 10 min
**Format:** Solo

Turn your top-priority assumption into a research question and a set of interview questions.

**Instructions:**

1. **(1 min)** Take your highest-priority assumption (top-left quadrant from the mapping activity).

2. **(2 min)** Write one research question for it. Use the format: *"How / What / Why do users [behaviour or attitude]?"* Keep it neutral — no solution language.

3. **(5 min)** Open your AI tool and paste this prompt:

   > *"I'm a UX designer preparing for a user interview. My research question is: [paste your research question]. Generate 8 open-ended interview questions that would help me answer this research question. Each question should invite a story, not a yes/no answer. Avoid hypothetical questions ('would you ever...?'). Start each question with Tell me, Walk me through, What, How, or Why."*

4. **(2 min)** Review the output. Cut any questions that are repetitive or leading. You should end up with 5–6 strong questions.

---

## AI in Practice

### 🤖 Try these prompts

**For assumption generation:**
> *"I'm a UX designer working on [project]. Generate 10 assumptions across 4 types: user, problem, solution, and business. For each, use the format: 'We believe [WHO] will [WHAT] because [WHY]. We'll know when [SIGNAL].'"*

**For interview question generation:**
> *"My research question is: [paste it]. Generate 8 open-ended interview questions. Avoid hypotheticals. Start each with Tell me, Walk me through, What, How, or Why."*

**For synthesis after interviews:**
> *"Here are my interview notes from 3 user sessions: [paste notes]. Identify the 3 most common themes across all three sessions. For each theme, quote one specific thing a user said that illustrates it. Then list 2 assumptions that these sessions either confirm or refute."*

### 🧠 Critical thinking

After using AI for assumption or question generation:
- Which assumptions did the AI generate that you wouldn't have thought of? Are any of them genuinely testable?
- Which AI-generated assumptions are too generic to be useful for your specific project?
- Did the AI produce any leading interview questions — ones that hint at an expected answer? Rewrite them.

---

## Assessment

### Quick knowledge check

Run verbally at the close of the assumptions section (2–3 min):

1. Name the 3 types of friction. Give one example of each from a product you use.
2. A team says: "We already know our users well — we don't need to map assumptions." What's the risk in that?
3. What's the difference between a research question and an interview question?
4. A user says "Yeah, this looks fine" in an interview. What do you do next?

---

## Assignments

### Assignment 1 — Conduct a User Interview
**Due:** Before next session
**Time estimate:** 60–90 min preparation + interview
**Type:** Research · Real conversation

Run one 60-minute user interview with a real user of your project. This is the most important deliverable in the course so far.

**Before the interview:**
1. Choose a participant — a real user or someone who fits your primary user description. Not a friend, colleague, or family member who already knows your project.
2. Use the research questions and interview questions from the in-class activity as your guide.
3. Brief the participant: explain the purpose (understanding their experience), the format (60 minutes, questions about their experience, no right or wrong answers), and whether you'll record (get consent first).
4. Set up a notes document: timestamp, participant pseudonym, direct quotes marked in quotation marks, observations noted separately from what was said.

**During the interview:**
5. Open with a warm-up: "Tell me a bit about yourself and your role" or "Walk me through your typical week using [relevant product or task]."
6. Ask your prepared questions. Follow any answer that surprises you.
7. End with: "Is there anything I didn't ask that you think would be helpful for me to understand?"

**After the interview:**
8. Write up your notes within 2 hours — memory fades quickly.
9. Identify your 3 most surprising findings. What did you learn that you didn't already know?
10. Note which assumptions were confirmed, which were refuted, and which need more data.

**Deliverable:** Interview notes document + reflection paragraph (what surprised you, what it means for your project). Share with your mentor before the next session.

> **AI in Practice:** *"Here are my interview notes: [paste notes]. What are the 3 most significant things this user told me? For each, tell me: which assumption it confirms or refutes, and what design implication it suggests."*

---

### Assignment 2 — Assumption Mapping
**Due:** Before next session
**Time estimate:** 45–60 min
**Type:** Analysis · FigJam or Miro

Build a full assumption map for your project and rate your confidence in each assumption.

1. List at least 10 assumptions across all four types (user, problem, solution, business). Use the formula: *"We believe [WHO] will [WHAT] because [WHY]. We'll know when [SIGNAL]."*
2. Place each assumption on the Assumption Map: importance (y-axis) vs evidence (x-axis).
3. Add a confidence level to each assumption: Unproven (no evidence), Partially validated (some indirect signals), or Validated (direct evidence from research).
4. Identify the 3 assumptions you most need to test. For each one, write one research question.
5. After your user interview (Assignment 1) — return to the map and update the confidence levels based on what you learned.

**Deliverable:** FigJam or Miro link with your Assumption Map. Come ready to discuss in the next session.

> **AI in Practice:** *"I'm a UX designer working on [project]. Generate 10 assumptions across all four types. For each assumption, suggest: 1 research question that would help test it, and whether desk research, a user interview, or analytics data would be the best way to get the answer."*

---

## Further Resources

- **IDEO Design Thinking — Empathise:** https://designthinking.ideo.com/ — Empathy methods overview including observation and interview guides
- **NNg — User Interviews:** https://www.nngroup.com/articles/user-interviews/ — When to use them, how to structure them, and common mistakes
- **Assumption Mapping (Strategyzer):** https://www.strategyzer.com/ — Original framework for testing business and product assumptions
- **Jobs-to-Be-Done:** https://jobs-to-be-done.com/ — Background on the JTBD framework referenced in this session
- **Steve Portigal — Interviewing Users** — The foundational book on conducting user interviews. Chapter 3 on question types is most directly useful.

---

*Created by Winnie Nguyen · UX Class · Last updated June 2026*
