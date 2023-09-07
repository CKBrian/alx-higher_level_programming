#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    res = add(a, b)
    print("{} + {} = {}\n".format(a, b, res), end="")
    res = sub(a, b)
    print("{} - {} = {}\n".format(a, b, res), end="")
    res = mul(a, b)
    print("{} * {} = {}\n".format(a, b, res), end="")
    res = div(a, b)
    print("{} / {} = {}\n".format(a, b, res), end="")
