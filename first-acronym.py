#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and not("A" <= s[i] and s[i] <= "Z"):
    i = i + 1

t = i
while t < len(s) and ("A" <= s[t] and s[t] <= "Z"):
    t = t + 1

if i < len(s):
    print(s[i:t], i)
else:
    print
