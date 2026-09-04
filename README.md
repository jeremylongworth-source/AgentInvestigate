# AgentInvestigate

AgentInvestigate is an open-source AI skill repository for lawful professional work in private investigation, investigative research, evidence management, corporate and workplace investigations, background screening and due diligence, private security operations, incident response, physical security, loss prevention, and security program management.

The project has completed baseline setup, domain-boundary work, master taxonomy integration, sensitivity/authority routing, skill authoring standards, source-handling standards, and the validation/evaluation framework.

Core principles:

```text
AUTHORITY BEFORE ACTION
EVIDENCE BEFORE CONCLUSION
HUMAN CONTROL BEFORE INTRUSIVE WORK
```

AgentInvestigate does not confer investigator licensing, security licensing, law-enforcement authority, legal authority, regulatory approval, use-of-force qualification, weapons qualification, emergency-response certification, engineering approval, or professional certification.

## Current Status

- Roadmap: `ROADMAP.md`
- Latest completed wave: `AI-06 Validation & Evaluation Framework`
- Recommended next wave: `AI-07 Shared Professional Foundations`
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
- Latest handoff: `docs/development/handoffs/AI-06-final-handoff.md`

## Development Approach

The repository is roadmap-wave driven. Early waves establish domain boundaries, taxonomy, sensitivity routing, source handling, testing, shared foundations, and four reference skill classes before bulk skill authoring.

Do not create placeholder skill folders or broad directory structures without active content and validation. Skills should remain atomic; professional roles belong in the skillset layer.

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
