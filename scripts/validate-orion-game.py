"""Play all 48 missions and test the packaged terminal UI, locally or over SSH."""
from pathlib import Path
import argparse
import base64
import contextlib
import importlib.util
import io
import json
import os
import select
import signal
import subprocess
import sys
import tarfile
import tempfile
import time

def demand(value, message):
    if not value: raise AssertionError(message)

def validate(package):
    import pty
    import fcntl
    import termios
    with tempfile.TemporaryDirectory(prefix='orion-validation-') as temp:
        root = Path(temp)
        with tarfile.open(package, 'r:gz') as archive:
            members = archive.getmembers()
            demand({m.name for m in members} == {'orion-academie/'+n for n in ['orion.py','missions.json','jouer.sh','README.md']},'Contenu inattendu dans le jeu')
            for member in members:
                demand(member.isfile() and not member.name.startswith('/') and '..' not in Path(member.name).parts,'Archive invalide')
                target=root/member.name;target.parent.mkdir(parents=True,exist_ok=True)
                target.write_bytes(archive.extractfile(member).read());target.chmod(member.mode)
        game_dir=root/'orion-academie'
        spec=importlib.util.spec_from_file_location('orion',game_dir/'orion.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        missions=module.load_missions()
        workspace=root/'campagne avec espaces';workspace.mkdir();module.seed(workspace)
        shell=module.BashSession(workspace,headless=True)
        checks=0
        try:
            for mission in missions:
                before=module.check_mission(mission,workspace,shell,'')
                demand(before,'Mission déjà gagnée avant travail : '+str(mission['id']))
                status, output=shell.execute(mission.get('test_solution',mission['solution']),display=False,timeout=8)
                demand(status==0,f'Mission {mission["id"]} : solution en échec {status}\n{output}')
                failed=module.check_mission(mission,workspace,shell,output)
                demand(not failed,f'Mission {mission["id"]} : '+str(failed)+'\n'+output)
                checks+=len(mission['checks'])
                print(f'  Mission {mission["id"]:02}/48 : OK — {mission["title"]}')
            # Real shell state, variables, arbitrary whitespace and return codes.
            shell.execute('false',display=False);shell.snapshot()
            rc,out=shell.execute('echo "$?"',display=False)
            demand(out=='1\n','Le code $? a été perdu par les contrôles du jeu')
            shell.execute('station="Orion Nord"\ncd "$ORION_ATELIER/capsule"',display=False)
            cwd,variables=shell.snapshot()
            demand(cwd==str(workspace/'capsule') and variables['station']=='Orion Nord','État Bash non conservé')
            shell.execute('export MESSAGE_ORION="Dans le Bash enfant"\nbash -c \'echo "$MESSAGE_ORION"\'',display=False)
            # Validate rejection of a wrong script, not just the official solution.
            wrong=workspace/'atelier/chiffre.sh';original=wrong.read_text();wrong.write_text('#!/bin/bash\necho "Chiffre valide"\n')
            demand(module.check_mission(missions[27],workspace,shell,''),'Un faux validateur accepte les bananes')
            wrong.write_text(original)
            # Script checks must not change persistent user scores.
            scores=workspace/'finale/scores.csv';saved=scores.read_bytes()
            module.check_mission(missions[45],workspace,shell,'')
            demand(scores.read_bytes()==saved,'La vérification a ajouté des scores réels')
            # Additional game scenarios, independent of mission checks.
            def run(name,args=(),stdin='',code=0,contains=()):
                result=subprocess.run(['bash',str(workspace/'finale'/name),*args],input=stdin,text=True,capture_output=True,timeout=4)
                demand(result.returncode==code,f'{name} : code {result.returncode} attendu {code} '+result.stderr)
                demand(all(s in result.stdout+result.stderr for s in contains),f'{name} : résultat incorrect '+result.stdout)
                return result
            run('jeu.sh',['Mila Vega','entrainement'],'1\n9\n6\n',contains=['BINGO en 3','Score enregistre'])
            saved=scores.read_bytes()
            for values,code in [('1\n'*5,1),('',2),('banane\n',2)]:
                run('jeu.sh',['Noe','entrainement'],values,code)
                demand(scores.read_bytes()==saved,'Un échec a enregistré un score')
            for pseudo in ['A;B','A\nB','A\rB']:
                run('jeu.sh',[pseudo,'entrainement'],'6\n',2)
            scores.chmod(0o400)
            run('jeu.sh',['Noe','entrainement'],'6\n',1)
            scores.chmod(0o600)
            for trial in range(12):
                result=subprocess.run(['bash',str(workspace/'finale/jeu.sh')],input='5\n'*5,text=True,capture_output=True,timeout=3)
                demand(result.returncode in (0,1) and 'BIP-42 defie visiteur' in result.stdout,'Mode normal ou pseudo par défaut invalide')
                if result.returncode==1:
                    import re
                    demand(re.search(r'code [1-9]\.',result.stdout),'Secret aléatoire hors limites')
            run('arcade.sh',stdin='1\n'+'5\n'*5+'3\n',contains=['ORION SAUVEE'])
        finally: shell.close()

        # Save/resume and game commands; preserve old campaigns when starting anew.
        with contextlib.redirect_stdout(io.StringIO()) as transcript:
            game=module.Game(root/'profil avec espaces',color=False)
            original_workspace=game.workspace
            game.command(':suivant')
            demand(game.state['index']==0,'Une mission non validée peut être sautée')
            game.command(':indice');game.command(':solution')
            game.run_bash(missions[0]['solution'])
            demand(game.state['points']==40 and game.state['completed']==[1],'XP après solution incorrects')
            game.command(':test');demand(game.state['points']==40,'XP comptés plusieurs fois')
            game.command(':suivant');demand(game.state['index']==1,'Mission suivante inaccessible')
            game.shell.execute('station="Orion sauvegardee"\nexport NOM_STATION="Orion exportee"',display=False)
            game.save();game.shell.close()
            resumed=module.Game(root/'profil avec espaces',color=False)
            demand(resumed.state['index']==1 and resumed.state['points']==40,'Progression perdue au chargement')
            _,out=resumed.shell.execute('echo "$station"\npwd',display=False)
            demand('Orion sauvegardee' in out and str(original_workspace/'capsule') in out,'Variables ou dossier perdus au chargement')
            _,out=resumed.shell.execute('bash -c \'echo "$NOM_STATION"\'',display=False)
            demand(out=='Orion exportee\n','Attribut export perdu après reprise')
            resumed.run_bash('exit')
            _,out=resumed.shell.execute('echo "Shell reparti"',display=False)
            demand('Shell reparti' in out,'exit ne permet pas la reprise')
            resumed.save();resumed.shell.close()
            new=module.Game(root/'profil avec espaces',new=True,color=False)
            demand(new.workspace!=original_workspace and original_workspace.is_dir(),'Nouvelle partie destructrice')
            demand(new.state['points']==0,'La nouvelle partie reprend les anciens XP')
            new.shell.execute('echo "guillemet non ferme',display=False)
            _,out=new.shell.execute('echo "$?"',display=False)
            demand(out=='2\n','Code de retour après erreur syntaxique incorrect')
            new.finale();new.save();new.shell.close()
        demand('STATION SAUVEE' in transcript.getvalue() and '\x1b' not in transcript.getvalue(),'Finale ou mode sans couleur invalide')

        # Real pseudo-terminal: read prompt, editor, multiline input, Ctrl+C, EOF.
        profile=root/'profil terminal'
        game=module.Game(profile,color=False)
        game.state.update(index=16,completed=list(range(1,17)),points=1600)
        game.save();tty_workspace=game.workspace;game.shell.close()
        master,slave=pty.openpty()
        def own_terminal():
            os.setsid()
            fcntl.ioctl(slave,termios.TIOCSCTTY,0)
        process=subprocess.Popen(['bash',str(game_dir/'jouer.sh'),'--dossier',str(profile),'--sans-couleur'],
            stdin=slave,stdout=slave,stderr=slave,preexec_fn=own_terminal,env={**os.environ,'TERM':'xterm'})
        os.close(slave)
        pending=bytearray();all_output=bytearray()
        def expect(text,timeout=8):
            needle=text.encode();deadline=time.monotonic()+timeout
            while needle not in pending:
                demand(time.monotonic()<deadline,'Terminal : attente de '+text+'\n'+all_output.decode(errors='replace')[-1800:])
                if select.select([master],[],[],.1)[0]:
                    try: chunk=os.read(master,65536)
                    except OSError: chunk=b''
                    demand(chunk,'Terminal fermé avant '+text)
                    pending.extend(chunk);all_output.extend(chunk)
            end=pending.index(needle)+len(needle);del pending[:end]
        def send(text): os.write(master,text.encode())
        try:
            expect('ORION 17> ')
            send("read -r -p 'Ton nom : ' pilote\n")
            expect('\r\nTon nom : ');send('Noe\n')
            expect('MISSION ACCOMPLIE');expect('ORION 17> ')
            send(':editer atelier/test-terminal.txt\n')
            expect('\x1b[?1049h')
            expect('\x1b[?25h')
            send('Chocolat terminal\r');time.sleep(.1);send('\x0f')
            expect('test-terminal.txt');send('\r');time.sleep(.2);send('\x18')
            expect('ORION 17> ')
            actual=(tty_workspace/'atelier/test-terminal.txt').read_text()
            demand(actual.strip()=='Chocolat terminal','Nano : contenu inattendu '+repr(actual))
            send(':bloc\n');expect('... ')
            send('echo "Bloc valide" > "$ORION_ATELIER/rapports/bloc.txt"\n:fin\n')
            expect('ORION 17> ')
            demand((tty_workspace/'rapports/bloc.txt').read_text()=='Bloc valide\n','Saisie multiligne cassée')
            send('sleep 30\n');time.sleep(.25);send('\x03')
            expect('Commande interrompue');expect('ORION 17> ',timeout=6)
            send('\x04');expect('Partie sauvegardée')
            demand(process.wait(timeout=4)==0,'Sortie du terminal en erreur')
        finally:
            if process.poll() is None:
                with contextlib.suppress(ProcessLookupError): os.killpg(process.pid,signal.SIGKILL)
                process.wait()
            os.close(master)
        demand(json.loads((profile/'sauvegarde.json').read_text())['variables']['pilote']=='Noe','Saisie interactive non sauvegardée')
        print(f'Orion : 48 missions jouées ; {checks} contrôles de mission validés.')
        print('Validés : vrais états Bash, codes de retour, sauvegarde/reprise, XP, aides, nouvelle partie, sortie du shell, saisies invalides, scores et hasard.')
        print('Terminal réel : read, nano, bloc multiligne, Ctrl+C et Ctrl+D validés.')

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--package',type=Path,default=Path(__file__).resolve().parents[1]/'content/telechargements/bash/orion-academie.tar.gz')
    parser.add_argument('--ssh')
    args=parser.parse_args()
    if args.ssh:
        payload=base64.b64encode(args.package.read_bytes()).decode()
        source=base64.b64encode(Path(__file__).read_bytes()).decode()
        code=f'''import base64,pathlib,subprocess,tempfile
with tempfile.TemporaryDirectory(prefix='orion-tests-') as temp:
    root=pathlib.Path(temp)
    archive=root/'orion.tar.gz';archive.write_bytes(base64.b64decode({payload!r}))
    test=root/'validate.py';test.write_bytes(base64.b64decode({source!r}))
    subprocess.run(['python3',str(test),'--package',str(archive)],check=True)
'''
        subprocess.run(['ssh','-o','BatchMode=yes','-o','ConnectTimeout=10',args.ssh,'python3 -'],input=code,text=True,check=True,timeout=180)
    else: validate(args.package)

if __name__=='__main__': main()
