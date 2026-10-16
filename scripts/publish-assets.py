"""Copy raw assets after Quartz and check every local link in emitted HTML."""
from pathlib import Path
import shutil
import re
import zipfile
import json
import hashlib
from urllib.parse import urlsplit, unquote
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
policy = ROOT / 'publication-policy.json'
allowed_corrections = set(json.loads(policy.read_text(encoding='utf-8'))['corrections']) if policy.exists() else set()
public = ROOT / 'public'
for source in (ROOT / 'content').rglob('*'):
    if source.is_file() and (source.suffix != '.md' or 'telechargements' in source.parts):
        destination = public / source.relative_to(ROOT / 'content')
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

class Links(HTMLParser):
    def __init__(self): super().__init__(); self.links=[]
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('href', 'src') and value: self.links.append(value)

errors=[]
checked=0
for page in public.rglob('*.html'):
    parser=Links(); parser.feed(page.read_text(encoding='utf-8'))
    for link in parser.links:
        url=urlsplit(link)
        if url.scheme and not (url.netloc == 'kayasam.github.io' and (url.path == '/linux-initiation' or url.path.startswith('/linux-initiation/'))): continue
        if url.netloc and url.netloc != 'kayasam.github.io': continue
        if not url.path: continue
        path=unquote(url.path)
        if path == '/linux-initiation': path=''
        elif path.startswith('/linux-initiation/'): path=path[len('/linux-initiation/'):]
        elif path.startswith('/'): path=path[1:]
        else: path=str(page.relative_to(public).parent / path)
        target=public/path
        checked+=1
        if not any(p.is_file() for p in (target, target.with_suffix('.html'), target/'index.html')):
            errors.append(f'{page.relative_to(public)} -> {link}')
assert not errors, '\n'.join(errors[:60])
with zipfile.ZipFile(public/'linux-initiation-obsidian.zip') as z:
    names=z.namelist()
    assert len([n for n in names if re.search(r'/cours/\d\d-.*\.md$',n)])==10
    tp_count = sum(chapter['tp'] is not None for chapter in json.loads((ROOT/'chapters.json').read_text(encoding='utf-8')))
    assert len([n for n in names if re.search(r'/tp/tp-.*\.md$',n) and not re.search(r'correction|corrig', n, re.I)])==tp_count
    assert not any(re.search(r'correction|corrig', n, re.I) and Path(n).name not in allowed_corrections for n in names)
print(f'Liens locaux vérifiés : {checked}. Archive : 10 cours et {tp_count} TP ; {len(allowed_corrections)} correction(s) autorisée(s).')
with zipfile.ZipFile(public/'linux-scripting-bash-obsidian.zip') as z:
    bash_names = z.namelist()
    assert sum(bool(re.search(r'/cours/\d\d-[^/]+/\d\d-[^/]+\.md$', n)) for n in bash_names) == 6
    bash_tp_count = sum(not re.search(r'correction|corrig', p.name, re.I) for p in (ROOT / 'content/telechargements/bash/tp').glob('*.md'))
    assert sum('/tp/' in n and n.endswith('.md') and not re.search(r'correction|corrig', Path(n).name, re.I) for n in bash_names) == bash_tp_count
    assert not any(re.search(r'correction|corrig', Path(n).name, re.I) and Path(n).name not in allowed_corrections for n in bash_names)
assert not any(re.search(r'correction|corrig', p.name, re.I) and p.with_suffix('.md').name not in allowed_corrections for p in (public/'bash').rglob('*') if p.is_file())
print(f'Bash : six cours et {bash_tp_count} TP dans le ZIP ; seules les corrections autorisées sont publiées.')
pdf_manifest = json.loads((ROOT / 'content/assets/course-pdfs.json').read_text(encoding='utf-8'))
assert len(pdf_manifest) == 16
for entry in pdf_manifest:
    assert hashlib.sha256((ROOT / 'content' / entry['source']).read_text(encoding='utf-8-sig').encode('utf-8')).hexdigest() == entry['sourceSha256'], 'PDF périmé : ' + entry['key']
    assert hashlib.sha256((public / entry['pdf']).read_bytes()).hexdigest() == entry['pdfSha256'], entry['key']
    assert (public / entry['pdf']).read_bytes().startswith(b'%PDF-')
    course = (ROOT / 'content' / entry['key'] / 'index.md').read_text(encoding='utf-8')
    assert 'resource-pdf' in course
    assert entry['href'] + '?v=' + entry['pdfSha256'][:12] in course, 'Lien PDF non actualisé : ' + entry['key']
assert sum('resource-pdf' in page.read_text(encoding='utf-8') for page in (ROOT / 'content').rglob('*.md') if 'telechargements' not in page.parts) == 16, 'PDF réservé aux 16 cours Markdown'
print('PDF : 16 chapitres à jour, boutons réservés aux cours Markdown.')
home = (ROOT / 'content/index.md').read_text(encoding='utf-8')
for archive in (ROOT / 'content').glob('*.zip'):
    assert archive.name + '?v=' + hashlib.sha256(archive.read_bytes()).hexdigest()[:12] in home
print('Téléchargements : liens ZIP et PDF versionnés avec le contenu des fichiers.')
