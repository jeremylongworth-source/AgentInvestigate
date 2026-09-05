# Public Release Distribution

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_38_PUBLIC_DISTRIBUTION_READY
```

## Scope And Audience

This document records the AI-38 public release distribution wave for AgentInvestigate. It is for maintainers, contributors, reviewers, and users who need to confirm that the repository is public, has a professional GitHub Wiki, and is installable through GitHub Copilot agent-skill tooling.

AI-38 adds distribution readiness evidence. It does not create new investigative skills, specialist modules, jurisdiction modules, legal determinations, regulatory certifications, privacy compliance certifications, security certifications, professional approvals, force training, weapons training, emergency-response certifications, or operational investigative procedures.

## Distribution Verdict

```text
PUBLIC_RELEASE_READY
```

AI-38 supersedes the public distribution blockers identified after AI-37:

- repository visibility is public;
- GitHub Wiki is enabled;
- professional wiki source pages exist in `docs/wiki/`;
- Copilot skill publication validation passes with `gh skill publish --dry-run`;
- README documents the Copilot install path.

AI-37 remains a conservative v1 release-candidate audit with verdict `V1_PARTIALLY_READY`. AI-38 establishes public distribution readiness, not unrestricted legal, privacy, regulatory, safety, or professional readiness.

## GitHub Repository State

Repository:

```text
https://github.com/jeremylongworth-source/AgentInvestigate
```

Required state:

- visibility: `PUBLIC`
- wiki: `enabled`
- topic: `agent-skills`
- secret scanning: requested through GitHub CLI
- secret scanning push protection: requested through GitHub CLI

## GitHub Wiki

Wiki URL:

```text
https://github.com/jeremylongworth-source/AgentInvestigate/wiki
```

Wiki source pages:

- `docs/wiki/Home.md`
- `docs/wiki/_Sidebar.md`
- `docs/wiki/Getting-Started.md`
- `docs/wiki/Architecture-Overview.md`
- `docs/wiki/Skill-Catalog.md`
- `docs/wiki/Professional-Skillsets.md`
- `docs/wiki/Sensitivity-And-Routing.md`
- `docs/wiki/Jurisdiction-Model.md`
- `docs/wiki/Safety-Boundaries.md`
- `docs/wiki/Validation-And-Testing.md`
- `docs/wiki/Contributing-Guide.md`
- `docs/wiki/Release-Readiness.md`

## Copilot Skill Install

GitHub CLI supports agent-skill publishing and install workflows. This repository validates with:

```powershell
gh skill publish --dry-run
```

Representative preview command:

```powershell
gh skill preview jeremylongworth-source/AgentInvestigate classify-request-type
```

Representative install command:

```powershell
gh skill install jeremylongworth-source/AgentInvestigate classify-request-type
```

Representative GitHub Copilot install command:

```powershell
gh skill install jeremylongworth-source/AgentInvestigate classify-request-type --agent github-copilot --scope user
```

## Remaining Caveats

- `gh skill` is a GitHub CLI preview feature and may change.
- GitHub release publishing is a maintainer decision.
- Tag protection may require repository ruleset configuration outside this wave.
- Current-source verification remains required before relying on high-supersession regulatory content.
- External legal, privacy, safety, and professional review are not replaced by this release-distribution wave.

## Validation

AI-38 validation checks:

- repository-side public distribution artifact exists;
- wiki source pages exist;
- README documents GitHub Wiki and `gh skill install`;
- validation scripts include AI-38;
- release fixture records repository visibility, wiki, skill dry-run, and distribution verdict.
