#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        fct(*args)
    except Exception as nerr:
        stderr.write("Exception: {}\n".format(nerr))
        return None
