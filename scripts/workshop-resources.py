"""Shared workshop metadata, overview cards and exercise/correction navigation."""
from pathlib import Path
import html
import json
import re

DEFINITIONS = {
    'synthese': ('Synthèse', 'Réunir les six chapitres dans un rapport de mission.', '<path d="M8 3h8l4 4v14H4V3h4Z"/><path d="M14 3v5h6M8 12h8M8 16h6"/>'),
    'final': ('Jeu final', 'Construire BIP-42, jouer une partie et conserver les scores.', '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>'),
    'bonus': ('Bonus', 'Choisir parmi trois petits jeux indépendants dans le terminal.', '<path d="M7 7h10c4 0 6 10 3 11-2 1-4-3-5-3H9c-1 0-3 4-5 3C1 17 3 7 7 7Z"/><path d="M6 10v4M4 12h4M15 11h.01M18 13h.01"/>'),
}


def entries(tps, routes, base, published_correction):
    result = []
    for order, kind in enumerate(DEFINITIONS):
        for tp in tps:
            if tp.parent.name != kind:
                continue
            label, description, paths = DEFINITIONS[kind]
            title = re.search(r'^# (.+)$', tp.read_text(encoding='utf-8-sig'), re.M)[1]
            correction = published_correction(tp)
            route = routes[tp]
            result.append(dict(key=route, kind=kind, order=order, label=label, title=title, description=description,
                symbol='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + paths + '</svg>',
                href=base + '/' + route, markdownHref=base + '/telechargements/bash/tp/' + tp.name,
                correctionHref=base + '/' + route.rsplit('/', 1)[0] + '/' + correction.stem if correction else None,
                correctionMarkdownHref=base + '/telechargements/bash/tp/' + correction.name if correction else None))
    return result


def resources(entry, kind):
    links = [('tp', 'Énoncé', entry['href'], entry['symbol'])]
    if entry['correctionHref']:
        links.append(('correction', 'Corrigé' if kind == 'correction' else 'Afficher les corrections', entry['correctionHref'], '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="m5 12 4 4L19 6"/></svg>'))
    buttons = ''.join('<a class="resource-button" href="' + html.escape(url, quote=True) + '"' + (' aria-current="page"' if tab == kind else '') + '><span class="resource-icon">' + symbol.replace('<svg ', '<svg class="resource-symbol" ') + '</span><span class="resource-label">' + label + '</span></a>' for tab, label, url, symbol in links)
    download = entry['correctionMarkdownHref'] if kind == 'correction' else entry['markdownHref']
    return '<nav class="chapter-resources workshop-resources" aria-label="Ressources de l’atelier" data-workshop-key="' + entry['key'] + '"><div class="resource-buttons">' + buttons + '</div><div class="resource-actions"><a class="resource-download" href="' + download + '" download aria-label="Télécharger ce support en Markdown">↓ Télécharger .md</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>'


def attach_resources(destination, workshops):
    for entry in workshops:
        pages = [(destination / (entry['key'] + '.md'), 'tp')]
        if entry['correctionHref']:
            pages.append((destination / (entry['key'].rsplit('/', 1)[0] + '/' + entry['correctionHref'].rsplit('/', 1)[1] + '.md'), 'correction'))
        for path, kind in pages:
            text = path.read_text(encoding='utf-8')
            title = re.search(r'^# (.+)$', text, re.M)
            if title:
                text = re.sub(r'^title:.*$', lambda _: 'title: ' + json.dumps(title[1], ensure_ascii=False), text, count=1, flags=re.M)
            text = re.sub(r'^# .+$', lambda _: resources(entry, kind), text, count=1, flags=re.M)
            path.write_text(text, encoding='utf-8')


def overview(workshops, base):
    cards = []
    for entry in workshops:
        correction = '<a href="' + entry['correctionHref'] + '">Corrigé à déplier →</a>' if entry['correctionHref'] else ''
        cards.append('<section class="workshop-card"><h2>' + html.escape(entry['title']) + '</h2><p>' + html.escape(entry['description']) + '</p><nav class="workshop-card__actions" aria-label="Ressources — ' + html.escape(entry['title'], quote=True) + '"><a href="' + entry['href'] + '">Énoncé</a>' + correction + '</nav></section>')
    cards.append('<section class="workshop-card"><h2>Orion Académie — Le jeu</h2><p>Des missions pour pratiquer dans le terminal.</p><nav class="workshop-card__actions" aria-label="Ressources — Orion Académie"><a href="' + base + '/bash/annexe/orion-academie">Ouvrir le jeu</a></nav></section>')
    return '# Annexe\n\nLes ateliers complémentaires et le jeu Orion Académie.\n\n<div class="workshop-grid">' + ''.join(cards) + '</div>\n'
