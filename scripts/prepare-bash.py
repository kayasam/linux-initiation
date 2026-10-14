"""Integrate the student Bash course and the two-track home into Linux's site."""
from pathlib import Path
import html
import json
import re
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path('C:/Users/kayaw/Nextcloud/Obsidian/CoffreSam/Formations/linux-scripting-bash')
BASE = 'https://kayasam.github.io/linux-initiation'


def write(path, body):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding='utf-8')


def normalize(body):
    kinds = {'info': 'NOTE', 'success': 'TIP', 'warning': 'WARNING', 'danger': 'DANGER'}
    def callout(match):
        return '> [!' + kinds.get(match[1], 'NOTE') + ']\n' + '\n'.join('> ' + line for line in match[2].strip().splitlines())
    return re.sub(r'^:::(\w+)\s*\n(.*?)^:::\s*$', callout, body, flags=re.M | re.S).strip() + '\n'


def metadata(title, body):
    return '---\ntitle: ' + json.dumps(title, ensure_ascii=False) + '\n---\n\n' + body


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
    routes = {p: (f'bash/{p.parent.parent.name}/tp' if p.is_relative_to(SOURCE / 'cours') else f'bash/ateliers/{p.stem}') for p in tps}
    export = {}
    bash_cards = []
    for course in courses:
        slug, title = course.stem, title_of(course)
        offline_body = normalize(course.read_text(encoding='utf-8-sig'))
        body = re.sub(r'\n\n<!-- ressources-locales -->\n(?:>[^\n]*\n)+', '', offline_body)
        html_name = f'{slug}-interactif.html'
        links = f'\n\n> [!TIP] Ressources du chapitre\n> - [Version HTML interactive]({BASE}/bash/cours/{html_name})\n> - <a href="{BASE}/telechargements/bash/cours/{course.name}" download>Télécharger le cours en Markdown</a>\n'
        matching = [p for p in tps if p.parent == course.parent / 'tp']
        if matching:
            links += f'> - [Passer au TP]({BASE}/{routes[matching[0]]})\n'
            body = body.replace(f'](tp/{matching[0].name})', f']({BASE}/{routes[matching[0]]})')
        site_body = re.sub(r'^(# .+)$', lambda m: m[0] + links, body, count=1, flags=re.M)
        site_body += f'\n[← Parcours Bash]({BASE}/#bash) · [Tous les TP Bash]({BASE}/bash/tp/)\n'
        write(destination / 'bash' / slug / 'index.md', metadata(f'{slug[:2]}. {title}', site_body))
        write(destination / 'telechargements/bash/cours' / course.name, body)
        interactive = course.with_suffix('.html').read_text(encoding='utf-8-sig')
        offline = interactive
        theme = '<link rel="stylesheet" href="../../assets/themes/theme.css">\n<script src="../../assets/themes/theme.js"></script>\n'
        interactive = interactive.replace('</head>', theme + '</head>', 1)
        nav = f'<nav class="bash-site-nav"><a href="{BASE}/bash/{slug}/">← Cours Markdown</a><a href="{BASE}/#bash">Parcours Bash →</a></nav>'
        interactive = interactive.replace('<body>', '<body>' + nav, 1)
        interactive = interactive.replace('</style>', '.bash-site-nav{display:flex;justify-content:space-between;gap:1rem;padding:1rem;flex-wrap:wrap}.bash-site-nav a{color:var(--accent);font-weight:700}\n</style>', 1)
        write(destination / 'bash/cours' / html_name, interactive)
        export[course.relative_to(SOURCE).as_posix()] = offline_body
        export[course.with_suffix('.html').relative_to(SOURCE).as_posix()] = offline
        bash_cards.append(card(slug[:2], title, f'./bash/{slug}/'))
    tp_links = []
    for tp in tps:
        offline_body = normalize(tp.read_text(encoding='utf-8-sig'))
        body = offline_body
        if tp.is_relative_to(SOURCE / 'cours'):
            slug = tp.parent.parent.name
            body = body.replace(f'](../{slug}.md)', f']({BASE}/bash/{slug}/)')
            body += f'\n[← Revenir au cours]({BASE}/bash/{slug}/)\n'
        links = f'\n[← Parcours Bash]({BASE}/#bash)\n\n<a href="{BASE}/telechargements/bash/tp/{tp.name}" download>Télécharger le TP en Markdown</a>\n'
        write(destination / (routes[tp] + '.md'), metadata(f'TP {tp.parent.parent.name[:2]}' if tp.is_relative_to(SOURCE / 'cours') else title_of(tp), body + links))
        write(destination / 'telechargements/bash/tp' / tp.name, body)
        export[tp.relative_to(SOURCE).as_posix()] = offline_body
        tp_links.append(f'- [{title_of(tp)}]({BASE}/{routes[tp]})')
        # Preserve previously published URLs without duplicating TP in the explorer.
        target = f'{BASE}/{routes[tp]}'
        write(destination / 'bash/tp' / (tp.stem + '.html'), f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0;url={target}"><link rel="canonical" href="{target}"><title>TP Bash</title></head><body><a href="{target}">Ouvrir le TP</a></body></html>')
    write(destination / 'bash/tp/index.md', metadata('Travaux pratiques', '# Travaux pratiques Bash\n\n' + '\n'.join(tp_links) + f'\n\n[← Parcours Bash]({BASE}/#bash)\n'))
    workshops = [p for p in tps if not p.is_relative_to(SOURCE / 'cours')]
    write(destination / 'bash/ateliers/index.md', metadata('Synthèse et bonus', '# Synthèse et bonus\n\n' + '\n'.join(f'- [{title_of(p)}]({BASE}/{routes[p]})' for p in workshops) + '\n'))
    write(destination / 'bash/index.md', metadata('Bash — Le parcours', '# Scripting Bash\n\n' + '\n'.join(f'- [{title_of(c)}]({BASE}/bash/{c.stem}/)' for c in courses) + f'\n\n[Travaux pratiques]({BASE}/bash/tp/)\n'))
    export['README.md'] = '# Scripting Bash\n\nOuvrez ce dossier dans Obsidian. Chaque chapitre est dans `cours/<chapitre>/` avec son cours Markdown, sa version HTML et son dossier `tp/`. Les exercices transversaux sont dans `tp/synthese/` et `tp/bonus/`. Les corrections sont exclues.\n'
    with zipfile.ZipFile(destination / 'linux-scripting-bash-obsidian.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
        for name, body in export.items():
            entry = zipfile.ZipInfo('Linux-scripting-bash/' + name, date_time=(2020, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(entry, body)
    linux_cards = ''.join(card(c['slug'][:2], c['title'], f'./{c["slug"]}/') for c in chapters)
    linux_overview = '# Linux initiation\n\n' + '\n'.join(f'- [{c["slug"][:2]}. {c["title"]}]({BASE}/{c["slug"]}/)' for c in chapters)
    linux_overview += f'\n\n[Programme et objectifs]({BASE}/ressources/)\n\n[Télécharger le coffre Obsidian]({BASE}/linux-initiation-obsidian.zip)\n'
    write(destination / 'linux-initiation/index.md', metadata('Linux initiation', linux_overview))
    home = '''<header class="home-header"><h1>Linux initiation &amp; Bash</h1><p>Deux parcours pour prendre en main Linux et automatiser vos tâches.</p><nav class="home-shortcuts" aria-label="Choisir une formation"><a href="#linux">Linux initiation <span>10 chapitres ↓</span></a><a href="#bash">Bash <span>6 chapitres ↓</span></a></nav></header>'''
    home += track('linux', 'Linux initiation', 'Découvrez Debian, le terminal, les fichiers, les permissions, le réseau et SSH.', linux_cards, './01-comprendre-linux/', 'tux.svg')
    home += track('bash', 'Bash', 'Passez des commandes aux scripts : variables, conditions, boucles et traitement de texte.', ''.join(bash_cards), './bash/01-shell-et-environnement/', 'bash.png')
    home += f'''<div class="home-links"><a href="./bash/tp/">Les {len(tps)} TP Bash →</a><a href="./ressources/">Programme Linux initiation →</a></div><section class="home-downloads"><h2>Supports hors ligne</h2><div class="home-downloads__grid"><a href="./linux-initiation-obsidian.zip" download><strong>Linux initiation</strong><span>10 cours, versions interactives, quiz et {sum(c['tp'] is not None for c in chapters)} TP.</span><em>Télécharger le ZIP →</em></a><a href="./linux-scripting-bash-obsidian.zip" download><strong>Bash</strong><span>6 cours, versions HTML et {len(tps)} TP pour Obsidian.</span><em>Télécharger le ZIP →</em></a></div></section>'''
    home += '<p class="brand-credits">Tux : Larry Ewing et The GIMP, Simon Budig, Garrett LeSage. <a href="./assets/brands/TUX-COPYRIGHT.txt">Crédits Tux</a> · <a href="https://commons.wikimedia.org/wiki/File:Bash_Logo_Colored.svg">Logo Bash</a></p>'
    write(destination / 'index.md', metadata('Linux initiation & Bash', home))
    assert not any(re.search(r'correction|corrig', name, re.I) for name in export)
    print(f'Bash : {len(courses)} cours, {len(tps)} TP, deux parcours et aucune correction.')


if __name__ == '__main__':
    populate(ROOT / 'content', json.loads((ROOT / 'chapters.json').read_text(encoding='utf-8-sig')))
