#!/usr/bin/env python3

i = 0


while i < 10:
    j = 0
    n = input()
    while j < len(n) and (n[j] != "+"):
        j = j + 1
    print(int(n[:j]) + int(n[j+1:]))
    i = i + 1


