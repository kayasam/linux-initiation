# Publier Linux initiation & Bash

L'accueil propose deux parcours comme le site GLPI/ITIL. Les URL Linux existantes sont conservées ; Bash est publié sous `/bash/` sur le même site. Le script `prepare-linux.py` appelle `prepare-bash.py` pour intégrer les six cours Bash et les neuf énoncés de TP depuis `Formations/linux-scripting-bash`.

Dans le coffre Bash, chaque chapitre est rangé dans `cours/<chapitre>/` avec son Markdown, son HTML et un sous-dossier `tp/` contenant les énoncés et leurs corrections. Les TP transversaux sont dans `tp/synthese/`, `tp/final/` et `tp/bonus/`. Les notes de session restent dans `sessions/`. Sur le site, `/bash/<chapitre>/tp` ouvre l'exercice ou la liste lorsqu'il y en a plusieurs ; chaque exercice possède alors une adresse distincte. Les anciennes URL des TP Bash redirigent vers leur nouvel emplacement. L'archive Bash conserve la même arborescence par chapitre que le coffre.

Les modifications des cours se font dans `Formations/linux-initiation` du coffre Obsidian. Les dix chapitres sont conservés dans leur ordre d’origine, chacun dans `cours/NN-sujet/`, avec le Markdown, le HTML, le quiz et son sous-dossier `tp/`. Les notes de session restent dans `sessions/`.

Pour Linux comme pour Bash, une correction avec `publier: false` (case décochée), ou sans cette propriété, reste exclue du site et du ZIP. Pour la diffuser, cocher `publier: true` puis lancer la publication. Son nom reprend celui de l'énoncé avec le suffixe `-correction.md`. Un lien apparaît depuis le TP ; le corrigé devient également disponible dans les téléchargements et le ZIP. Dans le ZIP, le lien du TP ouvre le fichier local. `publication-policy.json` est régénéré depuis le coffre et contrôle les corrections autorisées. Décocher la propriété retire la correction lors de la prochaine publication, sans retirer les copies déjà téléchargées.

Pour les corrigés Linux et Bash avec réponses dépliables, utiliser le suffixe `-corrigev2.md` (ou le prototype `-Corrigév2.md`) et des blocs Obsidian `> [!success]- Afficher la correction — A1` sous chaque question. Cocher `publier: true` dans la v2 et décocher l'ancien `-correction.md`. Le script refuse deux versions cochées pour le même TP. La v2 remplace l'ancien corrigé sur le site et dans le ZIP ; les anciens fichiers restent dans le coffre.

Double-cliquer sur **Publier les cours.cmd**, puis saisir un message et confirmer la publication. Le script prépare les cours, les quiz, les téléchargements et l’archive, construit Quartz, vérifie les liens et propose l’envoi vers GitHub.

L’accueil propose **un seul PDF complet** à côté des deux ZIP : il réunit les 10 chapitres Linux et les 6 chapitres Bash, avec sommaire et signets. Aucun bouton PDF n’apparaît dans les chapitres. Le PDF est régénéré depuis les mêmes sources que les téléchargements Markdown à chaque publication ; les cours intermédiaires restent locaux et ne sont pas publiés. Un contrôle bloque la publication si le document ne correspond plus à l’un de ses 16 chapitres. Les liens ZIP et PDF portent une version calculée sur leur contenu : un fichier modifié obtient une nouvelle version de téléchargement pour éviter les anciennes copies en cache. Une simple sauvegarde dans Obsidian ne met pas le site à jour : lancer la publication reste nécessaire.

Pour préparer les PDF sur une nouvelle machine, installer une fois les dépendances locales : `python -m pip install --target .pdf-tools -r scripts/requirements-pdf.txt`. Le générateur utilise les polices Arial et Consolas sous Windows, ou DejaVu sous Linux. Les pages de contrôle visuel sont dans `output/pdf/review/` et ne sont pas publiées.

Pour vérifier sans publier : `./publier-les-cours.ps1 -PrepareOnly`.

Les HTML Bash sont des compagnons interactifs conçus à la main, distincts du cours Markdown. Les modifier directement dans le coffre ; la publication copie les fichiers existants et adapte leurs liens, sans les régénérer ni les écraser. Le skill `cours-html-interactif` décrit leur forme. Pour actualiser uniquement les schémas SVG, lancer manuellement `python scripts/render-bash-supports.py` ; cette commande ne modifie aucun HTML.

Les boutons Markdown, HTML, Quiz et TP sont communs aux deux parcours. Leur bandeau est produit par `scripts/course-resources.py` ; les icônes sont dans `site-content/assets/resource-icons`, les styles dans `quartz/styles/course-resources.scss`. Le registre `content/assets/course-resources.json` alimente aussi les boutons de l’explorateur, via `course-resources.inline.ts`. Un chapitre sans TP n’affiche pas ce bouton. Les modifications de ce composant et de ses scripts doivent être commitées avec les supports avant l’envoi sur GitHub.

Le jeu Orion Académie est maintenu dans `Formations/linux-scripting-bash/jeu/` : moteur, missions, lanceur et README. La préparation génère une archive `.tar.gz` reproductible, sa somme SHA-256, la page `/bash/jeu/` et inclut les sources dans le ZIP Bash. Le contrôle de synchronisation vérifie aussi ces fichiers. Avant une évolution du jeu, lancer `python scripts/validate-orion-game.py --ssh debian`. La publication ordinaire reste utilisable sans accès à la VM ; GitHub Actions rejoue également la campagne et les scénarios de terminal sur Linux.

Les six quiz Bash sont rédigés dans `Formations/linux-scripting-bash/Ressources/quiz/bash-questions.json`, vingt questions par chapitre. La préparation crée les pages publiques `/bash/cours/quiz/<chapitre>.html`, les quiz dans chaque dossier de cours du coffre et leurs ressources hors ligne. Les versions HTML intègrent leur quiz en bas de page. Le contrôle commun vérifie 320 questions Linux/Bash, le mélange, les scores, les nouvelles tentatives et les thèmes. Les quiz Bash restent distincts des dix banques Linux.

Pour vérifier les manipulations Bash sur la VM : `python scripts/validate-bash-on-debian.py`. L'alias `ssh debian` doit fonctionner sans demande de mot de passe. La validation isole les exemples dans un dossier temporaire et le retire ensuite ; elle ne touche pas aux services existants. Les étapes de saisie dans nano restent manuelles. Ce contrôle distant est lancé séparément : une VM éteinte n'empêche pas de préparer le site.

La préparation actualise automatiquement les copies générées des quiz et thèmes dans le coffre Linux, puis vérifie la correspondance entre les cours/TP du coffre, les téléchargements et les deux ZIP. Les ZIP sont reproductibles : une seconde exécution sans modification ne change pas les fichiers publiables. La publication ne sélectionne que `content`, `site-content`, `chapters.json` et `publication-policy.json` ; les autres fichiers de travail ne sont pas ajoutés automatiquement au commit.

Après déploiement, vérifier les fichiers réellement servis en ligne avec `python scripts/check-source-sync.py --live`. Ce contrôle compare les 16 cours Markdown, les 17 TP, les 16 versions HTML, les quiz, les logos et les deux ZIP aux contenus préparés depuis le coffre. L'ancien lanceur dans `D:/Projet-git/linux-scripting-bash-web` délègue au même script commun.

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
