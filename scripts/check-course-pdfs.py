"""Check the complete PDF, its sixteen chapters and its visual samples."""
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.pdf-tools'))
import fitz
from PIL import Image, ImageDraw
import markdown
from bs4 import BeautifulSoup

CONTENT = ROOT / 'content'
manifest = json.loads((CONTENT / 'assets/course-pdfs.json').read_text(encoding='utf-8'))
assert len(manifest['chapters']) == 16
path = CONTENT / manifest['pdf']
assert hashlib.sha256(path.read_bytes()).hexdigest() == manifest['pdfSha256']
assert list(CONTENT.rglob('*.pdf')) == [path]
doc = fitz.open(path)
assert len(doc) == manifest['pages']
assert len(doc.get_toc()) == 18, 'Deux parcours et seize signets de chapitres'
output = ROOT / 'output/pdf/review'
output.mkdir(parents=True, exist_ok=True)
for chapter in manifest['chapters']:
    source = CONTENT / chapter['source']
    assert hashlib.sha256(source.read_text(encoding='utf-8-sig').encode('utf-8')).hexdigest() == chapter['sourceSha256']
    start = chapter['startPage'] - 1
    text = ' '.join(' '.join(doc[index].get_text().split()) for index in range(start, start + chapter['pages']))
    parsed = BeautifulSoup(markdown.markdown(source.read_text(encoding='utf-8-sig'), extensions=['tables', 'fenced_code']), 'html.parser')
    for heading in parsed.find_all(re.compile('^h[1-6]$')):
        assert ' '.join(heading.get_text().split()) in text, (chapter['key'], heading.get_text())
thumbnails = []
samples = {0, 1, 2, manifest['chapters'][10]['startPage'] - 1, len(doc) - 1}
for index, page in enumerate(doc):
    assert page.get_text().strip()
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines', []):
            for span in line['spans']:
                x0, y0, x1, y1 = span['bbox']
                assert x0 >= 20 and x1 <= page.rect.width - 18 and y0 >= 10 and y1 <= page.rect.height - 10, (index + 1, span['text'])
    pix = page.get_pixmap(matrix=fitz.Matrix(.7, .7), alpha=False)
    image = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
    image.thumbnail((420, 600))
    tile = Image.new('RGB', (440, 640), '#e4eaf0')
    tile.paste(image, ((440-image.width)//2, 24))
    ImageDraw.Draw(tile).text((10, 620), 'PDF complet / ' + str(index + 1), fill='#213547')
    thumbnails.append(tile)
    if index in samples:
        page.get_pixmap(matrix=fitz.Matrix(1.4, 1.4), alpha=False).save(output / f'complet-{index+1}.png')
for start in range(0, len(thumbnails), 12):
    sheet = Image.new('RGB', (1320, 2560), '#e4eaf0')
    for index, tile in enumerate(thumbnails[start:start+12]):
        sheet.paste(tile, ((index % 3)*440, (index // 3)*640))
    sheet.save(output / f'complet-pages-{start//12+1:02}.jpg', quality=88)
print(f'PDF complet vérifié : 16 chapitres, {len(doc)} pages, titres et signets conformes.')
