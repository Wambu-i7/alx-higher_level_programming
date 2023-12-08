#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_result = list(my_list)
    for i in range(len(list_result)):
        list_result[i] = list_result[i] % 2 == 0

    return list_result
