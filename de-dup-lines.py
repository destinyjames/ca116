#!/usr/bin/env python3

word = []
seen = []

s = input()
while s != "end":
    word.append(s)
    s = input()

i = 0
while i < len(word):
    j = 0
    while j < len(seen) and seen[j] != word[i]:
        j = j + 1

    if j < len(seen):
        print
    else:

        print(word[i])
        seen.append(word[i])
    i = i + 1
