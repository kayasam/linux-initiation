"""Shared resource buttons and explorer registry for Linux and Bash chapters."""
import html
import json
import posixpath

KINDS = {
    'markdown': ('Markdown', 'Lire le cours'),
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
        entries.append(dict(kind=kind, label=label, detail=detail, href=url, icon=icon))
        buttons.append(f'<a class="resource-button resource-{kind}" data-resource-kind="{kind}" href="{html.escape(url, quote=True)}">'
                       f'<span class="resource-icon" aria-hidden="true"><img src="{icon}" alt="" /></span>'
                       f'<span class="resource-label">{label}<small>{detail}</small></span></a>')
    download_url = f'{base}/telechargements/{track}cours/{slug}.md'
    download_button = f'<a class="resource-download" href="{download_url}" download><span aria-hidden="true">↓</span> Télécharger le .md</a>'
    registry_path = destination / 'assets/course-resources.json'
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    registry = json.loads(registry_path.read_text(encoding='utf-8')) if registry_path.exists() else {}
    registry[key] = entries
    registry_path.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    bar = ('\n\n<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="' + key + '" style="--resource-count:' + str(len(entries)) + '">'
            '<div class="chapter-resources-heading"><span class="chapter-resources-title">Ressources du chapitre</span>' + download_button + '</div><div class="resource-buttons">' + ''.join(buttons) + '</div></nav>\n')

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
            '<div class="support-toolbar"><span>' + suffix + '</span>'
            '<button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div>'
            f'<iframe class="support-frame" src="{source}" data-support-src="{frame_src}" title="{frame_title}"></iframe>'
            '<noscript><p>Pour afficher ce support avec les menus, activez JavaScript. '
            f'<a href="{source}">Ouvrir le support directement</a>.</p></noscript></section>\n', encoding='utf-8')
    return bar
