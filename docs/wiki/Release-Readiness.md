# Release Readiness

This page records the public distribution posture for AgentInvestigate.

## Public Repository

Repository:

```text
https://github.com/jeremylongworth-source/AgentInvestigate
```

Required public state:

```text
visibility: PUBLIC
wiki: enabled
```

## Copilot Skill Distribution

GitHub CLI skill validation:

```powershell
gh skill publish --dry-run
```

Install a skill:

```powershell
gh skill install jeremylongworth-source/AgentInvestigate classify-request-type
```

Install for GitHub Copilot:

```powershell
gh skill install jeremylongworth-source/AgentInvestigate classify-request-type --agent github-copilot --scope user
```

## Release State

AI-37 selected:

```text
V1_PARTIALLY_READY
```

AI-38 public distribution readiness uses:

```text
PUBLIC_RELEASE_READY
```

This means the project is public, has a GitHub Wiki, validates against repository checks, and passes `gh skill publish --dry-run`. It does not replace maintainer judgment, external review, or current-source verification before relying on regulated content.

## Required Maintenance

Before future release tags:

- run the full validation suite;
- run `gh skill publish --dry-run`;
- verify source freshness for high-supersession regulatory claims;
- review open issues and security reports;
- confirm release notes;
- decide whether the release should remain partially ready, public-ready, or v1-ready.
