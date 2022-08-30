#!/usr/bin/env python3

s = input()

i = 0

while i < len(s) and (s[i] < "0" or "9" < s[i]):
    i = i + 1

t = i
while t < len(s) and ("0" <= s[t] and s[t] <= "9"):
    t = t + 1

if t < len(s):
    print(s[i:t], i)
else:
    print
