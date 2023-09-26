#!/usr/bin/python3
""" A class for square attributes """


class Square:
    def __init__(self, size=0):
        """
            this initialises a square class
            Args:
                size (int): length of square sides
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
