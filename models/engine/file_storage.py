#!/usr/bin/python3
import os
import json


class FileStorage():
    __file_path = "file.json"
    __objects = {} #<class name>.id

    #@method.get()
    def all(self):
        return FileStorage.__objects

    #@set
    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        print(FileStorage.__file_path)
        with open(FileStorage.__file_path, 'w') as outfile:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, outfile)

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
