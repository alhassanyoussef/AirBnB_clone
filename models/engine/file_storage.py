#!/usr/bin/python3
"""
Module for serializing and deserializing data
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class FileStorage:
    """
    FileStorage Class: Handles storing, serializing, and deserializing data.

    Attributes:
        __file_path (str): The path to the JSON file for data storage.
        __objects (dict): A dictionary to store serialized objects.
    """
    __file_path = "file.json"

    __objects = {}

    def new(self, obj):
        """
        Adds a new object to the __objects dictionary with the key <obj class name>.id.
        """
        obj_cls_name = obj.__class__.__name__

        key = "{}.{}".format(obj_cls_name, obj.id)

        FileStorage.__objects[key] = obj


    def all(self):
        """
        Returns all objects stored in the __objects dictionary.
        """
        return  FileStorage.__objects


    def save(self):
        """
        Serializes the __objects dictionary into JSON format and saves it to the file specified by __file_path.
        """
        all_objs = FileStorage.__objects

        obj_dict = {}

        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file and reloads the objects into the __objects dictionary.
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')

                        cls = eval(class_name)

                        instance = cls(**value)

                        FileStorage.__objects[key] = instance
                except Exception:
                    pass





























