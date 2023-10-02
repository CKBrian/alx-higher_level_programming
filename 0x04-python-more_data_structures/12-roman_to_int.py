#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return None
    num = 0
    rome = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for numeral in roman_string:
        if numeral not in rome:
            return None
        num += rome[numeral]
    maxi = rome[roman_string[-1]]
    for x in roman_string:
        if maxi < rome[x]:
            return int(num)
    num = maxi - (num - maxi)
    return int(num)
