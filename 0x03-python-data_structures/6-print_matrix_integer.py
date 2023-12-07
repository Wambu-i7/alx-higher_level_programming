#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if row:
            for num in range(len(row)):
                space = ' ' if num != len(row) - 1 else ''
                print("{:d}".format(row[num]), end=space)
            print()
        else:
            print()

