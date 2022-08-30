#!/usr/bin/env python3

import sys

with open("a.txt") as file1:
    file1 = file1.read()   # words that accur in this but not 2

with open("b.txt") as file2:
    file2 = file2.read()

a = file1.split()
b = file2.split()
seen = {}

i = 0
while i < len(b):
    if b[i] not in seen:
        seen[b[i]] = "true"
    i = i + 1
j = 0
while j < len(a):
    if a[j] not in seen:
        sys.stdout.write(a[j] + "\n")
    j = j + 1
