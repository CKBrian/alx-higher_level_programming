#!/usr/bin/python3
def uniq_add(my_list=[]):
    ls = set(my_list)
    sum1 = sum(x for x in ls)
    return sum1
