"""Prepare student content; corrections require an explicit publier: true."""
from pathlib import Path
import argparse
import runpy
import html
import json
import re
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://kayasam.github.io/linux-initiation'
RESOURCE_UI = runpy.run_path(str(ROOT / 'scripts/course-resources.py'))['render_resources']
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

def themed_html(body, slug):
    if 'data-chapter=' not in body:
        body = body.replace('<html lang="fr">', f'<html lang="fr" data-chapter="{slug}">', 1)
    if 'assets/themes/theme.css' not in body:
        body = body.replace('</head>', '<link rel="stylesheet" href="assets/themes/theme.css">\n<script src="assets/themes/theme.js"></script>\n</head>', 1)
    return body

def flat_html(body, slug):
    """Keep existing public/offline URLs while the source uses chapter folders."""
    body = themed_html(body, slug)
    body = body.replace('../../Ressources/images/', '../Ressources/images/')
    body = body.replace('../../assets/themes/', 'assets/themes/')
    body = re.sub(r'href="\.\./(\d\d-[^/"<>]+)/\1\.html"', r'href="\1.html"', body)
    return re.sub(r'\s+data-quiz-href="[^"]*"', '', body)

def public_markdown(body, courses):
    for course in courses:
        slug = course.stem
        body = body.replace(f'](quiz/{slug}.html)', f']({BASE}/cours/quiz/{slug}.html)')
        body = body.replace(f']({slug}.md)', f']({BASE}/{slug}/)')
    return body.replace('../Ressources/images/', BASE + '/ressources/images/')

def is_published(file):
    body = file.read_text(encoding='utf-8-sig')
    frontmatter = re.match(r'^---\s*\n(.*?)\n---(?:\n|$)', body, re.S)
    return bool(frontmatter and re.search(r'^publier:\s*true\s*$', frontmatter[1], re.M | re.I))

def without_frontmatter(body):
    return re.sub(r'^---\s*\n.*?\n---\s*\n', '', body, count=1, flags=re.S)

