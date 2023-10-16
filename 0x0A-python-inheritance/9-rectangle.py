#!/usr/bin/python3

""" defines a class BaseGeometry. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ inherits from Base Geometry"""

    def __init__(self, width, height):
        """ initializes a rectangle """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ returns a formated string """
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__width, self.__height)

    def area(self):
        """ calculates Rectangle area """
        return self.__width * self.__height


if __name__ == "__main__":
    print(issubclass(Rectangle, BaseGeometry))
