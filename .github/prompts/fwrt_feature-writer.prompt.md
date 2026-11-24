---
name: create-feature
description: Draft or improve a Jira Feature through brief interactive discovery from a rough request, technical notes, requirements, or source documents.
agent: Feature Writer
argument-hint: Describe the Feature briefly. A component, initiative, business need, technical change, or rough idea is enough to start.
---

Use the Feature Writer Agent and `create-feature-skill`.

Invite me to describe what I want to build or change in my own words. A brief idea, component name, technical notes, requirements, or supporting documents are acceptable.

Use the Skill's guided discovery:
- Ask the four initial high-level questions.
- Present selectable choices where supported.
- Include a functional `Other` option that reveals an inline text input.
- Keep questions and choices brief.
- Ask one question at a time and adapt the next question to my answers.
- Do not force irrelevant choices.
- Treat custom answers exactly like predefined choices.

The initial questions establish:
1. Feature type: Business, Technical, Business & Technical, Umbrella/High-level, or Other.
2. Work type: BAU/Operational, New Capability/Initiative, Enhancement, POC/Exploration, Migration/Modernization, or Other.
3. Desired outcome.
4. Scope preference: single cohesive Feature, broad/Umbrella Feature, unsure, or Other.

These are a lightweight starting point, not a rigid questionnaire. Skip or adapt questions when the initial description already answers them.

Ask additional targeted questions only when material information is missing. Continue until the outcome, scope, and boundaries are sufficiently clear. Ask one question per turn.

Honor my grouping decisions. Draft one cohesive Feature unless I explicitly choose separate Features. Do not create Stories, Tasks, subtasks, or child work breakdowns.

Infer archetype internally; do not ask me to select it by default.

**Strict output format:** The final Feature preview and Jira description must contain exactly these three sections:
- Description
- Expected Value
- Measurement of Value

The Jira Summary is the title field, separate from these sections. Do not include Context/Why, Scope, Not in Scope, Assumptions, Dependencies, Open Questions, Archetype, discovery notes, or any other section in the Feature output. Keep unresolved questions and assumptions internal. They must not block a high-level Feature draft or creation; omit unresolved details unless necessary to accurately express one of the three required sections.

Be concise, high-level when requested, outcome-oriented, faithful to sources, and avoid invented details or metrics.

Show the complete preview with Summary and the three sections only. Review the draft before presenting it. Drafting does not authorize Jira operations or local file changes.
