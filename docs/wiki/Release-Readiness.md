# Release Readiness

This page explains the current public distribution posture and the distinction between public availability and unconditional v1 readiness.

## Current Public State

Repository:

```text
https://github.com/jeremylongworth-source/AgentInvestigate
```

Wiki:

```text
https://github.com/jeremylongworth-source/AgentInvestigate/wiki
```

Recorded public state:

- visibility: PUBLIC
- wiki: enabled
- repository visibility: `PUBLIC`;
- GitHub Wiki: enabled and published;
- repository topic: `agent-skills`;
- public release distribution verdict: `PUBLIC_RELEASE_READY`.

## Copilot Skill Distribution

Preview a skill:

```powershell
gh skill preview jeremylongworth-source/AgentInvestigate classify-request-type
```

Install a skill:

```powershell
gh skill install jeremylongworth-source/AgentInvestigate classify-request-type
```

Install for GitHub Copilot:

```powershell
gh skill install jeremylongworth-source/AgentInvestigate classify-request-type --agent github-copilot --scope user
```

Validate publication readiness:

```powershell
gh skill publish --dry-run
```

The `gh skill` command is a GitHub CLI preview feature and may change.

## Readiness States

| Record | Meaning |
| --- | --- |
| `PUBLIC_RELEASE_READY` | The repository is public, the wiki is enabled and published, distribution documentation exists, and repository validation covers the release-distribution record. |
| `V1_PARTIALLY_READY` | The v1 release-candidate audit supports public use but still requires explicit maintainer and external review decisions. |
| `V1_READY` | A future audit decision after all required maintainer, source, live evaluation, external review, release, and support conditions are recorded. |

Public availability does not replace legal, privacy, safety, regulatory, professional, or current-source review.

## Maintainer Checklist

Before a future release tag:

- run `.\scripts\validate-all.ps1`;
- run `gh skill publish --dry-run`;
- review high-supersession regulatory sources;
- review open issues and security reports;
- confirm release notes;
- record maintainer approval, release-risk acceptance, and support ownership;
- decide the release posture explicitly.

See the [v1 release-candidate audit](https://github.com/jeremylongworth-source/AgentInvestigate/blob/main/docs/evaluation/v1-release-candidate-audit.md) and [public distribution record](https://github.com/jeremylongworth-source/AgentInvestigate/blob/main/docs/release/public-release-distribution.md).
