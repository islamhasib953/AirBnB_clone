#!/usr/bin/python3
"""
Class FileStorage
"""
import json
import os
class FileStorage:
    """convert the dictionary representation to a JSON string and can reverse
    """
    __file_path="file.json"
    __objects={}
    def all(self):
        """
        returns the dictionary __objects
        """
        return(FileStorage.__objects)
    
    def new(self, obj):
        """
        sets in __objects the obj with key
        """
        FileStorage.__objects[obj.__class__.__name__+'.'+obj.id]=obj
    def save(self):
        """
        serializes __objects to the JSON file
        """
        dictionary_obj = {}
        for key, val in FileStorage.__objects.items():
            dictionary_obj[key] = val
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dictionary_obj, f)
    
    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path,'r') as f:
                FileStorage.__objects=json.load(f)
        else:
            pass
