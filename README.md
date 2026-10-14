# Linux initiation & Bash

Site Quartz de la formation Linux, construit sur le modèle ITIL.

Source officielle : `C:/Users/kayaw/Nextcloud/Obsidian/CoffreSam/Formations/linux-initiation`.

Deux parcours sur le même site : Linux initiation (10 chapitres et 8 TP) et Bash (6 chapitres et 8 TP). Versions HTML, téléchargements Markdown et une archive Obsidian par formation. Les corrections restent dans le coffre du formateur.

Dans les deux formations, chaque chapitre contient son cours Markdown, sa version HTML et son dossier `tp/`. Les six TP Bash sont placés sous leurs chapitres dans l'explorateur ; la synthèse et les exercices bonus sont regroupés à part.

Source Bash : `C:/Users/kayaw/Nextcloud/Obsidian/CoffreSam/Formations/linux-scripting-bash`.

Le parcours Bash débutant suit une progression terminal → variables → scripts → conditions → boucles → texte. Les huit TP utilisent des données fictives dans un atelier personnel, avec corrections privées. Les sept schémas et les HTML autonomes sont régénérés depuis les Markdown par `scripts/render-bash-supports.py`. Le mémo et les schémas sont inclus dans le ZIP.

Validation sur Debian : `python scripts/validate-bash-on-debian.py` exécute les exemples et les scénarios des solutions dans un espace temporaire, via l'alias `ssh debian`.

```powershell
npm ci
.\publier-les-cours.ps1 -PrepareOnly
```

Voir [le mode de publication](MODE-EMPLOI-PUBLICATION.md).
