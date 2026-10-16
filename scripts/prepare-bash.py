"""Integrate the student Bash course and the two-track home into Linux's site."""
from pathlib import Path
import html
import json
import re
import runpy
import shutil
import zipfile
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path('C:/Users/kayaw/Nextcloud/Obsidian/CoffreSam/Formations/linux-scripting-bash')
BASE = 'https://kayasam.github.io/linux-initiation'
RESOURCE_UI = runpy.run_path(str(ROOT / 'scripts/course-resources.py'))['render_resources']


def write(path, body):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding='utf-8')


def normalize(body):
    kinds = {'info': 'NOTE', 'success': 'TIP', 'warning': 'WARNING', 'danger': 'DANGER'}
    def callout(match):
        return '> [!' + kinds.get(match[1], 'NOTE') + ']\n' + '\n'.join('> ' + line for line in match[2].strip().splitlines())
    return re.sub(r'^:::(\w+)\s*\n(.*?)^:::\s*$', callout, body, flags=re.M | re.S).strip() + '\n'


def public_course_links(body, source_file, courses):
    """Resolve vault chapter links to their public routes, retaining anchors."""
    targets = {}
    for course in courses:
        targets[course.resolve()] = f'{BASE}/bash/{course.stem}/'
        targets[course.with_suffix('.html').resolve()] = f'{BASE}/bash/cours/{course.stem}-interactif.html'
    def convert(link):
        parsed = urlsplit(html.unescape(link))
        if parsed.scheme or parsed.netloc or not parsed.path:
            return link
        target = (source_file.parent / unquote(parsed.path)).resolve()
        if target not in targets:
            return link
        return targets[target] + ('?' + parsed.query if parsed.query else '') + ('#' + parsed.fragment if parsed.fragment else '')
    body = re.sub(r'(\]\()([^\s)]+)', lambda m: m[1] + convert(m[2]), body)
    return re.sub(r'''(\bhref\s*=\s*["'])([^"']+)(["'])''', lambda m: m[1] + convert(m[2]) + m[3], body)


def metadata(title, body, aliases=None):
    old_routes = '\naliases: ' + json.dumps(aliases) if aliases else ''
    return '---\ntitle: ' + json.dumps(title, ensure_ascii=False) + old_routes + '\n---\n\n' + body


def is_published(path):
    text = path.read_text(encoding='utf-8-sig')
    frontmatter = re.match(r'^---\s*\n(.*?)\n---(?:\n|$)', text, re.S)
    return bool(frontmatter and re.search(r'^publier:\s*true\s*$', frontmatter[1], re.M | re.I))


def without_frontmatter(text):
    return re.sub(r'^---\s*\n.*?\n---\s*\n', '', text, count=1, flags=re.S)


def published_correction(tp):
    candidates = [tp.with_name(tp.stem + suffix) for suffix in ('-correction.md', '-corrigev2.md', '-Corrigév2.md')]
    published = [path for path in candidates if path.is_file() and is_published(path)]
    assert len(published) <= 1, f'Plusieurs corrigés cochés pour {tp.name} : {published}'
    return published[0] if published else None


def title_of(path):
    return re.sub(r'^(?:Chapitre|TP)\s*\d+\s*[—–-]\s*', '', re.search(r'^#\s+(.*)', path.read_text(encoding='utf-8-sig'), re.M)[1])


def card(number, title, url):
    return f'<a class="home-chapter" href="{url}"><span class="home-chapter__number">{number}</span><strong>{html.escape(title)}</strong><span class="home-chapter__arrow" aria-hidden="true">→</span></a>'


def track(key, title, description, cards, first, icon):
    return f'''<section class="home-track home-track--{key}" id="{key}" aria-labelledby="{key}-title">
<div class="home-track__head"><div class="home-track__logo"><img src="./assets/brands/{icon}" alt="{'Tux, mascotte Linux' if key == 'linux' else 'Logo Bash'}" /></div><div class="home-track__heading"><h2 id="{key}-title">{title}</h2><p>{description}</p></div><a class="home-track__start" href="{first}">Commencer au chapitre 01 →</a></div>
<div class="home-chapter-grid">{cards}</div></section>'''


