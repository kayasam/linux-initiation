# TP 01 — Personnaliser son environnement Bash

> Chapitre associé : `01-shell-et-environnement.md`
> Durée estimée : 45 min

---

## Objectifs

- Savoir où se trouvent les fichiers de configuration Bash
- Comprendre la différence entre alias et fonction
- Créer des alias utiles dans `.bashrc`
- Écrire une fonction shell avec arguments
- Recharger la configuration sans redémarrer le terminal

---

## Partie A — Explorer l'environnement existant (10 min)

**A1.** Affiche le shell configuré pour ton utilisateur, et le shell du processus courant. Sont-ils identiques ?

**A2.** Vérifie si ton shell courant est un login shell ou non.

**A3.** Affiche le contenu de ton `.bashrc` actuel. Repère les sections déjà présentes.

**A4.** Affiche tous les alias déjà définis dans ton environnement.

**A5.** Affiche la liste des shells disponibles sur le système.

---

## Partie B — Redirections et tubes (15 min)

**B1.** Sauvegarde la liste du contenu de `/etc` dans un fichier `/tmp/liste_etc.txt`.

**B2.** Affiche le nombre total de lignes de ce fichier.

**B3.** Affiche uniquement les lignes contenant le mot `conf`, puis compte combien il y en a (deux commandes séparées).

**B4.** Tente de lister un dossier inexistant (`/dossier-inexistant`). Redirige uniquement le message d'erreur vers un fichier `/tmp/erreurs.txt`, puis affiche son contenu.

**B5.** Refais la même commande mais cette fois, jette l'erreur sans la sauvegarder nulle part. Vérifie qu'il ne s'affiche rien à l'écran.

---

## Partie C — Alias et fonctions (20 min)

**C1.** Ouvre ton `.bashrc` dans un éditeur de texte.

**C2.** Ajoute les alias suivants à la fin du fichier :

| Alias | Commande |
|-------|---------|
| `ll` | `ls -lh` |
| `la` | `ls -lha` |
| `..` | `cd ..` |
| `ports` | `ss -tulnp` |
| `myip` | `ip -br a` |
| `maj` | `sudo apt update && sudo apt upgrade` |

**C3.** Toujours dans `.bashrc`, ajoute une fonction `mkcd` qui crée un dossier et s'y déplace directement (en une seule commande).

**C4.** Sauvegarde le fichier et recharge la configuration **sans fermer le terminal**.

**C5.** Teste chacun des alias que tu as créés.

**C6.** Teste la fonction `mkcd` en créant le dossier `/tmp/mon-test`, et vérifie ensuite dans quel dossier tu te trouves.

---

## Bonus

**B+1.** Écris une fonction `compter` qui affiche le nombre d'éléments dans le dossier passé en argument. Teste-la sur `/etc` et `/tmp`.

**B+2.** Que se passe-t-il si tu précèdes une commande aliasée par un `\` (ex: `\rm`) ? Explique pourquoi.

---

## Questions de vérification

À la fin du TP, tu dois être capable de répondre sans regarder le cours :

- [ ] Quel fichier de config est chargé à chaque ouverture de terminal (non-login) ?
- [ ] Quelle commande recharge `.bashrc` dans le shell courant ?
- [ ] Quelle est la différence principale entre un alias et une fonction ?
- [ ] Comment redirige-t-on uniquement les erreurs d'une commande vers un fichier ?
- [ ] Quel opérateur connecte la sortie d'une commande à l'entrée de la suivante ?
