#!/usr/bin/python3
from sys import argv

argc = len(argv) - 1

if argc == 0:
    print("{} arguments.\n".format(argc), end="")
else:
    print("{} arguments:\n".format(argc), end="")
    for i in range(1, argc + 1):
        print("{}: {}\n".format(i, argv[i]), end="")
