#!/usr/bin/python3
""" defines ``7-add_item.py`` module that  adds all
arguments to a Python list, and then save them to a file:"""
import sys
import os
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_args_to_list(arg):
    """ adds all arguments to a Python list """
    filename = "add_item.json"
    my_list = []
    if not path.exists(filename):
        if arg != "":
            my_list.append(arg)
        save_to_json_file(my_list, filename)
    else:
        my_list = load_from_json_file(filename)
        my_list.append(arg)
        save_to_json_file(my_list, filename)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        add_args_to_list("")
        sys.exit(0)
    for i in range(1, len(sys.argv)):
        add_args_to_list(sys.argv[i])
    sys.exit(1)
