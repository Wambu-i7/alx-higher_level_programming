#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            value = my_list[i]
            if isinstance(value, int):
                print("{:d}".format(value), end=" ")
                count += 1
        print()
        if x > len(my_list):
            raise IndexError("Index out of range")
        return count
    except (ValueError, TypeError):
        return count
    except IndexError:
        print()
        raise
