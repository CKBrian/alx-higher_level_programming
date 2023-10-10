#!/usr/bin/python3
""" defines a ``5-save_to_json_file`` module """
from json import dump


def save_to_json_file(my_obj, filename):
    """ writes an object to a text file """
    with open(filename, "w", encoding="UTF-*") as jFile:
        return dump(my_obj, jFile, ensure_ascii=False)
