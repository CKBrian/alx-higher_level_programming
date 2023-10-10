#!/usr/bin/python3

""" defines a read_file module """


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout: """
    with open(filename) as myFile:
        print(myFile.readlines())
