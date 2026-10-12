"""Copy raw assets after Quartz and check every local link in emitted HTML."""
from pathlib import Path
import shutil
import re
import zipfile
from urllib.parse import urlsplit, unquote
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
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
    assert len([n for n in names if re.search(r'/tp/tp-.*\.md$',n)])==7
    assert not any(re.search(r'correction|corrig',n,re.I) for n in names)
print(f'Liens locaux vérifiés : {checked}. Archive : 10 cours et 7 TP, sans corrections.')