def prepare(source):
    courses = sorted(p for p in (source / 'cours').rglob('[0-9][0-9]-*.md') if p.parent == source / 'cours' or p.parent.name == p.stem)
    assert len(courses) == 10, '10 chapitres attendus'
    chapters = []
    published_corrections = set()
    stage = ROOT / '.publication-stage'
    # Resolve the target before removing only our generated staging directory.
    assert stage.resolve().parent == ROOT.resolve()
    if stage.exists(): shutil.rmtree(stage)
    shutil.copytree(ROOT / 'site-content', stage)
    shutil.copytree(ROOT / 'site-content/assets/themes', stage / 'cours/assets/themes', dirs_exist_ok=True)
    vault = stage / 'telechargements' / 'Linux-initiation'
    images = source / 'Ressources' / 'images'
    if images.is_dir():
        for destination in (stage / 'ressources/images', vault / 'Ressources/images'):
            shutil.copytree(images, destination, dirs_exist_ok=True)
    for i, course in enumerate(courses):
        slug = course.stem
        title = re.search(r'^#\s+(.*)', course.read_text(encoding='utf-8'), re.M)[1]
        title = re.sub(r'^Chapitre \d+\s*[—–-]\s*', '', title)
        number = slug[:2]
        tp_folder = course.parent / 'tp' if course.parent.name == slug else source / 'sessions/2026-05'
        tps = [p for p in tp_folder.glob(f'tp-{number}-*.md') if not re.search(r'correction|corrig', p.name, re.I)]
        assert len(tps) <= 1
        tp = tps[0] if tps else None
        body = normalize(course.read_text(encoding='utf-8'))
        body = re.sub(r'\n\n<!-- ressources-locales -->\n(?:>[^\n]*\n)+', '', body)
        body = body.replace('../../Ressources/images/', '../Ressources/images/')
        for linked in courses:
            linked_slug = linked.stem
            body = body.replace(f'](../{linked_slug}/{linked_slug}.md)', f']({linked_slug}.md)')
            body = body.replace(f']({linked_slug}-quiz.html)', f'](quiz/{linked_slug}.html)')
        write(vault / 'cours' / course.name, body)
        write(stage / 'telechargements' / 'cours' / course.name, public_markdown(body, courses))
        interactive = flat_html(course.with_suffix('.html').read_text(encoding='utf-8'), slug)
        interactive = interactive.replace('../Ressources/images/', '../ressources/images/')
        interactive = interactive.replace(f'href="{slug}-quiz.html"', f'href="quiz/{slug}.html"')
        for linked in courses:
            interactive = interactive.replace(f'href="{linked.stem}.html"', f'href="{BASE}/{linked.stem}/"')
            interactive = interactive.replace(f'href="{linked.stem}.md"', f'href="{BASE}/{linked.stem}/"')
        nav = f'<div class="course-site-nav"><a href="{BASE}/{slug}/">← Le cours en Markdown</a><a class="companion-download" href="{BASE}/telechargements/cours/{slug}.md" download>↓ Télécharger le .md</a><a href="quiz/{slug}.html">Quiz du chapitre →</a></div>'
        interactive = interactive.replace('<body>', '<body>\n' + nav, 1)
        interactive = interactive.replace('</style>', '.course-site-nav { display:flex; justify-content:space-between; gap:1rem; padding:.8rem 1rem; background:#1a1d27; flex-wrap:wrap; } .course-site-nav a {color:#93c5fd; font-weight:600;} .course-site-nav .companion-download {border:1px solid currentColor;border-radius:8px;padding:4px 10px;font-size:.8rem;text-decoration:none;}\n</style>', 1)
        write(stage / 'cours' / f'{slug}-interactif.html', interactive)
        # Offline interactive pages keep a working return link and their own quiz.
        offline = flat_html(course.with_suffix('.html').read_text(encoding='utf-8'), slug)
        offline = offline.replace(f'href="{slug}-quiz.html"', f'href="quiz/{slug}.html"')
        write(vault / 'cours' / f'{slug}.html', offline)
        links = RESOURCE_UI(stage, BASE, slug, slug, tp is not None)
        if tp:
            tpbody = normalize(tp.read_text(encoding='utf-8'))
            for correction in sorted(tp_folder.glob(f'tp-{number}-*correction.md')):
                if not is_published(correction): continue
                published_corrections.add(correction.name)
                correction_body = normalize(without_frontmatter(correction.read_text(encoding='utf-8')))
                correction_body += f'\n[← Énoncé du TP]({BASE}/{slug}/tp)\n'
                write(stage / slug / correction.name, metadata(f'Correction TP {number} — {title}', correction_body))
                write(stage / 'telechargements/tp' / correction.name, correction_body)
                write(vault / 'tp' / correction.name, normalize(correction.read_text(encoding='utf-8')))
                tpbody += f'\n[Correction du TP]({BASE}/{slug}/{correction.stem})\n'
            write(vault / 'tp' / tp.name, tpbody.replace(f'](../{slug}.md)', f'](../cours/{slug}.md)'))
            tpbody = tpbody.replace(f'](../{slug}.md)', f']({BASE}/{slug}/)')
            write(stage / 'telechargements' / 'tp' / tp.name, tpbody)
            write(stage / slug / 'tp.md', metadata(f'TP {number} — {title}', tpbody + f'\n[← Revenir au cours]({BASE}/{slug}/)\n\n<a href="{BASE}/telechargements/tp/{tp.name}" download>Télécharger ce TP en Markdown</a>\n'))
        body = re.sub(r'^(# .+)$', lambda m: m[0] + links, body, count=1, flags=re.M)
        previous = f'[← {chapters[-1]["title"]}]({BASE}/{chapters[-1]["slug"]}/)' if chapters else '[← Accueil](' + BASE + '/)'
        following = f'[Chapitre suivant →]({BASE}/{courses[i+1].stem}/)' if i+1 < len(courses) else f'[Revenir à l’accueil →]({BASE}/)'
        body = public_markdown(body, courses)
        write(stage / slug / 'index.md', metadata(f'{number}. {title}', body + '\n---\n\n' + previous + ' · ' + following + '\n'))
        chapters.append(dict(slug=slug, title=title, tp=tp.name if tp else None))
    for tp in source.rglob('tp-*.md'):
        if 'correction' in tp.name and tp.name not in published_corrections: continue
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
<section class="home-downloads"><h2>Supports hors ligne</h2><div class="home-downloads__grid"><a href="./linux-initiation-obsidian.zip" download><strong>Le cours pour Obsidian</strong><span>Les 10 cours Markdown, les 10 versions interactives et les 7 TP.</span><em>Télécharger le ZIP →</em></a></div></section>'''
    tp_count = sum(c['tp'] is not None for c in chapters)
    home = home.replace('sept travaux pratiques', f'{tp_count} travaux pratiques').replace('les 7 TP', f'les {tp_count} TP')
    write(stage / 'index.md', metadata('Linux — Initiation', home))
    write(vault / 'README.md', '# Linux — Initiation\n\nOuvrez ce dossier comme coffre dans Obsidian. Les cours se trouvent dans `cours/` et les exercices dans `tp/`. Ouvrez les fichiers HTML dans votre navigateur pour les versions interactives.\n\n' + '\n'.join(f'- [{c["title"]}](cours/{c["slug"]}.md)' for c in chapters))
    archive = stage / 'linux-initiation-obsidian.zip'
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
        for file in sorted(vault.rglob('*')):
            if file.is_file():
                entry = zipfile.ZipInfo(file.relative_to(vault.parent).as_posix(), date_time=(2020, 1, 1, 0, 0, 0))
                entry.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(entry, file.read_bytes())
    shutil.rmtree(vault)
    # Keep the shared home and Bash course in every normal publication.
    runpy.run_path(str(ROOT / 'scripts/prepare-bash.py'))['populate'](stage, chapters)
    forbidden = [p for p in stage.rglob('*') if p.is_file() and re.search(r'correction|corrig[eé]', p.name, re.I) and p.name not in published_corrections]
    assert not forbidden, forbidden
    assert not any(':::' in p.read_text(encoding='utf-8') for p in stage.rglob('*.md'))
    content = ROOT / 'content'
    assert content.resolve().parent == ROOT.resolve()
    if content.exists(): shutil.rmtree(content)
    stage.rename(content)
    write(ROOT / 'chapters.json', json.dumps(chapters, ensure_ascii=False, indent=2) + '\n')
    write(ROOT / 'publication-policy.json', json.dumps({'corrections': sorted(published_corrections)}, ensure_ascii=False, indent=2) + '\n')
    print(f'Préparation : 10 cours, 10 versions interactives, {tp_count} TP, archive Obsidian. {len(published_corrections)} correction(s) explicitement publiée(s).')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=Path, default=DEFAULT_SOURCE)
    prepare(parser.parse_args().source)
