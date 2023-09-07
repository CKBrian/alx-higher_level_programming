#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argSum = 0
    argc = len(argv)

    for i in range(1, argc):
        argSum += int(argv[i])

    print("{}\n".format(argSum), end="")
