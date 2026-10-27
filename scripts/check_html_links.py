#!/usr/bin/env python3
"""Check relative href targets used by the repository's HTML pages."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
missing = []
for page in ROOT.rglob('*.html'):
    for href in re.findall(r'href=["\']([^"\'#?]+)', page.read_text(encoding='utf-8')):
        if href.startswith(('http://', 'https://', 'mailto:', 'javascript:', 'YOUR_')):
            continue
        target = (page.parent / href).resolve()
        if not target.exists():
            missing.append(f'{page.relative_to(ROOT)} -> {href}')
if missing:
    print('Missing local HTML targets:')
    print('\n'.join(missing))
    sys.exit(1)
print('HTML link check passed.')
