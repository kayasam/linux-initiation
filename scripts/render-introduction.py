"""Prepare the visual companion for chapter 01 and its original SVG."""
from pathlib import Path
import runpy

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

# The interactive companion is intentionally authored separately from the full course.
page = (ROOT / 'templates/introduction-interactive.html').read_text(encoding='utf-8')
course.with_suffix('.html').write_text(page, encoding='utf-8')
print('HTML interactif du chapitre 01 : onglets, frise, portraits et activités.')
