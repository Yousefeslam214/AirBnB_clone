#!/usr/bin/python3

from base_model import BaseModel
from engine.file_storage import FileStorage

# Create an instance of FileStorage
storage = FileStorage()

# Create an instance of BaseModel (or any other class you want to store)
base_model = BaseModel()

# Add the BaseModel instance to the storage
storage.new(base_model)

# Save the data to the JSON file
storage.save()
