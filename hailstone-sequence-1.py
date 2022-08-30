#!/usr/bin/env python3

n = int(input())
m = int(input())

i = 0
while i < n:
    if m % 2 == 1:
        m = m * 3 + 1
        print(m)
    else: 
        m = m / 2
        print(m)
    i = i + 1
