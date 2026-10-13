param([string]$Message, [switch]$PrepareOnly)
$ErrorActionPreference = 'Stop'
Push-Location $PSScriptRoot
try {
  & python scripts/prepare-linux.py
  if ($LASTEXITCODE) { throw 'Échec de préparation des cours.' }
  & node scripts/prepare-quizzes.mjs
  if ($LASTEXITCODE) { throw 'Échec de préparation des quiz.' }
  & python scripts/finalize-html-supports.py
  if ($LASTEXITCODE) { throw 'Échec de préparation des supports HTML hors ligne.' }
  & node scripts/check-learning-ui.mjs
  if ($LASTEXITCODE) { throw 'Échec de vérification des quiz ou des contrastes.' }
  & node scripts/check-introduction.mjs
  if ($LASTEXITCODE) { throw 'Échec de vérification du chapitre 01 interactif.' }
  & node scripts/check-permissions.mjs
  if ($LASTEXITCODE) { throw 'Échec de vérification du laboratoire des permissions.' }
  & node scripts/fix-quartz-graph.mjs
  if ($LASTEXITCODE) { throw 'Échec de correction du graphe.' }
  & node quartz/bootstrap-cli.mjs build
  if ($LASTEXITCODE) { throw 'Échec du build Quartz.' }
  & python scripts/publish-assets.py
  if ($LASTEXITCODE) { throw 'Échec de vérification du site.' }
  if ($PrepareOnly) { Write-Host 'Préparation et vérifications terminées.' -ForegroundColor Green; exit 0 }
  if (-not (git status --porcelain)) { Write-Host 'Aucune modification.'; exit 0 }
  if (-not $Message) { $Message = Read-Host 'Message de publication' }
  if (-not $Message) { $Message = 'Mise à jour de la formation Linux' }
  if ((Read-Host 'Publier sur GitHub ? [o/N]') -notmatch '^(o|oui|y|yes)$') { exit 0 }
  & git add -A
  if ($LASTEXITCODE) { throw 'Échec git add.' }
  & git commit -m $Message
  if ($LASTEXITCODE) { throw 'Échec du commit.' }
  & git push -u origin main
  if ($LASTEXITCODE) { throw 'Échec de publication GitHub.' }
} finally { Pop-Location }
