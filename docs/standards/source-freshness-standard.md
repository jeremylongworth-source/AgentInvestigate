# AgentInvestigate Source Freshness Standard

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_05_SOURCE_STANDARD_READY
```

## Purpose

Source freshness controls when AgentInvestigate skills must verify current material before using it. Freshness requirements protect users from stale legal, regulatory, privacy, licensing, employment, standards, safety, security, technical, and system claims.

## Freshness Classes

Use the taxonomy freshness field and skill source requirements to assign one of these classes:

| Class | Meaning | Default verification behavior |
|---|---|---|
| `LOW` | Durable method, historical record, stable internal artifact, or source unlikely to change the current output. | Verify when first added, when challenged, or during scheduled review. |
| `MEDIUM` | Professional guidance, standards context, organization policy, vendor documentation, or source that can change but is not usually time-critical. | Verify before publication, material reuse, or when older than the skill's review window. |
| `HIGH` | Law, regulation, regulator guidance, privacy authority material, employment screening rules, licensing rules, emergency/safety guidance, platform behavior, fees, forms, or source where stale content could materially mislead. | Verify at time of use or immediately before the regulated claim is relied on. |

Use the highest applicable freshness class. If uncertainty exists, upgrade freshness.

## High-Freshness Triggers

Mark source freshness as `HIGH` when the output depends on:

- legislation, regulations, court rules, or current cases;
- government regulator material;
- privacy authority guidance;
- licensing, registration, training, or qualification requirements;
- employment screening or workplace investigation obligations;
- consent, monitoring, recording, retention, disclosure, or personal-information handling;
- emergency, alarm, fire, life-safety, force, weapons, restraint, or security-response material;
- access-control, camera, alarm, electrical, structural, or other qualified technical systems;
- forms, fees, contact paths, filing processes, reporting channels, deadlines, or enforcement thresholds;
- vendor platform behavior, API behavior, system fields, data-retention settings, or product features;
- any source with known amendments, unclear effective date, or conflicting versions.

## Verification Windows

Freshness windows are maximums, not guarantees of currency:

| Class | Maximum reusable-source age before recheck |
|---|---:|
| `LOW` | 365 days |
| `MEDIUM` | 90 days |
| `HIGH` | 0 days for final or relied-upon regulated claims; verify during the task |

For `HIGH` sources, a prior source log can guide research, but the source must be rechecked before producing a source-backed regulated output.

## Freshness Metadata

Every source-dependent skill must define how it records:

- `accessed_date`;
- `last_verified`;
- source freshness class;
- effective date or version when available;
- supersession risk;
- reviewer or skill that last verified the source;
- stale-source behavior.

Regulated source metadata must follow `docs/standards/regulatory-source-standard.md`.

## Stale Source Behavior

When a required source is stale, unavailable, inaccessible, contradicted, or missing freshness metadata, the skill must choose one of these outcomes:

| Outcome | Use when |
|---|---|
| `verify_now` | The agent has permission and tool access to check the current source. |
| `ask_for_source` | The user can supply the current authoritative source. |
| `research_brief_only` | The output can safely identify issues and source needs without relying on stale material. |
| `qualified_review_required` | A responsible human must confirm currency and applicability before use. |
| `stop_or_redirect` | The request would be unsafe, prohibited, or misleading without current verification. |

Do not hide freshness failure behind generic caveats.

## Currentness In Outputs

Outputs using current sources must state:

- source checked;
- verification date;
- jurisdiction or source scope;
- what claim the source supports;
- whether the source is current enough for the requested output;
- remaining review need.

If current verification was not performed, label the output as a draft research brief, issue-spotting summary, or preparation checklist.

## Local Reference Review

Local reference files that contain source-backed regulated content must include:

- source metadata;
- freshness class;
- last verified date;
- supersession risk;
- owner or reviewing skill;
- next review trigger.

Local references may contain durable methods without current verification only when they do not encode current legal, regulatory, privacy, licensing, employment, safety, emergency, vendor, or system claims.

## Skill Authoring Requirements

Each skill's `Source Requirements` section must state:

- freshness class;
- what claims require current verification;
- whether browsing, supplied sources, local references, or qualified review are required;
- stale-source stop condition;
- output label when verification is incomplete;
- test cases for stale, missing, and wrong-jurisdiction sources.

## Gate

Future source-backed regulated skills can update their source logs, citations, and reference material without changing repository architecture when they preserve this freshness contract.

## Validation Notes

AI-05 defines source freshness policy only. AI-06 must add executable tests for stale sources, wrong jurisdiction, unsupported inference, and output-format compliance.
