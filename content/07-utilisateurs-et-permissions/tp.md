---
title: "TP 07 — Utilisateurs et permissions"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="07-utilisateurs-et-permissions" style="--resource-count:4"><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" aria-label="Cours — Lire le cours en Markdown" href="https://kayasam.github.io/linux-initiation/07-utilisateurs-et-permissions/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg></span><span class="resource-label">Cours<small>Lire le cours en Markdown</small></span></a><a class="resource-button resource-html" data-resource-kind="html" aria-label="HTML — Explorer le chapitre" href="https://kayasam.github.io/linux-initiation/07-utilisateurs-et-permissions/html/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M2 2h24l-2 25-10 3-10-3Z" fill="#e44d26"/><path d="M14 5v22l7-2 2-20Z" fill="#f16529"/><path d="M7 8h15l-.3 3H11l.3 3h10l-.8 9-6.5 2-6.5-2-.4-5h3l.2 2.6 3.7 1 3.7-1 .3-3.6H8Z" fill="#fff"/></svg></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" aria-label="Quiz — 20 questions" href="https://kayasam.github.io/linux-initiation/07-utilisateurs-et-permissions/quiz/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="4" y="3" width="24" height="26" rx="6" fill="#7652ad"/><path d="M12 12a4 4 0 1 1 6 3.5c-1.5.8-2 1.4-2 3" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/><circle cx="16" cy="23" r="1.6" fill="#fff"/></svg></span><span class="resource-label">Quiz<small>20 questions</small></span></a><a class="resource-button resource-tp" data-resource-kind="tp" aria-label="TP — Mettre en pratique" href="https://kayasam.github.io/linux-initiation/07-utilisateurs-et-permissions/tp"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="resource-label">TP<small>Mettre en pratique</small></span></a></div><div class="resource-actions"><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/tp/tp-07-permissions.md" download aria-label="Télécharger le TP en Markdown">↓ Télécharger le TP (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>


> Durée estimée : 40 min

---

## Objectifs
Comprendre et manipuler les utilisateurs, groupes et permissions.

---

## Partie A — Utilisateurs (15 min)

**A1.** Affiche ton nom d'utilisateur, ton UID et tes groupes.

**A2.** Liste les utilisateurs connectés en ce moment.

**A3.** Affiche les 3 premières lignes de `/etc/passwd`. Identifie les champs (nom, UID, home, shell).

**A4.** Crée un nouvel utilisateur appelé `testuser`. Définis-lui un mot de passe.

**A5.** Connecte-toi en tant que `testuser` avec la commande `su - testuser`. Vérifie dans quel dossier tu es. Quitte avec `exit`.

**A6.** Supprime l'utilisateur `testuser` et son dossier personnel.

---

## Partie B — Permissions (25 min)

**B1.** Dans ton dossier `formation`, crée un fichier `secret.txt` et écris du texte dedans.

**B2.** Affiche ses permissions avec `ls -l`. Lis les droits (propriétaire, groupe, autres).

**B3.** Rends le fichier `secret.txt` accessible en lecture seule pour tout le monde.
> Indice : `chmod 444`

**B4.** Essaie d'écrire dedans avec `echo`. Que se passe-t-il ?

**B5.** Redonne-toi le droit d'écriture en mode symbolique.

**B6.** Crée un fichier `script.sh` contenant `echo "Bonjour !"`. Rends-le exécutable et exécute-le.

**B7.** Crée un dossier `prive` avec les permissions `700`. Vérifie qu'un autre utilisateur n'y a pas accès.

**Bonus.** Change le propriétaire de `notes.txt` vers `root` (avec `sudo`). Qu'est-ce que ça change pour toi ?

[← Revenir au cours](https://kayasam.github.io/linux-initiation/07-utilisateurs-et-permissions/)

<a href="https://kayasam.github.io/linux-initiation/telechargements/tp/tp-07-permissions.md" download>Télécharger ce TP en Markdown</a>
