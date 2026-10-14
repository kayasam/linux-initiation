---
title: "TP 03"
---

# TP 03 — Bases du scripting

> Chapitre associé : `03-bases-du-scripting.md`
> Durée estimée : 1h

---

## Objectifs

- Créer et exécuter un script bash
- Utiliser le shebang et les options de sécurité
- Récupérer et utiliser les arguments d'un script
- Lire le code de retour d'une commande

---

## Partie A — Premier script (15 min)

**A1.** Crée le répertoire `~/scripting` qui servira de dossier de travail pour tous les TP de scripting.

**A2.** Dans ce dossier, crée un script `bonjour.sh` qui affiche `Bonjour le monde !`.
Le script doit contenir : le shebang, les options de sécurité (`set -euo pipefail`), et la commande d'affichage.

**A3.** Exécute le script avec `bash`, sans lui donner le droit d'exécution.

**A4.** Donne le droit d'exécution au script et exécute-le avec `./`.

**A5.** Essaie de l'exécuter sans le `./` (juste `bonjour.sh`). Que se passe-t-il ? Explique pourquoi.

---

## Partie B — Code de retour (10 min)

**B1.** Exécute `ls /etc` et affiche immédiatement son code de retour.

**B2.** Exécute `ls /dossier-inexistant` et affiche son code de retour. Quelle valeur obtiens-tu ?

**B3.** Crée un script `test-retour.sh` qui :
1. Exécute `ls /etc`
2. Affiche le code de retour
3. Exécute `ls /dossier-inexistant`
4. Affiche le code de retour

Que se passe-t-il avec `set -e` actif quand `ls /dossier-inexistant` échoue ?

**B4.** Modifie le script pour désactiver `-e` juste autour de la commande qui échoue, puis le réactiver.

---

## Partie C — Arguments et variables spéciales (20 min)

**C1.** Crée un script `infos.sh` qui affiche :
- Le nom du script
- Le nombre d'arguments reçus
- Le premier et le deuxième argument
- Tous les arguments d'un coup

Teste-le avec : `./infos.sh Linux Bash Scripting`

**C2.** Crée un script `saluer.sh` qui prend un prénom en argument et affiche `Bonjour, <prénom> !`.
Teste-le avec ton prénom.

**C3.** Améliore `saluer.sh` pour qu'il affiche aussi le nombre d'arguments reçus et le nom du script.

**C4.** Crée un script `afficher-date.sh` qui :
1. Stocke la date du jour (format `AAAA-MM-JJ`) dans une variable
2. Affiche : `Nous sommes le <date>`

---

## Partie D — Script complet (15 min)

**D1.** Crée un script `rapport-systeme.sh` qui affiche les informations suivantes, chacune sur une ligne bien lisible :
- Nom de la machine (`hostname`)
- Utilisateur courant
- Date et heure actuelles
- Répertoire courant
- Espace disque disponible sur `/` (`df -h /`)

Le script doit utiliser le shebang correct et les options de sécurité.

---

## Questions de vérification

- [ ] Quelle est la première ligne obligatoire d'un script bash ?
- [ ] Quelle commande donne le droit d'exécution à un script ?
- [ ] Pourquoi faut-il écrire `./script.sh` et pas juste `script.sh` ?
- [ ] Que font `set -e`, `set -u` et `set -o pipefail` ?
- [ ] Quelle variable contient le code de retour de la dernière commande ?
- [ ] Comment récupère-t-on le premier argument passé à un script ?

---

[← Revenir au cours](https://kayasam.github.io/linux-initiation/bash/03-bases-du-scripting/)

[← Parcours Bash](https://kayasam.github.io/linux-initiation/#bash)

<a href="https://kayasam.github.io/linux-initiation/telechargements/bash/tp/tp-03-bases-du-scripting.md" download>Télécharger le TP en Markdown</a>
