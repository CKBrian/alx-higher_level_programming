#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    try:
        for elem in range(x):
            if isinstance(my_list[elem], int):
                print("{:d}".format(my_list[elem]), end="")
                i += 1
    except TypeError:
        return 0
    else:
        print()
        return i
