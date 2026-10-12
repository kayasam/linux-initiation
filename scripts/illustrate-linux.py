"""Create original, accessible SVG diagrams and insert them into the Obsidian course."""
from pathlib import Path
from html import escape
import argparse
import re

SOURCE = Path('C:/Users/kayaw/Nextcloud/Obsidian/CoffreSam/Formations/linux-initiation')

class Diagram:
    def __init__(self, number, title, subtitle):
        self.parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="600" viewBox="0 0 1000 600" role="img" aria-labelledby="title description">
<title id="title">{escape(title)}</title><desc id="description">{escape(subtitle)}</desc>
<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="4" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0 L8 4 L0 8" fill="#006575" class="arrow-fill"/></marker></defs>
<style>
text {{ font-family:'Segoe UI',Arial,sans-serif; fill:#182d3e; }}
.title {{font-size:28px;font-weight:750}} .subtitle {{font-size:18px;fill:#455d70}}
.label {{font-size:22px;font-weight:700}} .body {{font-size:20px}} .small {{font-size:17px;fill:#455d70}}
.mono {{font-family:Consolas,'DejaVu Sans Mono',monospace;font-size:20px}} .accent {{fill:#006575}}
.box {{fill:#fff;stroke:#8196a6;stroke-width:1.5}} .soft {{fill:#e5f2f4;stroke:#006575;stroke-width:1.5}}
.line {{fill:none;stroke:#006575;stroke-width:2.5;stroke-linecap:round;stroke-linejoin:round}}
@media (prefers-color-scheme:dark) {{
.background {{fill:#101923}} .badge {{fill:#243b4c}} text {{fill:#edf5fb}}
.subtitle,.small {{fill:#b7c9d8}} .accent,.arrow-fill {{fill:#72dfeb}}
.box {{fill:#192936;stroke:#587488}} .soft {{fill:#243b4c;stroke:#72dfeb}} .line {{stroke:#72dfeb}}
}}
</style>
<rect width="1000" height="600" rx="20" fill="#f4f7fa" class="background"/>
<rect x="28" y="26" width="48" height="42" rx="10" fill="#e5f2f4" class="badge"/>
<text x="52" y="54" text-anchor="middle" class="label accent">{number}</text>
<text x="92" y="52" class="title">{escape(title)}</text>
<text x="92" y="82" class="subtitle">{escape(subtitle)}</text>''']
    def rect(self, x,y,w,h,soft=False):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" class="{"soft" if soft else "box"}"/>')
    def text(self,x,y,text,cls='body',anchor='start'):
        self.parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(text)}</text>')
    def box(self,x,y,w,h,title,lines=(),soft=False):
        self.rect(x,y,w,h,soft)
        self.text(x+20,y+34,title,'label')
        for i,line in enumerate(lines): self.text(x+20,y+65+i*27,line,'body')
    def arrow(self,x1,y1,x2,y2):
        self.parts.append(f'<path d="M{x1} {y1} L{x2} {y2}" class="line" marker-end="url(#arrow)"/>')
    def path(self,d): self.parts.append(f'<path d="{d}" class="line"/>')
    def note(self,text): self.text(40,568,text,'small')
    def save(self,path): path.write_text('\n'.join(self.parts)+ '\n</svg>\n',encoding='utf-8')

def create_diagrams(destination):
    diagrams=[]
    d=Diagram('01','Le rôle du système Linux','Des applications au matériel : chaque couche a un rôle.')
    d.box(175,120,650,92,'Applications',['Firefox · LibreOffice · outils du terminal'])
    d.box(175,258,650,112,'Système Linux',['Outils et services + noyau Linux','Le noyau gère notamment mémoire, processeur et périphériques.'],True)
    d.box(175,418,650,92,'Matériel',['Processeur · mémoire vive · disque · carte réseau'])
    d.arrow(500,216,500,252);d.arrow(500,374,500,412)
    d.note('Une distribution réunit le noyau, les outils et les logiciels nécessaires à son utilisation.')
    diagrams.append(('01-systeme-linux',d))

    d=Diagram('02','Comprendre la machine virtuelle','Le système hôte et le système invité sont deux environnements distincts.')
    d.box(40,116,920,405,'PC physique — système hôte',['Windows, Linux ou macOS : il continue de fonctionner.'])
    d.box(80,218,840,270,'VirtualBox — logiciel de virtualisation',[],True)
    d.box(120,278,760,177,'Machine virtuelle — système invité Debian',['Son propre système, ses comptes et ses fichiers','RAM et processeur partagés avec le PC physique','Disque virtuel : un fichier VDI sur le disque de l’hôte'])
    d.note('Pour revenir à un état antérieur : restaurer un instantané créé auparavant. Redémarrer ne suffit pas.')
    diagrams.append(('02-hote-et-machine-virtuelle',d))

    d=Diagram('03','Deux interfaces, les mêmes fichiers','Le bureau et le terminal donnent accès au même système Linux.')
    d.box(55,136,390,135,'Interface graphique',['Fenêtres, icônes et souris','Gestionnaire de fichiers'],True)
    d.box(555,136,390,135,'Terminal',['Commandes saisies au clavier','ls · cd · cat'],True)
    d.box(235,365,530,123,'Un même fichier',['/home/stagiaire/Documents/notes.txt'])
    d.arrow(250,279,380,357);d.arrow(750,279,620,357)
    d.text(500,320,'Deux façons de lire ou modifier le document','small','middle')
    d.note('Un document créé dans le gestionnaire de fichiers peut aussi être manipulé en ligne de commande.')
    diagrams.append(('03-bureau-et-terminal',d))

    d=Diagram('04','Se repérer dans les chemins','Le chemin absolu part de / ; le chemin relatif part de votre position actuelle.')
    for x,y,w,title in [(55,126,180,'/'),(95,212,180,'home'),(135,298,210,'stagiaire'),(175,414,220,'formation')]:
        d.box(x,y,w,65,title,soft=title=='stagiaire')
    d.path('M75 191 V244 H89 M115 277 V330 H129 M155 363 V446 H169')
    d.text(155,392,'Vous êtes ici : /home/stagiaire','small')
    d.box(460,145,485,112,'Chemin absolu',['cd /home/stagiaire/formation'])
    d.box(460,290,485,112,'Chemin relatif depuis stagiaire',['cd formation'],True)
    d.text(480,449,'cd .. → remonte au dossier parent','mono')
    d.text(480,489,'cd ou cd ~ → dossier personnel','mono')
    d.note('~ désigne le dossier personnel. Le dossier courant est désigné par un point : .')
    diagrams.append(('04-chemins-absolus-et-relatifs',d))

    d=Diagram('05','Copier, déplacer, supprimer','Observer ce qui reste après chaque commande.')
    d.text(65,128,'COMMANDE','small');d.text(285,128,'AVANT','small');d.text(625,128,'APRÈS','small')
    for y,cmd,before,after,detail in [
        (152,'cp a.txt b.txt','a.txt','a.txt + b.txt','La source reste présente.'),
        (288,'mv a.txt b.txt','a.txt','b.txt','Le fichier porte le nouveau nom.'),
        (424,'rm a.txt','a.txt','Aucun fichier a.txt','Pas de passage par la corbeille.')]:
        d.rect(40,y,920,107)
        d.text(60,y+42,cmd,'mono');d.text(285,y+42,before,'mono')
        d.arrow(460,y+35,590,y+35);d.text(625,y+42,after,'mono')
        d.text(625,y+79,detail,'small')
    d.note('Exemples indépendants : b.txt n’existe pas au départ. Vérifier la cible avant toute suppression.')
    diagrams.append(('05-copier-deplacer-supprimer',d))

    d=Diagram('06','Les grands repères de l’arborescence','Tous les chemins partent d’une seule racine : /.')
    d.box(375,115,250,70,'/ — racine',soft=True)
    d.text(500,224,'Quelques chemins à connaître depuis la racine','body','middle')
    for x,title,detail in [(55,'/home','Documents personnels'),(375,'/etc','Configuration'),(695,'/var/log','Journaux système')]:
        d.box(x,255,250,100,title,[detail])
    for x,title,detail in [(55,'/usr/bin','Commandes'),(375,'/dev','Périphériques'),(695,'/tmp','Fichiers temporaires')]:
        d.box(x,407,250,100,title,[detail])
    d.text(500,387,'Exemple : /var/log est le dossier log dans /var','small','middle')
    d.note('Repères simplifiés. /root est le dossier personnel de root ; ce n’est pas la racine /.')
    diagrams.append(('06-reperes-arborescence',d))

    d=Diagram('07','Lire les permissions d’un fichier','Trois catégories distinctes : propriétaire, groupe et autres utilisateurs.')
    d.text(500,142,'- rw- r-- r--','mono','middle')
    for x,title,symbol,value,lines in [
        (55,'Propriétaire — u','rw-','6',['Lire et modifier','4 + 2 = 6']),
        (375,'Groupe — g','r--','4',['Lire seulement','4 = lecture']),
        (695,'Autres — o','r--','4',['Lire seulement','4 = lecture'])]:
        d.box(x,196,250,210,title,soft=True)
        d.text(x+125,280,symbol,'title','middle')
        for i,line in enumerate(lines):d.text(x+125,324+i*30,line,'body','middle')
        d.text(x+125,452,value,'title accent','middle')
    d.text(500,504,'chmod 644 notes.txt','mono','middle')
    d.note('r = 4, w = 2, x = 1. Pour un fichier lisible et modifiable uniquement par son propriétaire : chmod 600.')
    diagrams.append(('07-permissions-utilisateur-groupe-autres',d))

    d=Diagram('08','APT : listes et logiciels sont différents','Actualiser les informations ne met pas encore les logiciels à jour.')
    d.box(40,135,230,350,'Dépôts de paquets',['Informations','sur les versions','','Fichiers .deb','et dépendances'])
    d.box(395,135,565,350,'Votre machine Debian',[],True)
    d.box(440,212,475,85,'Liste locale des paquets',['apt update actualise cette liste.'])
    d.box(440,361,475,85,'Logiciels installés',['apt install ajoute ; apt upgrade met à jour.'])
    d.arrow(277,252,430,252);d.text(352,226,'update','mono','middle')
    d.arrow(277,402,430,402);d.text(352,374,'install','mono','middle');d.text(352,433,'upgrade','mono','middle')
    d.note('Les fichiers des logiciels sont téléchargés depuis les dépôts, pas depuis la liste locale.')
    diagrams.append(('08-apt-listes-et-logiciels',d))

    d=Diagram('09','Suivre les données dans un tube','Chaque commande reçoit le résultat de la commande précédente.')
    for x,title,lines in [(40,'cat journal.txt',['info démarrage','erreur disque','erreur réseau']),
                          (365,'grep erreur',['erreur disque','erreur réseau']),
                          (690,'wc -l',['2'])]:
        d.box(x,150,270,220,title,lines,True)
    d.arrow(315,255,356,255);d.arrow(640,255,681,255)
    d.text(500,420,'cat journal.txt | grep erreur | wc -l','mono','middle')
    d.text(500,465,'3 lignes → 2 lignes sélectionnées → résultat : 2','body','middle')
    d.text(500,510,'> remplace un fichier ; >> ajoute à la fin.','body','middle')
    d.note('Le tube | transmet la sortie normale (stdout). Les erreurs (stderr) ne sont pas incluses par défaut.')
    diagrams.append(('09-tubes-et-circulation-des-donnees',d))

    d=Diagram('10','SSH : travailler sur une machine distante','Exemple entre deux machines joignables sur le réseau.')
    d.box(45,145,340,180,'Poste du stagiaire',['Client SSH','Vous saisissez les commandes.'],True)
    d.box(615,145,340,180,'Machine Debian distante',['Serveur SSH — port 22','Les commandes s’exécutent ici.'],True)
    d.arrow(395,211,605,211);d.text(500,186,'Connexion chiffrée','small','middle')
    d.arrow(605,280,395,280);d.text(500,310,'Résultats affichés','small','middle')
    d.box(125,385,750,105,'Depuis le terminal du poste stagiaire',['ssh stagiaire@192.168.1.10'])
    d.note('L’adresse est un exemple. Avec une VM en NAT, l’accès depuis l’hôte peut nécessiter une redirection de port.')
    diagrams.append(('10-connexion-ssh',d))

    destination.mkdir(parents=True,exist_ok=True)
    for name,d in diagrams:d.save(destination/(name+'.svg'))
    return {name[:2]:name for name,_ in diagrams}

def integrate(source):
    names=create_diagrams(source/'Ressources/images')
    md_sections={'01':"## 1. Qu'est-ce qu'un système d'exploitation ?",'02':"## 1. Qu'est-ce qu'une machine virtuelle ?",'03':'## 6. Ouvrir un terminal','04':'## 5. Chemins absolus et relatifs','05':'## 3. Copier, déplacer, renommer','06':'## 1. Tout part de la racine','07':'## 6. Modifier les permissions','08':'## 3. APT','09':'## 3. Les tubes','10':'## 2. Se connecter à distance'}
    html_sections={'01':"Qu'est-ce qu'un système d'exploitation ?",'02':"Qu'est-ce qu'une machine virtuelle ?",'03':'Le terminal — outil central de Linux','04':'Chemin absolu vs relatif','05':'Récapitulatif cp vs mv','06':'Tout part de /','07':'Lire et comprendre les permissions','08':'apt — le gestionnaire de paquets','09':'Tubes et pipes — enchaîner les commandes','10':'SSH — connexion distante sécurisée'}
    captions={'01':'Le système Linux fait le lien entre les applications et le matériel.','02':'Le PC hôte exécute VirtualBox, qui fait fonctionner le système invité Debian.','03':'Le bureau et le terminal manipulent les mêmes fichiers.','04':'Deux chemins différents peuvent mener au même dossier.','05':'Comparer le résultat de cp, mv et rm.','06':'Quelques repères pour retrouver les dossiers essentiels.','07':'Lire les trois blocs de permissions et leur valeur numérique.','08':'apt update actualise les listes ; install et upgrade agissent sur les logiciels.','09':'Observer les lignes qui passent d’une commande à la suivante.','10':'Les commandes SSH s’exécutent sur la machine distante.'}
    for file in sorted(p for p in (source/'cours').rglob('[0-9][0-9]-*.md') if p.parent == source/'cours' or p.parent.name == p.stem):
        number=file.name[:2]; name=names[number]; caption=captions[number]
        marker=f'<!-- illustration-{number} -->'
        body=file.read_text(encoding='utf-8')
        if marker not in body:
            start=body.index(md_sections[number]); end=body.find('\n---',start)
            assert end>=0, file
            prefix='../../' if file.parent.name == file.stem else '../'
            block=f'\n\n{marker}\n![{caption}]({prefix}Ressources/images/{name}.svg)\n\n*{caption}*\n'
            body=body[:end]+block+body[end:]
            file.write_text(body,encoding='utf-8')
        html_file=file.with_suffix('.html');body=html_file.read_text(encoding='utf-8')
        if marker not in body:
            anchor='<h2>'+html_sections[number]+'</h2>'
            assert anchor in body,html_file
            figure=f'''\n{marker}\n<figure class="course-diagram" style="margin:1.25rem 0"><a href="../Ressources/images/{name}.svg" target="_blank" rel="noopener"><img src="../Ressources/images/{name}.svg" alt="{escape(caption,quote=True)}" width="1000" height="600" loading="lazy" style="width:100%;height:auto;border-radius:12px"></a><figcaption style="font-size:.9rem;margin-top:.5rem">{escape(caption)} Cliquez sur le schéma pour l’agrandir.</figcaption></figure>'''
            if file.parent.name == file.stem: figure=figure.replace('../Ressources/', '../../Ressources/')
            body=body.replace(anchor,anchor+figure,1)
            html_file.write_text(body,encoding='utf-8')
    print('10 SVG originaux intégrés dans les 10 cours Markdown et les 10 versions HTML du coffre.')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--source',type=Path,default=SOURCE)
    integrate(parser.parse_args().source)
