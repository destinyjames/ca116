#!/usr/bin/env python3

import sys
words = sys.stdin.readlines()
seen = {}
a = ""

i = 0
while i < len(words) and len(a) < 3:
    if words[i] in seen and words:
        a = ("snap: " + words[i].strip())
        print(a)
    else:
        seen[words[i]] = "true"
    i = i + 1
