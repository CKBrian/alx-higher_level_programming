#!/usr/bin/python3

""" defines a read_file module """


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout: """
    with open(filename, 'r', encoding="utf-8") as myFile:
        for line in myFile:
            print("{}".format(line))
