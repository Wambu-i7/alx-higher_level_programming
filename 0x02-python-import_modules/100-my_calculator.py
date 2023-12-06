#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    n = len(argv) - 1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    oprts = {"+": add, "-": sub, "*": mul, "/": div}
    if argv[2] not in oprts:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    print("{} {} {} = {}".format(a, argv[2], b, oprts[argv[2]](a, b)))
