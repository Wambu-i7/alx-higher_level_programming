#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
    for num in list(reversed(my_list)):
        print("{:d}".format(num))
