#!/usr/bin/python3

def print_square(size):
    """ a function that prints a square with the character #. """
    if not isinstance(size, int) or isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print("{}".format("\n".join("#" * size for _ in range(size))))
