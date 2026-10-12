"""Prepare student content from the Obsidian course, without publishing corrections."""
from pathlib import Path
import argparse
import html
import json
import re
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://kayasam.github.io/linux-initiation'
DEFAULT_SOURCE = Path('C:/Users/kayaw/Nextcloud/Obsidian/CoffreSam/Formations/linux-initiation')

def write(path, body):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding='utf-8')

def normalize(body):
    body = re.sub(r'^> \[(?:name|time)=.*\]\s*$', '', body, flags=re.M)
    body = re.sub(r'^\[TOC\]\s*$', '', body, flags=re.M)
    kinds = {'info': 'NOTE', 'success': 'TIP', 'warning': 'WARNING', 'danger': 'DANGER'}
    def callout(m):
        return '> [!' + kinds.get(m[1], 'NOTE') + ']\n' + '\n'.join('> ' + line if line else '>' for line in m[2].strip().splitlines())
    body = re.sub(r'^:::(\w+)\s*\n(.*?)^:::\s*$', callout, body, flags=re.M | re.S)
    return body.strip() + '\n'

def metadata(title, body):
    return '---\ntitle: ' + json.dumps(title, ensure_ascii=False) + '\n---\n\n' + body

def prepare(source):
    courses = sorted((source / 'cours').glob('[0-9][0-9]-*.md'))
    assert len(courses) == 10, '10 chapitres attendus'
    chapters = []
    stage = ROOT / '.publication-stage'
    # Resolve the target before removing only our generated staging directory.
    assert stage.resolve().parent == ROOT.resolve()
    if stage.exists(): shutil.rmtree(stage)
    shutil.copytree(ROOT / 'site-content', stage)
    vault = stage / 'telechargements' / 'Linux-initiation'
    for i, course in enumerate(courses):
        slug = course.stem
        title = re.search(r'^#\s+(.*)', course.read_text(encoding='utf-8'), re.M)[1]
        title = re.sub(r'^Chapitre \d+\s*[—–-]\s*', '', title)
        number = slug[:2]
        tp = next(iter(sorted((source / 'sessions' / '2026-05').glob(f'tp-{number}-*.md'))), None)
        # Corrections can never be selected even if filenames sort differently.
        tps = [p for p in (source / 'sessions' / '2026-05').glob(f'tp-{number}-*.md') if not re.search(r'correction|corrig', p.name, re.I)]
        assert len(tps) <= 1
        tp = tps[0] if tps else None
        body = normalize(course.read_text(encoding='utf-8'))
        write(vault / 'cours' / course.name, body)
        write(stage / 'telechargements' / 'cours' / course.name, body)
        interactive = (source / 'cours' / f'{slug}.html').read_text(encoding='utf-8')
        nav = f'<div class="course-site-nav"><a href="../{slug}/">← Chapitre {number}</a><a href="quiz/{slug}.html">Quiz du chapitre →</a></div>'
        interactive = interactive.replace('<body>', '<body>\n' + nav, 1)
        interactive = interactive.replace('</style>', '.course-site-nav { display:flex; justify-content:space-between; gap:1rem; padding:.8rem 1rem; background:#1a1d27; flex-wrap:wrap; } .course-site-nav a {color:#93c5fd; font-weight:600;}\n</style>', 1)
        write(stage / 'cours' / f'{slug}-interactif.html', interactive)
        # Offline interactive pages keep a working return link and their own quiz.
        offline = (source / 'cours' / f'{slug}.html').read_text(encoding='utf-8')
        write(vault / 'cours' / f'{slug}.html', offline)
        links = f'\n\n> [!TIP] Ressources du chapitre\n> - [Ouvrir le chapitre interactif]({BASE}/cours/{slug}-interactif.html)\n> - [Faire le quiz]({BASE}/cours/quiz/{slug}.html)\n> - <a href="{BASE}/telechargements/cours/{course.name}" download>Télécharger ce cours en Markdown</a>\n'
        if tp:
            links += f'> - [Passer au TP]({BASE}/{slug}/tp)\n'
            tpbody = normalize(tp.read_text(encoding='utf-8'))
            write(vault / 'tp' / tp.name, tpbody)
            write(stage / 'telechargements' / 'tp' / tp.name, tpbody)
            write(stage / slug / 'tp.md', metadata(f'TP {number} — {title}', tpbody + f'\n[← Revenir au cours]({BASE}/{slug}/)\n\n<a href="{BASE}/telechargements/tp/{tp.name}" download>Télécharger ce TP en Markdown</a>\n'))
        body = re.sub(r'^(# .+)$', lambda m: m[0] + links, body, count=1, flags=re.M)
        previous = f'[← {chapters[-1]["title"]}]({BASE}/{chapters[-1]["slug"]}/)' if chapters else '[← Accueil](' + BASE + '/)'
        following = f'[Chapitre suivant →]({BASE}/{courses[i+1].stem}/)' if i+1 < len(courses) else f'[Revenir à l’accueil →]({BASE}/)'
        write(stage / slug / 'index.md', metadata(f'{number}. {title}', body + '\n---\n\n' + previous + ' · ' + following + '\n'))
        chapters.append(dict(slug=slug, title=title, tp=tp.name if tp else None))
    for tp in (source / 'sessions' / '2026-05').glob('tp-*.md'):
        if 'correction' in tp.name: continue
        body = tp.read_text(encoding='utf-8')
        for image in re.findall(r'!\[\[([^]|]+)', body):
            media = tp.parent / image
            if not media.is_file(): media = tp.parent / 'Images' / image
            if media.is_file():
                for dest in (vault / 'tp' / 'Images' / media.name, stage / 'Images' / media.name):
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(media, dest)
    cards = '\n'.join(f'<a class="home-chapter" href="./{c["slug"]}/"><span class="home-chapter__number">{c["slug"][:2]}</span><strong>{html.escape(c["title"])}</strong><span class="home-chapter__arrow" aria-hidden="true">→</span></a>' for c in chapters)
    home = '''<header class="home-header"><h1>Linux — Initiation</h1><p>Comprendre Linux, installer Debian et prendre en main le terminal.</p></header>
<section class="home-track" aria-labelledby="parcours"><div class="home-track__head"><div class="home-track__logo"><span aria-hidden="true" style="font-size:2.4rem">&gt;_</span></div><div class="home-track__heading"><h2 id="parcours">Vos 10 chapitres</h2><p>Deux jours pour découvrir Linux pas à pas, avec des exemples, des quiz et sept travaux pratiques.</p></div><a class="home-track__start" href="./01-comprendre-linux/">Commencer au chapitre 01 →</a></div><div class="home-chapter-grid">''' + cards + '''</div></section>
<section class="home-downloads"><h2>Supports hors ligne</h2><div class="home-downloads__grid"><a href="./linux-initiation-obsidian.zip" download><strong>Le cours pour Obsidian</strong><span>Les 10 cours Markdown, les 10 versions interactives et les 7 TP.</span><em>Télécharger le ZIP →</em></a><a href="./ressources/"><strong>Préparer la formation</strong><span>Programme, objectifs et déroulement des deux journées.</span><em>Consulter le programme →</em></a></div></section>'''
    write(stage / 'index.md', metadata('Linux — Initiation', home))
    program = normalize((source / 'programme.md').read_text(encoding='utf-8'))
    program = program.split('## Fichiers cours')[0]
    write(stage / 'ressources' / 'index.md', metadata('Programme et objectifs', program))
    write(vault / 'README.md', '# Linux — Initiation\n\nOuvrez ce dossier comme coffre dans Obsidian. Les cours se trouvent dans `cours/` et les exercices dans `tp/`. Ouvrez les fichiers HTML dans votre navigateur pour les versions interactives.\n\n' + '\n'.join(f'- [{c["title"]}](cours/{c["slug"]}.md)' for c in chapters))
    archive = stage / 'linux-initiation-obsidian.zip'
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
        for file in sorted(vault.rglob('*')):
            if file.is_file(): z.write(file, file.relative_to(vault.parent))
    shutil.rmtree(vault)
    forbidden = [p for p in stage.rglob('*') if p.is_file() and re.search(r'correction|corrig[eé]', p.name, re.I)]
    assert not forbidden, forbidden
    assert not any(':::' in p.read_text(encoding='utf-8') for p in stage.rglob('*.md'))
    content = ROOT / 'content'
    assert content.resolve().parent == ROOT.resolve()
    if content.exists(): shutil.rmtree(content)
    stage.rename(content)
    write(ROOT / 'chapters.json', json.dumps(chapters, ensure_ascii=False, indent=2) + '\n')
    print('Préparation : 10 cours, 10 versions interactives, 7 TP, archive Obsidian. Aucune correction publiée.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=Path, default=DEFAULT_SOURCE)
    prepare(parser.parse_args().source)
