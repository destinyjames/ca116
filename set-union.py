#!/usr/bin/env python3

import sys

with open("a.txt") as file1:
    file1 = file1.read()

with open("b.txt") as file2:
    file2 = file2.read()

words = (file1 + "\n" + file2).split()

seen = {}
i = 0
while i < len(words):
    if words[i] not in seen:
        seen[words[i]] = "true"
    i = i + 1

for a in seen:
    sys.stdout.write(a + "\n")
