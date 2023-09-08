#!/usr/bin/python3
from calculator_1 import add, sub, div, mul
from sys import exit, argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>\n", end="")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == '+':
        res = a + b
        print("{} {} {} = {}\n".format(a, argv[2], b, res), end="")
    elif argv[2] == '-':
        res = a - b
        print("{} {} {} = {}\n".format(a, argv[2], b, res), end="")
    elif argv[2] == '*':
        res = a * b
        print("{} {} {} = {}\n".format(a, argv[2], b, res), end="")
    elif argv[2] == '/':
        if b == 0:
            exit(0)
        else:
            res = int(a / b)
        print("{} {} {} = {}\n".format(a, argv[2], b, res), end="")
    else:
        print("Unknown operator. Available operators: +, -, * and /\n", end="")
        exit(1)
