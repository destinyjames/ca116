#!/usr/bin/env python3

n = int(input())
m = int(input())

i = 0
while i <= n:
    if m % 2 == 1:
        print (m * 3 + 1)
    else:
        print ( m // 2)
    i = i + 1
