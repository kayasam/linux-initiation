# Publier Linux — Initiation

Les modifications des cours se font dans `Formations/linux-initiation` du coffre Obsidian. Les dix chapitres sont conservés dans leur ordre d’origine, chacun dans `cours/NN-sujet/`, avec le Markdown, le HTML, le quiz et son sous-dossier `tp/`. Les notes de session restent dans `sessions/`.

Les six corrections existantes possèdent la propriété `publier: false` (case décochée). Elles sont exclues du site et du ZIP. Pour en diffuser une plus tard, cocher cette propriété (`publier: true`) puis lancer la publication. Le contrôle de l’archive utilise la liste des corrections explicitement autorisées dans `publication-policy.json`, régénérée depuis le coffre à chaque préparation. Une propriété absente n’autorise pas la publication d’une correction.

Double-cliquer sur **Publier les cours.cmd**, puis saisir un message et confirmer la publication. Le script prépare les cours, les quiz, les téléchargements et l’archive, construit Quartz, vérifie les liens et propose l’envoi vers GitHub.

Pour vérifier sans publier : `./publier-les-cours.ps1 -PrepareOnly`.

Le dossier `content` est régénéré : ne pas y faire de modifications durables. Les quiz comprennent 20 questions chacun. Les questions de départ sont dans `site-content/assets/quiz/quiz-questions.json`, les compléments dans `questions-complementaires.txt`. Chaque ligne complémentaire contient la question, quatre réponses (la première est correcte) et l’explication, séparées par `§`.

Le générateur équilibre la banque (5 A, 5 B, 5 C, 5 D). Le moteur remélange les questions, les distracteurs et les positions des bonnes réponses à chaque tentative en conservant exactement cette répartition. Les contrôles vérifient 1 000 tentatives, les scores et le redémarrage.

Les thèmes HTML sont dans `site-content/assets/themes`. Le bouton clair/sombre mémorise le choix avec la même préférence que Quartz. Les quiz intégrés et les supports Obsidian utilisent ces mêmes thèmes et banques de questions.

Les dix schémas SVG sont dans `Formations/linux-initiation/Ressources/images` du coffre. Les liens restent locaux dans le coffre et dans le ZIP ; la publication copie automatiquement les images pour le site et les HTML. Pour régénérer les dessins et intégrer les illustrations manquantes : `python scripts/illustrate-linux.py`. Leur source graphique est dans ce script ; il conserve les blocs déjà présents dans les cours.

Le chapitre 01 enrichi utilise le Markdown du coffre comme source pour son HTML : après modification, lancer `python scripts/render-introduction.py` (module Python `Markdown` nécessaire), puis la préparation habituelle. Ce script régénère aussi le schéma Unix / GNU / Linux. La vidéo YouTube reste en ligne et nécessite Internet, même dans le support hors ligne.

Pour mettre également à jour les versions HTML originales du coffre après préparation :

```powershell
python scripts/finalize-html-supports.py --sync-source "C:/Users/kayaw/Nextcloud/Obsidian/CoffreSam/Formations/linux-initiation"
```

Site : https://kayasam.github.io/linux-initiation/
