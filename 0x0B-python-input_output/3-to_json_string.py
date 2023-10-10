#!/usr/bin/python3
""" defines ``2-append_write.py`` module """
from json import dumps


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string """
    return dumps(my_obj, ensure_ascii=False)
