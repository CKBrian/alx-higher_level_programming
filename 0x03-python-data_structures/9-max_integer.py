#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    ls = list(my_list)
    for f in range(0, len(ls) - 1):
        for x in range(0, len(ls) - 1):
            if ls[x + 1] > ls[x]:
                temp = ls[x + 1]
                ls[x + 1] = ls[x]
                ls[x] = temp
    return ls[0]
