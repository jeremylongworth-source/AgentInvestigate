# AgentInvestigate Master Taxonomy v1.0

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_02_MASTER_TAXONOMY_READY
```

## Canonical Source

`docs/architecture/taxonomy-index.yaml` is the canonical taxonomy source.
This markdown file is a human-readable projection of that index.

AI-02 found no standalone approved 212-skill taxonomy file outside the roadmap.
The canonical in-repository taxonomy is therefore reconstructed from `ROADMAP.md`, the explicitly named roadmap skills, the AI-01 domain contract, and the roadmap's stated 212-skill count.

This is a planning and routing contract. It does not mean any skill has been implemented.

## Required Fields

Every taxonomy entry in the canonical index includes:

- `name`
- `family`
- `tier`
- `sensitivity`
- `jurisdiction_requirement`
- `authority_requirement`
- `freshness_requirement`
- `priority`
- `dependencies`
- `professional_skillsets`

## Summary

- Skills: `212`
- Families: `20`
- Sensitivity counts: `{'CERTIFICATION_BOUNDARY': 10, 'INTRUSIVE': 27, 'REGULATED': 44, 'ROUTINE': 131}`
- Priority counts: `{'P0': 31, 'P1': 112, 'P2': 69}`
- Tier counts: `{'ADVANCED': 69, 'CORE': 112, 'FOUNDATION': 31}`

## Family Counts

| Family | Branch | Skills |
|---|---|---:|
| `01-professional-core-ethics` | Shared | 9 |
| `02-case-intake-scope-authority` | Shared | 11 |
| `03-law-licensing-privacy-compliance` | Shared | 11 |
| `04-investigation-planning-case-management` | Private Investigation | 13 |
| `05-research-osint-public-records` | Private Investigation | 14 |
| `06-identity-entity-timeline-analysis` | Private Investigation | 10 |
| `07-interviewing-witnesses-statements` | Private Investigation | 10 |
| `08-evidence-chain-of-custody` | Shared | 12 |
| `09-investigative-analysis` | Private Investigation | 11 |
| `10-observation-surveillance-governance` | Private Investigation | 8 |
| `11-reporting-findings-case-presentation` | Shared | 10 |
| `12-corporate-workplace-investigations` | Private Investigation | 10 |
| `13-background-screening-due-diligence` | Private Investigation | 10 |
| `14-security-operations-access-patrol` | Private Security | 15 |
| `15-incident-response` | Private Security | 9 |
| `16-communication-deescalation` | Private Security | 8 |
| `17-physical-security-risk-assessment` | Private Security | 11 |
| `18-security-systems-technology` | Private Security | 9 |
| `19-loss-prevention-asset-protection` | Hybrid | 8 |
| `20-investigation-security-program-management` | Shared | 13 |

## Skill Registry

| Skill | Family | Tier | Sensitivity | Priority |
|---|---|---|---|---|
| `define-professional-role-boundaries` | `01-professional-core-ethics` | FOUNDATION | ROUTINE | P0 |
| `assess-conflict-of-interest` | `01-professional-core-ethics` | FOUNDATION | ROUTINE | P0 |
| `apply-ethical-decision-framework` | `01-professional-core-ethics` | FOUNDATION | ROUTINE | P0 |
| `identify-investigative-bias` | `01-professional-core-ethics` | FOUNDATION | ROUTINE | P0 |
| `separate-fact-from-inference` | `01-professional-core-ethics` | FOUNDATION | ROUTINE | P0 |
| `assess-duty-of-care` | `01-professional-core-ethics` | FOUNDATION | ROUTINE | P0 |
| `protect-confidential-information` | `01-professional-core-ethics` | FOUNDATION | ROUTINE | P0 |
| `identify-escalation-requirement` | `01-professional-core-ethics` | FOUNDATION | ROUTINE | P0 |
| `document-professional-decision` | `01-professional-core-ethics` | FOUNDATION | ROUTINE | P0 |
| `classify-request-type` | `02-case-intake-scope-authority` | FOUNDATION | ROUTINE | P0 |
| `identify-client-role` | `02-case-intake-scope-authority` | FOUNDATION | ROUTINE | P0 |
| `identify-jurisdiction` | `02-case-intake-scope-authority` | FOUNDATION | REGULATED | P0 |
| `validate-investigative-authority` | `02-case-intake-scope-authority` | FOUNDATION | REGULATED | P0 |
| `validate-security-service-authority` | `02-case-intake-scope-authority` | FOUNDATION | REGULATED | P0 |
| `assess-lawful-purpose` | `02-case-intake-scope-authority` | FOUNDATION | REGULATED | P0 |
| `define-case-scope` | `02-case-intake-scope-authority` | FOUNDATION | ROUTINE | P0 |
| `define-scope-boundaries` | `02-case-intake-scope-authority` | FOUNDATION | ROUTINE | P0 |
| `identify-stakeholders-and-subjects` | `02-case-intake-scope-authority` | FOUNDATION | ROUTINE | P0 |
| `assess-consent-requirement` | `02-case-intake-scope-authority` | FOUNDATION | REGULATED | P0 |
| `prepare-authority-check` | `02-case-intake-scope-authority` | FOUNDATION | REGULATED | P0 |
| `identify-licensing-requirement` | `03-law-licensing-privacy-compliance` | FOUNDATION | REGULATED | P0 |
| `identify-regulated-activity` | `03-law-licensing-privacy-compliance` | FOUNDATION | REGULATED | P0 |
| `identify-privacy-obligation` | `03-law-licensing-privacy-compliance` | FOUNDATION | REGULATED | P0 |
| `identify-recording-law-issue` | `03-law-licensing-privacy-compliance` | FOUNDATION | REGULATED | P0 |
| `assess-information-collection-basis` | `03-law-licensing-privacy-compliance` | FOUNDATION | REGULATED | P0 |
| `assess-record-access-authority` | `03-law-licensing-privacy-compliance` | FOUNDATION | REGULATED | P0 |
| `assess-data-minimization-requirement` | `03-law-licensing-privacy-compliance` | FOUNDATION | REGULATED | P0 |
| `review-retention-obligation` | `03-law-licensing-privacy-compliance` | FOUNDATION | REGULATED | P0 |
| `identify-reporting-obligation` | `03-law-licensing-privacy-compliance` | FOUNDATION | REGULATED | P0 |
| `review-training-requirements` | `03-law-licensing-privacy-compliance` | FOUNDATION | REGULATED | P0 |
| `prepare-compliance-escalation` | `03-law-licensing-privacy-compliance` | FOUNDATION | REGULATED | P0 |
| `build-investigation-plan` | `04-investigation-planning-case-management` | CORE | ROUTINE | P1 |
| `define-investigative-question` | `04-investigation-planning-case-management` | CORE | ROUTINE | P1 |
| `create-case-timeline` | `04-investigation-planning-case-management` | CORE | ROUTINE | P1 |
| `prioritize-investigative-leads` | `04-investigation-planning-case-management` | CORE | ROUTINE | P1 |
| `estimate-investigative-resources` | `04-investigation-planning-case-management` | CORE | ROUTINE | P1 |
| `define-case-milestones` | `04-investigation-planning-case-management` | CORE | ROUTINE | P1 |
| `maintain-case-action-log` | `04-investigation-planning-case-management` | CORE | ROUTINE | P1 |
| `write-case-notes` | `04-investigation-planning-case-management` | CORE | ROUTINE | P1 |
| `prepare-case-status-update` | `04-investigation-planning-case-management` | CORE | ROUTINE | P1 |
| `review-case-retention-needs` | `04-investigation-planning-case-management` | CORE | ROUTINE | P1 |
| `conduct-case-file-review` | `04-investigation-planning-case-management` | CORE | ROUTINE | P1 |
| `identify-case-gaps` | `04-investigation-planning-case-management` | CORE | ROUTINE | P1 |
| `prepare-case-closure-summary` | `04-investigation-planning-case-management` | CORE | ROUTINE | P1 |
| `build-research-plan` | `05-research-osint-public-records` | CORE | ROUTINE | P1 |
| `identify-public-record-sources` | `05-research-osint-public-records` | CORE | REGULATED | P1 |
| `plan-open-source-research` | `05-research-osint-public-records` | CORE | ROUTINE | P1 |
| `research-corporate-records` | `05-research-osint-public-records` | CORE | REGULATED | P1 |
| `research-court-records` | `05-research-osint-public-records` | CORE | REGULATED | P1 |
| `research-regulatory-records` | `05-research-osint-public-records` | CORE | REGULATED | P1 |
| `assess-source-reliability` | `05-research-osint-public-records` | CORE | ROUTINE | P1 |
| `record-source-provenance` | `05-research-osint-public-records` | CORE | ROUTINE | P1 |
| `corroborate-open-source-information` | `05-research-osint-public-records` | CORE | ROUTINE | P1 |
| `resolve-source-conflict` | `05-research-osint-public-records` | CORE | ROUTINE | P1 |
| `research-organization-profile` | `05-research-osint-public-records` | CORE | ROUTINE | P1 |
| `research-property-context` | `05-research-osint-public-records` | CORE | REGULATED | P1 |
| `research-litigation-history` | `05-research-osint-public-records` | CORE | REGULATED | P1 |
| `write-research-summary` | `05-research-osint-public-records` | CORE | ROUTINE | P1 |
| `assess-identity-ambiguity` | `06-identity-entity-timeline-analysis` | CORE | INTRUSIVE | P1 |
| `differentiate-same-name-individuals` | `06-identity-entity-timeline-analysis` | CORE | INTRUSIVE | P1 |
| `normalize-person-identifiers` | `06-identity-entity-timeline-analysis` | CORE | INTRUSIVE | P1 |
| `normalize-organization-identifiers` | `06-identity-entity-timeline-analysis` | CORE | ROUTINE | P1 |
| `construct-subject-timeline` | `06-identity-entity-timeline-analysis` | CORE | INTRUSIVE | P1 |
| `map-relationship-evidence` | `06-identity-entity-timeline-analysis` | CORE | INTRUSIVE | P1 |
| `assess-association-strength` | `06-identity-entity-timeline-analysis` | CORE | INTRUSIVE | P1 |
| `identify-timeline-gap` | `06-identity-entity-timeline-analysis` | CORE | ROUTINE | P1 |
| `resolve-entity-contradiction` | `06-identity-entity-timeline-analysis` | CORE | INTRUSIVE | P1 |
| `state-identity-confidence` | `06-identity-entity-timeline-analysis` | CORE | ROUTINE | P1 |
| `define-interview-objectives` | `07-interviewing-witnesses-statements` | CORE | ROUTINE | P1 |
| `prepare-neutral-question-set` | `07-interviewing-witnesses-statements` | CORE | ROUTINE | P1 |
| `sequence-interview-topics` | `07-interviewing-witnesses-statements` | CORE | ROUTINE | P1 |
| `identify-interview-information-gaps` | `07-interviewing-witnesses-statements` | CORE | ROUTINE | P1 |
| `prepare-witness-interview-plan` | `07-interviewing-witnesses-statements` | CORE | ROUTINE | P1 |
| `summarize-witness-statement` | `07-interviewing-witnesses-statements` | CORE | ROUTINE | P1 |
| `compare-statement-consistency` | `07-interviewing-witnesses-statements` | CORE | ROUTINE | P1 |
| `identify-corroboration-needs` | `07-interviewing-witnesses-statements` | CORE | ROUTINE | P1 |
| `prepare-follow-up-questions` | `07-interviewing-witnesses-statements` | CORE | ROUTINE | P1 |
| `review-interview-bias-risk` | `07-interviewing-witnesses-statements` | CORE | ROUTINE | P1 |
| `create-evidence-log` | `08-evidence-chain-of-custody` | CORE | ROUTINE | P1 |
| `classify-evidence-type` | `08-evidence-chain-of-custody` | CORE | ROUTINE | P1 |
| `record-evidence-source` | `08-evidence-chain-of-custody` | CORE | ROUTINE | P1 |
| `assess-evidence-relevance` | `08-evidence-chain-of-custody` | CORE | ROUTINE | P1 |
| `build-chain-of-custody-summary` | `08-evidence-chain-of-custody` | CORE | ROUTINE | P1 |
| `identify-chain-of-custody-gap` | `08-evidence-chain-of-custody` | CORE | ROUTINE | P1 |
| `track-evidence-transfer` | `08-evidence-chain-of-custody` | CORE | ROUTINE | P1 |
| `compare-original-and-copy` | `08-evidence-chain-of-custody` | CORE | ROUTINE | P1 |
| `verify-evidence-timestamp` | `08-evidence-chain-of-custody` | CORE | ROUTINE | P1 |
| `map-evidence-to-allegation` | `08-evidence-chain-of-custody` | CORE | ROUTINE | P1 |
| `identify-evidence-continuity-issue` | `08-evidence-chain-of-custody` | CORE | ROUTINE | P1 |
| `prepare-evidence-handling-escalation` | `08-evidence-chain-of-custody` | CORE | REGULATED | P1 |
| `build-evidence-matrix` | `09-investigative-analysis` | CORE | ROUTINE | P1 |
| `generate-investigative-hypotheses` | `09-investigative-analysis` | CORE | ROUTINE | P1 |
| `test-investigative-hypothesis` | `09-investigative-analysis` | CORE | ROUTINE | P1 |
| `compare-alternative-explanations` | `09-investigative-analysis` | CORE | ROUTINE | P1 |
| `identify-evidence-contradiction` | `09-investigative-analysis` | CORE | ROUTINE | P1 |
| `construct-event-chronology` | `09-investigative-analysis` | CORE | ROUTINE | P1 |
| `analyze-pattern-of-events` | `09-investigative-analysis` | CORE | ROUTINE | P1 |
| `assess-source-weight` | `09-investigative-analysis` | CORE | ROUTINE | P1 |
| `assess-finding-confidence` | `09-investigative-analysis` | CORE | ROUTINE | P1 |
| `identify-unresolved-question` | `09-investigative-analysis` | CORE | ROUTINE | P1 |
| `draft-investigative-finding` | `09-investigative-analysis` | CORE | ROUTINE | P1 |
| `assess-observation-authorization` | `10-observation-surveillance-governance` | ADVANCED | INTRUSIVE | P2 |
| `assess-observation-necessity` | `10-observation-surveillance-governance` | ADVANCED | INTRUSIVE | P2 |
| `assess-observation-proportionality` | `10-observation-surveillance-governance` | ADVANCED | INTRUSIVE | P2 |
| `define-observation-purpose` | `10-observation-surveillance-governance` | ADVANCED | INTRUSIVE | P2 |
| `plan-lawful-observation-assignment` | `10-observation-surveillance-governance` | ADVANCED | INTRUSIVE | P2 |
| `record-field-observation` | `10-observation-surveillance-governance` | ADVANCED | INTRUSIVE | P2 |
| `minimize-third-party-information` | `10-observation-surveillance-governance` | ADVANCED | INTRUSIVE | P2 |
| `review-observation-record-for-compliance` | `10-observation-surveillance-governance` | ADVANCED | INTRUSIVE | P2 |
| `write-investigative-report` | `11-reporting-findings-case-presentation` | CORE | ROUTINE | P1 |
| `write-incident-report` | `11-reporting-findings-case-presentation` | CORE | ROUTINE | P1 |
| `prepare-case-chronology` | `11-reporting-findings-case-presentation` | CORE | ROUTINE | P1 |
| `summarize-evidence` | `11-reporting-findings-case-presentation` | CORE | ROUTINE | P1 |
| `prepare-findings-matrix` | `11-reporting-findings-case-presentation` | CORE | ROUTINE | P1 |
| `write-executive-summary` | `11-reporting-findings-case-presentation` | CORE | ROUTINE | P1 |
| `review-report-quality` | `11-reporting-findings-case-presentation` | CORE | ROUTINE | P1 |
| `prepare-case-presentation` | `11-reporting-findings-case-presentation` | CORE | ROUTINE | P1 |
| `prepare-testimony-support-outline` | `11-reporting-findings-case-presentation` | CORE | REGULATED | P1 |
| `identify-report-limitations` | `11-reporting-findings-case-presentation` | CORE | ROUTINE | P1 |
| `classify-workplace-allegation` | `12-corporate-workplace-investigations` | ADVANCED | REGULATED | P2 |
| `map-allegation-to-policy` | `12-corporate-workplace-investigations` | ADVANCED | ROUTINE | P2 |
| `build-allegations-matrix` | `12-corporate-workplace-investigations` | ADVANCED | ROUTINE | P2 |
| `plan-workplace-investigation` | `12-corporate-workplace-investigations` | ADVANCED | REGULATED | P2 |
| `identify-workplace-evidence-sources` | `12-corporate-workplace-investigations` | ADVANCED | INTRUSIVE | P2 |
| `prepare-workplace-interview-plan` | `12-corporate-workplace-investigations` | ADVANCED | ROUTINE | P2 |
| `compare-workplace-statements` | `12-corporate-workplace-investigations` | ADVANCED | ROUTINE | P2 |
| `assess-evidentiary-support` | `12-corporate-workplace-investigations` | ADVANCED | ROUTINE | P2 |
| `draft-workplace-finding` | `12-corporate-workplace-investigations` | ADVANCED | ROUTINE | P2 |
| `prepare-workplace-investigation-report` | `12-corporate-workplace-investigations` | ADVANCED | ROUTINE | P2 |
| `define-screening-purpose` | `13-background-screening-due-diligence` | ADVANCED | INTRUSIVE | P2 |
| `assess-background-screening-authority` | `13-background-screening-due-diligence` | ADVANCED | INTRUSIVE | P2 |
| `verify-screening-consent` | `13-background-screening-due-diligence` | ADVANCED | INTRUSIVE | P2 |
| `select-screening-source-type` | `13-background-screening-due-diligence` | ADVANCED | INTRUSIVE | P2 |
| `assess-screening-source-reliability` | `13-background-screening-due-diligence` | ADVANCED | INTRUSIVE | P2 |
| `evaluate-record-relevance` | `13-background-screening-due-diligence` | ADVANCED | INTRUSIVE | P2 |
| `identify-screening-identity-ambiguity` | `13-background-screening-due-diligence` | ADVANCED | INTRUSIVE | P2 |
| `resolve-screening-discrepancy` | `13-background-screening-due-diligence` | ADVANCED | INTRUSIVE | P2 |
| `prepare-due-diligence-summary` | `13-background-screening-due-diligence` | ADVANCED | INTRUSIVE | P2 |
| `identify-adverse-information-review-need` | `13-background-screening-due-diligence` | ADVANCED | INTRUSIVE | P2 |
| `review-post-orders` | `14-security-operations-access-patrol` | CORE | REGULATED | P1 |
| `build-shift-plan` | `14-security-operations-access-patrol` | CORE | ROUTINE | P1 |
| `plan-patrol-route` | `14-security-operations-access-patrol` | CORE | ROUTINE | P1 |
| `document-patrol-observation` | `14-security-operations-access-patrol` | CORE | ROUTINE | P1 |
| `log-security-occurrence` | `14-security-operations-access-patrol` | CORE | ROUTINE | P1 |
| `verify-access-event` | `14-security-operations-access-patrol` | CORE | ROUTINE | P1 |
| `triage-access-control-event` | `14-security-operations-access-patrol` | CORE | ROUTINE | P1 |
| `document-visitor-management-issue` | `14-security-operations-access-patrol` | CORE | ROUTINE | P1 |
| `record-key-control-event` | `14-security-operations-access-patrol` | CORE | REGULATED | P1 |
| `document-alarm-response` | `14-security-operations-access-patrol` | CORE | CERTIFICATION_BOUNDARY | P1 |
| `prepare-shift-handoff` | `14-security-operations-access-patrol` | CORE | ROUTINE | P1 |
| `review-security-log` | `14-security-operations-access-patrol` | CORE | ROUTINE | P1 |
| `identify-post-order-gap` | `14-security-operations-access-patrol` | CORE | ROUTINE | P1 |
| `prepare-security-operations-brief` | `14-security-operations-access-patrol` | CORE | ROUTINE | P1 |
| `identify-supervisor-notification-need` | `14-security-operations-access-patrol` | CORE | ROUTINE | P1 |
| `triage-security-incident` | `15-incident-response` | CORE | CERTIFICATION_BOUNDARY | P1 |
| `determine-emergency-escalation` | `15-incident-response` | CORE | CERTIFICATION_BOUNDARY | P1 |
| `support-emergency-service-access` | `15-incident-response` | CORE | CERTIFICATION_BOUNDARY | P1 |
| `preserve-incident-scene` | `15-incident-response` | CORE | CERTIFICATION_BOUNDARY | P1 |
| `identify-incident-notification-requirement` | `15-incident-response` | CORE | REGULATED | P1 |
| `document-incident-timeline` | `15-incident-response` | CORE | ROUTINE | P1 |
| `collect-incident-account` | `15-incident-response` | CORE | ROUTINE | P1 |
| `prepare-post-incident-review` | `15-incident-response` | CORE | ROUTINE | P1 |
| `identify-corrective-action` | `15-incident-response` | CORE | ROUTINE | P1 |
| `assess-conflict-risk` | `16-communication-deescalation` | CORE | CERTIFICATION_BOUNDARY | P1 |
| `prepare-deescalation-communication-plan` | `16-communication-deescalation` | CORE | CERTIFICATION_BOUNDARY | P1 |
| `draft-radio-communication` | `16-communication-deescalation` | CORE | ROUTINE | P1 |
| `prepare-incident-notification` | `16-communication-deescalation` | CORE | ROUTINE | P1 |
| `adapt-message-to-audience` | `16-communication-deescalation` | CORE | ROUTINE | P1 |
| `review-communication-bias` | `16-communication-deescalation` | CORE | ROUTINE | P1 |
| `document-deescalation-attempt` | `16-communication-deescalation` | CORE | ROUTINE | P1 |
| `identify-communication-escalation-need` | `16-communication-deescalation` | CORE | CERTIFICATION_BOUNDARY | P1 |
| `define-protected-assets` | `17-physical-security-risk-assessment` | ADVANCED | ROUTINE | P2 |
| `identify-security-threats` | `17-physical-security-risk-assessment` | ADVANCED | ROUTINE | P2 |
| `assess-physical-vulnerabilities` | `17-physical-security-risk-assessment` | ADVANCED | ROUTINE | P2 |
| `assess-security-consequences` | `17-physical-security-risk-assessment` | ADVANCED | ROUTINE | P2 |
| `assess-risk-likelihood` | `17-physical-security-risk-assessment` | ADVANCED | ROUTINE | P2 |
| `build-security-risk-register` | `17-physical-security-risk-assessment` | ADVANCED | ROUTINE | P2 |
| `map-existing-controls` | `17-physical-security-risk-assessment` | ADVANCED | ROUTINE | P2 |
| `identify-control-gaps` | `17-physical-security-risk-assessment` | ADVANCED | ROUTINE | P2 |
| `compare-security-improvement-options` | `17-physical-security-risk-assessment` | ADVANCED | ROUTINE | P2 |
| `prioritize-security-improvements` | `17-physical-security-risk-assessment` | ADVANCED | ROUTINE | P2 |
| `prepare-physical-security-assessment-summary` | `17-physical-security-risk-assessment` | ADVANCED | REGULATED | P2 |
| `define-access-control-requirements` | `18-security-systems-technology` | ADVANCED | REGULATED | P2 |
| `analyze-access-control-event` | `18-security-systems-technology` | ADVANCED | ROUTINE | P2 |
| `define-video-surveillance-requirements` | `18-security-systems-technology` | ADVANCED | REGULATED | P2 |
| `assess-camera-coverage-gap` | `18-security-systems-technology` | ADVANCED | REGULATED | P2 |
| `analyze-video-event-log` | `18-security-systems-technology` | ADVANCED | INTRUSIVE | P2 |
| `define-intrusion-detection-requirements` | `18-security-systems-technology` | ADVANCED | REGULATED | P2 |
| `analyze-alarm-event` | `18-security-systems-technology` | ADVANCED | CERTIFICATION_BOUNDARY | P2 |
| `identify-security-system-failure` | `18-security-systems-technology` | ADVANCED | CERTIFICATION_BOUNDARY | P2 |
| `prepare-security-system-requirements-summary` | `18-security-systems-technology` | ADVANCED | REGULATED | P2 |
| `assess-asset-protection-risk` | `19-loss-prevention-asset-protection` | ADVANCED | ROUTINE | P2 |
| `analyze-loss-event` | `19-loss-prevention-asset-protection` | ADVANCED | ROUTINE | P2 |
| `analyze-shrink-pattern` | `19-loss-prevention-asset-protection` | ADVANCED | ROUTINE | P2 |
| `triage-loss-prevention-incident` | `19-loss-prevention-asset-protection` | ADVANCED | REGULATED | P2 |
| `map-loss-event-evidence` | `19-loss-prevention-asset-protection` | ADVANCED | ROUTINE | P2 |
| `identify-process-control-weakness` | `19-loss-prevention-asset-protection` | ADVANCED | ROUTINE | P2 |
| `prepare-loss-prevention-case-summary` | `19-loss-prevention-asset-protection` | ADVANCED | ROUTINE | P2 |
| `build-asset-protection-improvement-plan` | `19-loss-prevention-asset-protection` | ADVANCED | ROUTINE | P2 |
| `draft-investigative-policy` | `20-investigation-security-program-management` | ADVANCED | REGULATED | P2 |
| `draft-security-post-orders` | `20-investigation-security-program-management` | ADVANCED | REGULATED | P2 |
| `review-investigative-procedure` | `20-investigation-security-program-management` | ADVANCED | REGULATED | P2 |
| `review-security-procedure` | `20-investigation-security-program-management` | ADVANCED | REGULATED | P2 |
| `audit-case-file` | `20-investigation-security-program-management` | ADVANCED | ROUTINE | P2 |
| `audit-security-program` | `20-investigation-security-program-management` | ADVANCED | REGULATED | P2 |
| `select-investigation-kpis` | `20-investigation-security-program-management` | ADVANCED | ROUTINE | P2 |
| `select-security-kpis` | `20-investigation-security-program-management` | ADVANCED | ROUTINE | P2 |
| `review-training-requirement` | `20-investigation-security-program-management` | ADVANCED | REGULATED | P2 |
| `track-corrective-action` | `20-investigation-security-program-management` | ADVANCED | ROUTINE | P2 |
| `measure-improvement-result` | `20-investigation-security-program-management` | ADVANCED | ROUTINE | P2 |
| `prepare-program-status-report` | `20-investigation-security-program-management` | ADVANCED | ROUTINE | P2 |
| `identify-program-governance-gap` | `20-investigation-security-program-management` | ADVANCED | REGULATED | P2 |

## Gate Result

```text
Exactly one canonical taxonomy source exists: docs/architecture/taxonomy-index.yaml
```

## AI-02 Sources

- `ROADMAP.md`
- `docs/architecture/domain-contract.md`
- `docs/architecture/scope-boundaries.md`
- `docs/architecture/prohibited-capabilities.md`
- `docs/development/handoffs/AI-01-final-handoff.md`
- ChatGPT task `Plan AgentLogistics Skills`, used only as roadmap provenance.
