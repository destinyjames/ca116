#!/usr/bin/env python3

n = input()
s = ""

s = n[len(n) - 1] + n[1:-1] + n[0]

print(s)
