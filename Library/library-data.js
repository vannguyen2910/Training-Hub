// ═══════════════════════════════════════════════════════════════
//  WINNIE NGUYEN — KNOWLEDGE LIBRARY DATA
//  This is your source of truth. Edit this file to manage
//  your library. The HTML site reads from here automatically.
//
//  HOW TO ADD A MATERIAL:
//  1. Copy an existing entry (from { to the closing },)
//  2. Paste it at the top of the array (after the first [)
//  3. Update all the fields
//  4. Save this file and refresh the site
//
//  FIELD REFERENCE:
//  id            → unique number (increment from the last one)
//  type          → "lesson" | "framework" | "slides" | "guide"
//  program       → "ux-class" | "private" | "both"
//  title         → display title of the material
//  description   → 1–2 sentence summary shown on the card
//  audience      → "Beginner" | "Intermediate" | "Advanced"
//  duration      → e.g. "90 min" or "Reference" or "Full deck"
//  tags          → array of short topic tags, e.g. ["Research", "Synthesis"]
//  objectives    → array of learning outcomes (keep to 2–4)
//  prerequisites → array of suggested prior knowledge (can be empty [])
//  date          → display date, e.g. "Apr 2026"
//  file          → relative path to the .md file, e.g. "lessons/my-lesson.md"
//                  leave as "" if no file yet
//
//  crossRef      → array of intentional links to other materials
//                  each item: { id: <number>, rel: "<relationship>" }
//                  rel options:
//                    "requires"  → students should complete this first
//                    "uses"      → this lesson/guide uses this framework/tool
//                    "extends"   → goes deeper on the same topic
//                    "companion" → pair these together in the same session
//                  leave as [] if no cross-references
// ═══════════════════════════════════════════════════════════════

