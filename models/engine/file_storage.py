#!/usr/bin/env python3

"""File storage"""

import json
from models.base_model import BaseModel
from models.user import User
import models

class FileStorage:
    """This class serializes instances to a JSON file
    deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel}

    def all(self):
        """Returns the dictionary containing all stored objects."""
        return self.__objects

    def new(self, obj):
        """Adds the object to __objects with the key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Reads the JSON file and converts the
        JSON string back into Python objects."""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
            for key, value in new_obj_dict.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
