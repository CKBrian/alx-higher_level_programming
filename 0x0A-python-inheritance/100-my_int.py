#!/usr/bin/python3

""" defines a MyInt class"""


class MyInt(int):
    """ initializes an int class that inherits from builtin int"""

    def __eq__(self, other):
        """ inverts == to != """
        return super().__ne__(other)

    def __ne__(self, other):
        """ inverts != to == """
        return super().__eq__(other)
