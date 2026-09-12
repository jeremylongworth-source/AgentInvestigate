# Getting Started

Use this page to move from a public repository checkout to a verified skill installation.

## Prerequisites

You need:

- Git;
- GitHub CLI with an authenticated account;
- a GitHub CLI version that provides the `gh skill` preview command;
- an agent host that supports the installed skill format.

The repository is public. Skill installation and preview still depend on the capabilities and authentication state of your local GitHub CLI.

## 1. Clone And Validate

```powershell
git clone https://github.com/jeremylongworth-source/AgentInvestigate.git
cd AgentInvestigate
.\scripts\validate-all.ps1
```

A passing validation run confirms repository contracts and fixtures. It does not certify legal correctness, privacy compliance, licensing eligibility, professional competence, emergency readiness, forensic admissibility, or live model behavior.

## 2. Preview A Skill

Start with the conservative request-routing skill:

```powershell
gh skill preview jeremylongworth-source/AgentInvestigate classify-request-type
```

The package is located at `skills/<family>/<skill>/SKILL.md`. Read its frontmatter, inputs, gates, output contract, limitations, and references before relying on it.

## 3. Install A Skill

For general agent-skill use:

```powershell
gh skill install jeremylongworth-source/AgentInvestigate classify-request-type
```

For GitHub Copilot:

```powershell
gh skill install jeremylongworth-source/AgentInvestigate classify-request-type --agent github-copilot --scope user
```

After installation, start or reload the agent session and confirm that the host can list the installed skill. The `gh skill` command is a preview feature and may change.

## 4. Use The Safe Request Path

For a new task:

1. classify the request;
2. check prohibited capabilities;
3. identify sensitivity and jurisdiction;
4. validate role, authority, lawful purpose, scope, source access, privacy basis, and human review when needed;
5. use the narrowest relevant skill;
6. preserve uncertainty, limitations, stop conditions, and escalation needs.

Appropriate first tasks include organizing supplied records into an evidence matrix, preparing neutral interview questions, constructing a chronology, or drafting a documentation-gap review.

## Where To Read Next

- [[Sensitivity And Routing]]
- [[Safety Boundaries]]
- [[Jurisdiction Model]]
- [[Skill Catalog]]
- [[Validation And Testing]]
