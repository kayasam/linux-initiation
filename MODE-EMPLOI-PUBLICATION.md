# Publier Linux — Initiation

Les modifications des cours se font dans `Formations/linux-initiation` du coffre Obsidian. Les dix chapitres sont conservés dans leur ordre d’origine. Les sept énoncés de TP sont repris depuis `sessions/2026-05`, sans leurs corrections.

Double-cliquer sur **Publier les cours.cmd**, puis saisir un message et confirmer la publication. Le script prépare les cours, les quiz, les téléchargements et l’archive, construit Quartz, vérifie les liens et propose l’envoi vers GitHub.

Pour vérifier sans publier : `./publier-les-cours.ps1 -PrepareOnly`.

Le dossier `content` est régénéré : ne pas y faire de modifications durables. Les quiz sont extraits des versions HTML du coffre. Le moteur et le style des quiz sont dans `site-content/assets/quiz`.

Site : https://kayasam.github.io/linux-initiation/
