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

python "$PSScriptRoot\validate-standards.py" --repo-root "$RepoRoot"
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

python "$PSScriptRoot\validate-tests.py" --repo-root "$RepoRoot"
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

python "$PSScriptRoot\validate-foundations.py" --repo-root "$RepoRoot"
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

python "$PSScriptRoot\validate-skills.py" --repo-root "$RepoRoot"
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

python "$PSScriptRoot\validate-specializations.py" --repo-root "$RepoRoot"
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

python "$PSScriptRoot\validate-skillsets.py" --repo-root "$RepoRoot"
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

python "$PSScriptRoot\validate-integration.py" --repo-root "$RepoRoot"
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

python "$PSScriptRoot\validate-safety.py" --repo-root "$RepoRoot"
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

Write-Host "All AgentInvestigate validation checks passed."
