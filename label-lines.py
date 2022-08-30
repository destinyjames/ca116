#!/usr/bin/env python3

a = []
i = 0

s = input()
while s != "end":
    a.append(s)
    s = input()
    i = i + 1


j = 0
while j < i:
    print(j, i, a[j])
    j = j + 1
