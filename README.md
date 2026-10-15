# Linux initiation & Bash

Site Quartz de la formation Linux, construit sur le modèle ITIL.

Source officielle : `C:/Users/kayaw/Nextcloud/Obsidian/CoffreSam/Formations/linux-initiation`.

Deux parcours sur le même site : Linux initiation (10 chapitres et 8 TP) et Bash (6 chapitres et 9 TP). Versions HTML, téléchargements Markdown et une archive Obsidian par formation. Les corrections restent dans le coffre du formateur.

Dans les deux formations, chaque chapitre contient son cours Markdown, sa version HTML et son dossier `tp/`. Les six TP Bash sont placés sous leurs chapitres dans l'explorateur ; le jeu final, la synthèse et les exercices bonus sont regroupés à part.

Source Bash : `C:/Users/kayaw/Nextcloud/Obsidian/CoffreSam/Formations/linux-scripting-bash`.

Le parcours Bash débutant suit une progression terminal → variables → scripts → conditions → boucles → texte. Les neuf TP utilisent des données fictives dans un atelier personnel, avec corrections privées. Les sept schémas et les HTML autonomes sont régénérés depuis les Markdown par `scripts/render-bash-supports.py`. Le mémo et les schémas sont inclus dans le ZIP.

Chaque chapitre Bash possède un quiz de vingt questions expliquées, soit 120 questions. Le générateur `scripts/prepare-bash-quizzes.py` lit `Ressources/quiz/bash-questions.json` dans le coffre et reprend le moteur des quiz Linux : ordre aléatoire, positions des réponses équilibrées, score, meilleur résultat et nouvelle tentative. Les quiz sont liés aux chapitres, intégrés aux HTML et inclus avec leurs ressources dans le ZIP hors ligne.

Orion Académie est une aventure hors ligne de 48 missions dans un vrai Bash, avec ASCII, indices, badges et sauvegarde. Les sources du coffre dans `jeu/` alimentent l’archive `telechargements/bash/orion-academie.tar.gz`, sa somme SHA-256 et le ZIP Obsidian. La page `/bash/jeu/` explique le téléchargement et le lancement. Le moteur utilise Python standard ; les exercices et l’arcade finale utilisent Bash. `python scripts/validate-orion-game.py --ssh debian` joue les 48 missions et vérifie le terminal interactif sur la VM. Le même contrôle tourne sur Linux dans GitHub Actions.

Validation sur Debian : `python scripts/validate-bash-on-debian.py` exécute les exemples et les scénarios des solutions dans un espace temporaire, via l'alias `ssh debian`.

```powershell
npm ci
.\publier-les-cours.ps1 -PrepareOnly
```

Voir [le mode de publication](MODE-EMPLOI-PUBLICATION.md).
