#!/usr/bin/env python3

even = []
odd = []
s = input()
while s != "end":
    s = int(s)
    if s % 2 == 0:
        even.append(s)
    else:
        odd.append(s)
    s = input()


i = 0
m = 0

while i < len(even):
    print(even[i])
    i = i + 1

while m < len(odd):
    print(odd[m])
    m = m + 1
