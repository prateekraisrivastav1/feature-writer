---
status: draft
summary: Migrate AURA processes from SnowSQL to SnowCLI
project:
issue_type: Feature
parent:
labels: [snowflake, aura, migration]
jira_key:
jira_url:
---

# Migrate AURA processes from SnowSQL to SnowCLI

## Description

### Context / Why

SnowSQL, Snowflake's legacy command-line client, is being retired, with end of support scheduled for April 16, 2028. SnowCLI is the supported replacement.

AURA processes currently using SnowSQL need to transition to SnowCLI to maintain compatibility with a supported Snowflake command-line tool.

### Scope

- Identify AURA applications, scripts, automation, users, and operational processes that currently use SnowSQL.
- Assess the existing SnowSQL usage, configurations, connections, and dependencies to determine migration requirements.
- Establish and validate SnowCLI in a non-production environment.
- Migrate applicable AURA processes, scripts, automation, connection configurations, and operational procedures to SnowCLI.
- Validate the migrated processes, including SQL execution, configuration handling, authentication, logging, error handling, and automation behavior as applicable.
- Update relevant documentation and operational procedures to reflect SnowCLI usage.
- Assess opportunities to consolidate Snowflake connection implementations where practical.

### Not in Scope

- Migration of applications, scripts, or processes outside the AURA scope unless explicitly agreed.
- Unrelated Snowflake enhancements or development work.
- Implementation of additional capabilities unrelated to replacing SnowSQL.

## Expected Value

Move AURA processes from SnowSQL to a supported Snowflake command-line tool, maintaining supportability and compatibility while simplifying Snowflake connectivity where practical.

## Measurement of Value

- Confirm that all identified in-scope AURA processes have migrated from SnowSQL to SnowCLI.
- Validate that migrated processes execute successfully using SnowCLI.
- Confirm that no in-scope process remains dependent on SnowSQL.

Specific connection-consolidation targets or other quantitative measures have not been defined.

## Assumptions / Dependencies

- SnowCLI is the approved replacement for SnowSQL for the in-scope AURA processes.
- The affected AURA processes and their dependencies will be identified during assessment.
- Required SnowCLI installation, configuration, connectivity, authentication, and access will be available for migration and validation.
- Migration must be completed ahead of the SnowSQL end-of-support date of April 16, 2028.
