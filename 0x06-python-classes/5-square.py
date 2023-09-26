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
        self.size = size

    @property
    def size(self):
        """ value (int): length of square """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ calculates square area """
        return self.__size ** 2

    def my_print(self):
        """ Prints a square """
        if self.__size == 0:
            print()
        for height in range(self.__size):
            for length in range(self.__size):
                print("#", end="")
            print()
