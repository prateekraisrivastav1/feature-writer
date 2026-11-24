# Feature vs Story Boundary

## Feature
A Feature is the high-level description of the capability, outcome, or work grouping. It explains **what** and **why**, at an appropriate level.

## Story
A Story is a detailed, implementable piece of work. It describes a specific unit of delivery and normally contains implementation detail and acceptance criteria according to the story writer.

## Practical test
Ask: “Does this describe the overall capability/outcome, or a discrete piece of work someone can implement?”

- Overall capability/outcome → likely Feature.
- Specific implementation task or bounded work item → likely Story.

## Example
Feature-level concept: A data process that makes Producer Contract data available through the history and downstream processing flow.

Potential Story-level work areas:
- Create the JS7 job.
- Load data into the staging/history table.
- Populate downstream data from the history table.

Do not expand these into detailed Story content while creating the Feature.

## Lifecycle
1. Create the Feature.
2. Create Stories.
3. Link the Stories to the Feature.
4. Retrieve linked child items dynamically when reporting progress or counts.

The initial Feature Writer scope ends after Feature creation and verification. Story creation and linking are future workflows.
