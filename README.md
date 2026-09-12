# AgentInvestigate

AgentInvestigate is an open-source AI skill repository for lawful professional investigation and private security support work.

It gives general-purpose AI agents bounded procedures, routing gates, evidence discipline, source requirements, output contracts, and escalation rules for professional work. The repository contains atomic skills, composed professional skillsets, Canadian jurisdiction foundations, evaluation fixtures, and repository validators.

```text
AUTHORITY BEFORE ACTION
EVIDENCE BEFORE CONCLUSION
HUMAN CONTROL BEFORE INTRUSIVE WORK
```

Current public distribution:

```text
PUBLIC_RELEASE_READY
```

Public readiness token:

```text
AGENTINVESTIGATE_AI_36_PUBLIC_READINESS_READY
```

Public distribution token:

```text
AGENTINVESTIGATE_AI_38_PUBLIC_DISTRIBUTION_READY
```

## Installation And Use

Clone the repository and run its validation gate:

```powershell
git clone https://github.com/jeremylongworth-source/AgentInvestigate.git
cd AgentInvestigate
.\scripts\validate-all.ps1
```

Preview a skill before installing it:

```powershell
gh skill preview jeremylongworth-source/AgentInvestigate classify-request-type
```

Install one skill for local agent-skill use:

```powershell
gh skill install jeremylongworth-source/AgentInvestigate classify-request-type
```

Install one skill for GitHub Copilot:

```powershell
gh skill install jeremylongworth-source/AgentInvestigate classify-request-type --agent github-copilot --scope user
```

These commands require GitHub CLI authentication and a GitHub CLI version that provides `gh skill`. The `gh skill` command is a preview feature and may change.

## Who It Is For

AgentInvestigate is for maintainers building investigation or security-oriented AI skills, evaluators testing routing and safety behavior, contributors adding roadmap-scoped content, and organizations that need reusable support patterns for lawful investigation, security operations, reporting, and escalation.

It is not a substitute for counsel, regulators, licensed investigators, licensed security managers, privacy officers, HR, emergency services, qualified trainers, forensic experts, engineers, fire/life-safety professionals, or other qualified reviewers.

## Choose A Path

