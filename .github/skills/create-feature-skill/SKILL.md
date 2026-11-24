---
name: create-feature-skill
description: Conversational discovery, instructions, format, quality criteria, archetypes, and a primary example for drafting clear Jira Features from rough or incomplete inputs.
---

# Create Feature Skill

## Objective

Create clear, concise, outcome-oriented Jira Features from rough requests, technical notes, requirements, existing Features, or source documents. Improve Feature quality—not merely copy the source's wording or weaknesses.

## Conversational Discovery

### Opening

Invite the user to provide a **brief or detailed description** in their own words. They may provide business context, technical notes, requirements, documents, or an existing Feature. Avoid forcing a template or asking them to select a work type upfront.

Example:

> Describe the Feature you want to create. A brief description is fine, or you can share detailed requirements, technical notes, or supporting documents.

### Classify the Work from the User's Input

Infer the likely work type to guide relevant clarification. This classification is for the Copilot's reasoning—not a required user selection and not necessarily the Feature archetype.

Common work types and useful follow-up dimensions:

| Work type | Clarify only if material and missing |
|---|---|
| Migration | Source, target, what is being migrated, migration boundary (all vs selected), coexistence/cutover constraints |
| New capability | Capability needed, intended users/consumers, desired outcome |
| Enhancement | Existing capability/process, desired change, reason or pain point |
| Automation | Current manual/automated process, what should be automated, trigger, desired result |
| Integration | Systems involved, direction/flow, expected interaction or outcome |
| Data pipeline / processing | Source data, processing/transformation, destination/consumer, outcome or schedule if relevant |
| Infrastructure / platform change | Current environment/component, desired change, affected scope, constraints |
| Investigation / POC | Question or uncertainty to resolve, what will be explored, evidence/outcome needed, whether implementation is included |
| BAU / operational work | Recurring activity or theme, scope, intended operational result |

Do not mechanically ask every question in a row. Use what the user already provided and ask only the most important missing detail.

### Mandatory Multi-Turn Discovery Loop

**Discovery is a continuing conversation, not a single clarification step. Do not stop after asking one question.**

After the user's initial description:

1. Understand the request and identify the likely work type.
2. Extract all information already provided.
3. Identify the material information still missing.
4. Select the single most important unanswered question.
5. Ask that question in natural language and wait for the user's response.
6. Incorporate the answer into the working understanding of the Feature.
7. Reassess the remaining gaps and determine the next most useful question.
8. Repeat this process until enough information is available to draft a clear and correctly scoped Feature.

After every user response, reassess the information. Do not simply move through a predefined list of questions.

Maintain the following discovery state internally throughout the conversation:

- **Confirmed information:** Facts and decisions explicitly supplied by the user or supported by provided sources.
- **Information still needed:** Missing details that could materially affect the Feature.
- **Scope decisions:** The user's decisions about what is included, excluded, or grouped together.
- **Assumptions:** Reasonable but unconfirmed details that must be disclosed.
- **Open questions:** Details that remain unresolved and should be recorded in the draft.

Do not ask the user to repeat information already supplied.

**Continue asking questions when:**
- The answer reveals another important gap.
- The scope is still unclear.
- The source and target of a migration are not established.
- The intended outcome is not understood.
- The answer introduces additional systems, processes, or scope that need clarification.
- The user's response creates ambiguity about grouping or delivery expectations.

**Stop asking questions when:**
- The intended outcome is sufficiently clear.
- The main scope and boundaries are understood.
- Material grouping decisions have been resolved.
- Remaining unknowns can be transparently documented as assumptions or open questions.
- Further clarification would not materially improve the draft.

Do not ask questions merely to complete a checklist. The goal is sufficient understanding, not collecting every possible detail.

When discovery is complete, briefly summarize the understanding and proceed to the Feature draft. Do not require an additional confirmation if the user has already provided enough information and has not requested one.

### Clarification Rules

- Ask **one focused question per turn**.
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

Example conversation:

User:
"We need to migrate from SnowSQL to SnowCLI."

Feature Writer:
"Which SnowSQL usage are we migrating—scripts, scheduled jobs, applications, automation, or all existing usage?"

User:
"All AURA scripts and scheduled jobs."

Feature Writer:
"Is SnowCLI already configured in the target environment, or should setting it up be included in this migration?"

User:
"We need to configure it first."

Feature Writer:
"Which environments should this migration cover?"

The Feature Writer should continue based on each answer, asking the next relevant question until the migration scope is sufficiently understood.

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
- Refer to `./feature-vs-story-boundary.md` for the boundary and examples.

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

The Jira Summary is the Feature title and is separate from the description sections.

