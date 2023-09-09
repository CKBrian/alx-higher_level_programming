#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a
    b = tuple_b
    if not b and not a:
        return None
    if not a:
        return (b[0], b[1])
    elif not b:
        return (a[0], a[1])
    elif not a[1] and not b[1]:
        return (a[0] + b[0], 0)
    elif len(a) == 1:
        return (a[0] + b[0], b[1])
    elif len(b) == 1:
        return (a[0] + b[0], a[1])
    else:
        return (a[0] + b[0], b[1] + a[1])
