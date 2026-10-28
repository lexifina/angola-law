"""Prints the law of Angola as it stood on a given day, read from this repository's history.

    python tools/vigente_em.py 2022-01-01 constituicao 109        # art. 109.º of the Constitution on 1 January 2022
    python tools/vigente_em.py 2022-01-01 constituicao art-109    # the same, by file name
    python tools/vigente_em.py 2022-01-01 constituicao 132-a      # art. 132.º-A
    python tools/vigente_em.py 2022-01-01 constituicao            # the whole Constitution on 1 January 2022
    python tools/vigente_em.py --law 2022-01-01 constituicao 109  # also name the law behind that wording

A thin wrapper around tools/on.py: the version is chosen by each commit's `In-force:` trailer, never by its commit
date, and branches named wip* are ignored. A bare article number (`109`, `132-a` for 132.º-A) means the file
`art-109` or `art-132-a`. Standard library only.
"""
import re
import runpy
import subprocess
import sys
from pathlib import Path


def article(act: str, unit: str) -> str:
    m = re.fullmatch(r'(\d+)(-?[a-z-]*)', unit.lower())
    if not m:
        return unit
    files = set()
    for ref in ('main', 'futuro'):
        out = subprocess.run(['git', 'ls-tree', '-r', '--name-only', ref, f'{act}/'], capture_output=True,
                             text=True, encoding='utf-8')
        files.update(out.stdout.split())
    suffix = '-' + m.group(2).lstrip('-') if m.group(2) else ''
    for width in (3, 4):
        key = f'art-{int(m.group(1)):0{width}d}{suffix}'
        if f'{act}/{key}.md' in files:
            return key
    return unit


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    args = [a for a in sys.argv[1:] if a != '--law']
    if len(args) == 3:
        i = len(sys.argv) - 1 - sys.argv[::-1].index(args[2])
        sys.argv[i] = article(args[1], args[2])
    sys.argv[0] = str(Path(__file__).with_name('on.py'))
    runpy.run_path(sys.argv[0], run_name='__main__')
