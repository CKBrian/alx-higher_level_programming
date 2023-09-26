#!/usr/bin/python3
""" A class for square attributes """


class Square:
    """ Defines a class named square  """

    def __init__(self, size=0):
        """
            this initialises a square class
            Args:
                size (int): length of square sides
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ calculates square area """
        return self.__size ** 2
