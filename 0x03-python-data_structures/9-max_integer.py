#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)

    max_V = my_list[0]

    for num in my_list:
        if num > max_V:
            max_V = num
    return (max_V)
