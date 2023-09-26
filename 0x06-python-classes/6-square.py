#!/usr/bin/python3
""" A class for square attributes """


class Square:
    """ Defines a class named square  """

    def __init__(self, size=0, position=(0, 0)):
        """
            this initialises a square class
            Args:
                size (int): length of square sides
                position (tuple): tuple of two positive integers
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ value (tuple): length of square """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ calculates square area """
        return self.__size ** 2

    def my_print(self):
        """ Prints a square """
        if self.__size == 0:
            print()
            return
        for pos_V in range(self.__position[1]):
            print()
        for height in range(self.__size):
            for pos_H in range(self.__position[0]):
                print(" ", end="")
            for length in range(self.__size):
                print("#", end="")
            print()
