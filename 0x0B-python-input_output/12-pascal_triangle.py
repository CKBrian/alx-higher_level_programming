#!/usr/bin/python3
"""
defines a module ``12-pascal_triangle``
with ``def pascal_triangle`` function
"""


def pascal_triangle(n):
    """ returns a list of lists of integers
        representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    ls = [[1]]
    for i in range(n - 1):
        ls2 = [1]
        for x in range(len(ls[i])):
            if x == len(ls[i]) - 1:
                ls2.append(1)
            else:
                ls2.append(ls[i][x] + ls[i][x + 1])
        ls.append(ls2)
    return ls
