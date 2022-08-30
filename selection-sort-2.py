#!/usr/bin/env python3

a = []
s = input()

while s != "end":
    a.append(s)
    s = input()

t = int(input())
i = t 
while i < len(a):
    if int(a[i]) < int(a[t]):
        t = i
    i = i + 1
print(t)

