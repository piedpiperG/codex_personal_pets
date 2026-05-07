param(
    [Parameter(Mandatory = $true)]
    [string]$PetName,

    [string]$CodexHome = "$env:USERPROFILE\.codex"
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$sourceDir = Join-Path $repoRoot "pets\$PetName"
$targetDir = Join-Path $CodexHome "pets\$PetName"

if (-not (Test-Path -LiteralPath $sourceDir)) {
    throw "Pet package not found: $sourceDir"
}

$manifest = Join-Path $sourceDir "pet.json"
$spritesheet = Join-Path $sourceDir "spritesheet.webp"

if (-not (Test-Path -LiteralPath $manifest)) {
    throw "Missing pet.json: $manifest"
}

if (-not (Test-Path -LiteralPath $spritesheet)) {
    throw "Missing spritesheet.webp: $spritesheet"
}

New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
Copy-Item -LiteralPath $manifest -Destination (Join-Path $targetDir "pet.json") -Force
Copy-Item -LiteralPath $spritesheet -Destination (Join-Path $targetDir "spritesheet.webp") -Force

Write-Host "Installed $PetName to $targetDir"
