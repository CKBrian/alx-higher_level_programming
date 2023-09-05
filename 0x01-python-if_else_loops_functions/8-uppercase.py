#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) <= 122 and ord(c) >= 97:
            char = chr(ord(c) - 32)
        else:
            char = c
        print("{}".format(char), end="")
    else:
        print("\n", end="")
