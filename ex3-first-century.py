#!/usr/bin/env python3

import sys

lines = sys.stdin.read()
lines = lines.split()

i = 0
while i < len(lines) and int(lines[i]) <= 100:
    i = i + 1

if i < len(lines):
    print(lines[i])
else:
    print("none")
