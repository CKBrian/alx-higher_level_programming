#!/usr/bin/python3

""" defines a class BaseGeometry. """


class BaseGeometry():
    """ initialise an BaseGeometry class """

    def area(self):
        """ raises an Exception with the message area() is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value
        Args:
            name (str): The name value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0."""

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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
