#/usr/bin/env python3

import sys

nums = sys.stdin.read().split()
fruits = {
    "one": "eins",
    "two": "zwei",
    "three": "drei",
    "four": "vier",
    "five": "funf",
    "six": "sechs",
    "seven": "sieben",
    "eight": "acht",
    "nine": "neun",
    "ten": "zehn",
}

i = 0 
while i < len(nums):
    if nums[i] in fruits:
        sys.stdout.write(fruits[nums[i]] + "\n")
    i = i + 1

