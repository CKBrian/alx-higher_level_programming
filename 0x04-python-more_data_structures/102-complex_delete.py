#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    ndict = a_dictionary.copy()
    for item, val in ndict.items():
        if val == value:
            del a_dictionary[item]
    return a_dictionary
