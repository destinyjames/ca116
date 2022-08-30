#!/usr/bin/env python3

x = int(input())

print("first:", x >= 70)
print("second:", x >= 50 and x <= 69)
print("third:", x >= 40 and x <= 49)
print("fail:", x < 40)
