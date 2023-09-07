#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv) - 1

    if argc == 0:
        print("{} arguments.\n".format(argc), end="")
    elif argc == 1:
        print("{} argument:\n".format(argc), end="")
        print("{}: {}\n".format(argc, argv[1]), end="")
    else:
        print("{} arguments:\n".format(argc), end="")
        for i in range(1, argc + 1):
            print("{}: {}\n".format(i, argv[i]), end="")
