#/usr.bin/env python3

import sys

lines = sys.argv[1:]
i = 0

while i < len(lines):
    with open(lines[i]) as f:
        f = f.read()
        if len(f) != 0:
            sys.stdout.write(lines[i] + "\n")
    i = i + 1
