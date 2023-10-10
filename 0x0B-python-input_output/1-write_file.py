#!/usr/bin/python3
""" defines a write_file module"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8) and
    returns the number of characters written:"""
    with open(filename, 'w', encoding="UTF-8") as tFile:
        return tFile.write(text)
