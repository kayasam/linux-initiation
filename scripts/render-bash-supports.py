"""Render standalone Bash lessons and explanatory SVGs from the vault Markdown."""
from pathlib import Path
import html
import re
try:
    import markdown
except ModuleNotFoundError:
    raise SystemExit('Installer le rendu Markdown : python -m pip install -r scripts/requirements-bash.txt')

SOURCE = Path('C:/Users/kayaw/Nextcloud/Obsidian/CoffreSam/Formations/linux-scripting-bash')
IMAGES = SOURCE / 'Ressources/images'
IMAGES.mkdir(parents=True, exist_ok=True)

DIAGRAMS = [
    ('01-terminal', 'De ta fenêtre à Debian', [('Terminal', 'Tu saisis une commande'), ('SSH', 'Le transport vers la VM'), ('Bash sur Debian', 'Il interprète la commande'), ('Résultat', 'Il revient dans le terminal')]),
    ('02-variables', 'Une valeur, un nom, une utilisation', [('prenom="Mila"', 'Affecter une valeur'), ('prenom', 'Le nom de la variable'), ('"$prenom"', 'Lire la valeur en un argument'), ('Bonjour Mila', 'Utiliser la valeur')]),
    ('03-script', 'Le cycle d’un petit script', [('Écrire', 'nano accueil.sh'), ('Vérifier', 'bash -n accueil.sh'), ('Exécuter', 'bash accueil.sh Mila'), ('Observer', 'Résultat et code de retour')]),
    ('04-condition', 'Une question choisit un chemin', [('Test', 'Le fichier existe-t-il ?'), ('Vrai', 'Lire le fichier'), ('Faux', 'Expliquer le problème'), ('Suite', 'Continuer ou terminer')]),
    ('05-boucle', 'Une action pour chaque élément', [('Liste', 'accueil.txt · radio.txt'), ('Premier passage', 'Traiter accueil.txt'), ('Deuxième passage', 'Traiter radio.txt'), ('Fin', 'Il ne reste aucun élément')]),
    ('06-colonnes', 'Une ligne, quatre champs séparés par ;', [('clavier', '$1 : produit'), ('informatique', '$2 : catégorie'), ('8', '$3 : quantité'), ('25', '$4 : prix unitaire')]),
]
for slug, title, cards in DIAGRAMS:
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="240" viewBox="0 0 1000 240" role="img" aria-labelledby="title"><title id="title">{html.escape(title)}</title><rect width="1000" height="240" rx="18" fill="#f4f8fc"/><text x="30" y="43" font-family="Segoe UI,sans-serif" font-size="24" font-weight="700" fill="#162c3d">{html.escape(title)}</text>'
    for i, (heading, subtitle) in enumerate(cards):
        x = 24 + i * 245
        svg += f'<rect x="{x}" y="78" width="218" height="122" rx="12" fill="white" stroke="#a4bdc8"/><text x="{x+16}" y="110" font-family="Segoe UI,sans-serif" font-size="14" font-weight="700" fill="#176e78">ÉTAPE {i+1}</text><text x="{x+16}" y="142" font-family="Segoe UI,sans-serif" font-size="19" font-weight="700" fill="#162c3d">{html.escape(heading)}</text><text x="{x+16}" y="174" font-family="Segoe UI,sans-serif" font-size="14" fill="#40566a">{html.escape(subtitle)}</text>'
        if i < 3:
            svg += f'<path d="M{x+223} 140h17m-6-6 6 6-6 6" fill="none" stroke="#176e78" stroke-width="2"/>'
    (IMAGES / f'bash-{slug}.svg').write_text(svg + '</svg>', encoding='utf-8')

# A condition branches: drawing it as a linear chain would imply both paths run.
(IMAGES / 'bash-04-condition.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="330" viewBox="0 0 1000 330" role="img" aria-labelledby="title"><title id="title">Une condition choisit une seule branche</title><rect width="1000" height="330" rx="18" fill="#f4f8fc"/><g font-family="Segoe UI,sans-serif" fill="#162c3d"><text x="30" y="40" font-size="24" font-weight="700">Une question, deux chemins possibles</text><path d="M500 65 620 112 500 159 380 112Z" fill="white" stroke="#176e78" stroke-width="2"/><text x="500" y="109" text-anchor="middle" font-size="17">Le fichier</text><text x="500" y="132" text-anchor="middle" font-size="17">existe-t-il ?</text><path d="M380 112H260V180M620 112H740V180" fill="none" stroke="#176e78" stroke-width="2"/><text x="285" y="100" font-size="17" font-weight="700">VRAI</text><text x="665" y="100" font-size="17" font-weight="700">FAUX</text><rect x="70" y="180" width="380" height="82" rx="12" fill="white" stroke="#176e78"/><rect x="550" y="180" width="380" height="82" rx="12" fill="white" stroke="#8b5b11"/><text x="260" y="215" text-anchor="middle" font-size="20" font-weight="700">Lire le fichier</text><text x="260" y="242" text-anchor="middle" font-size="16">Branche then</text><text x="740" y="215" text-anchor="middle" font-size="20" font-weight="700">Expliquer le problème</text><text x="740" y="242" text-anchor="middle" font-size="16">Branche else</text><text x="500" y="305" text-anchor="middle" font-size="18">Une seule branche est exécutée pour ce test.</text></g></svg>''', encoding='utf-8')