The Feature description must contain **exactly these three sections**, in this order:

### Description
A concise, clear overview of the Feature. Keep it at the level appropriate to the user's requested scope. For an Umbrella/high-level Feature, describe the overall outcome and coordinated scope without expanding into detailed activities, implementation plans, or task lists.

### Expected Value
State the intended value or benefit. Keep it distinct from the Description and grounded in what the user or source supports. If benefits are not specified, phrase only the defensible intended value without inventing business benefits.

### Measurement of Value
Describe how the value or outcome can be assessed. Use verifiable or qualitative measures when supported. Do not invent KPIs, baselines, targets, or numbers. If specific measures are not defined, say so concisely within this section.

**Do not add any other sections to the Feature draft or Jira description.** In particular, do not output Context / Why, Scope, Not in Scope, Assumptions, Dependencies, Open Questions, Archetype, Discovery notes, or additional headings, appendices, or sections.

These items may be considered internally during discovery and drafting. They must not appear in the final Feature output. Unanswered questions are not a reason to block a high-level draft or Jira creation; when the user requests a high-level/umbrella Feature, keep it high-level and omit unresolved details rather than listing them.

## Field Guidance

- **Summary:** concise, specific, outcome-oriented. Avoid vague titles and task phrasing. Preserve naming conventions only when user/project context supports them.
- **Description:** provide a concise overview of intended outcome and scope. Do not add separate Context/Why or Scope subsections. Avoid detailed implementation instructions and Story-level acceptance criteria.
- **Expected Value:** express why the work matters; do not simply repeat Description. Do not overstate or invent benefits.
- **Measurement of Value:** use verifiable outcomes or qualitative validation. Distinguish proposed validation from agreed measures. Never fabricate metrics.
- **Sources:** ground the draft in provided sources; include source references only when appropriate and do not invent references.

## Source Handling

When the user supplies files, requirements, or existing Jira content, ground the Feature in those sources. Preserve important terminology and facts. Do not silently correct, reconcile, fill gaps, or supplement with general knowledge. Clearly label inference internally. If source details are unavailable, ask a focused clarification conversationally; do not add a separate Open Questions section to the Feature.

## Preview Format

Show the complete draft with only:
- **Summary** (Jira title field)
- **Description**
- **Expected Value**
- **Measurement of Value**

Do not display archetype, assumptions, dependencies, open questions, discovery notes, or any other sections in the final Feature preview. Keep those internal. If the user explicitly chooses one Feature for an end-to-end outcome, output exactly one Feature.

## Quality Check Before Preview

- Does the Summary state an outcome rather than a task?
- Is the Description concise, clear, grounded, and appropriately high-level?
- Is Expected Value distinct from Description and not overstated?
- Is Measurement credible without fabricated metrics?
- Did the draft honor the user's latest grouping decision?
- Did discovery adapt to the user's answers?
- Were choices concise and relevant?
- Was `Other` available and functional when choices were presented?
- Did discovery continue across turns where necessary?
- Did the draft ask only necessary clarification questions?
- **Does the final Feature contain exactly the three required sections and no additional headings or notes?**
- Are the three sections mapped to separate Jira fields rather than combined into Description?
- Does explicit user approval trigger creation without another conversational permission prompt?
- Is the result clearer and more useful than the original?

## Primary Example

Read `examples/fwrt_primary-example_snowcli-migration.md`. This is the primary writing reference. Learn its structure and level of detail—not its domain-specific facts. Do not treat the example as a source of requirements for other Features.

## Jira Field Mapping and Creation

The three Feature sections are separate Jira fields, not headings embedded inside the Description:

- **Description** → Jira Description field only.
- **Expected Value** → its dedicated Jira field.
- **Measurement of Value** → its dedicated Jira field.

Use the project's configured field mapping/custom field IDs. Never place Expected Value or Measurement of Value inside Description as a workaround. If the dedicated fields cannot be identified or are unavailable, do not create a ticket with the content incorrectly combined; briefly report the mapping limitation.

## Approval and Execution

- Present the draft preview first.
- When the user explicitly approves the draft (e.g., "approved", "create it", "go ahead"), that approval authorizes the Jira creation workflow for this reviewed Feature.
- Immediately start the Jira create workflow. Do not ask for a second conversational confirmation, repeat the approval request, or discuss technical/tool permission prompts.
- Do not bypass platform, runtime, or security permission controls. If execution is blocked by the environment, report the blocker briefly and plainly, without launching technical troubleshooting or back-and-forth.
- Do not make unrelated Jira changes.
- Local file write, modify, overwrite, rename, and delete actions still require their own explicit, action-specific approval.

