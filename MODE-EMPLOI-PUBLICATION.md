# Publier Linux — Initiation

Les modifications des cours se font dans `Formations/linux-initiation` du coffre Obsidian. Les dix chapitres sont conservés dans leur ordre d’origine, chacun dans `cours/NN-sujet/`, avec le Markdown, le HTML, le quiz et son sous-dossier `tp/`. Les notes de session restent dans `sessions/`.

Les six corrections existantes possèdent la propriété `publier: false` (case décochée). Elles sont exclues du site et du ZIP. Pour en diffuser une plus tard, cocher cette propriété (`publier: true`) puis lancer la publication. Le contrôle de l’archive utilise la liste des corrections explicitement autorisées dans `publication-policy.json`, régénérée depuis le coffre à chaque préparation. Une propriété absente n’autorise pas la publication d’une correction.

Double-cliquer sur **Publier les cours.cmd**, puis saisir un message et confirmer la publication. Le script prépare les cours, les quiz, les téléchargements et l’archive, construit Quartz, vérifie les liens et propose l’envoi vers GitHub.

Pour vérifier sans publier : `./publier-les-cours.ps1 -PrepareOnly`.

Le dossier `content` est régénéré : ne pas y faire de modifications durables. Les quiz comprennent 20 questions chacun. Les questions de départ sont dans `site-content/assets/quiz/quiz-questions.json`, les compléments dans `questions-complementaires.txt`. Chaque ligne complémentaire contient la question, quatre réponses (la première est correcte) et l’explication, séparées par `§`.

Le générateur équilibre la banque (5 A, 5 B, 5 C, 5 D). Le moteur remélange les questions, les distracteurs et les positions des bonnes réponses à chaque tentative en conservant exactement cette répartition. Les contrôles vérifient 1 000 tentatives, les scores et le redémarrage.

Les thèmes HTML sont dans `site-content/assets/themes`. Le bouton clair/sombre mémorise le choix avec la même préférence que Quartz. Les quiz intégrés et les supports Obsidian utilisent ces mêmes thèmes et banques de questions.

Les dix schémas SVG sont dans `Formations/linux-initiation/Ressources/images` du coffre. Les liens restent locaux dans le coffre et dans le ZIP ; la publication copie automatiquement les images pour le site et les HTML. Pour régénérer les dessins et intégrer les illustrations manquantes : `python scripts/illustrate-linux.py`. Leur source graphique est dans ce script ; il conserve les blocs déjà présents dans les cours.

Le chapitre 01 possède un compagnon interactif distinct du cours Markdown : onglets, frise illustrée et activités. Son modèle est `templates/introduction-interactive.html`. Après modification de ce modèle, lancer `python scripts/render-introduction.py`, puis la préparation habituelle. Ce script régénère aussi le schéma Unix / GNU / Linux. Les portraits et leurs crédits sont conservés dans `Ressources/images` du coffre et copiés dans le ZIP. La vidéo YouTube nécessite Internet, même dans le support hors ligne.

Le laboratoire du chapitre 07 est dans `templates/permissions-interactive.html`. Pour le mettre à jour dans le coffre : `python scripts/render-permissions.py`, puis la préparation habituelle. Il simule les identités, les permissions et les changements de propriétaire sans exécuter de commandes sur la machine. Aucun SVG n’est intégré dans ce HTML. Les tests `node scripts/check-permissions.mjs` vérifient les 512 modes classiques, la priorité propriétaire/groupe/autres, les droits sur les dossiers et les interactions ; ils sont aussi exécutés lors de la publication.

Pour mettre également à jour les versions HTML originales du coffre après préparation :

```powershell
python scripts/finalize-html-supports.py --sync-source "C:/Users/kayaw/Nextcloud/Obsidian/CoffreSam/Formations/linux-initiation"
```

Site : https://kayasam.github.io/linux-initiation/
