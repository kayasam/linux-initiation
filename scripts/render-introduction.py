"""Render chapter 01 from the vault Markdown (requires Python Markdown)."""
from pathlib import Path
import html
import re
import runpy
import markdown

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path('C:/Users/kayaw/Nextcloud/Obsidian/CoffreSam/Formations/linux-initiation')
course = SOURCE / 'cours/01-comprendre-linux/01-comprendre-linux.md'

# Original vector: ideas inherited from Unix, two independent projects, one assembly.
Diagram = runpy.run_path(str(ROOT / 'scripts/illustrate-linux.py'))['Diagram']
d = Diagram('01', 'Unix, GNU, Linux : qui apporte quoi ?', 'Des principes hérités, des projets distincts et un système assemblé.')
d.box(55,116,890,90,'1969 — Unix',['Des principes : utilisateurs, fichiers et petits outils combinables.'])
d.text(500,244,'GNU et Linux sont des projets développés indépendamment d’Unix.','small','middle')
d.box(55,277,420,116,'1983 / 1984 — Projet GNU',['Richard Stallman','Des outils libres : Bash, GCC, ls, cp…'],True)
d.box(525,277,420,116,'1991 — Noyau Linux',['Linus Torvalds','Gestion du processeur et de la mémoire'],True)
d.arrow(265,401,380,447);d.arrow(735,401,620,447)
d.box(175,455,650,80,'Une distribution GNU/Linux — exemple : Debian',['GNU + Linux + d’autres composants et applications'])
d.note('Ces flèches montrent un assemblage de composants, pas une filiation du code d’Unix.')
d.save(SOURCE / 'Ressources/images/01-unix-gnu-linux.svg')

body = course.read_text(encoding='utf-8')
body = re.sub(r'^# .+\n', '', body, count=1)
body = re.sub(r'\n<!-- ressources-locales -->\n(?:>[^\n]*\n)+', '', body)
body = re.sub(r'<!--[^>]+-->', '', body)
body = re.sub(r'\]\(([^)]+)\.md\)', r'](\1.html)', body)

# Convert native Obsidian callouts while preserving their Markdown contents.
def callout(match):
    kind, title, content = match.groups()
    content = '\n'.join(re.sub(r'^> ?', '', line) for line in content.splitlines())
    kind = 'tip' if kind == 'TIP' else 'note'
    rendered = markdown.markdown(content, extensions=['tables', 'fenced_code'])
    return f'<aside class="callout {kind}"><p class="callout-title">{html.escape(title)}</p>{rendered}</aside>\n\n'
