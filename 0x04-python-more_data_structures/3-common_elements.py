#!/usr/bin/python3
def common_elements(set_1, set_2):
    setc = set_1 & set_2  # { a & b for a, b in zip(set_1, set_2)}
    return setc
