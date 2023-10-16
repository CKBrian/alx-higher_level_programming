#!/usr/bin/python3
""" defines the `base` module containing a class Base"""
from json import dumps
from json import loads
from os import path
from csv import DictWriter
from csv import DictReader


class Base:
    """ defines a base class for all python-almost_a_circle projects"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes the class Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return dumps(list_dictionaries, ensure_ascii=False)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w", encoding="UTF-8") as obj_file:
            if list_objs is None:
                obj_file.write("[]")
            else:
                obj_strn = cls.to_json_string([item.to_dictionary()
                                              for item in list_objs])
                obj_file.write(obj_strn)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        obj = cls(1, 1, 1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        obj_list = []
        if not path.exists(filename):
            return obj_list
        with open(filename, "r", encoding="UTF-8") as obj_file:
            for item in obj_file:
                obj_dict = cls.from_json_string(item)
                for dict_item in obj_dict:
                    new_obj = cls.create(**dict_item)
                    obj_list.append(new_obj)
        return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes dictionary objects to CSV """
        filename = "{}.csv".format(cls.__name__)
        list_dicts = [obj.to_dictionary() for obj in list_objs]

        with open(filename, "w", newline="") as f:
            writer = DictWriter(f, fieldnames=list_dicts[0].keys())
            writer.writeheader()
            for row in list_dicts:
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes in CSV to dictionary objects """
        filename = "{}.csv".format(cls.__name__)
        list_objs = []

        if not path.exists(filename):
            return list_objs

        with open(filename, "r", newline="") as f:
            reader = DictReader(f)
            for row in reader:
                dict_item = {k: int(v) if v.isdigit()
                             else v for k, v in row.items()}
                new_obj = cls.create(**dict_item)
                list_objs.append(new_obj)

        return list_objs
