"""Check every PDF page and render an overview for visual review."""
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
output = ROOT / 'output/pdf/review'
output.mkdir(parents=True, exist_ok=True)
thumbnails = []
total = 0
for entry in manifest:
    path = CONTENT / entry['pdf']
    source = CONTENT / entry['source']
    assert hashlib.sha256(source.read_text(encoding='utf-8-sig').encode('utf-8')).hexdigest() == entry['sourceSha256']
    assert hashlib.sha256(path.read_bytes()).hexdigest() == entry['pdfSha256']
    doc = fitz.open(path)
    assert len(doc) == entry['pages']
    text = ' '.join(' '.join(page.get_text().split()) for page in doc)
    parsed = BeautifulSoup(markdown.markdown(source.read_text(encoding='utf-8-sig'), extensions=['tables', 'fenced_code']), 'html.parser')
    for heading in parsed.find_all(re.compile('^h[1-6]$')):
        expected = ' '.join(heading.get_text().split())
        assert expected in text, (entry['key'], 'Titre absent ou tronqué', expected)
    for index, page in enumerate(doc):
        total += 1
        assert page.get_text().strip()
        for block in page.get_text('dict')['blocks']:
            for line in block.get('lines', []):
                for span in line['spans']:
                    x0, y0, x1, y1 = span['bbox']
                    assert x0 >= 20 and x1 <= page.rect.width - 18 and y0 >= 10 and y1 <= page.rect.height - 10, (entry['key'], index + 1, span['text'], span['bbox'])
        pix = page.get_pixmap(matrix=fitz.Matrix(.7, .7), alpha=False)
        image = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
        tile = Image.new('RGB', (440, 640), '#e4eaf0')
        image.thumbnail((420, 600))
        tile.paste(image, ((440-image.width)//2, 24))
        ImageDraw.Draw(tile).text((10, 620), entry['key'] + ' / ' + str(index + 1), fill='#213547')
        thumbnails.append(tile)
    # Inspect high-resolution samples in addition to all-page contact sheets.
    if entry['key'] in ('01-comprendre-linux', 'bash/04-tests-et-conditions', 'bash/05-boucles', '08-gestion-des-paquets'):
        for index in (0, min(2, len(doc)-1), len(doc)-1):
            doc[index].get_pixmap(matrix=fitz.Matrix(1.4, 1.4), alpha=False).save(output / (entry['key'].replace('/', '-') + '-' + str(index+1) + '.png'))
for start in range(0, len(thumbnails), 12):
    sheet = Image.new('RGB', (440*3, 640*4), '#e4eaf0')
    for index, tile in enumerate(thumbnails[start:start+12]):
        sheet.paste(tile, ((index % 3)*440, (index // 3)*640))
    sheet.save(output / f'pages-{start//12+1:02}.jpg', quality=88)
print(f'PDF vérifiés : {len(manifest)} chapitres, {total} pages, titres présents, texte dans la page. Aperçus : {output}')
