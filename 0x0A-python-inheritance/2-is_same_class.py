#!/usr/bin/python3

""" defines a class Mylist that inherits from list"""


def is_same_class(obj, a_class):
    """  returns True if the object is exactly an instance of the
        specified class ; otherwise False"""
    return isinstance(obj, a_class)
