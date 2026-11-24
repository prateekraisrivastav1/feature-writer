---
name: create-feature-skill
description: Interactive discovery, instructions, format, quality criteria, archetypes, and a primary example for drafting clear Jira Features from rough or incomplete inputs.
---

# Create Feature Skill

## Objective

Create clear, concise, outcome-oriented Jira Features from rough requests, technical notes, requirements, existing Features, or source documents. Improve Feature quality—not merely copy the source's wording or weaknesses.

## Conversational Discovery

### Opening

Invite the user to provide a brief description in their own words. They may describe a component, initiative, business need, technical change, rough idea, or provide supporting documents.

Do not require a structured template or detailed requirements upfront.

Example:

> What Feature would you like to create? A brief description or component name is enough to get started.

### Guided Initial Discovery

After the user's initial description, begin a lightweight interactive discovery session using the following four questions to establish the broad nature of the Feature.

These questions are a starting framework—not a rigid questionnaire. Use information already provided by the user to skip, adapt, or simplify questions when appropriate.

#### Question 1 — What type of Feature is this?

Suggested choices:

- Business-focused
- Technical
- Business & Technical
- Umbrella / High-level
- Other

Use the user's choice to guide the writing approach and level of detail. Do not treat this selection as the Feature archetype.

#### Question 2 — What kind of work is this?

Suggested choices:

- BAU / Operational work
- New Capability / Initiative
- Enhancement to existing functionality
- Proof of Concept / Exploration
- Migration / Modernization
- Other

Adapt the choices to the user's context when appropriate. The user should not be forced to select an irrelevant option.

#### Question 3 — What are you trying to achieve?

Ask the user to briefly describe the desired outcome.

Example:

> What are you trying to achieve with this Feature? A sentence or two is enough.

This can be free text. Do not ask for detailed requirements at this stage.

#### Question 4 — What is the scope at a high level?

Suggested choices:

- A single cohesive Feature
- A broad / Umbrella Feature
- I'm not sure yet
- Other

Use the response to understand how the user wants the work tracked. Do not split or merge work contrary to the user's decision.

### Interactive Choice Behavior

Where the interface supports interactive choice controls:

- Present choices as selectable buttons/options.
- Keep the question and option labels short and clear.
- Include an **Other** option wherever choices are presented.
- Selecting **Other** must reveal an inline text input where the user can enter a custom answer.
- The custom answer must be submitted as the user's answer and treated exactly like a predefined choice.
- After a custom answer is submitted, continue the discovery conversation using that answer.
- Do not require the user to select a predefined option if their answer does not fit.

If interactive buttons are unavailable, present the same choices in a concise conversational format and allow the user to type their response.

### Adaptive Discovery

The four initial questions establish a high-level overview. They do not necessarily provide enough information to draft a good Feature.

After each response:

1. Incorporate the user's answer into the working understanding.
2. Reassess what is known and what remains unclear.
3. Determine whether another question is materially needed.
4. Ask the next most useful question, one at a time.
5. Adapt the question to the user's answers and the type of work.
6. Stop when the Feature can be drafted clearly and responsibly.

Do not mechanically ask all four questions if the user's initial description already answers some of them.

Do not mechanically ask additional questions just to complete a checklist.

### Mandatory Multi-Turn Discovery Loop

**Discovery is a continuing conversation, not a single clarification step. Do not stop after asking one question or after the initial four questions if important gaps remain.**

After the user's initial description:

1. Understand the request and identify the likely work type.
2. Extract all information already provided.
3. Identify the material information still missing.
4. Select the single most important unanswered question.
5. Present the question with relevant options when useful.
6. Include a working `Other` option for custom answers.
7. Wait for the user's response.
8. Incorporate the answer into the working understanding of the Feature.
9. Reassess the remaining gaps and determine the next most useful question.
10. Repeat until enough information is available to draft a clear and correctly scoped Feature.

After every user response, reassess the information. Do not simply move through a predefined list of questions.

Maintain the following discovery state internally throughout the conversation:

- **Confirmed information:** Facts and decisions explicitly supplied by the user or supported by provided sources.
- **Information still needed:** Missing details that could materially affect the Feature.
- **Scope decisions:** The user's decisions about what is included, excluded, or grouped together.
- **Assumptions:** Reasonable but unconfirmed details that must be disclosed.
- **Open questions:** Details that remain unresolved and should be recorded in the draft.

Do not ask the user to repeat information already supplied.

### Continue Asking Questions When

