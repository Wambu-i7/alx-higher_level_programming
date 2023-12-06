#!/usr/bin/python3
from sys import argv
n = len(argv) - 1
Sum = 0
for i in range(1, n + 1):
    Sum += int(argv[i])
     
print(Sum)
