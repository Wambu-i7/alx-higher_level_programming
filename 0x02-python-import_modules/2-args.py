#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    n = len(argv) - 1
    if n < 1:
        print("{} arguments.".format(n))
    elif n == 1:
        print("{} argument:".format(n))
    else:
        print("{} arguments:".format(n))
    for i in range(1, n + 1):
        print("{}: {}".format(i, argv[i]))
