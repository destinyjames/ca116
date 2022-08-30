#!/usr/bin/env python3

import sys

args = sys.argv[1:]
a = []

s = input()

while s != "end":
    a.append(s)
    s = input()

j = 0
i = 0
while j < len(a):
    while i < len(a[j]) - len(args[0]) - 1:
        if a[j][i: i + len(args[0])] == args[0]:
            print (a[j])
        i = i + 1
    j = j + 1

    i = 0
