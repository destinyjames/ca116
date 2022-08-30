#!/usr/bin/env python3

import sys

args = sys.argv[1:]

b = "."
j = " "
i = 0

while i < int(args[0]):
    if i == 0:
        print(b)
    else:
        print(i * j + (b))
    i = i + 1
