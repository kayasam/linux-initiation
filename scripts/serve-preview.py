"""Serve the local Quartz build under its real base path, without production requests."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import argparse
import mimetypes

ROOT = Path(__file__).resolve().parents[1] / 'public'
parser = argparse.ArgumentParser()
parser.add_argument('--port', type=int, default=8770)
args = parser.parse_args()
PREFIX = '/linux-initiation'

class Preview(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        self.directory = str(ROOT)
        if path.startswith(PREFIX + '/') or path == PREFIX:
            path = path[len(PREFIX):] or '/'
        target = super().translate_path(path)
        # GitHub Pages resolves extensionless TP links to their .html file.
        if not Path(target).exists() and Path(target + '.html').is_file():
            return target + '.html'
        return target

    def do_GET(self):
        if self.path == '/':
            self.send_response(302)
            self.send_header('Location', PREFIX + '/')
            self.end_headers()
            return
        path = Path(self.translate_path(self.path.split('?', 1)[0]))
        if path.is_dir(): path = path / 'index.html'
        if path.is_file() and path.suffix in {'.html', '.js', '.json', '.css', '.svg'}:
            origin = 'http://' + self.headers.get('Host', f'127.0.0.1:{args.port}')
            data = path.read_text(encoding='utf-8').replace('https://kayasam.github.io', origin).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', (mimetypes.guess_type(path.name)[0] or 'text/plain') + '; charset=utf-8')
            self.send_header('Cache-Control', 'no-store')
            self.send_header('Content-Length', str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        else:
            super().do_GET()

    def log_message(self, *_): pass

print(f'Aperçu local : http://127.0.0.1:{args.port}{PREFIX}/', flush=True)
ThreadingHTTPServer(('127.0.0.1', args.port), Preview).serve_forever()
