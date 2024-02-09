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
        with open(FileStorage.__file_path, 'a') as outfile:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, outfile)

    def reload(self):
        if not os.path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path,'r') as outfile:
            deserialized = None
            try:
                deserialized = json.load(outfile)
            except json.JSONDecodeError:
                pass
            if deserialized is None:
                return
            



