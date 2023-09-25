#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for elem in my_list:
            if x <= 0:
                break
            print("{}".format(elem), end="")
            x -= 1
            i += 1
    except TypeError:
        pass
    else:
        print()
        return i
