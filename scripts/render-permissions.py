"""Prepare the interactive permissions laboratory without embedding SVGs."""
from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = Path('C:/Users/kayaw/Nextcloud/Obsidian/CoffreSam/Formations/linux-initiation')
parser = argparse.ArgumentParser()
parser.add_argument('--source', type=Path, default=DEFAULT_SOURCE)
args = parser.parse_args()
page = (ROOT / 'templates/permissions-interactive.html').read_text(encoding='utf-8')
assert '.svg' not in page and '<svg' not in page
target = args.source / 'cours/07-utilisateurs-et-permissions/07-utilisateurs-et-permissions.html'
assert target.is_file(), target
target.write_text(page, encoding='utf-8')
print('Chapitre 07 : identités, décodeur, atelier chmod, missions et quiz. Aucun SVG intégré.')
