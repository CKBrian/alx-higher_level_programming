#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    a_ls = my_list
    ls = [True if i % 2 == 0 else False for i in a_ls]
    return ls
