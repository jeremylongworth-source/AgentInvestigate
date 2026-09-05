# Evidence And Records

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_27_CANADA_FEDERAL_READY
```

## Scope

This reference covers Canada Evidence Act and evidence-related federal concepts issue spotting for AgentInvestigate. It supports evidence handling, source logging, continuity questions, electronic-record questions, and report limitations. It does not determine admissibility or provide legal conclusions.

## Source Basis

Use `source-log.yaml` entry:

- `canada-federal-evidence-act`

Freshness: `HIGH`. Recheck current official sources and route to counsel before relying on evidence-law claims.

## Federal Evidence Concepts To Flag

When a skill touches evidence or records in a Canadian federal context, preserve:

- source identity and provenance;
- original versus copy status;
- timestamps and time zone;
- collection authority and privacy basis;
- chain of custody or continuity;
- transfer history;
- integrity, completeness, and alteration questions;
- electronic document or system-record context;
- hearsay, privilege, confidentiality, or compelled-production questions when raised by supplied facts;
- limitations and unresolved questions.

## AgentInvestigate Boundaries

The module may support:

- evidence issue spotting;
- source logs;
- chain-of-custody gap lists;
- records request questions;
- electronic-record integrity questions;
- counsel-review packets.

The module must not support:

- evidence admissibility conclusions;
- advice to alter, hide, destroy, backdate, sanitize, or fabricate records;
- advice to obtain private records without authority;
- compelled-production instructions;
- privilege determinations;
- court strategy;
- legal opinions.

## Required Output Boundary

Any output relying on this reference must state:

- the source and verification date;
- the evidence or record type;
- whether the record is original, copy, extract, screenshot, export, summary, or unknown;
- collection and handling gaps;
- continuity and integrity concerns;
- what requires counsel, court, tribunal, regulator, privacy, or qualified-review input;
- that federal evidence concepts do not decide whether investigative or security work was authorized.
