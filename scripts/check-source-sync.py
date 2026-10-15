"""Audit the vault against generated downloads/ZIPs, optionally the live site."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse
import hashlib
import json
from html.parser import HTMLParser
import re
import runpy
import sys
import tarfile
import zipfile
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / 'content'
BASE = 'https://kayasam.github.io/linux-initiation'
sys.stdout.reconfigure(encoding='utf-8')


def text(data):
    return data.decode('utf-8-sig').replace('\r\n', '\n').strip()


def equal(expected, actual, label):
    if text(expected.encode('utf-8')) != text(actual):
        raise AssertionError('Contenu différent : ' + label)


def local_audit():
    linux = runpy.run_path(str(ROOT / 'scripts/prepare-linux.py'))
    bash = runpy.run_path(str(ROOT / 'scripts/prepare-bash.py'))
    linux_source, bash_source = linux['DEFAULT_SOURCE'], bash['SOURCE']
    linux_courses = sorted(p for p in (linux_source / 'cours').glob('*/*.md') if p.stem == p.parent.name)
    bash_courses = sorted(p for p in (bash_source / 'cours').glob('*/*.md') if p.stem == p.parent.name)
    assert len(linux_courses) == 10 and len(bash_courses) == 6
    tp_count = 0
    with zipfile.ZipFile(CONTENT / 'linux-initiation-obsidian.zip') as archive:
        for course in linux_courses:
            slug = course.stem
            body = linux['normalize'](course.read_text(encoding='utf-8-sig'))
            body = re.sub(r'\n\n<!-- ressources-locales -->\n(?:>[^\n]*\n)+', '', body)
            body = body.replace('../../Ressources/images/', '../Ressources/images/')
            for linked in linux_courses:
                body = body.replace(f'](../{linked.stem}/{linked.stem}.md)', f']({linked.stem}.md)')
                body = body.replace(f']({linked.stem}-quiz.html)', f'](quiz/{linked.stem}.html)')
            equal(body, archive.read('Linux-initiation/cours/' + course.name), course.name + ' (ZIP Linux)')
            equal(linux['public_markdown'](body, linux_courses), (CONTENT / 'telechargements/cours' / course.name).read_bytes(), course.name + ' (téléchargement Linux)')
            offline_html = linux['flat_html'](course.with_suffix('.html').read_text(encoding='utf-8-sig'), slug)
            offline_html = offline_html.replace(f'href="{slug}-quiz.html"', f'href="quiz/{slug}.html"')
            equal(offline_html, archive.read('Linux-initiation/cours/' + slug + '.html'), slug + ' (HTML ZIP Linux)')
            assert (CONTENT / 'cours' / (slug + '-interactif.html')).is_file()
            for tp in (course.parent / 'tp').glob('tp-*.md'):
                if re.search(r'correction|corrig', tp.name, re.I): continue
                expected = linux['normalize'](tp.read_text(encoding='utf-8-sig'))
                for correction in sorted(tp.parent.glob(f'tp-{slug[:2]}-*correction.md')):
                    if linux['is_published'](correction):
                        expected += f'\n[Correction du TP]({BASE}/{slug}/{correction.stem})\n'
                equal(expected.replace(f'](../{slug}.md)', f'](../cours/{slug}.md)'), archive.read('Linux-initiation/tp/' + tp.name), tp.name + ' (ZIP Linux)')
                equal(expected.replace(f'](../{slug}.md)', f']({BASE}/{slug}/)'), (CONTENT / 'telechargements/tp' / tp.name).read_bytes(), tp.name + ' (téléchargement Linux)')
                assert (CONTENT / slug / 'tp.md').is_file()
                tp_count += 1
    with zipfile.ZipFile(CONTENT / 'linux-scripting-bash-obsidian.zip') as archive:
        public_banks=json.loads((CONTENT/'bash/assets/quiz/quiz-banks.js').read_text(encoding='utf-8').split('=',1)[1])
        authored=json.loads((bash_source/'Ressources/quiz/bash-questions.json').read_text(encoding='utf-8'))
        assert archive.read('Linux-scripting-bash/Ressources/quiz/bash-questions.json')==(bash_source/'Ressources/quiz/bash-questions.json').read_bytes()
        offline_banks=json.loads((bash_source/'assets/quiz/quiz-banks.js').read_text(encoding='utf-8').split('=',1)[1])
        assert len(public_banks)==len(offline_banks)==6
        class QuizLinks(HTMLParser):
            def handle_starttag(self,tag,attrs):
                for key,value in attrs:
                    if key in ('href','src') and value and not value.startswith(('#','http:','https:')):
                        assert (self.folder/value).resolve().is_file(), 'Lien du quiz hors ligne absent : '+value
        for course in bash_courses:
            slug=course.stem;key='bash-'+slug
            bank=public_banks[key]
            assert len(bank['questions'])==20 and bank['questions']==offline_banks[key]['questions']
            for question,original in zip(bank['questions'],authored[slug]):
                assert question['question']==original['question'] and question['explanation']==original['explanation']
                assert set(question['choices'])==set(original['choices']) and question['choices'][question['answer']]==original['choices'][original['answer']]
            assert bank['chapterLink']=='../../'+slug+'/' and offline_banks[key]['chapterLink']==slug+'.html'
            quiz=course.with_name(slug+'-quiz.html')
            equal(quiz.read_text(encoding='utf-8'),archive.read('Linux-scripting-bash/'+quiz.relative_to(bash_source).as_posix()),'Quiz Bash '+slug+' (ZIP)')
            parser=QuizLinks();parser.folder=quiz.parent;parser.feed(quiz.read_text(encoding='utf-8'))
            assert (CONTENT/'bash/cours/quiz'/f'{slug}.html').is_file()
            assert f'{BASE}/bash/cours/quiz/{slug}.html' in (CONTENT/'bash'/slug/'index.md').read_text(encoding='utf-8')
        for folder in ['assets/quiz','assets/themes']:
            for asset in (bash_source/folder).glob('*'):
                if asset.is_file():assert archive.read('Linux-scripting-bash/'+folder+'/'+asset.name)==asset.read_bytes()
        with tarfile.open(CONTENT / 'telechargements/bash/orion-academie.tar.gz', 'r:gz') as game:
            for name in ['orion.py','missions.json','jouer.sh','README.md']:
                expected = (bash_source / 'jeu' / name).read_bytes().replace(b'\r\n', b'\n')
                assert game.extractfile('orion-academie/' + name).read() == expected, 'Jeu Orion désynchronisé : ' + name
                assert archive.read('Linux-scripting-bash/jeu/' + name) == expected, 'Jeu Orion dans le ZIP : ' + name
        game_archive = CONTENT / 'telechargements/bash/orion-academie.tar.gz'
        assert game_archive.with_suffix('.gz.sha256').read_text().strip() == hashlib.sha256(game_archive.read_bytes()).hexdigest() + '  ' + game_archive.name
        equal((bash_source / 'Résumé.md').read_text(encoding='utf-8-sig'), archive.read('Linux-scripting-bash/Résumé.md'), 'Mémo Bash (ZIP)')
        for image in sorted((bash_source / 'Ressources/images').glob('bash-*.svg')):
            assert archive.read('Linux-scripting-bash/Ressources/images/' + image.name) == image.read_bytes()
            assert (CONTENT / 'bash/images' / image.name).read_bytes() == image.read_bytes()
        for course in bash_courses:
            slug = course.stem
            offline = bash['normalize'](course.read_text(encoding='utf-8-sig'))
            equal(offline, archive.read('Linux-scripting-bash/' + course.relative_to(bash_source).as_posix()), course.name + ' (ZIP Bash)')
            equal(course.with_suffix('.html').read_text(encoding='utf-8-sig'), archive.read('Linux-scripting-bash/' + course.with_suffix('.html').relative_to(bash_source).as_posix()), slug + ' (HTML ZIP Bash)')
            body = re.sub(r'\n\n<!-- ressources-locales -->\n(?:>[^\n]*\n)+', '', offline)
            body = body.replace('../../Ressources/images/', BASE + '/bash/images/')
            body = bash['public_course_links'](body, course, bash_courses)
            tps = [p for p in (course.parent / 'tp').glob('tp-*.md') if not re.search(r'correction|corrig', p.name, re.I)]
            assert len(tps) == 1
            body = body.replace(f'](tp/{tps[0].name})', f']({BASE}/bash/{slug}/tp)')
            equal(body, (CONTENT / 'telechargements/bash/cours' / course.name).read_bytes(), course.name + ' (téléchargement Bash)')
            assert (CONTENT / 'bash' / slug / 'tp.md').is_file()
        tps = list(bash_source.glob('cours/*/tp/tp-*.md')) + list(bash_source.glob('tp/*/tp-*.md'))
        for tp in tps:
            if re.search(r'correction|corrig', tp.name, re.I): continue
            offline = bash['normalize'](tp.read_text(encoding='utf-8-sig'))
            equal(offline, archive.read('Linux-scripting-bash/' + tp.relative_to(bash_source).as_posix()), tp.name + ' (ZIP Bash)')
            body = offline
            body = bash['public_course_links'](body, tp, bash_courses)
            if tp.is_relative_to(bash_source / 'cours'):
                slug = tp.parent.parent.name
                body = body.replace(f'](../{slug}.md)', f']({BASE}/bash/{slug}/)')
                body += f'\n[← Revenir au cours]({BASE}/bash/{slug}/)\n'
            equal(body, (CONTENT / 'telechargements/bash/tp' / tp.name).read_bytes(), tp.name + ' (téléchargement Bash)')
            tp_count += 1
        assert not any(re.search(r'correction|corrig', name, re.I) for name in archive.namelist())
    assert tp_count == 17
    banks = json.loads((CONTENT / 'assets/quiz/quiz-banks.js').read_text(encoding='utf-8-sig').split('=', 1)[1])
    source_banks = json.loads((linux_source / 'assets/quiz/quiz-banks.js').read_text(encoding='utf-8-sig').split('=', 1)[1])
    assert source_banks == {slug: {**bank, 'chapterLink': slug + '.html'} for slug, bank in banks.items()}
    for slug in banks:
        expected = (CONTENT / 'cours/quiz' / (slug + '.html')).read_text(encoding='utf-8-sig')
        expected = expected.replace('../../' + slug + '/', slug + '.html')
        equal(expected, (linux_source / 'cours' / slug / (slug + '-quiz.html')).read_bytes(), slug + ' (quiz du coffre)')
    for folder in ['assets/themes', 'assets/quiz']:
        for asset in (CONTENT / folder).glob('*'):
            if asset.name == 'quiz-banks.js' or not asset.is_file(): continue
            if folder == 'assets/quiz' and asset.name not in {'quiz.css', 'quiz-engine.js'}: continue
            equal(asset.read_text(encoding='utf-8-sig'), (linux_source / folder / asset.name).read_bytes(), str(asset.relative_to(CONTENT)) + ' (coffre)')
    print('Coffre → contenus : 10 cours Linux + 6 cours Bash, 17 TP, ZIP et téléchargements conformes.')
    print('Quiz et thèmes du coffre : dix quiz Linux et six quiz Bash de vingt questions conformes, avec les ressources hors ligne.')


def live_audit():
    paths = sorted(set(CONTENT.glob('telechargements/**/*.md')) | set(CONTENT.glob('telechargements/**/*.tar.gz')) | set(CONTENT.glob('telechargements/**/*.sha256')) | set(CONTENT.glob('cours/*-interactif.html')) | set(CONTENT.glob('bash/cours/*-interactif.html')) | set(CONTENT.glob('bash/images/*.svg')) | set(CONTENT.glob('cours/quiz/*.html')) | set(CONTENT.glob('assets/brands/*')) | {CONTENT / 'assets/quiz/quiz-banks.js', CONTENT / 'linux-initiation-obsidian.zip', CONTENT / 'linux-scripting-bash-obsidian.zip'})
    paths=sorted(set(paths)|set(CONTENT.glob('bash/cours/quiz/*.html'))|{CONTENT/'bash/assets/quiz/quiz-banks.js'})
    def compare(path):
        relative = path.relative_to(CONTENT).as_posix()
        try:
            with urlopen(Request(BASE + '/' + relative, headers={'User-Agent': 'Course-sync-audit'}), timeout=30) as response:
                remote = response.read()
            local = path.read_bytes()
            same = text(local) == text(remote) if path.suffix in {'.md', '.html', '.js', '.json', '.svg', '.txt', '.sha256'} else local == remote
            return None if same else relative
        except Exception as error:
            return relative + ': ' + str(error)
    with ThreadPoolExecutor(max_workers=6) as pool:
        differences = [result for result in pool.map(compare, paths) if result]
    if differences:
        raise AssertionError('Écarts avec le site en ligne :\n' + '\n'.join(differences))
    print(f'Contenus → site en ligne : {len(paths)} fichiers conformes, dont les 2 ZIP et les 16 HTML de cours.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--live', action='store_true')
    args = parser.parse_args()
    local_audit()
    if args.live: live_audit()
