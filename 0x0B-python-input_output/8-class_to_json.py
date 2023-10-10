#!/usr/bin/python3
"""defines a ``class_to_json`` module"""


def class_to_json(obj):
    """ returns the dictionary description with simple data structure
        for JSON serialization of an object:
        obj (class): is an instance of a Class
    """
    return obj.__dict__
