#!/usr/bin/env python3

s = input()
t = ""

i = 0
while i < len(s):
    if s[i] != " ":
        t = t + s[i]
    else:
        t = t + ""
    i = i + 1

print (t)