- The answer reveals another important gap.
- The scope is still unclear.
- The source and target of a migration are not established.
- The intended outcome is not understood.
- The answer introduces additional systems, processes, or scope that need clarification.
- The user's response creates ambiguity about grouping or delivery expectations.
- The difference between exploration and implementation materially affects the Feature.

### Stop Asking Questions When

- The intended outcome is sufficiently clear.
- The main scope and boundaries are understood.
- Material grouping decisions have been resolved.
- Remaining unknowns can be transparently documented as assumptions or open questions.
- Further clarification would not materially improve the draft.

Do not ask questions merely to complete a checklist. The goal is sufficient understanding, not collecting every possible detail.

When discovery is complete, briefly summarize the understanding and proceed to the Feature draft. Do not require an additional confirmation if the user has already provided enough information and has not requested one.

### Clarification Rules

- Ask **one focused question per turn**.
- Use interactive options where they help the user answer quickly.
- Always make `Other` functional when choices are presented.
- Wait for the user's answer before asking the next question.
- Continue the discovery conversation across multiple turns until sufficient information is available.
- Prefer concrete, natural-language questions over jargon or archetype labels.
- Questions should be relevant to the detected work type and the user's stated goal.
- Do not ask for information already supplied, inferable with confidence from source material, or unnecessary to draft.
- Prioritize questions that materially affect outcome, scope, grouping, source/target, implementation-vs-exploration commitment, or boundaries.
- If the user cannot answer, accept that and record the uncertainty as an assumption/open question.
- If a reasonable draft can be produced, stop questioning. Do not prolong discovery to achieve perfect completeness.
- If scope/grouping is materially ambiguous, ask the user whether they want one cohesive end-to-end Feature or separate independently tracked Features. Their choice is binding. Do not silently split or merge later.
- Clarify whether a POC/investigation is exploratory or intended to include delivery only when that changes commitment or scope.
- Do not ask the user to choose a Feature archetype by default.
- Do not combine several unrelated clarification questions into one long message.
- Do not generate the Feature immediately after the first answer if important discovery questions remain unanswered.

### Work-Type Discovery Guidance

Use these questions as guidance, not as a mandatory questionnaire. Ask only what is relevant and not already known.

**Migration**

Understand:

- What is the source system or technology?
- What is the target system or technology?
- What needs to be migrated?
- Is the migration complete or limited to selected workloads, applications, or processes?
- Which environments or business areas are included?
- Are setup, configuration, validation, or cutover part of the intended scope?
- Are there known constraints or dependencies?

**New Capability**

Understand:

- What capability is needed?
- Who or what will use it?
- What outcome should it enable?
- What is the intended scope?

**Enhancement**

Understand:

- What existing capability or process is being enhanced?
- What needs to change?
- Why is the change needed?
- What is the desired outcome?

**Automation**

Understand:

- What is the current process?
- Which parts should be automated?
- What initiates the automation?
- What should the automation produce or achieve?

**Integration**

Understand:

- Which systems are involved?
- What information or actions need to flow between them?
- What is the expected interaction or outcome?
- Are there important integration boundaries?

**Data Pipeline / Processing**

Understand:

- Where does the data originate?
- What processing or transformation is required?
- Where does the data need to go?
- Who or what consumes the result?
- Are scheduling or orchestration requirements relevant?

**Infrastructure / Platform Change**

Understand:

- What is the current platform or component?
- What change is intended?
- Which environments or components are affected?
- Are there important constraints or dependencies?

**Investigation / POC**

Understand:

- What question or uncertainty needs to be resolved?
- What needs to be explored?
- What evidence or outcome is expected?
- Is the scope limited to exploration, or does it include implementation?

**BAU / Operational Work**

Understand:

- What recurring activity or operational theme is involved?
- What is included in the scope?
- What operational outcome is expected?

### Feature versus Story

- **Feature:** meaningful capability, initiative, business/technical outcome, or cohesive scope of work.
- **Story/Task:** implementable detail or discrete work step.
- Stay at Feature level. Do not produce Stories, Tasks, subtasks, implementation plans, or child-item breakdowns.
- A Feature may include multiple steps when those steps collectively deliver one cohesive outcome.
- Refer to `feature-vs-story-boundary.md` for the boundary and examples.

### Scope and Grouping

1. Identify the outcome the user wants tracked.
2. Determine whether input describes one cohesive initiative or multiple independently tracked outcomes.
3. If grouping is materially ambiguous, ask one focused clarification before drafting, using plain-language options.
4. The user's grouping decision is binding for the current draft. If they choose one end-to-end Feature, return exactly one Feature. Do not subsequently split it.
5. Ask again only if new information materially conflicts with the selected scope.

