#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result: {}".format(result))
        print("{} / {} = {}".format(a, b, result))
    except ZeroDivisionError:
        print("Inside result: None")
        print("{} / {} = None".format(a, b))
        return None
    except Exception as e:
        print("Inside result: None")
        print("{} / {} = An unexpected error occurred: {}".format(a, b, e))
        return None
