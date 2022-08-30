#!/usr/bin/env python3

import sys

a = sys.argv[1:]

i = 0
total = 0
while i < len(a):
    total = total + (int(a[i]))
    i = i + 1

print(total)
