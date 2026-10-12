"""Bundle the same 20-question quizzes and theme controls for offline learning."""
from pathlib import Path
import argparse
import json
import zipfile
import runpy

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / 'content'
parser = argparse.ArgumentParser()
parser.add_argument('--sync-source', type=Path)
args = parser.parse_args()
banks = json.loads((CONTENT / 'assets/quiz/quiz-banks.js').read_text(encoding='utf-8').split('=', 1)[1])
offline_banks = {slug: {**bank, 'chapterLink': '../' + slug + '.html'} for slug, bank in banks.items()}
files = {}
for folder in ['assets/themes', 'cours/assets/themes']:
    for file in (CONTENT / folder).glob('*'):
        if file.is_file(): files[folder + '/' + file.name] = file.read_bytes()
for name in ['quiz.css', 'quiz-engine.js']:
    files['assets/quiz/' + name] = (CONTENT / 'assets/quiz' / name).read_bytes()
files['assets/quiz/quiz-banks.js'] = ('window.linuxQuizBanks = ' + json.dumps(offline_banks, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
for slug in banks:
    page = (CONTENT / 'cours/quiz' / (slug + '.html')).read_text(encoding='utf-8')
    page = page.replace('../../' + slug + '/', '../' + slug + '.html')
    files['cours/quiz/' + slug + '.html'] = page.encode('utf-8')
archive = CONTENT / 'linux-initiation-obsidian.zip'
temp = archive.with_suffix('.tmp.zip')
assert temp.resolve().parent == CONTENT.resolve()
with zipfile.ZipFile(archive) as old, zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED) as new:
    for entry in old.infolist():
        relative = entry.filename.removeprefix('Linux-initiation/')
        if relative not in files: new.writestr(entry, old.read(entry.filename))
    for relative, data in files.items(): new.writestr('Linux-initiation/' + relative, data)
temp.replace(archive)
if args.sync_source:
    source = args.sync_source.resolve()
    nested = (source / 'cours/01-comprendre-linux/01-comprendre-linux.html').is_file()
    assert nested or (source / 'cours/01-comprendre-linux.html').is_file()
    themed_html = runpy.run_path(str(ROOT / 'scripts/prepare-linux.py'))['themed_html']
    for slug in banks:
        file = source / 'cours' / slug / (slug + '.html') if nested else source / 'cours' / (slug + '.html')
        body = file.read_text(encoding='utf-8')
        file.write_text(themed_html(body, slug), encoding='utf-8')
    for relative, data in files.items():
        if nested:
            if relative.startswith('cours/assets/'): continue
            if relative.startswith('cours/quiz/'):
                slug = Path(relative).stem
                relative = f'cours/{slug}/{slug}-quiz.html'
                data = data.decode('utf-8').replace('../' + slug + '.html', slug + '.html').encode('utf-8')
            elif relative == 'assets/quiz/quiz-banks.js':
                nested_banks = {slug: {**bank, 'chapterLink': slug + '.html'} for slug, bank in banks.items()}
                data = ('window.linuxQuizBanks = ' + json.dumps(nested_banks, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
        file = source / relative
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_bytes(data)
print('Supports HTML : 10 quiz de 20 questions, thèmes clair/sombre, disponibles hors ligne.')