body = re.sub(r'^> \[!(NOTE|TIP)\] ([^\n]+)\n((?:>[^\n]*\n)*)', callout, body, flags=re.M)
renderer = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc'])
article = renderer.convert(body)
# SVGs open at full size; tables scroll within narrow screens.
article = re.sub(r'<img ([^>]+)>', r'<img \1 loading="lazy" style="width:100%;height:auto">', article)
article = article.replace('<table>', '<div class="table-wrap"><table>').replace('</table>', '</table></div>')
anchors = [(item['id'], item['name']) for item in renderer.toc_tokens]
nav = ''.join(f'<a href="#{html.escape(id)}">{html.escape(name)}</a>' for id, name in anchors)
page = '''<!DOCTYPE html>
<html lang="fr" data-chapter="01-comprendre-linux" data-quiz-href="01-comprendre-linux-quiz.html">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Comprendre Unix, GNU/Linux, le logiciel libre et ses licences, pas à pas avec des schémas, une vidéo et un quiz.">
<title>01 — Comprendre Linux</title>
<style>
:root{--bg:#f4f7fa;--surface:#fff;--surface2:#e5edf3;--text:#182d3e;--text-dim:#455d70;--accent:#006575;--accent2:#005969;--border:#8196a6;--code-bg:#eef3f7;--success:#17623c;--radius:14px}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:2rem}
body{margin:0;background:var(--bg);color:var(--text);font:17px/1.8 'Segoe UI',system-ui,sans-serif}
header{padding:3rem 1.5rem 2.4rem;border-bottom:1px solid var(--border);background:var(--surface)}
.hero{max-width:900px;margin:auto}.badge{display:inline-block;padding:.25rem .8rem;border-radius:30px;background:var(--surface2);color:var(--accent);font-size:.8rem;font-weight:700;letter-spacing:.05em}
h1{font-size:clamp(2rem,5vw,3rem);line-height:1.15;margin:1rem 0}.lead{font-size:1.12rem;color:var(--text-dim);max-width:65ch}
.layout{max-width:1240px;display:grid;grid-template-columns:230px minmax(0,1fr);gap:2.5rem;margin:auto;padding:2rem 1.5rem}
nav{align-self:start;position:sticky;top:1rem;border:1px solid var(--border);border-radius:var(--radius);padding:1rem;background:var(--surface)}
nav strong{display:block;margin-bottom:.6rem}nav a{display:block;font-size:.87rem;line-height:1.45;padding:.45rem 0;text-decoration:none}
main{min-width:0}h2{font-size:1.55rem;line-height:1.35;color:var(--accent2);margin:2rem 0 1rem}h3{font-size:1.12rem;line-height:1.5;margin:1.7rem 0 .8rem}
p{margin:.8rem 0 1.1rem}a{color:var(--accent2);text-underline-offset:3px}a:hover{text-decoration-thickness:2px}
hr{border:0;border-top:1px solid var(--border);margin:2.5rem 0}img{border-radius:var(--radius)}
.callout{padding:1rem 1.3rem;margin:1.5rem 0;border:1px solid var(--border);border-left:4px solid var(--accent);border-radius:var(--radius);background:var(--surface)}
.callout-title{font-weight:700;margin:0 0 .5rem}.callout p:last-child{margin-bottom:0}.callout.tip{border-left-color:var(--success)}
.table-wrap{overflow-x:auto;margin:1.3rem 0;border:1px solid var(--border);border-radius:var(--radius)}
table{border-collapse:collapse;width:100%;font-size:.94rem}th,td{text-align:left;padding:.8rem 1rem;border-bottom:1px solid var(--border);vertical-align:top}th{background:var(--surface2)}tr:last-child td{border-bottom:0}
pre{overflow-x:auto;background:var(--code-bg);padding:1.2rem;border-radius:var(--radius);border:1px solid var(--border);line-height:1.55}code{font: .9em Consolas,monospace}
details{padding:1rem 1.3rem;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);margin:1.5rem 0}summary{cursor:pointer;font-weight:700;color:var(--accent2)}
.quiz-section{padding:1rem 0 2rem}.course-quiz-frame{width:100%;height:1000px;border:0;border-radius:var(--radius);margin-top:1rem}.theme-toolbar{max-width:1240px;margin:auto}
footer{padding:1.5rem;text-align:center;color:var(--text-dim);border-top:1px solid var(--border)}
@media(max-width:900px){.layout{grid-template-columns:minmax(0,1fr);gap:1rem}nav{position:static}nav a{display:inline-block;margin-right:1rem}body{font-size:16px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
@media print{nav,.theme-toolbar,.quiz-section,iframe{display:none}.layout{display:block;padding:0}body{font-size:11pt}header{padding:0}details{break-inside:avoid}}
</style>
<link rel="stylesheet" href="../../assets/themes/theme.css">
<script src="../../assets/themes/theme.js"></script>
</head><body>
<header><div class="hero"><span class="badge">LINUX INITIATION · CHAPITRE 01</span><h1>Comprendre Linux</h1><p class="lead">Des origines d’Unix aux licences libres : les repères pour comprendre le système que vous allez utiliser.</p></div></header>
<div class="layout"><nav aria-label="Sommaire du chapitre"><strong>Dans ce chapitre</strong>''' + nav + '''<a href="#quiz-chapitre">Quiz · 20 questions</a></nav><main>
''' + article + '''
<section class="quiz-section" aria-labelledby="quiz-chapitre"><h2 id="quiz-chapitre">Quiz · 20 questions</h2><div id="tab-quiz"><a href="01-comprendre-linux-quiz.html">Ouvrir le quiz</a></div></section>
</main></div><footer>Linux initiation · Comprendre avant de pratiquer</footer>
</body></html>
'''
course.with_suffix('.html').write_text(page, encoding='utf-8')
print('Chapitre 01 HTML régénéré depuis le Markdown ; schéma Unix / GNU / Linux créé.')
