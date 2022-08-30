#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and (s[i] < "0" or "9" < s[i]):
    i = i + 1

t = i
while t < len(s) and ("0" <= s[t] and s[t] <= "9"):
    t = t + 1

b = t
while b < len(s) and (s[b] < "0" or "9" < s[b]):
    b = b + 1

w = b
while w < len(s) and ("0" <= s[w] and s[w] <= "9"):
    w = w + 1

if i < len(s):
    print (s[b:w], b)
else:
    print