| Need | Start here |
| --- | --- |
| Understand the project | [GitHub Wiki](https://github.com/jeremylongworth-source/AgentInvestigate/wiki) and [Architecture Overview](docs/wiki/Architecture-Overview.md) |
| Use a single capability | [Skill Catalog](docs/wiki/Skill-Catalog.md), then a skill's `SKILL.md` |
| Build a role-oriented workflow | [Professional Skillsets](docs/wiki/Professional-Skillsets.md) |
| Review a sensitive request | [Sensitivity And Routing](docs/wiki/Sensitivity-And-Routing.md) and [Safety Boundaries](docs/wiki/Safety-Boundaries.md) |
| Add or change repository content | [CONTRIBUTING.md](CONTRIBUTING.md) and the [Contributing Guide](docs/wiki/Contributing-Guide.md) |

## Supported Domains

AgentInvestigate supports two related but distinct professional branches.

Private investigation coverage includes intake and authority review, case planning, public-source research, public records, identity and entity analysis, interviewing, evidence organization, investigative analysis, reporting, corporate and workplace investigations, and background screening and due diligence.

Private security coverage includes security operations, access and patrol, incident response, communication and de-escalation, physical security, risk assessment, security systems governance, loss prevention, asset protection, and investigation or security program management.

The repository also includes Canadian federal, Ontario, British Columbia, and Alberta regulatory foundations, professional skillset composition, multi-skill integration evaluation, adversarial safety evaluation, and a framework for future specialist modules.

## Skill Examples

Atomic skills live under `skills/<family>/<skill>/SKILL.md`. Representative skills include:

- `classify-request-type`
- `check-prohibited-capabilities`
- `identify-jurisdiction`
- `assess-lawful-purpose`
- `validate-investigative-authority`
- `plan-open-source-research`
- `record-source-provenance`
- `prepare-neutral-question-set`
- `create-evidence-log`
- `build-evidence-matrix`
- `prepare-findings-summary`
- `triage-security-incident`
- `document-alarm-response`
- `assess-camera-coverage-gap`
- `identify-control-gaps`
- `prepare-compliance-escalation`

Professional roles compose atomic skills through `skillsets/professional-skillsets.json`. They do not duplicate the underlying procedures.

## Sensitivity Model

AgentInvestigate uses six global routing states:

| State | Use |
| --- | --- |
| `PROCEED_ROUTINE` | The request is routine and has enough scope and inputs. |
| `CLARIFY_SCOPE` | Material facts are missing, but the request is not prohibited. |
| `REGULATED_RESEARCH_ONLY` | Legal, licensing, privacy, employment, records, or compliance issues require current source-backed framing and no final determination. |
| `INTRUSIVE_GATE_REQUIRED` | Sensitive information, surveillance, monitoring, identity, or screening work must stop until authority, privacy, necessity, proportionality, and human approval are addressed. |
| `CERTIFICATION_ESCALATION` | Emergency, force, weapons, restraints, alarm response, engineering, life-safety, or other qualified work requires professional recognition, documentation, and escalation only. |
| `PROHIBITED_REDIRECT` | The requested conduct is outside the repository boundary and must be refused at the procedural level. |

Sensitive work must not route directly from a raw request to execution. See [docs/architecture/authority-routing.md](docs/architecture/authority-routing.md) and [docs/architecture/prohibited-capabilities.md](docs/architecture/prohibited-capabilities.md).

## Jurisdiction Model

Jurisdiction is required when an answer depends on licensing, privacy, employment screening, workplace investigations, recording or monitoring, record access, evidence handling, security authority, emergency boundaries, alarm response, force, weapons, restraints, fire, life safety, or other regulated requirements.

Current Canadian foundations are organized under:

- `specializations/canada/federal/`
- `specializations/canada/ontario/`
- `specializations/canada/british-columbia/`
- `specializations/canada/alberta/`

These are source-backed architecture foundations. They do not grant authority, licensing, legal advice, privacy compliance certification, or professional approval. Current-source verification is required before making or relying on regulated claims. See [Jurisdiction Model](docs/wiki/Jurisdiction-Model.md), [Canadian jurisdiction roadmap](docs/architecture/canadian-jurisdiction-roadmap.md), and [specialization roadmap](docs/architecture/specialization-roadmap.md).

## Typical Use

Use the narrowest relevant skill and preserve the output's limitations.

```text
request
  -> classify
  -> check prohibited capabilities
  -> identify sensitivity and jurisdiction
  -> validate authority, purpose, privacy, and source access
  -> use the bounded skill or escalate
  -> record evidence, uncertainty, and review needs
```

Examples of appropriate use include building an evidence matrix from supplied records, preparing neutral interview questions, organizing a case chronology, reviewing a security incident for documentation gaps, or identifying questions for qualified legal or privacy review.

## Validation

Run the complete repository gate:

```powershell
.\scripts\validate-all.ps1
```

The suite checks baseline documentation, taxonomy integrity, routing, authoring and source standards, shared foundations, skill packages, Canadian specialization foundations, professional skillsets, integration scenarios, adversarial safety scenarios, specialization planning, public documentation, v1 release-candidate records, and public release distribution readiness.

Validate Copilot skill publication readiness with:

```powershell
gh skill publish --dry-run
```

The suite validates repository contracts and fixtures. It does not prove live model behavior, legal correctness, privacy compliance, licensing eligibility, professional competence, emergency readiness, forensic admissibility, or real-world operational safety. See [Validation And Testing](docs/wiki/Validation-And-Testing.md).

## Limitations

AgentInvestigate is a skill repository and evaluation corpus. It is not a licensed investigation service, private security company, law firm, regulator, emergency service, forensic lab, HR department, insurer, engineering firm, fire/life-safety authority, or training provider.

The repository does not confer investigator licensing, security licensing, law-enforcement authority, legal authority, regulatory approval, use-of-force qualification, weapons qualification, emergency-response certification, engineering approval, fire or life-safety approval, privacy compliance certification, or professional certification.

Outputs still require qualified human review when legal, licensing, privacy, employment, safety, emergency, evidence, professional, or operational consequences are present. AgentInvestigate is not a substitute for counsel, regulators, licensed investigators, licensed security managers, privacy officers, HR, emergency services, qualified trainers, forensic experts, engineers, fire/life-safety professionals, or other qualified reviewers.

## Prohibited Capabilities

AgentInvestigate must not provide procedural assistance for:

- hacking, credential theft, or unauthorized account access;
- lock bypass, forced entry, access-control circumvention, alarm defeat, or camera evasion;
- covert tracker installation, illegal GPS tracking, stalking, harassment, or intimate-partner monitoring;
- impersonation of police, government, regulators, employers, courts, banks, telecom providers, platforms, or emergency services;
- coercive interrogation, threats, intimidation, detention tactics, search tactics, physical control, weapons, firearms, batons, handcuffs, pain compliance, restraint techniques, combat techniques, or takedowns;
- evidence fabrication, alteration, concealed source gaps, or false statement coaching.

When a request crosses a boundary, the correct response is to stop the prohibited procedure, name the boundary without operational detail, preserve any benign professional need, and redirect to documentation, safety planning, incident reporting, source logging, policy review, authority checks, escalation, or qualified professional consultation. AgentInvestigate must not provide procedural assistance for prohibited conduct even when the request is framed as investigation, OSINT, due diligence, safety, security assessment, penetration testing, interviewing, or training.

## Repository Structure

```text
skills/                    Atomic skill packages
skillsets/                 Professional role composition
specializations/           Canadian jurisdiction foundations
docs/architecture/         Domain, taxonomy, routing, and extension contracts
docs/standards/            Skill, evidence, source, and testing standards
docs/foundations/          Shared vocabulary, schemas, and report contracts
docs/evaluation/           Integration, safety, and release-candidate evidence
docs/wiki/                 Versioned source for the GitHub Wiki
tests/                     Routing, validation, evaluation, and safety fixtures
scripts/                   Validators and generators
```

## Current Status

- Latest completed wave: `AI-38 Public Release Distribution`
- Current public distribution verdict: `PUBLIC_RELEASE_READY`
- Current v1 audit verdict: `V1_PARTIALLY_READY`
- Recommended next step: Post-v1 candidate tracks require separate review before roadmap admission.
- Roadmap: [ROADMAP.md](ROADMAP.md)
- Release-candidate audit: [docs/evaluation/v1-release-candidate-audit.md](docs/evaluation/v1-release-candidate-audit.md)
- Public distribution record: [docs/release/public-release-distribution.md](docs/release/public-release-distribution.md)
- Latest handoff: [docs/development/handoffs/AI-38-final-handoff.md](docs/development/handoffs/AI-38-final-handoff.md)
- GitHub Wiki: `https://github.com/jeremylongworth-source/AgentInvestigate/wiki`

## Contributing

Contributions follow `ROADMAP.md` and the latest handoff.

Before opening a pull request:

- read `ROADMAP.md` and the latest handoff;
- keep the change scoped to the active wave;
- preserve the private investigation and private security distinction;
- use authoritative sources and verification dates for regulated or safety-sensitive claims;
- avoid prohibited procedural content;
- update fixtures and validators with behavior changes;
- run `.\scripts\validate-all.ps1`;
- document changed files, validation, source evidence, and known limitations.

See [CONTRIBUTING.md](CONTRIBUTING.md) and the [Contributing Guide](docs/wiki/Contributing-Guide.md).

## Public Files

- `README.md`
- `ROADMAP.md`
- `CONTRIBUTING.md`
- `CHANGELOG.md`
- `LICENSE`
- `SECURITY.md`
- `CODE_OF_CONDUCT.md`

## License

MIT. See [LICENSE](LICENSE).
