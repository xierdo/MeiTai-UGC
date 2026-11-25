#!/usr/bin/env python3
"""Count exact UTF-8 prompt file/stdin, with no implicit trimming or newline normalization."""
import argparse
import json
import sys
from pathlib import Path

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('file', nargs='?', help='UTF-8 file; omit or use - for stdin')
p.add_argument('--max', type=int, default=2500, help='hard limit in selected units')
p.add_argument('--unit', choices=['codepoints', 'utf16', 'bytes'], default='codepoints')
a = p.parse_args()
if a.max < 1:
    p.error('--max must be positive')
try:
    raw = sys.stdin.buffer.read() if a.file in (None, '-') else Path(a.file).read_bytes()
    s = raw.decode('utf-8')
except (OSError, UnicodeError) as e:
    p.exit(2, f'{e}\n')
counts = {'codepoints': len(s), 'utf16': len(s.encode('utf-16-le')) // 2, 'bytes': len(raw)}
passed = counts[a.unit] <= a.max
print(json.dumps({**counts, 'limit': a.max, 'unit': a.unit, 'remaining': a.max - counts[a.unit], 'pass': passed}, ensure_ascii=False))
sys.exit(0 if passed else 1)
