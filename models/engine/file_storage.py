#!/usr/bin/python3
import os
import json
from models.base_model import BaseModel
class FileStorage():
    def __init__(self):
        self.__file_path = "file path"
        self.__objects = {} #<class name>.id

    #@method.get()
    def all(self):
        return self.__objects
    
    #@set
    def new(self, obj):
        dict = BaseModel.to_dict()
        for i in dict:
            print(i)
        #self.__objects = {to_dict()}


FileStorage.new()
