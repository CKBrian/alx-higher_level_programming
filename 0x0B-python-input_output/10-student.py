#!/usr/bin/python3
""" ``9-student`` module that defines a class Student """


class Student:
    """ defines a class Student"""

    def __init__(self, first_name, last_name, age):
        """ initializes a class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of a
            Student instance """
        return self.__dict__

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a
            Student instance """
        if not attrs:
            return self.__dict__
        s_dic = self.__dict__
        return {key: s_dic.get("key") for key in sorted(attrs) if key in s_dic}
