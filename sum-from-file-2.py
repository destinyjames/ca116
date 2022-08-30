#!/usr/bin/env python3

import sys

args = sys.argv[1]

with open(args) as f:
    lines = f.readlines()

i = 0 
total = 0
while i < len(lines):
    total = total + int(lines[i])
    i = i + 1

print(total)