def populate(destination, chapters):
    shutil.copytree(ROOT / 'site-content/assets/brands', destination / 'assets/brands', dirs_exist_ok=True)
    courses = sorted(p for p in (SOURCE / 'cours').glob('[0-9][0-9]-*/*.md') if p.stem == p.parent.name)
    assert len(courses) == 6, 'Six cours Bash attendus'
    candidates = list((SOURCE / 'cours').glob('*/tp/tp-*.md')) + list((SOURCE / 'tp').glob('*/tp-*.md'))
    tps = sorted(p for p in candidates if not re.search(r'correction|corrig', p.name, re.I))
    routes = {p: (f'bash/{p.parent.parent.name}/tp' if p.is_relative_to(SOURCE / 'cours') else f'bash/annexe/{p.stem}') for p in tps}
    for tp in tps:
        if tp.is_relative_to(SOURCE / 'cours') and sum(p.parent == tp.parent for p in tps) > 1:
            routes[tp] += '/' + tp.stem
    export = {}
    published_corrections = set()
    export.update(runpy.run_path(str(ROOT / 'scripts/prepare-bash-quizzes.py'))['populate'](SOURCE,destination,courses))
    game = SOURCE / 'jeu'
    export.update(runpy.run_path(str(ROOT / 'scripts/package-orion.py'))['package'](game, destination))
    game_page = (game / 'README.md').read_text(encoding='utf-8')
    game_page += f'\n\n[Télécharger Orion Académie]({BASE}/telechargements/bash/orion-academie.tar.gz) · [← Parcours Bash]({BASE}/#bash)\n'
    write(destination / 'bash/annexe/orion-academie.md', metadata('Orion Académie — Le jeu', game_page, ['bash/jeu/index']))
    images = SOURCE / 'Ressources/images'
    if images.is_dir():
        shutil.copytree(images, destination / 'bash/images', dirs_exist_ok=True)
        for image in sorted(images.glob('bash-*.svg')):
            export['Ressources/images/' + image.name] = image.read_bytes()
    bash_cards = []
    for course in courses:
        slug, title = course.stem, title_of(course)
        offline_body = normalize(course.read_text(encoding='utf-8-sig'))
        body = re.sub(r'\n\n<!-- ressources-locales -->\n(?:>[^\n]*\n)+', '', offline_body)
        body = body.replace('../../Ressources/images/', BASE + '/bash/images/')
        body = public_course_links(body, course, courses)
        html_name = f'{slug}-interactif.html'
        matching = [p for p in tps if p.parent == course.parent / 'tp']
        for exercise in matching:
            body = body.replace(f'](tp/{exercise.name})', f']({BASE}/{routes[exercise]})')
        links = RESOURCE_UI(destination, BASE, 'bash/' + slug, slug, bool(matching), f'{slug[:2]}. {title}')
        site_body = re.sub(r'^(# .+)$', lambda m: m[0] + links, body, count=1, flags=re.M)
        site_body += f'\n[← Parcours Bash]({BASE}/#bash) · [Tous les TP Bash]({BASE}/bash/tp/)\n'
        write(destination / 'bash' / slug / 'index.md', metadata(f'{slug[:2]}. {title}', site_body))
        write(destination / 'telechargements/bash/cours' / course.name, body)
        interactive = course.with_suffix('.html').read_text(encoding='utf-8-sig')
        offline = interactive
        interactive = public_course_links(interactive, course.with_suffix('.html'), courses)
        interactive = interactive.replace('../../Ressources/images/', BASE + '/bash/images/')
        for linked in courses:
            interactive = interactive.replace(f'href="../{linked.stem}/{linked.stem}.html"', f'href="{BASE}/bash/cours/{linked.stem}-interactif.html"')
        interactive = interactive.replace(f'href="{course.name}"', f'href="{BASE}/bash/{slug}/"')
        interactive = interactive.replace(f'href="{slug}-quiz.html"', f'href="{BASE}/bash/cours/quiz/{slug}.html"').replace(f'src="{slug}-quiz.html"', f'src="{BASE}/bash/cours/quiz/{slug}.html"')
        interactive = interactive.replace(f'data-quiz-src="{slug}-quiz.html"', f'data-quiz-src="{BASE}/bash/cours/quiz/{slug}.html"')
        for exercise in matching:
            interactive = interactive.replace(f'href="tp/{exercise.name}"', f'href="{BASE}/{routes[exercise]}"')
        theme = '<link rel="stylesheet" href="../../assets/themes/theme.css">\n<script src="../../assets/themes/theme.js"></script>\n'
        if 'assets/themes/theme.css' not in interactive:
            interactive = interactive.replace('</head>', theme + '</head>', 1)
        # A course link opens the rendered course; downloading is an explicit second action.
        back = f'<a href="{BASE}/bash/{slug}/">← Le cours en Markdown</a>'
        actions = back + f'<a class="companion-download" href="{BASE}/telechargements/bash/cours/{slug}.md" download>↓ Télécharger le .md</a>'
        assert back in interactive, f'Lien retour du compagnon manquant : {slug}'
        interactive = interactive.replace(back, actions, 1)
        interactive = interactive.replace('</style>', '.toolbar .companion-download{border:1px solid var(--border);border-radius:8px;padding:6px 10px;color:var(--text);font-size:.78rem;background:var(--surface)}\n</style>', 1)
        write(destination / 'bash/cours' / html_name, interactive)
        export[course.relative_to(SOURCE).as_posix()] = offline_body
        export[course.with_suffix('.html').relative_to(SOURCE).as_posix()] = offline
        bash_cards.append(card(slug[:2], title, f'./bash/{slug}/'))
    tp_links = []
    for tp in tps:
        offline_body = normalize(tp.read_text(encoding='utf-8-sig'))
        body = offline_body
        body = public_course_links(body, tp, courses)
        for sibling in tps:
            if sibling.parent == tp.parent:
                body = body.replace(f']({sibling.name})', f']({BASE}/{routes[sibling]})')
        if tp.is_relative_to(SOURCE / 'cours'):
            slug = tp.parent.parent.name
            body = body.replace(f'](../{slug}.md)', f']({BASE}/bash/{slug}/)')
            body += f'\n[← Revenir au cours]({BASE}/bash/{slug}/)\n'
        correction = published_correction(tp)
        if correction:
            published_corrections.add(correction.name)
            correction_route = routes[tp].rsplit('/', 1)[0] + '/' + correction.stem
            original = normalize(without_frontmatter(correction.read_text(encoding='utf-8-sig')))
            offline_body += f'\n[Correction du TP]({correction.name})\n'
            export[correction.relative_to(SOURCE).as_posix()] = original
            correction_body = public_course_links(original, correction, courses)
            for sibling in tps:
                if sibling.parent == tp.parent:
                    correction_body = correction_body.replace(f']({sibling.name})', f']({BASE}/{routes[sibling]})')
            correction_body += f'\n[← Énoncé du TP]({BASE}/{routes[tp]})\n'
            aliases = [f'bash/ateliers/{correction.stem}'] if not tp.is_relative_to(SOURCE / 'cours') else None
            write(destination / (correction_route + '.md'), metadata('Correction — ' + title_of(tp), correction_body, aliases))
            write(destination / 'telechargements/bash/tp' / correction.name, correction_body)
            body += f'\n[Correction du TP]({BASE}/{correction_route})\n'
        links = f'\n[← Parcours Bash]({BASE}/#bash)\n\n<a href="{BASE}/telechargements/bash/tp/{tp.name}" download>Télécharger le TP en Markdown</a>\n'
        aliases = [f'bash/ateliers/{tp.stem}'] if not tp.is_relative_to(SOURCE / 'cours') else None
        write(destination / (routes[tp] + '.md'), metadata(f'TP {tp.parent.parent.name[:2]}' if tp.is_relative_to(SOURCE / 'cours') else title_of(tp), body + links, aliases))
        write(destination / 'telechargements/bash/tp' / tp.name, body)
        export[tp.relative_to(SOURCE).as_posix()] = offline_body
        tp_links.append(f'- [{title_of(tp)}]({BASE}/{routes[tp]})')
        # Preserve previously published URLs without duplicating TP in the explorer.
        target = f'{BASE}/{routes[tp]}'
        write(destination / 'bash/tp' / (tp.stem + '.html'), f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0;url={target}"><link rel="canonical" href="{target}"><title>TP Bash</title></head><body><a href="{target}">Ouvrir le TP</a></body></html>')
    write(destination / 'bash/tp/index.md', metadata('Travaux pratiques', '# Travaux pratiques Bash\n\n' + '\n'.join(tp_links) + f'\n\n[← Parcours Bash]({BASE}/#bash)\n'))
    for course in courses:
        matching = [p for p in tps if p.parent == course.parent / 'tp']
        if len(matching) > 1:
            title = 'Travaux pratiques — ' + title_of(course)
            body = '# ' + title + '\n\n' + '\n\n'.join(f'- [{title_of(p)}]({BASE}/{routes[p]})' for p in matching)
            write(destination / 'bash' / course.stem / 'tp.md', metadata(title, body))
    workshops = [p for p in tps if not p.is_relative_to(SOURCE / 'cours')]
    workshop_ui = runpy.run_path(str(ROOT / 'scripts/workshop-resources.py'))
    workshop_entries = workshop_ui['entries'](workshops, routes, BASE, published_correction)
    write(destination / 'assets/workshops.json', json.dumps(workshop_entries, ensure_ascii=False, indent=2) + '\n')
    workshop_ui['attach_resources'](destination, workshop_entries)
    write(destination / 'bash/annexe/index.md', metadata('Annexe', workshop_ui['overview'](workshop_entries, BASE), ['bash/ateliers/index']))
    write(destination / 'bash/index.md', metadata('Bash — Le parcours', '# Scripting Bash\n\n' + '\n'.join(f'- [{title_of(c)}]({BASE}/bash/{c.stem}/)' for c in courses) + f'\n\n[Travaux pratiques]({BASE}/bash/tp/) · [Annexe]({BASE}/bash/annexe/)\n'))
    export['README.md'] = '# Scripting Bash\n\nOuvrez ce dossier dans Obsidian. Chaque chapitre est dans `cours/<chapitre>/` avec son cours Markdown, sa version HTML et son dossier `tp/`. Les exercices transversaux sont dans `tp/synthese/`, `tp/final/` et `tp/bonus/`. Seules les corrections explicitement publiées sont incluses.\n'
    export['cours/README.md'] = (SOURCE / 'cours/README.md').read_text(encoding='utf-8-sig')
    with zipfile.ZipFile(destination / 'linux-scripting-bash-obsidian.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
        for name, body in export.items():
            entry = zipfile.ZipInfo('Linux-scripting-bash/' + name, date_time=(2020, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(entry, body)
    linux_cards = ''.join(card(c['slug'][:2], c['title'], f'./{c["slug"]}/') for c in chapters)
    linux_overview = '# Linux initiation\n\n' + '\n'.join(f'- [{c["slug"][:2]}. {c["title"]}]({BASE}/{c["slug"]}/)' for c in chapters)
    linux_overview += f'\n\n[Télécharger le coffre Obsidian]({BASE}/linux-initiation-obsidian.zip)\n'
    write(destination / 'linux-initiation/index.md', metadata('Linux initiation', linux_overview))
    home = '''<header class="home-header"><h1>Linux initiation &amp; Bash</h1><p>Deux parcours pour prendre en main Linux et automatiser vos tâches.</p><nav class="home-shortcuts" aria-label="Choisir une formation"><a href="#linux">Linux initiation <span>10 chapitres ↓</span></a><a href="#bash">Bash <span>6 chapitres ↓</span></a></nav></header>'''
    home += track('linux', 'Linux initiation', 'Découvrez Debian, le terminal, les fichiers, les permissions, le réseau et SSH.', linux_cards, './01-comprendre-linux/', 'tux.svg')
    home += track('bash', 'Bash', 'Passez des commandes aux scripts : variables, conditions, boucles et traitement de texte.', ''.join(bash_cards), './bash/01-shell-et-environnement/', 'bash.png')
    home += f'''<section class="home-downloads"><h2>Supports hors ligne</h2><div class="home-downloads__grid"><a href="./linux-initiation-obsidian.zip" download><strong>Linux initiation</strong><span>10 cours, versions interactives, quiz et {sum(c['tp'] is not None for c in chapters)} TP.</span><em>Télécharger le ZIP →</em></a><a href="./linux-scripting-bash-obsidian.zip" download><strong>Bash</strong><span>6 cours, versions HTML et {len(tps)} TP pour Obsidian.</span><em>Télécharger le ZIP →</em></a><a class="home-pdf-download" href="{BASE}/telechargements/linux-initiation-et-bash.pdf" download><strong>Tous les cours en PDF</strong><span>Les 16 chapitres Linux et Bash réunis, avec sommaire.</span><em>Télécharger le PDF →</em></a></div></section>'''
    home += '<p class="brand-credits">Tux : Larry Ewing et The GIMP, Simon Budig, Garrett LeSage. <a href="./assets/brands/TUX-COPYRIGHT.txt">Crédits Tux</a> · <a href="https://commons.wikimedia.org/wiki/File:Bash_Logo_Colored.svg">Logo Bash</a></p>'
    write(destination / 'index.md', metadata('Linux initiation & Bash', home))
    assert not any(re.search(r'correction|corrig', Path(name).name, re.I) and Path(name).name not in published_corrections for name in export)
    print(f'Bash : {len(courses)} cours, {len(tps)} TP, {len(published_corrections)} correction(s) explicitement publiée(s).')
    return published_corrections


if __name__ == '__main__':
    populate(ROOT / 'content', json.loads((ROOT / 'chapters.json').read_text(encoding='utf-8-sig')))
