#!/usr/bin/python3

""" imports a Rectangle class fri 9-rectangle module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ initializes a square subclass"""

    def __init__(self, size):
        """ size (int): Size of square sides"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculates area of square"""
        return self.__size ** 2

    def __str__(self):
        """ returns a formated string """
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__size, self.__size)
