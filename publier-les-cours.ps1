param([string]$Message, [switch]$PrepareOnly)
$ErrorActionPreference = 'Stop'
$previousPythonUtf8 = $env:PYTHONUTF8
$env:PYTHONUTF8 = '1'
Push-Location $PSScriptRoot
try {
  & python scripts/prepare-linux.py
  if ($LASTEXITCODE) { throw 'Échec de préparation des cours.' }
  & node scripts/prepare-quizzes.mjs
  if ($LASTEXITCODE) { throw 'Échec de préparation des quiz.' }
  & python scripts/finalize-html-supports.py --sync-source 'C:/Users/kayaw/Nextcloud/Obsidian/CoffreSam/Formations/linux-initiation'
  if ($LASTEXITCODE) { throw 'Échec de préparation des supports HTML hors ligne.' }
  & python scripts/check-source-sync.py
  if ($LASTEXITCODE) { throw 'Échec de synchronisation avec le coffre Obsidian.' }
  & python scripts/prepare-course-pdfs.py
  if ($LASTEXITCODE) { throw 'Échec de génération des PDF des cours.' }
  & python scripts/check-course-pdfs.py
  if ($LASTEXITCODE) { throw 'Échec de vérification des PDF des cours.' }
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
  if ($PrepareOnly) { Write-Host 'Préparation et vérifications terminées.' -ForegroundColor Green; return }
  $publicationPaths = @('content', 'site-content', 'chapters.json', 'publication-policy.json')
  if (-not (git status --porcelain -- @publicationPaths)) { Write-Host 'Aucune modification des supports à publier.'; return }
  if (-not $Message) { $Message = Read-Host 'Message de publication' }
  if (-not $Message) { $Message = 'Mise à jour des formations Linux et Bash' }
  if ((Read-Host 'Publier sur GitHub ? [o/N]') -notmatch '^(o|oui|y|yes)$') { return }
  & git add -- @publicationPaths
  if ($LASTEXITCODE) { throw 'Échec git add.' }
  & git commit --only -m $Message -- @publicationPaths
  if ($LASTEXITCODE) { throw 'Échec du commit.' }
  & git push -u origin main
  if ($LASTEXITCODE) { throw 'Échec de publication GitHub.' }
} finally { Pop-Location; $env:PYTHONUTF8 = $previousPythonUtf8 }
