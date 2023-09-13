#!/usr/bin/python3
def search_replace(my_list, search, replace):
    ls = [replace if item == search else item for item in my_list]
    return ls
