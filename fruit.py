#!/usr/bin/env python3

import sys
words = sys.stdin.read().split()

fruits = {
    "apple": True,
    "pear": True,
    "orange": True,
    "banana": True,
    "cherry": True,
}

i = 0
while i < len(words):
    if words[i] in fruits:
        sys.stdout.write(words[i] + "\n")
    i = i + 1
