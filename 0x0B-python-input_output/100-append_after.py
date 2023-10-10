#!/usr/bin/python3
"""defines"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after
    each line containing a specific string"""
    with open(filename, "r", encoding="UTF-8") as my_file:
        lines = my_file.readlines()
    with open(filename, "w", encoding="UTF-8") as my_file:
        for line in lines:
            my_file.write(line)
            if search_string in line:
                # print(my_file.tell())
                my_file.write(new_string)
