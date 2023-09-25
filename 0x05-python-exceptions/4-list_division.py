#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ls = [0] * list_length
    idx = 0
    for idx in range(list_length):
        try:
            ls[idx] = my_list_1[idx] / my_list_2[idx]
        except IndexError:
            print("out of range")
            continue
        except ZeroDivisionError:
            print("division by 0")
            continue
        except TypeError:
            print("wrong type")
            continue
        finally:
            idx += 1
    return ls
