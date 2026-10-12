# TP 02 — Installer la machine virtuelle

> Durée estimée : 1h (guidé par le formateur)

---

## Objectifs
Créer une machine virtuelle sous VirtualBox et installer Debian.

---

## Étape 1 — Créer la VM dans VirtualBox

1. Ouvre VirtualBox → clique sur **Nouvelle**
2. Remplis les champs :
   - **Nom** : `Debian-Formation`
   - **Type** : Linux
   - **Version** : Debian (64-bit)
3. **RAM** : alloue 2 Go (2048 Mo) minimum
4. **Disque** : crée un nouveau disque virtuel de 20 Go (type VDI, dynamique)
5. Clique sur **Finir**

---

## Étape 2 — Configurer le réseau

1. Sélectionne ta VM → **Configuration** → **Réseau**
2. Carte 1 : mode **NAT** ✓ (accès Internet)

---

## Étape 3 — Démarrer l'installation

1. Sélectionne ta VM → **Démarrer**
2. Sélectionne l'ISO Debian fournie par le formateur
3. Au menu de démarrage, choisis **Graphical Install**

---

## Étape 4 — Suivre l'installation

| Étape | Valeur à choisir |
|-------|----------------|
| Langue | Français |
| Pays | France |
| Clavier | Français |
| Nom machine | `debian` |
| Domaine | (laisser vide) |
| Mot de passe root | À ton choix — **note-le !** |
| Nom utilisateur | `stagiaire` |
| Mot de passe | À ton choix — **note-le !** |
| Partitionnement | Assisté — disque entier |
| Schéma | Tout dans une seule partition |
| Miroir | France, deb.debian.org |
| Logiciels | Cocher : **Environnement de bureau Debian** + **Utilitaires standard** |
| GRUB | Oui, sur `/dev/sda` |

---

## Étape 5 — Premier démarrage

1. La VM redémarre automatiquement après l'installation
2. Connecte-toi avec le compte `stagiaire` et ton mot de passe
3. Explore l'interface graphique quelques minutes
4. Ouvre un terminal : **Activités** → taper `terminal`

---

## Vérification finale

Dans le terminal, tape les commandes suivantes et vérifie que tout fonctionne :

```bash
whoami          # doit afficher : stagiaire
hostname        # doit afficher : debian
ping -c 3 8.8.8.8  # doit recevoir des réponses (connexion Internet)
```
