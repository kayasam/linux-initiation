"""Build a reproducible, executable, offline Orion adventure package."""
from pathlib import Path
import gzip
import hashlib
import io
import json
import tarfile

FILES = ['orion.py', 'missions.json', 'jouer.sh', 'README.md']


def package(source, destination):
    missions = json.loads((source / 'missions.json').read_text(encoding='utf-8'))
    assert len(missions) == 48 and [m['id'] for m in missions] == list(range(1, 49))
    data = io.BytesIO()
    with gzip.GzipFile(fileobj=data, mode='wb', mtime=0, filename='') as compressed:
        with tarfile.open(fileobj=compressed, mode='w', format=tarfile.USTAR_FORMAT) as archive:
            for name in FILES:
                body = (source / name).read_bytes().replace(b'\r\n', b'\n')
                info = tarfile.TarInfo('orion-academie/' + name)
                info.size = len(body); info.mtime = 0; info.mode = 0o755 if name.endswith(('.py','.sh')) else 0o644
                archive.addfile(info, io.BytesIO(body))
    target = destination / 'telechargements/bash/orion-academie.tar.gz'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data.getvalue())
    checksum = hashlib.sha256(data.getvalue()).hexdigest()
    target.with_suffix('.gz.sha256').write_text(checksum + '  ' + target.name + '\n', encoding='ascii')
    return {f'jeu/{name}': (source/name).read_bytes().replace(b'\r\n',b'\n') for name in FILES}
