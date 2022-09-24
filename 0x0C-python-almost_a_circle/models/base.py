#!/usr/bin/python3
"""
    First class Base.
"""
import json


class Base:
    """first class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """changing json to string"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON to file"""
        filename = cls.__name__ + ".json"
        newFile = []
        if list_objs is None:
            list_objs = []
        for element in list_objs:
            newFile.append(cls.to_dictionary(element))
        with open(filename, 'w', encoding="UTF8") as f:
            return f.write(cls.to_json_string(newFile))
