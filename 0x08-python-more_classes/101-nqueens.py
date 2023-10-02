#!/usr/bin/python3
""" A class of Qeen attributes"""
import sys


class Queens:
    """
        defines the class Queens
    """
    def __init__(self, num=0):
        """ initializes the class Queens"""
        self.num = num

    @property
    """ value (int): N to be evaluated"""
    def num(self):
        return self.__num

    @num.setter
    def num(self, value):
        if not isinstance(num, int):
            raise TypeError("N must be a number")
        if value < 4:
            raise ValueError("N must be at least 4")

    def print_soln(self):
        """ value (int): N to be evaluated"""
        pass


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    N = sys.argv[1]
