# AgentInvestigate Shared Foundation Catalog

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_07_SHARED_FOUNDATIONS_READY
```

## Purpose

This catalog defines the shared professional foundations AgentInvestigate skills may reuse after AI-07. Foundations provide common vocabulary, schema contracts, and report-structure contracts so future skills do not re-invent core concepts or drift away from the repository's routing, evidence, source, and output standards.

## Boundary

AI-07 creates foundation contracts. It does not create production skill assets, filled templates, jurisdiction-specific rule sets, source maps, or operational procedures.

The roadmap rule applies:

```text
Do not create a shared asset unless a real skill consumes it.
```

To satisfy that rule before production skills exist, AI-07 records planned consumers in `docs/foundations/foundation-consumer-map.json`. Future waves must not materialize a reusable template file inside a skill package unless the consuming skill exists and names the foundation in its `Dependencies` or `References`.

## Foundation Files

| Foundation | File | Purpose |
|---|---|---|
| Professional and evidence vocabulary | `docs/foundations/professional-vocabulary.md` | Shared terms for professional boundaries, evidence, case status, confidence, and source reliability. |
| Shared schemas | `docs/foundations/shared-schemas.md` | Jurisdiction, authority, sensitivity, source, evidence, and artifact field contracts. |
| Report structure contracts | `docs/foundations/report-structure-contracts.md` | Common report and template structures as contracts, not filled template assets. |
| Consumer map | `docs/foundations/foundation-consumer-map.json` | Machine-readable map from foundations to canonical taxonomy skill consumers. |

## Foundation Categories

AI-07 covers the roadmap candidate resources:

- professional terminology;
- evidence terminology;
- case status vocabulary;
- confidence vocabulary;
- source reliability vocabulary;
- jurisdiction schema;
- authority schema;
- sensitivity schema;
- common report structures.

AI-07 also records template contracts for:

- case-intake;
- conflict-check;
- authority-check;
- investigation-plan;
- case-action-log;
- research-source-log;
- interview-plan;
- evidence-log;
- chain-of-custody;
- evidence-matrix;
- case-chronology;
- incident-report;
- shift-handoff;
- risk-register;
- case-closure.

## Consumer Rule

A future skill may consume a foundation when:

- the skill exists in `docs/architecture/taxonomy-index.yaml`;
- the foundation is relevant to the skill's atomic output;
- the skill names the foundation in `Dependencies` or `References`;
- any materialized template or fixture has at least one implemented skill consumer;
- the consuming skill still follows AI-03 through AI-06 standards.

## Validation

Run:

```powershell
.\scripts\validate-all.ps1
```

AI-07 validation checks required foundation files, roadmap candidate resources, template-contract names, consumer-map schema, and taxonomy-backed planned consumers.
