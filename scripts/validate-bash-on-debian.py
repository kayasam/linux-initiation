"""Execute the authored Bash examples and solution scenarios in a disposable VM lab."""
from pathlib import Path
import base64
import json
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')
SOURCE = Path('C:/Users/kayaw/Nextcloud/Obsidian/CoffreSam/Formations/linux-scripting-bash')
ROOT = Path(__file__).resolve().parents[1]


def blocks(path):
    body = path.read_text(encoding='utf-8-sig')
    result = []
    for match in re.finditer(r'^```bash\n(.*?)^```\s*$', body, re.M | re.S):
        prefix = body[max(0, match.start()-120):match.start()]
        annotation = re.search(r'<!-- (fichier|ajouter): ([\w.-]+\.sh) -->\s*$', prefix)
        result.append({'code': match[1], 'kind': annotation[1] if annotation else ('skip' if re.search(r'<!-- interactif: editeur -->\s*$', prefix) else 'run'), 'file': annotation[2] if annotation else None})
    return result


cases = []
for course in sorted(p for p in (SOURCE / 'cours').glob('*/*.md') if p.stem == p.parent.name):
    number = course.stem[:2]
    cases.append({'label': 'cours-' + number, 'blocks': blocks(course), 'target': 'cours-' + number})
    tp = next(p for p in (course.parent / 'tp').glob('tp-*.md') if 'correction' not in p.name)
    correction = tp.with_name(tp.stem + '-correction.md')
    cases.append({'label': 'solution-' + number, 'blocks': blocks(correction), 'target': number})
    cases.append({'label': 'enonce-' + number, 'blocks': blocks(correction) + blocks(tp), 'target': ''})
for kind, name in [('synthese', 'tp-synthese'), ('bonus', 'tp-bonus-exercices-ludiques'), ('final', 'tp-final-bip-42')]:
    correction = SOURCE / 'tp' / kind / (name + '-correction.md')
    tp = SOURCE / 'tp' / kind / (name + '.md')
    cases.append({'label': 'solution-' + kind, 'blocks': blocks(correction), 'target': kind})
    cases.append({'label': 'enonce-' + kind, 'blocks': blocks(correction) + blocks(tp), 'target': ''})

