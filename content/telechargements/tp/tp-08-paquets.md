# TP 08 — Gestion des paquets

> Durée estimée : 30 min

---

## Objectifs
Installer, rechercher et supprimer des logiciels avec APT.

---

**A1.** Mets à jour la liste des paquets disponibles.

**A2.** Installe le paquet `tree` (affiche l'arborescence en forme d'arbre). Teste-le sur `/etc/apt`.

**A3.** Installe `curl` et `htop`.

**A4.** Cherche un paquet lié à l'édition de texte avec le mot-clé `text editor`.

**A5.** Affiche les détails du paquet `vim` (description, version, taille, dépendances).

**A6.** Installe `vim`. Vérifie qu'il est bien installé.

**A7.** Supprime `vim` mais garde sa configuration.

**A8.** Lance une mise à jour complète du système (liste + paquets).

**A9.** Supprime les paquets devenus inutiles.

**A10.** Liste les 10 premiers paquets installés sur le système.

**Bonus.** Combien de paquets sont installés sur ton système ?
> Indice : `apt list --installed | wc -l`
