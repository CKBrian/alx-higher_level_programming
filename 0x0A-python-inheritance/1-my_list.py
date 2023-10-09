#!/usr/bin/python3

""" defines a class Mylist that inherits from list"""


class MyList(list):
    """ implements sorted list print function """

    def print_sorted(self):
        """ print a sortend list of integers"""
        print(sorted(self))