# Two separate lanes show that the parent keeps its own working directory.
(IMAGES / 'bash-01-sous-shell.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="590" viewBox="0 0 1000 590" role="img" aria-labelledby="title desc">
<title id="title">Le sous-shell se déplace, le parent reste dans son dossier</title>
<desc id="desc">Avant : le shell parent est dans le dossier personnel. Pendant : un sous-shell exécute cd /tmp et affiche /tmp, pendant que le parent attend. Après : le sous-shell se termine, et le parent affiche toujours son dossier personnel.</desc>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0 10 5 0 10Z" fill="#176e78"/></marker></defs>
<rect width="1000" height="590" rx="18" fill="#f4f8fc"/>
<g font-family="Segoe UI,sans-serif" fill="#162c3d">
<text x="30" y="42" font-size="26" font-weight="700">Deux shells, deux dossiers courants indépendants</text>
<text x="30" y="72" font-size="18">Exemple : on commence dans son dossier personnel (~).</text>
<rect x="35" y="105" width="280" height="135" rx="12" fill="white" stroke="#176e78" stroke-width="2"/>
<text x="55" y="137" font-size="17" fill="#176e78" font-weight="700">1 · AVANT — PARENT</text>
<text x="55" y="174" font-family="Consolas,monospace" font-size="23">pwd</text>
<text x="55" y="211" font-size="20">Résultat : dossier personnel</text>
<path d="M315 172H685" stroke="#667b8b" stroke-width="2" stroke-dasharray="7 6"/>
<text x="500" y="141" text-anchor="middle" font-size="18">Le parent attend.</text>
<text x="500" y="202" text-anchor="middle" font-size="18">Son dossier reste ~.</text>
<rect x="685" y="105" width="280" height="135" rx="12" fill="white" stroke="#176e78" stroke-width="2"/>
<text x="705" y="137" font-size="17" fill="#176e78" font-weight="700">3 · APRÈS — MÊME PARENT</text>
<text x="705" y="174" font-family="Consolas,monospace" font-size="23">pwd</text>
<text x="705" y="211" font-size="20">Résultat : dossier personnel</text>
<path d="M315 220H330V382H350" fill="none" stroke="#176e78" stroke-width="3" marker-end="url(#arrow)"/>
<text x="40" y="285" font-size="18">Début du groupe (</text>
<text x="40" y="310" font-size="18">Le sous-shell démarre.</text>
<rect x="360" y="315" width="280" height="145" rx="12" fill="#fff6e5" stroke="#8b5b11" stroke-width="2"/>
<text x="380" y="347" font-size="17" fill="#76500e" font-weight="700">2 · PENDANT — SOUS-SHELL</text>
<text x="380" y="382" font-family="Consolas,monospace" font-size="23">cd /tmp</text>
<text x="380" y="412" font-family="Consolas,monospace" font-size="23">pwd</text>
<text x="380" y="443" font-size="20">Résultat : /tmp</text>
<path d="M650 382H670V220H680" fill="none" stroke="#176e78" stroke-width="3" marker-end="url(#arrow)"/>
<text x="690" y="285" font-size="18">Fin du groupe )</text>
<text x="690" y="310" font-size="18">Le parent reprend.</text>
<rect x="30" y="490" width="940" height="76" rx="12" fill="white" stroke="#a4bdc8"/>
<text x="50" y="521" font-size="21" font-weight="700">Le cd agit uniquement dans le shell qui l'exécute.</text>
<text x="50" y="550" font-size="18">Le sous-shell se termine : son changement de dossier ne remonte pas au parent.</text>
</g></svg>''', encoding='utf-8')

CSS = '''
:root{color-scheme:light;--bg:#f4f7fa;--surface:#fff;--text:#172c3c;--text-dim:#455c6d;--accent:#176e78;--border:#c7d6df;--code-bg:#edf3f7;--ink:var(--text);--muted:var(--text-dim);--line:var(--border);--code:var(--code-bg)}
@media(prefers-color-scheme:dark){:root{color-scheme:dark;--bg:#0e1921;--surface:#172630;--text:#edf6fc;--text-dim:#b9cdd9;--accent:#81d9d9;--border:#405864;--code-bg:#10202a}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:18px/1.75 'Segoe UI',system-ui,sans-serif}main{max-width:920px;margin:auto;padding:30px 34px 70px;background:var(--surface)}a{color:var(--accent);text-underline-offset:3px}h1{font-size:2.2rem;line-height:1.2;margin:.5em 0 1em}h2{margin:2.3em 0 .7em;padding-top:.5em;border-top:1px solid var(--line);font-size:1.45rem;line-height:1.35}h3{font-size:1.15rem}p,ul,ol{margin:.8em 0}li{margin:.3em 0}code{font-family:'Cascadia Code',Consolas,monospace;font-size:.94em;background:var(--code);padding:.12em .3em;border-radius:4px}pre{padding:18px 20px;background:var(--code);border:1px solid var(--line);border-radius:10px;overflow-x:auto;line-height:1.6}pre code{padding:0;background:transparent;white-space:pre}table{display:block;overflow:auto;border-collapse:collapse;width:100%;margin:1em 0;font-size:.94em}th,td{text-align:left;padding:10px 13px;border-bottom:1px solid var(--line)}th{background:var(--code)}img{display:block;max-width:100%;height:auto;margin:1.4em auto;border-radius:12px}aside{border-left:4px solid var(--accent);padding:12px 18px;background:var(--code);border-radius:0 8px 8px 0;margin:1.2em 0}aside.warning{border-color:#b87913}aside p{margin:.3em 0}.lesson-nav{display:flex;flex-wrap:wrap;justify-content:space-between;gap:12px;padding:12px 0 22px;font-size:.9rem}.lesson-nav a{font-weight:650}.chapter-label{color:var(--muted);font-size:.83rem;font-weight:700;letter-spacing:.06em}summary{cursor:pointer;font-weight:650}details.toc{border:1px solid var(--line);border-radius:8px;padding:12px 18px;margin-bottom:25px}details.toc ul{margin:.4em 0}hr{border:0;border-top:1px solid var(--line);margin:2em 0}.table-wrap{overflow:auto}@media(max-width:620px){body{font-size:17px}main{padding:20px 18px 45px}h1{font-size:1.8rem}pre{padding:12px}}
'''


def callouts(body):
    def render(match):
        kind, title, rest = match.group(1), match.group(2), match.group(3)
        lines = [re.sub(r'^> ?', '', line) for line in rest.splitlines()]
        label = title.strip() or {'NOTE': 'Repère', 'TIP': 'Conseil', 'WARNING': 'Attention'}.get(kind, 'Repère')
        return f'\n<aside class="{kind.lower()}" markdown="1">\n**{label}**\n\n' + '\n'.join(lines) + '\n</aside>\n'
    return re.sub(r'^> \[!(NOTE|TIP|WARNING)\]([^\n]*)\n((?:>[^\n]*(?:\n|$))+)', render, body, flags=re.M)


courses = sorted(p for p in (SOURCE / 'cours').glob('*/*.md') if p.stem == p.parent.name)
assert len(courses) == 6
for index, course in enumerate(courses):
    body = course.read_text(encoding='utf-8-sig')
    body = re.sub(r'\n\n<!-- ressources-locales -->\n(?:>[^\n]*\n)+', '', body)
    title = re.search(r'^#\s+(.+)', body, re.M)[1]
    renderer = markdown.Markdown(extensions=['fenced_code', 'tables', 'toc', 'md_in_html'])
    article = renderer.convert(callouts(body))
    previous = f'<a href="../{courses[index-1].stem}/{courses[index-1].stem}.html">← Chapitre précédent</a>' if index else '<span>Début du parcours</span>'
    following = f'<a href="../{courses[index+1].stem}/{courses[index+1].stem}.html">Chapitre suivant →</a>' if index+1 < len(courses) else '<span>Fin du parcours</span>'
    nav = f'<nav class="lesson-nav" aria-label="Parcours">{previous}<a href="{course.name}">Cours Markdown</a>{following}</nav>'
    page = f'<!doctype html>\n<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} — Bash débutant</title><style>{CSS}</style></head><body><main>{nav}<p class="chapter-label">BASH · CHAPITRE {index+1:02d} / 06</p><details class="toc"><summary>Sommaire du chapitre</summary>{renderer.toc}</details>{article}{nav}</main></body></html>\n'
    course.with_suffix('.html').write_text(page, encoding='utf-8')
print('Bash : six HTML autonomes et sept schémas pédagogiques régénérés depuis le coffre.')
