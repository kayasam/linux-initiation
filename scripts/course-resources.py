"""Shared resource buttons and explorer registry for Linux and Bash chapters."""
import html
from pathlib import Path
import json
import posixpath
import re

KINDS = {
    'markdown': ('Cours', 'Lire le cours en Markdown'),
    'html': ('HTML', 'Explorer le chapitre'),
    'quiz': ('Quiz', '20 questions'),
    'tp': ('TP', 'Mettre en pratique'),
}


def render_resources(destination, base, key, slug, has_tp=False, title=None):
    track = 'bash/' if key.startswith('bash/') else ''
    urls = {
        'markdown': f'{base}/{key}/',
        'html': f'{base}/{key}/html/',
        'quiz': f'{base}/{key}/quiz/',
    }
    if has_tp:
        urls['tp'] = f'{base}/{key}/tp'
    entries = []
    buttons = []
    for kind, url in urls.items():
        label, detail = KINDS[kind]
        icon = f'{base}/assets/resource-icons/{kind}.svg'
        symbol = (Path(__file__).resolve().parents[1] / 'site-content/assets/resource-icons' / (kind + '.svg')).read_text(encoding='utf-8').strip()
        symbol = symbol.replace('<svg ', '<svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" ', 1)
        entries.append(dict(kind=kind, label=label, detail=detail, href=url, icon=icon, symbol=symbol, chapterTitle=title or slug))
        buttons.append(f'<a class="resource-button resource-{kind}" data-resource-kind="{kind}" aria-label="{label} — {detail}" href="{html.escape(url, quote=True)}">'
                       f'<span class="resource-icon" aria-hidden="true">{symbol}</span>'
                       f'<span class="resource-label">{label}<small>{detail}</small></span></a>')
    download_url = f'{base}/telechargements/{track}cours/{slug}.md'
    download_button = f'<a class="resource-download" href="{download_url}" download aria-label="Télécharger le cours en Markdown"><span aria-hidden="true">↓</span> Télécharger .md</a>'
    registry_path = destination / 'assets/course-resources.json'
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    registry = json.loads(registry_path.read_text(encoding='utf-8')) if registry_path.exists() else {}
    registry[key] = entries
    registry_path.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    bar = ('\n\n<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="' + key + '" style="--resource-count:' + str(len(entries)) + '">'
            '<div class="resource-buttons">' + ''.join(buttons) + '</div><div class="resource-actions">' + download_button +
            '<button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>\n')

    # Quartz supplies the same site navigation around each existing standalone support.
    for kind, suffix, source in (
        ('html', 'HTML interactif', f'{base}/{track}cours/{slug}-interactif.html'),
        ('quiz', 'Quiz', f'{base}/{track}cours/quiz/{slug}.html'),
    ):
        page_title = (title or slug) + ' — ' + suffix
        page = destination / key / kind / 'index.md'
        page.parent.mkdir(parents=True, exist_ok=True)
        frame_title = html.escape(page_title, quote=True)
        frame_src = posixpath.relpath(source.removeprefix(base + '/'), start=key + '/' + kind)
        page.write_text('---\ntitle: ' + json.dumps(page_title, ensure_ascii=False) + '\n---\n\n' + bar +
            f'<section class="support-viewer" data-course-key="{key}" data-support-kind="{kind}">'
            f'<iframe class="support-frame" src="{source}" data-support-src="{frame_src}" title="{frame_title}"></iframe>'
            '<noscript><p>Pour afficher ce support avec les menus, activez JavaScript. '
            f'<a href="{source}">Ouvrir le support directement</a>.</p></noscript></section>\n', encoding='utf-8')
    return bar


def attach_tp_resources(destination):
    """Use the same support navigation on the chapter's exercise page."""
    registry = json.loads((destination / 'assets/course-resources.json').read_text(encoding='utf-8'))
    for key, resources in registry.items():
        if not any(resource['kind'] == 'tp' for resource in resources):
            continue
        course = (destination / key / 'index.md').read_text(encoding='utf-8')
        bar = re.search(r'<nav class="chapter-resources".*?</nav>', course, re.S)[0]
        paths = [destination / key / 'tp.md', *(destination / key).glob('*-correction.md'), *(destination / key / 'tp').glob('*.md')]
        for path in paths:
            if not path.is_file():
                continue
            page = path.read_text(encoding='utf-8')
            if 'class="chapter-resources"' not in page:
                page = re.sub(r'^(# .+)$', lambda match: match[0] + '\n\n' + bar, page, count=1, flags=re.M)
                path.write_text(page, encoding='utf-8')
