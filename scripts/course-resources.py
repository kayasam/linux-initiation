"""Shared resource buttons and explorer registry for Linux and Bash chapters."""
import html
import json

KINDS = {
    'markdown': ('Markdown', 'Télécharger le cours'),
    'html': ('HTML', 'Explorer le chapitre'),
    'quiz': ('Quiz', '20 questions'),
    'tp': ('TP', 'Mettre en pratique'),
}


def render_resources(destination, base, key, slug, has_tp=False):
    track = 'bash/' if key.startswith('bash/') else ''
    urls = {
        'markdown': f'{base}/telechargements/{track}cours/{slug}.md',
        'html': f'{base}/{track}cours/{slug}-interactif.html',
        'quiz': f'{base}/{track}cours/quiz/{slug}.html',
    }
    if has_tp:
        urls['tp'] = f'{base}/{key}/tp'
    entries = []
    buttons = []
    for kind, url in urls.items():
        label, detail = KINDS[kind]
        icon = f'{base}/assets/resource-icons/{kind}.svg'
        entries.append(dict(kind=kind, label=label, detail=detail, href=url, icon=icon))
        download = ' download' if kind == 'markdown' else ''
        buttons.append(f'<a class="resource-button resource-{kind}" data-resource-kind="{kind}" href="{html.escape(url, quote=True)}"{download}>'
                       f'<span class="resource-icon" aria-hidden="true"><img src="{icon}" alt="" /></span>'
                       f'<span class="resource-label">{label}<small>{detail}</small></span></a>')
    registry_path = destination / 'assets/course-resources.json'
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    registry = json.loads(registry_path.read_text(encoding='utf-8')) if registry_path.exists() else {}
    registry[key] = entries
    registry_path.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return ('\n\n<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="' + key + '" style="--resource-count:' + str(len(entries)) + '">'
            '<span class="chapter-resources-title">Ressources du chapitre</span><div class="resource-buttons">' + ''.join(buttons) + '</div></nav>\n')
