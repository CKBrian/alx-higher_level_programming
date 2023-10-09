#!/usr/bin/python3
""" defines a class Mylist that inherits from list"""


class MyList(list):
    """ MyList subclass """

    def __init__(self):
        """ initialises MyList subclass """
        super().__init__()

    def print_sorted(self):
        """ print a sortend list of integers"""
        print(sorted(self))
