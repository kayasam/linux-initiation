# TP 09 — Redirections et tubes

> Durée estimée : 30 min

---

## Objectifs
Utiliser les redirections et les tubes pour traiter et filtrer des données.

---

**A1.** Sauvegarde la liste du contenu de `/etc` dans un fichier `~/liste_etc.txt`.

**A2.** Affiche le nombre de lignes de ce fichier.

**A3.** Ajoute à la fin de `~/liste_etc.txt` la liste du contenu de `/usr/bin`.

**A4.** Tente de lister un dossier inexistant. Redirige l'erreur vers `~/erreurs.txt`. Affiche le fichier pour vérifier.

**A5.** Cherche toutes les lignes contenant `conf` dans `~/liste_etc.txt`. Compte-les.

**A6.** Affiche les 5 premières lignes de `/etc/passwd`, triées par ordre alphabétique.

**A7.** Affiche uniquement les noms d'utilisateurs (premier champ) de `/etc/passwd`, triés.
> Indice : `cut -d: -f1`

**A8.** Recherche le mot `error` (insensible à la casse) dans `/var/log/syslog`. Affiche seulement les 5 dernières occurrences.

**A9.** Affiche les processus en cours (`ps aux`), filtre ceux qui concernent `bash`, et compte-les.

**Bonus.** Affiche les 3 dossiers les plus lourds dans `/var`, avec leur taille.
