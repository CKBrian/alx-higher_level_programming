#!/usr/bin/python3
""" ``11-student`` module that defines a class Student """
from json import load


class Student:
    """ defines a class Student"""

    def __init__(self, first_name, last_name, age):
        """ initializes a class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a
            Student instance """
        if not attrs:
            return self.__dict__
        my_dict = self.__dict__
        return {key: my_dict[key] for key in sorted(attrs) if key in my_dict}

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance:"""
        obj = json
        self.first_name = obj.get("first_name")
        self.last_name = obj.get("last_name")
        self.age = obj.get("age")
