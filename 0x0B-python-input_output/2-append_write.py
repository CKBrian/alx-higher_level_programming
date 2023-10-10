#!/usr/bin/python3
""" defines a append_write module"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)"""
    with open(filename, 'a', encoding="utf-8") as tFile:
        return tFile.write(text)
