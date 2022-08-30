#!/usr/bin/env python3

a = []

s = input()
while s != "end":
    a.append(int(s))
    s = input()


i = 0
n = int(input())
while i < len(a):
    print (n + a[i])
    i = i + 1
