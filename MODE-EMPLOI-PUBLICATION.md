# Publier Linux — Initiation

Les modifications des cours se font dans `Formations/linux-initiation` du coffre Obsidian. Les dix chapitres sont conservés dans leur ordre d’origine. Les sept énoncés de TP sont repris depuis `sessions/2026-05`, sans leurs corrections.

Double-cliquer sur **Publier les cours.cmd**, puis saisir un message et confirmer la publication. Le script prépare les cours, les quiz, les téléchargements et l’archive, construit Quartz, vérifie les liens et propose l’envoi vers GitHub.

Pour vérifier sans publier : `./publier-les-cours.ps1 -PrepareOnly`.

Le dossier `content` est régénéré : ne pas y faire de modifications durables. Les quiz comprennent 20 questions chacun. Les questions de départ sont dans `site-content/assets/quiz/quiz-questions.json`, les compléments dans `questions-complementaires.txt`. Chaque ligne complémentaire contient la question, quatre réponses (la première est correcte) et l’explication, séparées par `§`.

Le générateur équilibre la banque (5 A, 5 B, 5 C, 5 D). Le moteur remélange les questions, les distracteurs et les positions des bonnes réponses à chaque tentative en conservant exactement cette répartition. Les contrôles vérifient 1 000 tentatives, les scores et le redémarrage.

Les thèmes HTML sont dans `site-content/assets/themes`. Le bouton clair/sombre mémorise le choix avec la même préférence que Quartz. Les quiz intégrés et les supports Obsidian utilisent ces mêmes thèmes et banques de questions.

Pour mettre également à jour les versions HTML originales du coffre après préparation :

```powershell
python scripts/finalize-html-supports.py --sync-source "C:/Users/kayaw/Nextcloud/Obsidian/CoffreSam/Formations/linux-initiation"
```

Site : https://kayasam.github.io/linux-initiation/
