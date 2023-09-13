#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None
    ls = sorted(a_dictionary.items(), key=lambda x: x[1])
    return ls[-1][0]
