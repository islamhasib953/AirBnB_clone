#!/usr/bin/python3
"""
Class FileStorage
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """convert the dictionary representation
    to a JSON string and can reverse"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key
        """
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        dictionary_obj = {}
        for key, val in FileStorage.__objects.items():
            dictionary_obj[key] = val.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dictionary_obj, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.load(f)
                for key, val in FileStorage.__objects.items():
                    if val["__class__"] == "BaseModel":
                        FileStorage.__objects[key] = BaseModel(**val)
                    elif val["__class__"] == "User":
                        FileStorage.__objects[key] = User(**val)
                    elif val["__class__"] == "Place":
                        FileStorage.__objects[key] = Place(**val)
                    elif val["__class__"] == "State":
                        FileStorage.__objects[key] = State(**val)
                    elif val["__class__"] == "City":
                        FileStorage.__objects[key] = City(**val)
                    elif val["__class__"] == "Amenity":
                        FileStorage.__objects[key] = Amenity(**val)
                    elif val["__class__"] == "Review":
                        FileStorage.__objects[key] = Review(**val)
        else:
            pass
