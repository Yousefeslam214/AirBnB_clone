#!/usr/bin/python3
import json
import os

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        objects_dict = {}
        
        for key, obj in self.__objects.items():
            objects_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(objects_dict, file)

    def reload(self):
        """
        deserializes the JSON file
        to __objects (only if the
        JSON file (__file_path)
        """

        try:
            with open(self.__file_path, "r", encoding='utf-8') as f:
                json_objs = json.load(f)
            for key, value in json_objs.items():
                print(key)
                print(value)
        except FileNotFoundError:
            pass