window.LIBRARY_DATA = [

  {
    id: 1,
    type: "lesson",
    program: "both",
    title: "Synthesis & Problem Definition in UX",
    description: "How to move from raw research findings to actionable insights using Affinity Mapping and How Might We statements. Includes a practice dataset and AI integration exercises.",
    audience: "Intermediate",
    duration: "90–120 min",
    tags: ["Research", "Synthesis", "HMW"],
    objectives: [
      "Apply affinity mapping to organise raw research findings into themes",
      "Write effective How Might We statements that reframe problems as opportunities",
      "Distinguish between a data point, an insight, and a problem statement",
    ],
    prerequisites: ["Basic familiarity with user interviews or observation"],
    date: "Apr 2026",
    file: "lessons/lesson-synthesis-problem-definition.md",
    page: "lessons/synthesis-problem-definition-in-ux/synthesis-problem-definition-in-ux.html",
    crossRef: [{ id: 6, rel: "requires" }, { id: 3, rel: "uses" }, { id: 8, rel: "companion" }]
  },

  {
    id: 2,
    type: "lesson",
    program: "ux-class",
    title: "Mental Models in UX Design",
    description: "Understanding how users build mental maps of systems — and how to design interfaces that align with those expectations rather than fight them.",
    audience: "Beginner",
    duration: "60–75 min",
    tags: ["UX Research", "Cognition"],
    objectives: [
      "Explain what a mental model is and why it matters in UX",
      "Identify mismatches between a product's design model and user expectations",
      "Apply mental model thinking to a critique of an existing interface",
    ],
    prerequisites: [],
    date: "Mar 2025",
    file: "",
    page: "lessons/mental-models-in-ux-design/mental-models-in-ux-design.html",
    crossRef: [{ id: 4, rel: "companion" }, { id: 7, rel: "extends" }]
  },

  {
    id: 3,
    type: "framework",
    program: "both",
    title: "Journey Mapping Workshop Guide",
    description: "A step-by-step facilitation guide for running a 2-hour journey mapping session with cross-functional teams. Includes warmup activities, facilitation cues, and debrief prompts.",
    audience: "Intermediate",
    duration: "2 hr workshop",
    tags: ["Research", "Workshop", "Facilitation"],
    objectives: [
      "Facilitate a structured journey mapping session with a mixed team",
      "Guide participants from raw touchpoints to emotional insight",
      "Extract actionable opportunities from the completed map",
    ],
    prerequisites: ["Some prior exposure to user research"],
    date: "Jan 2025",
    file: "",
    page: "frameworks/journey-mapping-workshop-guide/journey-mapping-workshop-guide.html",
    crossRef: [{ id: 6, rel: "requires" }, { id: 1, rel: "companion" }]
  },

  {
    id: 4,
    type: "framework",
    program: "ux-class",
    title: "UX Design Principles Reference",
    description: "A one-page cheat sheet of 12 core UX design principles — from Fitts's Law to progressive disclosure. Designed to be printed and used as a daily reference.",
    audience: "Beginner",
    duration: "Reference",
    tags: ["Foundations", "Principles"],
    objectives: [
      "Recall and apply 12 foundational UX design principles",
      "Use the reference sheet to evaluate design decisions in critiques",
    ],
    prerequisites: [],
    date: "Oct 2024",
    file: "",
    page: "frameworks/ux-design-principles-reference/ux-design-principles-reference.html",
    crossRef: [{ id: 2, rel: "companion" }, { id: 7, rel: "companion" }]
  },

  {
    id: 5,
    type: "slides",
    program: "ux-class",
    title: "Product Thinking Foundations",
    description: "Core concepts for thinking like a product designer — balancing user needs, business goals, and technical constraints. Full class deck with speaker notes.",
    audience: "Intermediate",
    duration: "Full class deck",
    tags: ["Product", "Strategy"],
    objectives: [
      "Explain the product design triangle: user, business, technology",
      "Apply product thinking to evaluate feature proposals",
      "Practise reframing design problems as business opportunities",
    ],
    prerequisites: ["Intro to UX Design"],
    date: "Nov 2024",
    file: "",
    page: "slides/product-thinking-foundations/product-thinking-foundations.html",
    crossRef: [{ id: 2, rel: "requires" }, { id: 7, rel: "companion" }]
  },

  {
    id: 6,
    type: "slides",
    program: "ux-class",
    title: "Intro to UX Research Methods",
    description: "An overview of the most common UX research methods — when to use each, what they're good for, and how to choose the right method for your question.",
    audience: "Beginner",
    duration: "45 min",
    tags: ["Research", "Methods"],
    objectives: [
      "Identify 6+ common UX research methods and their use cases",
      "Choose the right method given a research question and constraints",
      "Distinguish between generative and evaluative research",
    ],
    prerequisites: [],
    date: "Sep 2024",
    file: "",
    page: "slides/intro-to-ux-research-methods/intro-to-ux-research-methods.html",
    crossRef: [{ id: 8, rel: "companion" }, { id: 1, rel: "extends" }]
  },

  {
    id: 7,
    type: "guide",
    program: "both",
    title: "How to Give Design Critique",
    description: "A structured approach to critiquing design work — focusing on intent, not taste. Covers the ABCD method and common mistakes that make critique feel personal.",
    audience: "Intermediate",
    duration: "Reference",
    tags: ["Coaching", "Critique", "Culture"],
    objectives: [
      "Give specific, useful feedback grounded in design intent",
      "Avoid the most common critique pitfalls (taste, solutions, vagueness)",
      "Use the ABCD framework to structure any design feedback",
    ],
    prerequisites: [],
    date: "Sep 2024",
    file: "",
    page: "guides/how-to-give-design-critique/how-to-give-design-critique.html",
    crossRef: [{ id: 4, rel: "companion" }, { id: 2, rel: "extends" }]
  },

  {
    id: 8,
    type: "guide",
    program: "private",
    title: "Interviewing Users Effectively",
    description: "Techniques and scripts for running user interviews that uncover real behaviour, not just stated preferences. Includes a question bank and common pitfalls.",
    audience: "Beginner",
    duration: "Reference",
    tags: ["UX Research", "Methods", "Interviews"],
    objectives: [
      "Write open-ended questions that reveal real user behaviour",
      "Avoid leading questions and confirmation bias in interviews",
      "Synthesise interview notes into key observations on the same day",
    ],
    prerequisites: [],
    date: "Aug 2024",
    file: "",
    page: "guides/interviewing-users-effectively/interviewing-users-effectively.html",
    crossRef: [{ id: 6, rel: "companion" }, { id: 1, rel: "extends" }]
  },

  {
    id: 9,
    type: "lesson",
    program: "both",
    title: "Information Architecture",
    description: "How to organise content around users — not the org chart. Covers inherited vs evidence-based IA, card sorting, sitemaps, and drawing a current-state user flow before touching a wireframe.",
    audience: "Intermediate",
    duration: "90–120 min",
    tags: ["IA", "Navigation", "Card Sorting", "Sitemaps", "User Flows", "JTBD"],
    objectives: [
      "Distinguish between inherited IA and evidence-based IA — and audit an existing product structure",
      "Apply card sorting to reveal how users mentally group content",
      "Draw a current-state sitemap and identify where structure reflects business logic rather than user logic",
      "Map a current-state user flow using correct shapes and swimlanes before wireframing",
    ],
    prerequisites: ["JTBD Map from Session 2", "Validated Problem Statement from Session 3", "Screenshots of your current product screens"],
    date: "Apr 2026",
    file: "",
    page: "lessons/information-architecture/information-architecture.html",
    crossRef: []
  }

];
