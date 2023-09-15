#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    rome = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for numeral in roman_string:
        num += rome[numeral]
    maxi = rome[roman_string[-1]]
    if maxi > num - maxi:
        num = maxi - (num - maxi)
    return int(num)
