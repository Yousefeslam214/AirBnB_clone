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
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
