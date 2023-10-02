#!/usr/bin/python3
""" A class for attributes and methods describing a Rectangle """


class Rectangle:
    """
        defines a Rectangle class
    """
    def __init__(self, width=0, height=0):
        """ initializes a Rectangle class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ value (int): value of the width """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ value (int): value of the height """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ returns the rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """ returns the rectangle perimeter """
        return (self.__width * 2) + (self.__height * 2)
