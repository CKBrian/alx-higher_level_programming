#!/usr/bin/python3
"""
    calculates the sum of two integer and float numbers
"""
def add_integer(a, b=98):
    """
		adds two integers and returns result
		if b is not provided it defaults to 98
	"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
