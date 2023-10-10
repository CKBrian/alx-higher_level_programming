#!/usr/bin/python3
""" defines a module ```6-load_from_json_file` """
from json import load


def load_from_json_file(filename):
    """ creates an Object from a “JSON file” """
    with open(filename, "r", encode="UTF-8") as f:
        load(f)
