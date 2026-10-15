window.linuxQuizBanks = {
  "bash-01-shell-et-environnement": {
    "id": "bash-01-shell-et-environnement",
    "title": "Chapitre 01 — Le shell et son environnement",
    "chapter": "Bash — Chapitre 01",
    "track": "Bash",
    "intro": "Vérifie les notions du cours. Chaque réponse est expliquée.",
    "questions": [
      {
        "theme": "Bash — 01",
        "question": "Quel programme interprète nos commandes dans cette formation ?",
        "choices": [
          "Bash",
          "Le terminal",
          "SSH",
          "Le noyau uniquement"
        ],
        "answer": 0,
        "explanation": "Le terminal affiche les échanges ; Bash interprète les commandes sur Debian."
      },
      {
        "theme": "Bash — 01",
        "question": "Quel est le rôle de SSH ici ?",
        "choices": [
          "Créer automatiquement tous les scripts",
          "Transporter les échanges avec la VM",
          "Remplacer Bash",
          "Afficher seulement des images"
        ],
        "answer": 1,
        "explanation": "SSH relie le poste Windows à la VM distante."
      },
      {
        "theme": "Bash — 01",
        "question": "Que faut-il recopier depuis une ligne commençant par stagiaire@debian:~$ ?",
        "choices": [
          "Toute la ligne avec le signe $",
          "Seulement le signe $",
          "Seulement la commande après l'invite",
          "Le nom de la machine uniquement"
        ],
        "answer": 2,
        "explanation": "L'invite indique que le shell attend ; elle ne fait pas partie de la commande."
      },
      {
        "theme": "Bash — 01",
        "question": "Sur la VM Debian du cours, quel programme lance /bin/sh ?",
        "choices": [
          "Bash dans tous les cas",
          "PowerShell",
          "nano",
          "dash"
        ],
        "answer": 3,
        "explanation": "Sur cette VM, /bin/sh est un lien vers dash. Ce choix peut varier selon le système."
      },
      {
        "theme": "Bash — 01",
        "question": "Quelle commande identifie la cible réelle de /bin/sh ?",
        "choices": [
          "readlink -f /bin/sh",
          "cat /bin/sh",
          "mkdir /bin/sh",
          "echo sh"
        ],
        "answer": 0,
        "explanation": "readlink -f suit le lien symbolique jusqu'au programme réel."
      },
      {
        "theme": "Bash — 01",
        "question": "Que renseigne normalement $SHELL ?",
        "choices": [
          "Toujours le processus courant",
          "Le shell de connexion configuré",
          "Le dossier courant",
          "La dernière commande lancée"
        ],
        "answer": 1,
        "explanation": "$SHELL n'est pas automatiquement mise à jour quand on lance un autre interpréteur."
      },
      {
        "theme": "Bash — 01",
        "question": "Que fait bash -c 'echo Bonjour' ?",
        "choices": [
          "Il modifie définitivement le shell de connexion",
          "Il ouvre nano",
          "Un Bash enfant exécute la commande puis se termine",
          "Il installe Bash"
        ],
        "answer": 2,
        "explanation": "-c fournit une chaîne de commandes à un nouveau Bash."
      },
      {
        "theme": "Bash — 01",
        "question": "Le parent est dans /home/stagiaire. Après ( cd /tmp ), où reste-t-il ?",
        "choices": [
          "/tmp",
          "/",
          "Dans aucun dossier",
          "/home/stagiaire"
        ],
        "answer": 3,
        "explanation": "Le cd agit dans le sous-shell créé par les parenthèses ; le parent conserve son dossier."
      },
      {
        "theme": "Bash — 01",
        "question": "Un fichier créé dans un sous-shell disparaît-il à sa fin ?",
        "choices": [
          "Non, l'écriture reste sur le disque",
          "Oui, tous les fichiers sont temporaires",
          "Oui, sauf s'il est exécutable",
          "Oui, sauf avec export"
        ],
        "answer": 0,
        "explanation": "Le sous-shell isole notamment ses variables et son dossier courant, pas le disque."
      },
      {
        "theme": "Bash — 01",
        "question": "Quel élément est une option dans ls -l /tmp ?",
        "choices": [
          "ls",
          "-l",
          "/tmp",
          "Toute la ligne est une seule option"
        ],
        "answer": 1,
        "explanation": "-l demande l'affichage détaillé ; /tmp est l'argument désignant le dossier."
      },
      {
        "theme": "Bash — 01",
        "question": "Que montre pwd ?",
        "choices": [
          "Le mot de passe",
          "Les droits de tous les fichiers",
          "Le dossier courant",
          "La version de Bash"
        ],
        "answer": 2,
        "explanation": "pwd affiche le chemin du dossier où le shell travaille."
      },
      {
        "theme": "Bash — 01",
        "question": "Que désigne ~ dans nos commandes Bash ?",
        "choices": [
          "La racine /",
          "Le dossier /tmp",
          "Le dernier fichier lu",
          "Le dossier personnel"
        ],
        "answer": 3,
        "explanation": "Le tilde est développé par le shell vers le dossier personnel dans ces usages."
      },
      {
        "theme": "Bash — 01",
        "question": "Quel chemin est absolu ?",
        "choices": [
          "/home/stagiaire",
          "messages",
          "../messages",
          "./journal.txt"
        ],
        "answer": 0,
        "explanation": "Un chemin absolu commence par / ; les autres dépendent du dossier courant."
      },
      {
        "theme": "Bash — 01",
        "question": "Que fait cd .. ?",
        "choices": [
          "Il va toujours dans le dossier personnel",
          "Il remonte au dossier parent",
          "Il efface le dossier courant",
          "Il ferme SSH"
        ],
        "answer": 1,
        "explanation": ".. désigne le parent du dossier courant."
      },
      {
        "theme": "Bash — 01",
        "question": "Pourquoi utiliser mkdir -p ~/atelier-bash/decouverte ?",
        "choices": [
          "Demander un mot de passe",
          "Créer obligatoirement un fichier",
          "Créer les parents manquants et accepter un dossier déjà présent",
          "Effacer l'ancien atelier"
        ],
        "answer": 2,
        "explanation": "-p facilite la préparation d'une arborescence, y compris lors d'une relance."
      },
      {
        "theme": "Bash — 01",
        "question": "Que fait echo Bonjour > journal.txt si le fichier existe ?",
        "choices": [
          "Il ajoute une ligne à la fin",
          "Il refuse toujours d'écrire",
          "Il renomme le fichier",
          "Il remplace son contenu"
        ],
        "answer": 3,
        "explanation": "> ouvre le fichier en remplacement avant l'exécution de la commande."
      },
      {
        "theme": "Bash — 01",
        "question": "Quel opérateur ajoute du texte sans remplacer les lignes existantes ?",
        "choices": [
          ">>",
          ">",
          "|",
          "<"
        ],
        "answer": 0,
        "explanation": ">> ouvre la destination en ajout."
      },
      {
        "theme": "Bash — 01",
        "question": "Que fait le tube dans cat journal.txt | grep Radio ?",
        "choices": [
          "Il ajoute Radio au fichier",
          "Il transmet la sortie de cat à grep",
          "Il déplace le fichier",
          "Il lance grep sur Windows"
        ],
        "answer": 1,
        "explanation": "Le tube relie la sortie d'une commande à l'entrée de la suivante."
      },
      {
        "theme": "Bash — 01",
        "question": "Que fait Ctrl+C dans le terminal ?",
        "choices": [
          "Il copie toujours un fichier",
          "Il ferme forcément la VM",
          "Il interrompt normalement la commande en cours",
          "Il efface l'historique"
        ],
        "answer": 2,
        "explanation": "Ctrl+C demande l'interruption du programme au premier plan."
      },
      {
        "theme": "Bash — 01",
        "question": "Quelle aide convient à la commande intégrée cd ?",
        "choices": [
          "cd --install",
          "man --delete cd",
          "echo help > cd",
          "help cd"
        ],
        "answer": 3,
        "explanation": "help explique les commandes intégrées à Bash, comme cd."
      }
    ],
    "chapterLink": "../../01-shell-et-environnement/"
  },
  "bash-02-variables": {
    "id": "bash-02-variables",
    "title": "Chapitre 02 — Les variables",
    "chapter": "Bash — Chapitre 02",
    "track": "Bash",
    "intro": "Vérifie les notions du cours. Chaque réponse est expliquée.",
    "questions": [
      {
        "theme": "Bash — 02",
        "question": "Quelle affectation est correcte ?",
        "choices": [
          "prenom=\"Mila\"",
          "prenom = \"Mila\"",
          "$prenom=\"Mila\"",
          "prenom: \"Mila\""
        ],
        "answer": 0,
        "explanation": "Une affectation Bash ne comporte pas d'espace autour de = et ne préfixe pas le nom par $."
      },
      {
        "theme": "Bash — 02",
        "question": "Comment lire la valeur de prenom comme un seul argument ?",
        "choices": [
          "prenom",
          "\"$prenom\"",
          "'prenom'",
          "=$prenom"
        ],
        "answer": 1,
        "explanation": "$ lit la variable et les guillemets doubles préservent les espaces dans sa valeur."
      },
      {
        "theme": "Bash — 02",
        "question": "Quel nom de variable est valide ?",
        "choices": [
          "2station",
          "nom-station",
          "nom_station",
          "nom station"
        ],
        "answer": 2,
        "explanation": "Le nom utilise notamment des lettres, chiffres et _, sans commencer par un chiffre."
      },
      {
        "theme": "Bash — 02",
        "question": "prenom et PRENOM désignent-ils la même variable ?",
        "choices": [
          "Oui, toujours",
          "Oui, si la valeur est un nombre",
          "Oui, seulement après export",
          "Non, la casse compte"
        ],
        "answer": 3,
        "explanation": "Bash distingue les majuscules des minuscules dans les noms."
      },
      {
        "theme": "Bash — 02",
        "question": "station=\"Orion Nord\". Que produit echo \"$station\" ?",
        "choices": [
          "Orion Nord",
          "$station",
          "station",
          "Orion uniquement"
        ],
        "answer": 0,
        "explanation": "Les doubles guillemets autorisent l'expansion et gardent la valeur groupée."
      },
      {
        "theme": "Bash — 02",
        "question": "station=\"Orion Nord\". Que produit echo '$station' ?",
        "choices": [
          "Orion Nord",
          "$station",
          "Une chaîne vide",
          "Une erreur numérique"
        ],
        "answer": 1,
        "explanation": "Les guillemets simples conservent le texte littéral, sans expansion de variable."
      },
      {
        "theme": "Bash — 02",
        "question": "Pourquoi écrit-on \"${mission}_rapport.txt\" ?",
        "choices": [
          "Pour exporter mission",
          "Pour exécuter rapport.txt",
          "Pour délimiter le nom mission avant le suffixe",
          "Pour faire un calcul"
        ],
        "answer": 2,
        "explanation": "Les accolades évitent de chercher une variable nommée mission_rapport."
      },
      {
        "theme": "Bash — 02",
        "question": "Que fait read -r -p 'Ton prenom : ' prenom ?",
        "choices": [
          "Il lit forcément un fichier nommé prenom",
          "Il exporte prenom",
          "Il transforme le prénom en commande",
          "Il pose une question et range la ligne saisie dans prenom"
        ],
        "answer": 3,
        "explanation": "read attend une ligne ; le dernier mot désigne la variable de destination."
      },
      {
        "theme": "Bash — 02",
        "question": "À quoi sert -r dans read ?",
        "choices": [
          "Conserver les antislashs sans les traiter comme des échappements",
          "Lire le fichier à l'envers",
          "Relancer la VM",
          "Rendre la variable exécutable"
        ],
        "answer": 0,
        "explanation": "-r évite l'interprétation des antislashs par read."
      },
      {
        "theme": "Bash — 02",
        "question": "Après la question de read, pourquoi écrit-on prenom sans $ ?",
        "choices": [
          "On veut afficher le mot prenom",
          "On indique la variable à remplir",
          "$ est interdit dans toutes les commandes",
          "Cela transforme la saisie en nombre"
        ],
        "answer": 1,
        "explanation": "La destination est un nom ; $prenom lirait une valeur déjà présente."
      },
      {
        "theme": "Bash — 02",
        "question": "Que contient machine=$(hostname) ?",
        "choices": [
          "Le texte littéral hostname",
          "Le code de retour de hostname",
          "La sortie de hostname",
          "Le contenu de /etc/shells"
        ],
        "answer": 2,
        "explanation": "$(...) exécute une commande et récupère sa sortie, sans les fins de ligne terminales."
      },
      {
        "theme": "Bash — 02",
        "question": "Quelle différence entre \"$machine\" et $(hostname) ?",
        "choices": [
          "Les deux exécutent hostname",
          "Le premier calcule ; le second lit un fichier",
          "Aucune dans tous les cas",
          "Le premier lit une variable ; le second exécute une commande"
        ],
        "answer": 3,
        "explanation": "Expansion de variable et substitution de commande répondent à deux besoins différents."
      },
      {
        "theme": "Bash — 02",
        "question": "Que donne energie=$((4 * 25)) ?",
        "choices": [
          "100",
          "4 * 25",
          "425",
          "Une valeur aléatoire"
        ],
        "answer": 0,
        "explanation": "$((...)) effectue ici une multiplication entière."
      },
      {
        "theme": "Bash — 02",
        "question": "Que donne $((7 / 2)) dans Bash ?",
        "choices": [
          "3.5",
          "3",
          "4",
          "Une erreur systématique"
        ],
        "answer": 1,
        "explanation": "L'arithmétique de Bash utilise ici des entiers et tronque la division."
      },
      {
        "theme": "Bash — 02",
        "question": "Que donne $((7 % 2)) ?",
        "choices": [
          "3",
          "2",
          "1",
          "7"
        ],
        "answer": 2,
        "explanation": "% calcule le reste de la division entière."
      },
      {
        "theme": "Bash — 02",
        "question": "Que contient normalement HOME ?",
        "choices": [
          "Tous les fichiers de la machine",
          "Le dernier code de retour",
          "La liste des commandes saisies",
          "Le chemin du dossier personnel"
        ],
        "answer": 3,
        "explanation": "HOME est une variable d'environnement fournie au shell."
      },
      {
        "theme": "Bash — 02",
        "question": "À quoi sert PATH ?",
        "choices": [
          "Lister les dossiers où rechercher les commandes sans /",
          "Stocker le dossier courant uniquement",
          "Donner le mot de passe SSH",
          "Énumérer les fichiers ouverts"
        ],
        "answer": 0,
        "explanation": "Quand un nom ne contient pas de /, le shell utilise notamment PATH pour trouver un programme."
      },
      {
        "theme": "Bash — 02",
        "question": "Que change export NOM_STATION=\"Orion\" ?",
        "choices": [
          "Elle devient permanente dans tous les comptes",
          "La variable devient disponible aux programmes enfants lancés ensuite",
          "Elle modifie la variable du shell parent",
          "Elle écrit automatiquement dans .bashrc"
        ],
        "answer": 1,
        "explanation": "export transmet la variable dans l'environnement des futurs processus enfants."
      },
      {
        "theme": "Bash — 02",
        "question": "surnom est vide. Que donne ${surnom:-visiteur} ?",
        "choices": [
          "Une erreur",
          "Le mot surnom",
          "visiteur",
          "La valeur 0"
        ],
        "answer": 2,
        "explanation": ":- fournit la valeur de remplacement si la variable est vide ou absente, sans la remplir automatiquement."
      },
      {
        "theme": "Bash — 02",
        "question": "Dans printf 'Bonjour %s\\n' \"$prenom\", que représente %s ?",
        "choices": [
          "Un nom de fichier",
          "Un calcul en secondes",
          "Une option de read",
          "Un emplacement pour l'argument texte suivant"
        ],
        "answer": 3,
        "explanation": "Le format reste fixe ; %s insère la valeur passée ensuite et \\n ajoute une fin de ligne."
      }
    ],
    "chapterLink": "../../02-variables/"
  },
  "bash-03-bases-du-scripting": {
    "id": "bash-03-bases-du-scripting",
    "title": "Chapitre 03 — Écrire son premier script",
    "chapter": "Bash — Chapitre 03",
    "track": "Bash",
    "intro": "Vérifie les notions du cours. Chaque réponse est expliquée.",
    "questions": [
      {
        "theme": "Bash — 03",
        "question": "Quel est le rôle d'un script shell ?",
        "choices": [
          "Regrouper des commandes dans un fichier",
          "Remplacer le noyau Linux",
          "Stocker uniquement des images",
          "Installer obligatoirement un service"
        ],
        "answer": 0,
        "explanation": "Un script permet de rejouer une suite de commandes et d'y ajouter de la logique."
      },
      {
        "theme": "Bash — 03",
        "question": "À quoi sert #!/bin/bash en première ligne ?",
        "choices": [
          "Afficher le nom du fichier",
          "Choisir Bash pour l'exécution directe",
          "Créer une variable bash",
          "Accorder le droit d'exécution"
        ],
        "answer": 1,
        "explanation": "Le shebang indique l'interpréteur ; il ne remplace pas chmod."
      },
      {
        "theme": "Bash — 03",
        "question": "Avec quel outil du cours peut-on écrire accueil.sh ?",
        "choices": [
          "hostname",
          "whoami",
          "nano",
          "readlink"
        ],
        "answer": 2,
        "explanation": "nano est l'éditeur de texte utilisé pour écrire les premiers scripts."
      },
      {
        "theme": "Bash — 03",
        "question": "Comment enregistrer puis quitter nano dans le cours ?",
        "choices": [
          "Ctrl+C puis supprimer le fichier",
          "Ctrl+L puis Ctrl+D",
          "Tab puis Flèche haut",
          "Ctrl+O, Entrée, puis Ctrl+X"
        ],
        "answer": 3,
        "explanation": "Ctrl+O propose l'enregistrement ; Entrée confirme le nom ; Ctrl+X quitte."
      },
      {
        "theme": "Bash — 03",
        "question": "Que vérifie bash -n accueil.sh ?",
        "choices": [
          "La syntaxe sans exécuter le script",
          "Que toutes les données sont correctes",
          "Que le réseau répond",
          "Que le fichier est exécutable"
        ],
        "answer": 0,
        "explanation": "Un contrôle syntaxique réussi ne garantit pas que le comportement est correct."
      },
      {
        "theme": "Bash — 03",
        "question": "Que fait bash accueil.sh ?",
        "choices": [
          "Le fichier devient automatiquement exécutable",
          "Bash lit et exécute le fichier",
          "Le script s'ouvre dans nano",
          "Le shell change de compte"
        ],
        "answer": 1,
        "explanation": "Lancer explicitement Bash ne nécessite pas le droit d'exécution du fichier, mais le fichier doit être lisible."
      },
      {
        "theme": "Bash — 03",
        "question": "Quel droit ajoute chmod +x accueil.sh ?",
        "choices": [
          "Le droit administrateur",
          "Le droit réseau",
          "Le droit d'exécution",
          "Le droit de changer tous les propriétaires"
        ],
        "answer": 2,
        "explanation": "+x permet l'exécution directe pour les catégories auxquelles la commande l'applique."
      },
      {
        "theme": "Bash — 03",
        "question": "Que signifie ./accueil.sh ?",
        "choices": [
          "Chercher accueil.sh uniquement dans /etc",
          "Ouvrir forcément une nouvelle connexion SSH",
          "Afficher le dossier parent",
          "Exécuter le fichier accueil.sh du dossier courant"
        ],
        "answer": 3,
        "explanation": "./ fournit un chemin explicite vers le fichier dans le dossier courant."
      },
      {
        "theme": "Bash — 03",
        "question": "Un script utilise [[ ... ]]. Quel lancement est adapté au cours ?",
        "choices": [
          "bash script.sh",
          "sh script.sh dans tous les cas",
          "python3 script.sh",
          "cat script.sh uniquement"
        ],
        "answer": 0,
        "explanation": "[[ ... ]] est une fonction de Bash ; sh peut être un autre shell comme dash."
      },
      {
        "theme": "Bash — 03",
        "question": "Que désigne $1 dans un script ?",
        "choices": [
          "Le nombre de fichiers dans le dossier",
          "Le premier argument",
          "Le code de retour",
          "Le dossier personnel"
        ],
        "answer": 1,
        "explanation": "Les paramètres positionnels contiennent les arguments du lancement."
      },
      {
        "theme": "Bash — 03",
        "question": "Que désigne $# ?",
        "choices": [
          "Le dernier argument",
          "Le nombre de lignes du script",
          "Le nombre d'arguments",
          "La valeur de PATH"
        ],
        "answer": 2,
        "explanation": "Le shell fournit $# pour compter les arguments reçus."
      },
      {
        "theme": "Bash — 03",
        "question": "./arguments.sh \"Mila Vega\" pilote reçoit combien d'arguments ?",
        "choices": [
          "3",
          "1",
          "0",
          "2"
        ],
        "answer": 3,
        "explanation": "Les guillemets regroupent Mila Vega en un seul argument, suivi de pilote."
      },
      {
        "theme": "Bash — 03",
        "question": "Pourquoi parcourir les arguments avec \"$@\" ?",
        "choices": [
          "Préserver chaque argument, y compris ses espaces",
          "Fusionner tous les arguments sans séparation",
          "Ne lire que le premier argument",
          "Remplacer les arguments par PATH"
        ],
        "answer": 0,
        "explanation": "\"$@\" développe les arguments séparément en conservant leurs limites."
      },
      {
        "theme": "Bash — 03",
        "question": "Que signifie ${1:-visiteur} ?",
        "choices": [
          "Toujours remplacer le premier argument",
          "Utiliser visiteur si le premier argument est absent ou vide",
          "Refuser tous les visiteurs",
          "Créer un dossier visiteur"
        ],
        "answer": 1,
        "explanation": "Le remplacement donne une valeur par défaut sans demander d'autre saisie."
      },
      {
        "theme": "Bash — 03",
        "question": "Un script termine avec exit 2. Quelle valeur le parent lit-il immédiatement dans $? ?",
        "choices": [
          "0",
          "1 obligatoirement",
          "2",
          "Le nombre d'arguments"
        ],
        "answer": 2,
        "explanation": "exit transmet le code choisi au processus appelant."
      },
      {
        "theme": "Bash — 03",
        "question": "Quel code indique habituellement le succès d'une commande ?",
        "choices": [
          "1",
          "2",
          "255",
          "0"
        ],
        "answer": 3,
        "explanation": "La convention shell utilise 0 pour le succès et une valeur non nulle pour un échec ou un autre état."
      },
      {
        "theme": "Bash — 03",
        "question": "Pourquoi lire $? immédiatement ?",
        "choices": [
          "Une autre commande peut le remplacer",
          "Il disparaît après une seconde",
          "Il nécessite sudo",
          "Il contient toujours une chaîne vide"
        ],
        "answer": 0,
        "explanation": "$? correspond à la dernière commande terminée, pas à une commande plus ancienne."
      },
      {
        "theme": "Bash — 03",
        "question": "Que montre bash -x accueil.sh Mila ?",
        "choices": [
          "Uniquement les commentaires",
          "Une trace des commandes exécutées après expansion",
          "La syntaxe sans lancement",
          "Une liste des permissions SSH"
        ],
        "answer": 1,
        "explanation": "-x aide à suivre les valeurs et les commandes réellement exécutées."
      },
      {
        "theme": "Bash — 03",
        "question": "Que fait 2> /dev/null dans l'exemple de ls en échec ?",
        "choices": [
          "Il force le code 0",
          "Il supprime le dossier recherché",
          "Il masque la sortie d'erreur sans transformer l'échec en succès",
          "Il masque uniquement les sorties normales"
        ],
        "answer": 2,
        "explanation": "2 désigne la sortie d'erreur ; le code de retour reste disponible dans $?."
      },
      {
        "theme": "Bash — 03",
        "question": "Pourquoi conserver les fins de ligne LF pour un script Linux ?",
        "choices": [
          "Rendre le script automatiquement plus rapide",
          "Accorder le droit d'exécution",
          "Changer le nombre d'arguments",
          "Éviter les caractères CR parasites des fins de ligne Windows"
        ],
        "answer": 3,
        "explanation": "Des fins de ligne CRLF peuvent notamment perturber le shebang et certaines lignes de commande."
      }
    ],
    "chapterLink": "../../03-bases-du-scripting/"
  },
  "bash-04-tests-et-conditions": {
    "id": "bash-04-tests-et-conditions",
    "title": "Chapitre 04 — Les tests et les conditions",
    "chapter": "Bash — Chapitre 04",
    "track": "Bash",
    "intro": "Vérifie les notions du cours. Chaque réponse est expliquée.",
    "questions": [
      {
        "theme": "Bash — 04",
        "question": "Quel mot ferme un bloc if dans Bash ?",
        "choices": [
          "fi",
          "endif",
          "done",
          "esac"
        ],
        "answer": 0,
        "explanation": "if se termine par fi ; done ferme une boucle et esac ferme case."
      },
      {
        "theme": "Bash — 04",
        "question": "Dans if commande; then ..., quelle situation lance la branche then ?",
        "choices": [
          "La commande affiche du texte",
          "La commande renvoie 0",
          "La commande renvoie toujours 1",
          "Le fichier est obligatoirement vide"
        ],
        "answer": 1,
        "explanation": "if teste le code de retour, pas la présence de texte affiché."
      },
      {
        "theme": "Bash — 04",
        "question": "À quoi sert elif ?",
        "choices": [
          "Lancer une boucle infinie",
          "Terminer le script sans code",
          "Tester une autre condition si les précédentes sont fausses",
          "Définir une variable d'environnement"
        ],
        "answer": 2,
        "explanation": "elif permet de chaîner des branches conditionnelles."
      },
      {
        "theme": "Bash — 04",
        "question": "Quel opérateur signifie « inférieur à » pour les comparaisons entières du cours ?",
        "choices": [
          "-gt",
          "-eq",
          "-ne",
          "-lt"
        ],
        "answer": 3,
        "explanation": "-lt signifie less than, donc strictement inférieur."
      },
      {
        "theme": "Bash — 04",
        "question": "Quel opérateur teste l'égalité entre deux entiers ?",
        "choices": [
          "-eq",
          "-lt",
          "-gt",
          "-f"
        ],
        "answer": 0,
        "explanation": "-eq compare les valeurs numériques ; -f teste un fichier."
      },
      {
        "theme": "Bash — 04",
        "question": "Énergie : moins de 20 = faible, moins de 80 = correcte, sinon excellente. Que vaut 20 ?",
        "choices": [
          "Faible",
          "Correcte",
          "Excellente",
          "Aucune branche"
        ],
        "answer": 1,
        "explanation": "20 n'est pas inférieur à 20, mais est inférieur à 80."
      },
      {
        "theme": "Bash — 04",
        "question": "Quel test reconnaît une chaîne vide dans le cours ?",
        "choices": [
          "[[ -f \"$nom\" ]]",
          "[[ -d \"$nom\" ]]",
          "[[ -z \"$nom\" ]]",
          "[[ -r \"$nom\" ]]"
        ],
        "answer": 2,
        "explanation": "-z teste une longueur de chaîne nulle."
      },
      {
        "theme": "Bash — 04",
        "question": "Que teste [[ -f \"$chemin\" ]] ?",
        "choices": [
          "N'importe quel dossier",
          "Une variable exportée",
          "Une connexion ouverte",
          "Un fichier régulier"
        ],
        "answer": 3,
        "explanation": "Un dossier ne satisfait pas -f ; le test suit normalement un lien symbolique vers sa cible."
      },
      {
        "theme": "Bash — 04",
        "question": "Que teste [[ -d \"$chemin\" ]] ?",
        "choices": [
          "Un dossier",
          "Un nombre décimal",
          "Un script Bash uniquement",
          "Une chaîne vide"
        ],
        "answer": 0,
        "explanation": "-d vérifie que le chemin correspond à un répertoire."
      },
      {
        "theme": "Bash — 04",
        "question": "Que teste [[ -r \"$chemin\" ]] ?",
        "choices": [
          "Le droit de renommer",
          "L'accessibilité en lecture",
          "L'exécution obligatoire",
          "La présence d'un mot de passe"
        ],
        "answer": 1,
        "explanation": "-r vérifie la permission de lecture pour le contexte du processus."
      },
      {
        "theme": "Bash — 04",
        "question": "Pourquoi mettre une garde au début d'un script ?",
        "choices": [
          "Faire fonctionner toutes les erreurs silencieusement",
          "Supprimer les arguments inutiles",
          "Arrêter tôt un cas invalide avec une explication",
          "Éviter toute condition ensuite"
        ],
        "answer": 2,
        "explanation": "Les gardes rendent le déroulement normal plus clair en traitant d'abord les entrées invalides."
      },
      {
        "theme": "Bash — 04",
        "question": "Que signifie ! dans if ! commande; then ... ?",
        "choices": [
          "Exécuter en administrateur",
          "Répéter la commande",
          "Masquer forcément toutes les erreurs",
          "Inverser le succès ou l'échec testé"
        ],
        "answer": 3,
        "explanation": "La branche then est alors choisie si la commande échoue."
      },
      {
        "theme": "Bash — 04",
        "question": "Pourquoi utiliser grep -qx 'ORION-OK' billet.txt ?",
        "choices": [
          "Tester silencieusement une ligne exactement égale au texte",
          "Rechercher seulement une partie du mot",
          "Ajouter un code au billet",
          "Chiffrer le billet"
        ],
        "answer": 0,
        "explanation": "-q coupe l'affichage et -x exige une correspondance sur la ligne entière."
      },
      {
        "theme": "Bash — 04",
        "question": "Un billet contient uniquement PAS-ORION-OK. Le test grep -qx ORION-OK réussit-il ?",
        "choices": [
          "Oui, car le texte est inclus",
          "Non",
          "Oui, si le fichier finit par .txt",
          "Oui, avec n'importe quel shell"
        ],
        "answer": 1,
        "explanation": "La ligne entière doit être ORION-OK ; une sous-chaîne ne suffit pas."
      },
      {
        "theme": "Bash — 04",
        "question": "Que fait echo 'Erreur' >&2 ?",
        "choices": [
          "Il crée un fichier nommé 2",
          "Il renvoie automatiquement le code 2",
          "Il envoie le message sur la sortie d'erreur",
          "Il modifie le deuxième argument"
        ],
        "answer": 2,
        "explanation": "La redirection de sortie et le code de retour sont deux mécanismes différents."
      },
      {
        "theme": "Bash — 04",
        "question": "Que signifie exit 2 dans controle.sh du cours ?",
        "choices": [
          "Une définition universelle de toutes les erreurs Linux",
          "Attendre deux secondes",
          "Lire deux fichiers",
          "Signaler une erreur d'utilisation ou de fichier selon notre convention"
        ],
        "answer": 3,
        "explanation": "Le script choisit et documente ses codes ; la valeur 2 n'a pas un sens unique pour tous les programmes."
      },
      {
        "theme": "Bash — 04",
        "question": "Quel bloc est adapté pour choisir entre radio, reserve et quitter ?",
        "choices": [
          "case",
          "for uniquement",
          "export",
          "printf uniquement"
        ],
        "answer": 0,
        "explanation": "case organise clairement plusieurs choix nommés."
      },
      {
        "theme": "Bash — 04",
        "question": "Quel est le rôle de *) dans case ?",
        "choices": [
          "Accepter seulement le caractère étoile",
          "Traiter les valeurs qui n'ont pas correspondu aux cas précédents",
          "Compter les arguments",
          "Répéter le premier cas"
        ],
        "answer": 1,
        "explanation": "* est un motif général, souvent utilisé pour le cas par défaut."
      },
      {
        "theme": "Bash — 04",
        "question": "Quand la commande B s'exécute-t-elle dans A && B ?",
        "choices": [
          "Si A échoue uniquement",
          "Toujours en parallèle",
          "Si A réussit",
          "Avant A"
        ],
        "answer": 2,
        "explanation": "&& chaîne une commande suivante après un succès."
      },
      {
        "theme": "Bash — 04",
        "question": "Quand la commande B s'exécute-t-elle dans A || B ?",
        "choices": [
          "Si A réussit uniquement",
          "Toujours avant A",
          "Seulement si A affiche du texte",
          "Si A échoue"
        ],
        "answer": 3,
        "explanation": "|| permet notamment de gérer un échec, selon le code de retour de A."
      }
    ],
    "chapterLink": "../../04-tests-et-conditions/"
  },
  "bash-05-boucles": {
    "id": "bash-05-boucles",
    "title": "Chapitre 05 — Les boucles",
    "chapter": "Bash — Chapitre 05",
    "track": "Bash",
    "intro": "Vérifie les notions du cours. Chaque réponse est expliquée.",
    "questions": [
      {
        "theme": "Bash — 05",
        "question": "Quel est le rôle d'une boucle for ?",
        "choices": [
          "Répéter une action pour chaque élément d'une liste",
          "Exécuter seulement le dernier élément",
          "Changer les droits de tous les fichiers",
          "Créer une variable permanente"
        ],
        "answer": 0,
        "explanation": "for associe successivement chaque élément à sa variable de boucle."
      },
      {
        "theme": "Bash — 05",
        "question": "Quel mot ferme les boucles for et while ?",
        "choices": [
          "fi",
          "done",
          "esac",
          "stop"
        ],
        "answer": 1,
        "explanation": "do ouvre le corps de la boucle et done le termine."
      },
      {
        "theme": "Bash — 05",
        "question": "Combien de passages fait for nom in Mila Noe Sami ?",
        "choices": [
          "1",
          "2",
          "3",
          "4"
        ],
        "answer": 2,
        "explanation": "La liste contient trois éléments distincts."
      },
      {
        "theme": "Bash — 05",
        "question": "Pourquoi écrire for nom in \"Mila Vega\" Noe ?",
        "choices": [
          "Empêcher toute lecture de nom",
          "Exécuter Vega comme commande",
          "Transformer les noms en fichiers",
          "Garder Mila Vega comme un seul élément"
        ],
        "answer": 3,
        "explanation": "Les guillemets regroupent les mots du premier élément."
      },
      {
        "theme": "Bash — 05",
        "question": "Que signifie messages/*.txt ?",
        "choices": [
          "Un motif développé vers les noms finissant par .txt",
          "Uniquement un fichier littéralement nommé *.txt",
          "Tous les fichiers du système",
          "Seulement les scripts exécutables"
        ],
        "answer": 0,
        "explanation": "Le shell développe le glob à partir du dossier indiqué."
      },
      {
        "theme": "Bash — 05",
        "question": "Dans for fichier in messages/*.txt, pourquoi utiliser ensuite \"$fichier\" ?",
        "choices": [
          "Développer une deuxième fois toutes les variables",
          "Préserver chaque nom, y compris les espaces",
          "Supprimer l'extension",
          "Éviter la création du compteur"
        ],
        "answer": 1,
        "explanation": "Le développement du glob fournit les noms ; les guillemets protègent leur utilisation ultérieure."
      },
      {
        "theme": "Bash — 05",
        "question": "Pourquoi placer [[ -f \"$fichier\" ]] || continue dans la boucle ?",
        "choices": [
          "Arrêter toute la boucle au premier fichier",
          "Supprimer les fichiers vides",
          "Écarter les dossiers et les motifs sans fichier correspondant",
          "Renommer les noms composés"
        ],
        "answer": 2,
        "explanation": "-f garde les fichiers réguliers ; continue saute le passage courant."
      },
      {
        "theme": "Bash — 05",
        "question": "Le dossier ne contient aucun .txt et Bash utilise son comportement par défaut. Pourquoi le test -f aide-t-il ?",
        "choices": [
          "Le motif efface le dossier",
          "Le motif devient forcément /tmp",
          "Le motif ajoute automatiquement un fichier",
          "Le motif peut rester littéral et le test le refuse"
        ],
        "answer": 3,
        "explanation": "Sans option particulière, un glob sans correspondance peut rester inchangé ; -f évite de le traiter comme un vrai fichier."
      },
      {
        "theme": "Bash — 05",
        "question": "Où initialise-t-on normalement un compteur de fichiers ?",
        "choices": [
          "Avant la boucle",
          "À chaque passage avec la valeur 0",
          "Uniquement après l'affichage final",
          "Dans le shebang"
        ],
        "answer": 0,
        "explanation": "Une initialisation à chaque tour perdrait le cumul des passages précédents."
      },
      {
        "theme": "Bash — 05",
        "question": "Comment augmenter nombre de 1 ?",
        "choices": [
          "nombre=\"nombre + 1\"",
          "nombre=$((nombre + 1))",
          "nombre + 1",
          "export nombre+1"
        ],
        "answer": 1,
        "explanation": "L'expansion arithmétique calcule la nouvelle valeur avant l'affectation."
      },
      {
        "theme": "Bash — 05",
        "question": "Quand while [[ \"$compteur\" -gt 0 ]] continue-t-elle ?",
        "choices": [
          "Uniquement si compteur vaut 0",
          "Un nombre de fois toujours fixé à 10",
          "Tant que compteur est strictement positif",
          "Tant que compteur est négatif"
        ],
        "answer": 2,
        "explanation": "while réévalue sa condition avant chaque passage."
      },
      {
        "theme": "Bash — 05",
        "question": "Pourquoi décrémenter le compte à rebours dans son corps ?",
        "choices": [
          "Pour rendre le fichier exécutable",
          "Pour changer d'utilisateur",
          "Pour fermer nano",
          "Pour que la condition finisse par devenir fausse"
        ],
        "answer": 3,
        "explanation": "La boucle doit progresser vers sa condition d'arrêt."
      },
      {
        "theme": "Bash — 05",
        "question": "Que fait continue ?",
        "choices": [
          "Passer au tour suivant de la boucle",
          "Quitter forcément tout le script",
          "Relancer SSH",
          "Renvoyer automatiquement 0 au parent"
        ],
        "answer": 0,
        "explanation": "continue saute le reste du corps du passage courant."
      },
      {
        "theme": "Bash — 05",
        "question": "Que fait break ?",
        "choices": [
          "Continuer au tour suivant",
          "Quitter la boucle en cours",
          "Fermer forcément le terminal",
          "Supprimer la variable de boucle"
        ],
        "answer": 1,
        "explanation": "Après break, le script poursuit après la boucle, sauf instruction de sortie distincte."
      },
      {
        "theme": "Bash — 05",
        "question": "Pourquoi lire l'équipage avec while IFS= read -r personne ?",
        "choices": [
          "Découper forcément les noms sur les espaces",
          "Lire uniquement le dernier mot",
          "Conserver les espaces et les antislashs des lignes",
          "Exécuter chaque nom comme commande"
        ],
        "answer": 2,
        "explanation": "IFS= évite de retirer les séparateurs de bord ; -r conserve les antislashs."
      },
      {
        "theme": "Bash — 05",
        "question": "Quel opérateur fournit un fichier en entrée à une boucle de lecture ?",
        "choices": [
          ">",
          ">>",
          "&&",
          "<"
        ],
        "answer": 3,
        "explanation": "done < fichier.txt fait lire le contenu sur l'entrée de la boucle."
      },
      {
        "theme": "Bash — 05",
        "question": "Une dernière ligne sans fin de ligne est-elle toujours traitée par un simple while read ?",
        "choices": [
          "Non, il faut traiter ce cas si on veut la conserver",
          "Oui, read renvoie toujours un succès",
          "Non, Bash refuse tout le fichier",
          "Oui, si le fichier est exécutable"
        ],
        "answer": 0,
        "explanation": "read peut fournir le texte tout en renvoyant un échec à la fin du fichier ; un test complémentaire permet de garder cette dernière ligne."
      },
      {
        "theme": "Bash — 05",
        "question": "Pourquoi mkdir -p facilite-t-il une relance du script de copie ?",
        "choices": [
          "Il supprime toutes les copies",
          "Il accepte le dossier de copies déjà présent",
          "Il transforme les dossiers en fichiers",
          "Il empêche les noms avec espaces"
        ],
        "answer": 1,
        "explanation": "Le script peut préparer sa destination à chaque lancement."
      },
      {
        "theme": "Bash — 05",
        "question": "Le script copie un fichier vers le même nom déjà présent. S'agit-il d'une sauvegarde versionnée ?",
        "choices": [
          "Oui, cp crée toujours une version datée",
          "Oui, si on utilise for",
          "Non, la copie précédente peut être remplacée",
          "Oui, si le nom finit par .txt"
        ],
        "answer": 2,
        "explanation": "Pour conserver plusieurs versions, il faudrait prévoir des noms ou dossiers distincts."
      },
      {
        "theme": "Bash — 05",
        "question": "À quoi sert local dans une fonction Bash ?",
        "choices": [
          "Créer un compte local",
          "Exporter vers tous les scripts",
          "Écrire automatiquement dans un fichier",
          "Limiter une variable au contexte de cette fonction"
        ],
        "answer": 3,
        "explanation": "local aide à éviter de modifier involontairement une variable du contexte appelant."
      }
    ],
    "chapterLink": "../../05-boucles/"
  },
  "bash-06-sed-et-awk": {
    "id": "bash-06-sed-et-awk",
    "title": "Chapitre 06 — Traiter du texte avec sed et awk",
    "chapter": "Bash — Chapitre 06",
    "track": "Bash",
    "intro": "Vérifie les notions du cours. Chaque réponse est expliquée.",
    "questions": [
      {
        "theme": "Bash — 06",
        "question": "Quel programme du cours effectue des substitutions de texte simples ?",
        "choices": [
          "sed",
          "chmod",
          "whoami",
          "mkdir"
        ],
        "answer": 0,
        "explanation": "sed applique notamment des transformations ligne par ligne."
      },
      {
        "theme": "Bash — 06",
        "question": "Que fait sed 's/informatique/IT/' stock.csv sans -i ?",
        "choices": [
          "Il écrase forcément stock.csv",
          "Il affiche une version transformée sans modifier stock.csv",
          "Il efface les lignes contenant informatique",
          "Il change les permissions"
        ],
        "answer": 1,
        "explanation": "Sans édition en place, sed écrit le résultat sur sa sortie."
      },
      {
        "theme": "Bash — 06",
        "question": "Comment garder le résultat transformé dans un autre fichier ?",
        "choices": [
          "Rediriger vers le fichier source lui-même",
          "Utiliser chmod +x",
          "Rediriger vers un nouveau nom avec >",
          "Supprimer d'abord le dossier"
        ],
        "answer": 2,
        "explanation": "La destination doit être distincte du fichier d'entrée pour préserver les données."
      },
      {
        "theme": "Bash — 06",
        "question": "Pourquoi sed 's/a/b/' fichier > fichier est-il dangereux pour les données ?",
        "choices": [
          "sed refuse toujours cette syntaxe",
          "Le fichier devient exécutable",
          "Le shell écrit forcément une copie .bak",
          "Le shell vide la destination avant que sed lise la source"
        ],
        "answer": 3,
        "explanation": "L'ouverture en remplacement par > se produit avant le démarrage du programme."
      },
      {
        "theme": "Bash — 06",
        "question": "Sans indicateur g, combien de correspondances s/ancien/nouveau/ remplace-t-il par ligne ?",
        "choices": [
          "La première",
          "Toutes",
          "Aucune",
          "Uniquement la dernière"
        ],
        "answer": 0,
        "explanation": "Le suffixe g demanderait un remplacement global dans chaque ligne."
      },
      {
        "theme": "Bash — 06",
        "question": "Que fait sed -n '2,3p' stock.csv ?",
        "choices": [
          "Afficher les colonnes 2 et 3",
          "Afficher seulement les lignes 2 et 3",
          "Supprimer les lignes 2 et 3",
          "Créer trois fichiers"
        ],
        "answer": 1,
        "explanation": "-n coupe l'affichage automatique ; p imprime la plage choisie."
      },
      {
        "theme": "Bash — 06",
        "question": "Que fait sed '1d' stock.csv sans -i ?",
        "choices": [
          "Effacer définitivement tout le fichier",
          "Afficher seulement la première colonne",
          "Afficher le contenu sans la première ligne",
          "Trier les quantités"
        ],
        "answer": 2,
        "explanation": "d retire la ligne du flux de sortie, sans modifier le fichier source dans cet usage."
      },
      {
        "theme": "Bash — 06",
        "question": "À quoi sert -F ';' dans awk ?",
        "choices": [
          "Remplacer chaque ; par un espace dans le fichier",
          "Ignorer toutes les lignes",
          "Ouvrir un fichier en ajout",
          "Choisir le séparateur de champs"
        ],
        "answer": 3,
        "explanation": "Le séparateur permet à awk de repérer les colonnes du fichier."
      },
      {
        "theme": "Bash — 06",
        "question": "Que désigne $1 dans un programme awk ?",
        "choices": [
          "Le premier champ de la ligne courante",
          "Le premier argument du script Bash dans tous les cas",
          "Le code de retour de sed",
          "Le nombre de lignes"
        ],
        "answer": 0,
        "explanation": "Le sens de $1 dépend du langage : dans awk, c'est un champ de la ligne."
      },
      {
        "theme": "Bash — 06",
        "question": "Que représente NR dans awk ?",
        "choices": [
          "Le nombre de processeurs",
          "Le numéro de l'enregistrement lu",
          "Le prix unitaire",
          "Le dernier argument Bash"
        ],
        "answer": 1,
        "explanation": "Avec les fichiers à lignes de ce cours, NR suit le numéro de ligne depuis le début de la lecture."
      },
      {
        "theme": "Bash — 06",
        "question": "Pourquoi utiliser NR > 1 pour notre inventaire ?",
        "choices": [
          "Ignorer tous les produits",
          "Garder seulement le premier produit",
          "Ignorer la ligne d'en-tête",
          "Trier les catégories"
        ],
        "answer": 2,
        "explanation": "L'en-tête n'est pas une ligne de données à additionner."
      },
      {
        "theme": "Bash — 06",
        "question": "Que produit print $1, $3 dans awk avec la configuration par défaut ?",
        "choices": [
          "Deux fichiers distincts",
          "Un calcul de multiplication",
          "Une ligne séparée obligatoirement par ;",
          "Deux champs séparés par un espace"
        ],
        "answer": 3,
        "explanation": "La virgule sépare les valeurs à afficher ; le séparateur de sortie vaut ici un espace."
      },
      {
        "theme": "Bash — 06",
        "question": "Comment filtrer les produits dont la quantité, en champ 3, est inférieure à 10 ?",
        "choices": [
          "NR > 1 && $3 < 10",
          "NR < 1 && $3 > 10",
          "$1 < 10 uniquement",
          "print 10 > $3"
        ],
        "answer": 0,
        "explanation": "Le filtre exclut l'en-tête et compare le champ de quantité."
      },
      {
        "theme": "Bash — 06",
        "question": "Quel calcul donne la valeur d'une ligne quantité/prix ?",
        "choices": [
          "$3 + $4",
          "$3 * $4",
          "$4 uniquement",
          "NR * $1"
        ],
        "answer": 1,
        "explanation": "Le stock en valeur est la quantité multipliée par le prix unitaire."
      },
      {
        "theme": "Bash — 06",
        "question": "À quoi sert END dans awk ?",
        "choices": [
          "Terminer automatiquement Bash avec 1",
          "Ignorer la dernière ligne",
          "Exécuter une action après la lecture de toutes les lignes",
          "Réinitialiser tous les champs avant chaque ligne"
        ],
        "answer": 2,
        "explanation": "END est adapté à l'affichage d'un total accumulé pendant la lecture."
      },
      {
        "theme": "Bash — 06",
        "question": "Un stock contient 8 claviers, 12 souris, 20 cahiers, 4 écrans et 30 stylos. Quelle quantité totale doit calculer awk ?",
        "choices": [
          "1220",
          "5",
          "10",
          "74"
        ],
        "answer": 3,
        "explanation": "Les quantités 8 + 12 + 20 + 4 + 30 donnent 74 ; on ignore l'en-tête."
      },
      {
        "theme": "Bash — 06",
        "question": "Deux lignes indiquent 8 claviers à 25 et 4 écrans à 180. Quelle valeur totale doit calculer awk ?",
        "choices": [
          "920",
          "1220",
          "205",
          "12"
        ],
        "answer": 0,
        "explanation": "On additionne quantité × prix : 8×25 + 4×180 = 200 + 720 = 920."
      },
      {
        "theme": "Bash — 06",
        "question": "Quantités : clavier 8, souris 12, cahier 20, ecran 4, stylo 30. Quels produits vérifient $3 < 10 ?",
        "choices": [
          "souris et stylo",
          "clavier et ecran",
          "cahier et stylo",
          "Tous les produits"
        ],
        "answer": 1,
        "explanation": "Les quantités du clavier et de l'écran sont 8 et 4 ; les autres sont au moins égales à 10."
      },
      {
        "theme": "Bash — 06",
        "question": "Que fait GNU sed -i.bak sur la copie utilisée dans le bonus ?",
        "choices": [
          "Il modifie seulement l'affichage",
          "Il supprime toutes les sauvegardes",
          "Il modifie la copie en place et conserve une sauvegarde avec .bak",
          "Il crée une archive ZIP"
        ],
        "answer": 2,
        "explanation": "-i.bak conserve le contenu d'avant modification sous un nom suffixé .bak ; le cours l'utilise sur une copie."
      },
      {
        "theme": "Bash — 06",
        "question": "Notre méthode awk -F ';' convient-elle à tous les CSV avec champs entre guillemets et séparateurs inclus ?",
        "choices": [
          "Oui, à tous les CSV sans exception",
          "Oui, si on rend le fichier exécutable",
          "Oui, en ajoutant > au fichier source",
          "Non, elle convient au format simple choisi pour le cours"
        ],
        "answer": 3,
        "explanation": "Un vrai CSV peut nécessiter un lecteur tenant compte des guillemets et des séparateurs à l'intérieur des champs."
      }
    ],
    "chapterLink": "../../06-sed-et-awk/"
  }
}
