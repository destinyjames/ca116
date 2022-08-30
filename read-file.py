#!/usr/bin/env python3

with open("text.txt") as f:
    lines = f.readlines()

i = 0 
while i < len(lines):
    lines[i] = lines[i].rstrip()
    print(lines[i])
    i = i + 1