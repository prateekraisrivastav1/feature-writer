---
name: create-feature
description: Draft or improve a Jira Feature through brief interactive discovery from a rough request, technical notes, requirements, or source documents.
agent: Feature Writer
argument-hint: Describe the Feature briefly. You can start with a component, initiative, business need, technical change, or rough idea.
---

Use the Feature Writer Agent and `create-feature-skill`.

Start by inviting me to describe what I want to build or change in my own words. I may provide a brief idea, a component name, technical notes, requirements, or supporting documents.

Use the Skill's guided discovery flow:
- Ask the four initial high-level questions.
- Present answer choices as interactive options where supported.
- Include a functional `Other` option that allows me to enter a custom answer.
- Keep the questions and choices brief.
- Ask one question at a time.
- Adapt the next question based on my previous answers.
- Do not force choices that are irrelevant to my request.
- Treat custom answers exactly like predefined choices.

The initial questions should establish:
1. Whether the Feature is primarily Business, Technical, Business & Technical, or Umbrella/High-level.
2. Whether it is BAU/Operational work, a New Capability/Initiative, an Enhancement, a POC/Exploration, a Migration/Modernization, or another type of work.
3. What outcome I am trying to achieve.
4. Whether the scope is a single cohesive Feature, an Umbrella/broad Feature, or still uncertain.

Do not treat these as a rigid questionnaire. Use my answers and initial description to avoid asking unnecessary questions, and adapt the discovery conversation.

After the initial discovery, ask additional targeted questions only if important information is still missing. Continue the conversation until the outcome, scope, and boundaries are sufficiently clear. Ask one question per turn.

Honor my scope and grouping decisions. Draft one cohesive Feature unless I explicitly choose separate Features. Do not create Stories, Tasks, subtasks, or child work breakdowns.

Infer the archetype rather than asking me to select one by default. Use the Skill's format and quality criteria. Be concise, outcome-oriented, faithful to sources, and explicit about assumptions and unknowns.

Show the complete preview including Summary, Description (Context / Why, Scope, and Not in Scope when relevant), Expected Value, Measurement of Value, Archetype, and Assumptions / Dependencies / Open Questions.

Review the draft before presenting it. Drafting does not authorize Jira operations or local file changes.
