#!/usr/bin/python3
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    __file_path = "file.json"
    __objects = {}  # <class name>.id

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w') as outfile:
            json.dump({k: v.to_dict()
                       for k, v in FileStorage.__objects.items()}, outfile)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        models = {'BaseModel': BaseModel, 'User': User,
                           'Amenity': Amenity, 'City': City, 'State': State,
                           'Place': Place, 'Review': Review}
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for k, v in obj_dict.items():
                    for model, cls in models.items():
                        if v["__class__"] == model:
                            self.__objects[k] = cls(**v)
        except FileNotFoundError:
            pass