payload = base64.b64encode(json.dumps(cases, ensure_ascii=False).encode()).decode()
RUNNER = r'''
import base64,json,os,pathlib,re,shutil,subprocess,tempfile
cases=json.loads(base64.b64decode('__PAYLOAD__'))
root=pathlib.Path(tempfile.mkdtemp(prefix='validation-bash-',dir='/tmp')).resolve()
report={'environment':{},'documents':[],'scenarios':0,'blocks':0,'syntax_checks':0,'editors_checked':0}
def demand(condition,message):
    if not condition: raise AssertionError(message)
def run(args,cwd,env,stdin=''):
    return subprocess.run(args,cwd=cwd,env=env,input=stdin,text=True,encoding='utf-8',capture_output=True,timeout=12)
try:
    report['environment']['bash']=subprocess.check_output(['bash','--version'],text=True).splitlines()[0]
    report['environment']['distribution']=pathlib.Path('/etc/os-release').read_text().splitlines()[0]
    demand(shutil.which('nano') is not None,'nano absent')
    for case in cases:
        home=root/case['label'];home.mkdir()
        env=dict(os.environ,HOME=str(home),LC_ALL='C.UTF-8')
        lines=['shopt -s expand_aliases','set -E',"trap 'printf \"__ERR__|%s|%s\\n\" \"$?\" \"$BASH_COMMAND\"' ERR"]
        for i,block in enumerate(case['blocks']):
            kind,code=block['kind'],block['code']
            if kind=='skip': report['editors_checked']+=1;continue
            report['blocks']+=1
            if kind in ('fichier','ajouter'):
                blob=base64.b64encode(code.encode()).decode()
                op='>>' if kind=='ajouter' else '>'
                lines += [f"printf '%s' '{blob}' | base64 -d {op} '{block['file']}'",f"bash -n '{block['file']}'"]
                report['syntax_checks']+=1
            else:
                snippet=home/f'block-{i}.sh';snippet.write_text(code)
                check=run(['bash','-n',str(snippet)],home,env)
                demand(check.returncode==0,case['label']+': syntaxe du bloc '+str(i)+' '+check.stderr)
                report['syntax_checks']+=1
                lines.append('source '+str(snippet))
            lines.append(f"printf '__BLOCK__|{i}|%s\\n' \"$?\"")
        program=home/'validation.sh';program.write_text('\n'.join(lines)+'\n')
        result=run(['bash',str(program)],home,env,'Mila\nMila\nMila\n')
        demand(result.returncode==0,case['label']+': '+result.stderr)
        statuses=re.findall(r'^__BLOCK__\|(\d+)\|(\d+)$',result.stdout,re.M)
        demand(all(code=='0' for _,code in statuses),case['label']+': bloc en échec '+str(statuses)+' '+result.stderr)
        errors=re.findall(r'^__ERR__\|(\d+)\|(.+)$',result.stdout,re.M)
        expected=['ls dossier-inexistant-orion 2> /dev/null','bash controle.sh introuvable.txt','./sas.sh billet-refuse.txt','./sas.sh absent.txt','./sas.sh','./sas.sh .','./copieur.sh absent','./mission.sh']
        for code,command in errors:
            demand(command in expected,case['label']+': erreur inattendue '+command+' ('+code+') '+result.stderr)
        item={'label':case['label'],'executed_blocks':len(statuses),'expected_errors':len(errors),'status':'passed'}
        report['documents'].append(item)
        def locate(name):
            paths=list(home.glob('atelier-bash/**/'+name))
            demand(len(paths)==1,'Script introuvable ou ambigu : '+case['label']+'/'+name)
            return paths[0]
        def scenario(name,args=(),stdin='',code=0,contains=()):
            file=locate(name)
            r=run(['bash',str(file),*args],file.parent,env,stdin)
            demand(r.returncode==code,case['label']+'/'+name+': code '+str(r.returncode)+' au lieu de '+str(code)+' '+r.stderr)
            demand(all(s in r.stdout+r.stderr for s in contains),case['label']+'/'+name+': résultat différent '+r.stdout+r.stderr)
            report['scenarios']+=1
            return r
        target=case['target']
        if target=='cours-01':
            demand((home/'atelier-bash/decouverte/journal.txt').read_text()=='Station Orion ouverte\nRadio disponible\n','Journal cours 01')
        elif target=='cours-02':
            demand('Energie disponible : 100 unites' in result.stdout,'Calcul cours 02')
            demand('Station recue : Orion' in result.stdout,'Export cours 02')
        elif target=='cours-03':
            scenario('accueil.sh',(),contains=['Bienvenue visiteur sur Orion.'])
            scenario('accueil.sh',['Mila Vega'],contains=['Bienvenue Mila Vega sur Orion.'])
            scenario('arguments.sh',['Mila Vega','pilote'],contains=['Nombre : 2','Argument : Mila Vega','Argument : pilote'])
        elif target=='cours-04':
            scenario('controle.sh',['billet.txt'],contains=['Fichier disponible'])
            scenario('controle.sh',code=2,contains=['Usage'])
            scenario('controle.sh',['introuvable.txt'],code=2,contains=['Fichier absent'])
        elif target=='cours-05':
            scenario('copier.sh',['messages'],contains=['Copies realisees : 2'])
        elif target in ('cours-06','06'):
            folder=home/('atelier-bash/texte' if target=='cours-06' else 'atelier-bash/06-stock')
            original=(folder/'stock.csv').read_text()
            demand(original.count('informatique')==3,'Original sed altéré')
            total=run(['awk','-F',';','NR > 1 { t += $3 * $4 } END { print t }','stock.csv'],folder,env)
            demand(total.stdout.strip()=='1220','Total awk')
            demand((folder/'stock-test.csv.bak').read_text()==original,'Sauvegarde sed incorrecte')
            if target=='06': demand((folder/'rapport.txt').read_text().endswith('TOTAL 1220\n'),'Rapport TP06')
        elif target=='01':
            folder=home/'atelier-bash/01-orion'
            demand((folder/'journal.txt').read_text()=='ORION : poste ouvert\nRadio : OK\nReserve : OK\n','Journal TP01')
            demand((folder/'journal de bord').is_dir(),'Dossier avec espaces TP01')
        elif target=='02':
            badge=(home/'atelier-bash/02-badge/badge.txt').read_text()
            demand('Prenom : Mila\n' in badge and 'Station : Orion Nord\n' in badge and 'Energie restante : 85\n' in badge,'Badge TP02')
        elif target=='03':
            scenario('robot.sh',contains=['Bonjour visiteur','explorateur','Arguments recus : 0'])
            scenario('robot.sh',['Mila','pilote'],contains=['Bonjour Mila','pilote','Arguments recus : 2'])
            scenario('robot.sh',['Mila Vega','responsable radio'],contains=['Bonjour Mila Vega','responsable radio'])
            log=locate('robot.sh').parent/'arrivees.txt'
            demand(len(log.read_text().splitlines())==3,'Journal bonus TP03')
        elif target=='04':
            scenario('sas.sh',['billet-valide.txt'],contains=['SAS OUVERT'])
            scenario('sas.sh',['billet-refuse.txt'],code=1,contains=['SAS FERME'])
            scenario('sas.sh',['absent.txt'],code=2)
            scenario('sas.sh',code=2,contains=['Usage'])
            scenario('sas.sh',['.'],code=2)
            scenario('sas.sh',['billet equipe.txt'],contains=['SAS OUVERT'])
            unreadable=locate('sas.sh').parent/'billet-illisible.txt'
            unreadable.write_text('ORION-OK\n');unreadable.chmod(0)
            scenario('sas.sh',[str(unreadable)],code=2)
            unreadable.chmod(0o600)
            for value,code,message in [('1\n',0,'Radio disponible'),('2\n',0,'Reserve disponible'),('x\n',2,'Choix inconnu')]:
                scenario('menu.sh',stdin=value,code=code,contains=[message])
        elif target=='05':
            scenario('copieur.sh',['messages'],contains=['Copies realisees : 3'])
            scenario('copieur.sh',['messages'],contains=['Copies realisees : 3'])
            scenario('copieur.sh',['vide'],contains=['Copies realisees : 0'])
            scenario('copieur.sh',['absent'],code=2)
            scenario('copieur.sh',['messages','extra'],code=2)
            folder=locate('copieur.sh').parent
            demand((folder/'messages/journal radio.txt').read_bytes()==(folder/'messages/copies/journal radio.txt').read_bytes(),'Copie avec espaces TP05')
            blocked=folder/'blocage';blocked.mkdir();(blocked/'copies').write_text('fichier au lieu de dossier')
            scenario('copieur.sh',['blocage'],code=1)
            blocked_copy=folder/'copie-bloquee';(blocked_copy/'copies/accueil.txt').mkdir(parents=True)
            (blocked_copy/'accueil.txt').write_text('Message\n')
            scenario('copieur.sh',['copie-bloquee'],code=1,contains=['Copie impossible'])
        elif target=='synthese':
            scenario('mission.sh',contains=['MISSION Orion','Personnes : 3','Articles : 74','Valeur : 1220','clavier 8','ecran 4'])
            scenario('mission.sh',['Orion Nord'],contains=['MISSION Orion Nord'])
            scenario('mission.sh',['un','deux'],code=2)
            folder=locate('mission.sh').parent
            file=folder/'donnees/equipe.txt';hold=file.with_name('equipe-attente.txt');file.rename(hold)
            scenario('mission.sh',code=2,contains=['Equipage absent'])
            hold.rename(file)
            scenario('mission.sh',contains=['Personnes : 3'])
            stock=folder/'donnees/stock.csv';hold_stock=stock.with_suffix('.attente');stock.rename(hold_stock)
            scenario('mission.sh',code=2,contains=['Inventaire absent'])
            hold_stock.rename(stock)
            output=folder/'rapports/mission.txt';saved=output.with_suffix('.attente');output.rename(saved);output.mkdir()
            scenario('mission.sh',code=1,contains=['Ecriture du rapport impossible'])
            output.rmdir();saved.rename(output)
        elif target=='final':
            scenario('jeu-v1.sh',stdin='1\n',contains=['Trop petit !'])
            scenario('jeu-v1.sh',stdin='9\n',contains=['Trop grand !'])
            scenario('jeu-v1.sh',stdin='6\n',contains=['BINGO !'])
            scenario('jeu-v1.sh',stdin='banane\n',code=2)
            scenario('jeu-v1.sh',stdin='',code=2,contains=['Saisie interrompue'])
            scenario('jeu-v2.sh',stdin='1\n9\nbanane\n6\n',contains=['en 3 essais'])
            scenario('jeu-v2.sh',stdin='1\n'*5,code=1,contains=['PERDU !','code etait 6'])
            scenario('jeu-v2.sh',stdin='',code=2)
            folder=locate('jeu.sh').parent
            scores=folder/'scores.csv'
            scenario('jeu.sh',['Mila Vega','entrainement'],stdin='1\n9\n6\n',contains=['Mila Vega','en 3 essais','BIP-42 : Qui ose'])
            demand('Mila Vega;3;' in scores.read_text(),'Pseudo composé ou score incorrect')
            scenario('jeu.sh',['Noe','entrainement'],stdin='banane\n\n10\n08\n-1\n999999999999999999999\n6\n',contains=['en 1 essai.'])
            before=scores.read_bytes()
            scenario('jeu.sh',['Noe','entrainement'],stdin='1\n'*5,code=1,contains=['PERDU !'])
            scenario('jeu.sh',['Noe','entrainement'],stdin='',code=2)
            scenario('jeu.sh',['Noe','turbo'],code=2,contains=['Usage'])
            scenario('jeu.sh',['a','normal','extra'],code=2)
            for pseudo in ['Mila;Vega','Mila\nVega','Mila\rVega']:
                scenario('jeu.sh',[pseudo,'entrainement'],code=2,contains=['Pseudo interdit'])
            demand(scores.read_bytes()==before,'Un échec ou une saisie invalide a enregistré un score')
            scenario('statistiques.sh',contains=['Meilleur resultat : 1 essai(s)'])
            robot=folder/'robot.txt';hold=folder/'robot.attente';robot.rename(hold)
            scenario('jeu.sh',['Noe','entrainement'],stdin='6\n',code=2,contains=['Message du robot absent'])
            hold.rename(robot)
            robot.chmod(0)
            scenario('jeu.sh',['Noe','entrainement'],stdin='6\n',code=2)
            robot.chmod(0o600)
            demand(robot.read_text()=='ROBOT : Qui ose toucher a mon chocolat ?\n','sed a modifié le fichier source')
            scores.chmod(0o400)
            scenario('jeu.sh',['Noe','entrainement'],stdin='6\n',code=1,contains=['scores inutilisable'])
            scores.chmod(0o600)
            saved=folder/'scores.attente';scores.rename(saved);scores.mkdir()
            scenario('jeu.sh',['Noe','entrainement'],stdin='6\n',code=1)
            scores.rmdir()
            scenario('statistiques.sh',code=2,contains=['Pas encore de scores'])
            scores.write_text('joueur;essais;date\n')
            scenario('statistiques.sh',contains=['Aucune victoire'])
            scores.unlink();saved.rename(scores)
            # Random mode: either a victory at 5 or a revealed losing secret in 1..9.
            for trial in range(10):
                r=run(['bash','jeu.sh','Test hasard'],folder,env,'5\n'*5)
                demand(r.returncode in (0,1),'Mode normal invalide '+r.stderr)
                if r.returncode==0:
                    demand('en 1 essai.' in r.stdout,'Victoire aléatoire incohérente')
                else:
                    demand(re.search(r'code etait [1-9]\.',r.stdout) is not None,'Secret aléatoire hors limites')
                report['scenarios']+=1
            scenario('arcade.sh',stdin='x\n2\n3\n',contains=["Ce bouton n'existe pas",'Victoires :','Enfin seul'])
            scenario('arcade.sh',stdin='',code=2)
        elif target=='bonus':
            scenario('depart.sh',contains=['3\n2\n1\nDecollage !'])
            scenario('quiz.sh',stdin='Bash\nawk\n0\n',contains=['Score : 3/3'])
            scenario('quiz.sh',stdin='x\ny\nz\n',contains=['Score : 0/3'])
            scenario('quiz.sh',stdin='',code=2,contains=['Saisie interrompue'])
            scenario('quiz.sh',stdin='Bash\n',code=2,contains=['Saisie interrompue'])
            scenario('quiz.sh',stdin='Bash\nawk\n',code=2,contains=['Saisie interrompue'])
            for value,code,message in [('7\n',0,'Tresor trouve'),('4\n7\n',0,'Tresor trouve'),('0\n9\n7\n',0,'Tresor trouve'),('1\n2\n3\n',1,'Perdu'),('chat\n7\n',0,'Tresor trouve'),('\n7\n',0,'Tresor trouve'),('10\n7\n',0,'Tresor trouve'),('',2,'Saisie interrompue')]:
                scenario('tresor.sh',stdin=value,code=code,contains=[message])
            random_check=run(['bash','-c','for essai in {1..100}; do n=$((RANDOM % 10)); [[ "$n" -ge 0 && "$n" -le 9 ]] || exit 1; done; sleep 1'],home,env)
            demand(random_check.returncode==0,'Bonus : aleatoire ou sleep')
            report['scenarios']+=1
    report['status']='passed'
    print(json.dumps(report,ensure_ascii=False))
finally:
    demand(root.parent==pathlib.Path('/tmp') and root.name.startswith('validation-bash-'),'Refus de nettoyage hors atelier de validation')
    shutil.rmtree(root)
'''
remote = RUNNER.replace('__PAYLOAD__', payload)
result = subprocess.run(['ssh', '-o', 'BatchMode=yes', '-o', 'ConnectTimeout=10', 'debian', 'python3 -'], input=remote, text=True, encoding='utf-8', capture_output=True, timeout=180)
if result.returncode:
    print(result.stderr)
    raise SystemExit('Validation Debian en échec.')
report = json.loads(result.stdout)
backup = Path('D:/Projet-git/backups/validation-bash-debian.json')
backup.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
note = SOURCE / 'Ressources/validation-debian.md'
if note.exists():
    content = note.read_text(encoding='utf-8')
    tp_total = (len(report['documents']) - 6) // 2
    content = re.sub(r'\d+ documents parcourus : six cours, .*? corrections\.', f"{len(report['documents'])} documents parcourus : six cours, {tp_total} énoncés et {tp_total} corrections.", content)
    content = re.sub(r'\d+ exécutions de blocs', f"{report['blocks']} exécutions de blocs", content)
    content = re.sub(r'\d+ scénarios de comportement', f"{report['scenarios']} scénarios de comportement", content)
    note.write_text(content, encoding='utf-8')
print(report['environment']['distribution'])
print(report['environment']['bash'])
print(f"Debian : {len(report['documents'])} documents, {report['blocks']} blocs, {report['syntax_checks']} vérifications syntaxiques et {report['scenarios']} scénarios validés.")
print('Les étapes nano sont vérifiées comme prérequis ; la saisie dans l’éditeur reste une action de l’élève.')
print('Rapport : ' + str(backup))
