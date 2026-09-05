# AgentInvestigate

AgentInvestigate is an open-source AI skill repository for lawful professional work in private investigation, investigative research, evidence management, corporate and workplace investigations, background screening and due diligence, private security operations, incident response, physical security, loss prevention, and security program management.

The project has completed baseline setup, domain-boundary work, master taxonomy integration, sensitivity/authority routing, skill authoring standards, source-handling standards, the validation/evaluation framework, shared professional foundations, the four-class reference implementation, the Professional Core & Ethics skill family, the intake, authority, law, licensing, privacy, and compliance control layer, the Investigation Planning & Case Management skill family, the Research, OSINT & Public Records skill family, the Identity, Entity & Timeline Analysis skill family, the Interviewing, Witnesses & Statements skill family, the Evidence & Chain of Custody skill family, the Investigative Analysis skill family, the Reporting, Findings & Case Presentation skill family, the Observation & Surveillance Governance skill family, the Corporate & Workplace Investigations skill family, and the Background Screening & Due Diligence skill family.

Core principles:

```text
AUTHORITY BEFORE ACTION
EVIDENCE BEFORE CONCLUSION
HUMAN CONTROL BEFORE INTRUSIVE WORK
```

AgentInvestigate does not confer investigator licensing, security licensing, law-enforcement authority, legal authority, regulatory approval, use-of-force qualification, weapons qualification, emergency-response certification, engineering approval, or professional certification.

## Current Status

- Roadmap: `ROADMAP.md`
- Latest completed wave: `AI-20 Background Screening & Due Diligence`
- Recommended next wave: `AI-21 Security Operations, Access & Patrol`
- Baseline audit: `docs/development/AI-00-baseline-audit.md`
- Domain contract: `docs/architecture/domain-contract.md`
- Scope boundaries: `docs/architecture/scope-boundaries.md`
- Prohibited capabilities: `docs/architecture/prohibited-capabilities.md`
- Master taxonomy: `docs/architecture/master-taxonomy-v1.md`
- Canonical taxonomy index: `docs/architecture/taxonomy-index.yaml`
- Sensitivity model: `docs/architecture/sensitivity-model.md`
- Authority routing: `docs/architecture/authority-routing.md`
- Intrusive task gate: `docs/architecture/intrusive-task-gate.md`
- Certification boundaries: `docs/architecture/certification-boundaries.md`
- Skill authoring standard: `docs/standards/skill-authoring-standard.md`
- Skill naming standard: `docs/standards/skill-naming-standard.md`
- Output contract standard: `docs/standards/output-contract-standard.md`
- Research and evidence standard: `docs/standards/research-and-evidence-standard.md`
- Regulatory source standard: `docs/standards/regulatory-source-standard.md`
- Source freshness standard: `docs/standards/source-freshness-standard.md`
- Testing standard: `docs/standards/testing-standard.md`
- Evaluation standard: `docs/standards/evaluation-standard.md`
- Validation scenarios: `tests/validation-scenarios.json`
- Evaluation rubric: `tests/evaluation-rubric.json`
- Foundation catalog: `docs/foundations/foundation-catalog.md`
- Professional vocabulary: `docs/foundations/professional-vocabulary.md`
- Shared schemas: `docs/foundations/shared-schemas.md`
- Report structure contracts: `docs/foundations/report-structure-contracts.md`
- Foundation consumer map: `docs/foundations/foundation-consumer-map.json`
- Reference skill scenarios: `tests/reference-skills/AI-08-reference-scenarios.json`
- Professional core scenarios: `tests/reference-skills/AI-09-professional-core-scenarios.json`
- Authority and compliance scenarios: `tests/reference-skills/AI-10-authority-compliance-scenarios.json`
- Case management scenarios: `tests/reference-skills/AI-11-case-management-scenarios.json`
- Research and OSINT scenarios: `tests/reference-skills/AI-12-research-osint-scenarios.json`
- Entity analysis scenarios: `tests/reference-skills/AI-13-entity-analysis-scenarios.json`
- Interviewing scenarios: `tests/reference-skills/AI-14-interviewing-scenarios.json`
- Evidence scenarios: `tests/reference-skills/AI-15-evidence-scenarios.json`
- Investigative analysis scenarios: `tests/reference-skills/AI-16-investigative-analysis-scenarios.json`
- Reporting scenarios: `tests/reference-skills/AI-17-reporting-scenarios.json`
- Observation governance scenarios: `tests/reference-skills/AI-18-observation-governance-scenarios.json`
- Workplace investigation scenarios: `tests/reference-skills/AI-19-workplace-investigations-scenarios.json`
- Background screening and due diligence scenarios: `tests/reference-skills/AI-20-screening-due-diligence-scenarios.json`
- Latest handoff: `docs/development/handoffs/AI-20-final-handoff.md`

## Development Approach

The repository is roadmap-wave driven. Early waves establish domain boundaries, taxonomy, sensitivity routing, source handling, testing, shared foundations, and four reference skill classes before bulk skill authoring.

Do not create placeholder skill folders or broad directory structures without active content and validation. Skills should remain atomic; professional roles belong in the skillset layer.

Family skill authoring should continue only in roadmap-scoped waves with validation updated alongside each wave.

## Safety Boundaries

The roadmap excludes procedural assistance for hacking, credential theft, unauthorized access, lock bypass, forced entry, illegal tracking, stalking, intimate-partner monitoring, impersonation, coercive interrogation, access-control circumvention, camera or alarm defeat, weapons use, restraint techniques, combat techniques, and similar misuse-prone conduct.

Regulated, intrusive, and certification-boundary content requires jurisdiction, authority, source, and human-review controls before implementation.

## Validation

Run the current baseline checks:

```powershell
.\scripts\validate-all.ps1
```

## License

MIT. See `LICENSE`.
