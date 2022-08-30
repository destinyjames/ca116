#!/usr/bin/env python3
import sys

words = sys.stdin.read()

total = 0
i = 0
while i < len(words):
    if "A" <= words[i] and words[i] <= "Z":
        total = total + 1
    i = i + 1

sys.stdout.write(str(total) + "\n")
