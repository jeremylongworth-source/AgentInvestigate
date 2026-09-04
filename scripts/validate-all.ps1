$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot

python "$PSScriptRoot\validate-docs.py" --repo-root "$RepoRoot"
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

python "$PSScriptRoot\validate-taxonomy.py" --repo-root "$RepoRoot"
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

python "$PSScriptRoot\validate-routing.py" --repo-root "$RepoRoot"
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

Write-Host "All AgentInvestigate validation checks passed."
