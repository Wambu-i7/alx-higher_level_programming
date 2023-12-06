#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    n = len(argv) - 1
    if n < 1:
        print("{} arguments.".format(n), end=" ")
    elif n == 1:
        print("{} argument:".format(n), end=" ")
    else:
        print("{} arguments:".format(n), end=" ")
    for i in range(1, n + 1):
        print("\n{}: {}".format(i, argv[i]), end=" ")
    print()
