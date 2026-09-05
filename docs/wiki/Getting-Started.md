# Getting Started

This page explains how to inspect, validate, and install AgentInvestigate skills.

## Clone The Repository

```powershell
git clone https://github.com/jeremylongworth-source/AgentInvestigate.git
cd AgentInvestigate
```

## Validate Locally

Run:

```powershell
.\scripts\validate-all.ps1
```

The validation suite checks public documentation, taxonomy structure, routing, standards, foundations, skill packages, Canadian regulatory specialization foundations, professional skillsets, integration scenarios, adversarial safety scenarios, specialization planning, public readiness, and release-candidate audit records.

## Install With GitHub Copilot Skill Tooling

GitHub CLI supports agent-skill preview, install, update, and publish commands.

Preview a skill before installing:

```powershell
gh skill preview jeremylongworth-source/AgentInvestigate classify-request-type
```

Install a specific skill:

```powershell
gh skill install jeremylongworth-source/AgentInvestigate classify-request-type
```

Install for GitHub Copilot explicitly:

```powershell
gh skill install jeremylongworth-source/AgentInvestigate classify-request-type --agent github-copilot --scope user
```

After installation, start or reload the agent session and ask the agent to list available skills.

## First Useful Skill Paths

Start with conservative routing and safety skills:

- `classify-request-type`
- `check-prohibited-capabilities`
- `identify-jurisdiction`
- `assess-lawful-purpose`
- `validate-investigative-authority`
- `identify-privacy-obligation`
- `prepare-compliance-escalation`

## First Useful Documents

- `README.md`
- `ROADMAP.md`
- `docs/architecture/domain-contract.md`
- `docs/architecture/authority-routing.md`
- `docs/architecture/prohibited-capabilities.md`
- `tests/evaluation-rubric.json`

## Safe Use Pattern

1. Classify the request.
2. Check prohibited capabilities.
3. Identify jurisdiction if regulated or intrusive issues are present.
4. Validate role, authority, lawful purpose, scope, source access, privacy basis, and human review.
5. Use the narrowest relevant atomic skill.
6. Preserve limitations and escalation needs.