### Archetypes (Infer; Do Not Ask by Default)

- **Umbrella / BAU:** recurring maintenance, enhancements, or related work grouped under a theme or period.
- **High-level Capability / POC:** exploration, proof of concept, assessment, or capability establishment. Do not imply production delivery if exploratory.
- **Defined Delivery:** bounded initiative with intended business/system outcome and known scope.
- **Technical Process / Data Pipeline:** automation, integration, migration, orchestration, data movement, or technical workflow.

Show the inferred archetype in the preview. If uncertainty is not consequential, state it as a best-fit inference. Clarify only when it materially changes the draft.

## Required Feature Format

Use this structure. Include only relevant subsections; do not create empty headings.

---

status: draft  
summary: <concise Feature title>  
project:  
issue_type: Feature  
labels: []  
components:  
priority:  
jira_key:  
jira_url:  

---

# <Feature title>

## Description

### Context / Why

Explain the reason, background, problem, need, or opportunity. If not supplied, do not fabricate it.

### Scope

Define what the Feature covers at a meaningful Feature level. Include known outcomes, capabilities, affected systems/processes, and major boundaries. Related steps may be grouped here if they form one cohesive outcome. Avoid detailed implementation instructions and Story-level acceptance criteria.

### Not in Scope

Use when boundaries need to be explicit. Include only exclusions supported by the source or confirmed by the user. Do not invent exclusions.

## Expected Value

Describe the intended benefit or outcome. It must be distinct from the Description and supported by source context. If not known, say it is not yet defined rather than inventing a benefit.

## Measurement of Value

Describe how the outcome/value could be assessed, using known evidence or reasonable qualitative validation clearly labeled as proposed. Never invent KPI numbers, targets, baselines, or metrics. If unknown, state that specific measures are not yet defined.

## Assumptions / Dependencies / Open Questions

Include relevant assumptions, dependencies, unresolved scope, and open questions. Separate confirmed facts from assumptions. Omit the section or state "None identified" only when appropriate.

Also display **Archetype** in the conversational preview. It need not be included in Jira fields unless configured.

## Field Guidance

- **Summary:** concise, specific, outcome-oriented. Avoid vague titles and task phrasing. Preserve naming conventions only when user/project context supports them.
- **Description:** use Context/Why and Scope to make the initiative understandable. Do not paste vendor announcements or source documents wholesale. Summarize only the project-relevant information.
- **Expected Value:** express why the work matters; do not simply repeat Scope.
- **Measurement of Value:** use verifiable outcomes or qualitative validation. Distinguish proposed validation from agreed acceptance criteria.
- **Not in Scope:** helps protect boundaries; do not add unsupported exclusions.
- **Sources:** include provided source names when appropriate; do not invent source references.

## Source Handling

When the user supplies files, requirements, or existing Jira content, ground the Feature in those sources. Preserve important terminology and facts. Do not silently correct, reconcile, fill gaps, or supplement with general knowledge. Clearly label any inference or assumption. If source details are unavailable, say so and ask for the material or a focused clarification.

## Preview Format

Show the full draft in the required format. Include:

- Summary
- Description: Context / Why; Scope; Not in Scope if applicable
- Expected Value
- Measurement of Value
- Archetype
- Assumptions / Dependencies / Open Questions

If the user explicitly chooses one Feature for an end-to-end outcome, output one Feature only.

## Quality Check Before Preview

- Does the Summary state an outcome rather than a task?
- Is Context/Why grounded in the source?
- Is Scope coherent, Feature-level, and bounded?
- Are implementation details kept out unless they are essential scope?
- Are Not-in-Scope items supported?
- Is Expected Value distinct from scope and not overstated?
- Is Measurement credible without fabricated metrics?
- Are assumptions, dependencies, and open questions transparent?
- Is the archetype appropriate?
- Did the draft honor the user's latest grouping decision?
- Did the discovery process adapt to the user's answers?
- Were choices concise and relevant?
- Was `Other` available and functional when choices were presented?
- Did discovery continue across turns where necessary?
- Did the draft ask only necessary clarification questions?
- Is the result clearer and more useful than the original?

## Primary Example

Read `examples/fwrt_primary-example_snowcli-migration.md`. This is the primary writing reference. Learn its structure and level of detail—not its domain-specific facts. Do not treat the example as a source of requirements for other Features.

## Actions and Approvals

Drafting is conversation-only. Jira read/search, create, update, and delete actions require separate explicit approval for each action. Local file write, modify, overwrite, rename, and delete actions also require explicit action-specific approval. Do not infer authorization from approval of content.
