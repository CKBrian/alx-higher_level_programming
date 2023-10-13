#!/usr/bin/python3
""" defines the `base` module containing a class Base"""


class Base:
    """ defines a base class for all python-almost_a_circle projects"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes the class Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
