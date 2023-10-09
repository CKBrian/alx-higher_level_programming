#!/usr/bin/python3
""" defines a subclass checking function"""


def is_kind_of_class(obj, a_class):
    """ returns True if the object is an instance of a class that
        inherited (directly or indirectly) from the specified class
        otherwise False"""
    return issubclass(obj, a_class)
