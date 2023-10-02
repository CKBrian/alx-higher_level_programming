#!/usr/bin/python3
""" A class for attributes and methods describing a Rectangle """


class Rectangle:
    """
        defines a Rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initializes a Rectangle class"""
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    def __del__(self):
        """ deletes a Rectangle class"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @classmethod
    def set_print_symbol(cls, print_symbol):
        """ makes print_symbol attribute available to all class methods """
        cls.print_symbol = print_symbol

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
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ returns a user friendly string representing a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        sym = str(self.print_symbol)
        return "\n".join(sym * self.__width for _ in range(self.__height))

    def __repr__(self):
        """ returns a developer friendly string representing a rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"
