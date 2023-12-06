#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import math
    n = len(argv) - 1
    Sum = 0
    for i in range(1, n + 1):
        Sum += int(argv[i])
     
    print("{}".format(Sum))
