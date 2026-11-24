---
name: create-feature
description: Draft or improve a Jira Feature from a rough request, technical notes, requirements, or source documents.
agent: Feature Writer
argument-hint: Describe the work briefly or in detail. Include source/target or other specifics if known.
---

Use the Feature Writer Agent and `create-feature-skill`.

Start by inviting me to describe the Feature in my own words. I can provide a brief or detailed description, technical notes, requirements, or documents. Do not require a structured form.

Infer the work type and ask targeted follow-up questions only for material information that is missing. Ask one question at a time; do not run through a fixed questionnaire. For example, for a migration, clarify source, target, what is migrating, and boundaries as needed.

Honor my scope and grouping decisions. Draft one cohesive Feature unless I explicitly choose separate Features. Do not create Stories, Tasks, subtasks, or child work breakdowns.

Infer the archetype rather than asking me to select one by default. Use the Skill's format and quality criteria. Be concise, outcome-oriented, faithful to sources, and explicit about assumptions and unknowns.

Show the complete preview including Summary, Description (Context / Why, Scope, and Not in Scope when relevant), Expected Value, Measurement of Value, Archetype, and Assumptions / Dependencies / Open Questions.

Review the draft before presenting it. Drafting does not authorize Jira operations or local file changes.
