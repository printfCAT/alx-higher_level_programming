#!/usr/bin/python3
""" define a class """


import json
import os
import csv


class Base:
    """ superclass Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Args:
                id(int). integer counter for objects initialized
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON string rep """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string rep of an object to a file """
        filename = cls.__name__ + ".json"
        list_dict = []
        if list_objs is not None:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
        with open(filename, mode='w', encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """ returns list of JSON string rep """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes set """
        s1 = cls(3, 5, 1)
        for key, value in dictionary.items():
            setattr(s1, key, value)
        return s1

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = cls.__name__ + ".json"
        inst_lst = []
        if not os.path.exists(filename):
            return inst_lst
        else:
            with open(filename, 'r') as f:
                string = cls.from_json_string(f.read())
                for dct in string:
                    inst = cls.create(**dct)
                    inst_lst.append(inst)
        return inst_lst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes a file in CSV """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csv_file:
            if cls.__name__ == 'Rectangle':
                field = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == 'Square':
                field = ['id', 'size', 'x', 'y']
            csv_writer = csv.DictWriter(csv_file, fieldnames=field)
            for obj in list_objs:
                csv_writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes a file from CSV """
        filename = cls.__name__ + ".csv"
        with open(filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            instances = []
            for row in csv_reader:
                row_dict = {k: int(v) for k, v in row.items()}
                inst = cls.create(**row_dict)
                instances.append(inst)
        return instances
