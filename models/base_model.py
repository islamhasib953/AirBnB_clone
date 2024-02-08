#!/usr/bin/python3
"""
Class BaseModel
"""

import uuid
import datetime
import models


class BaseModel:
    """public instance attributes.

    Methods:
        __init__: Initialize a new instance from BaseModle
        __str__: str function that return class name, id and dict
        save: updates the public instance attribute updated_at
        to_dict: returns a dictionary containing all keys/values of __dict__ of the instance
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new instance from BaseModle

        Args:
            args: from it can pass any number of positional arguments is a tuple
            kwargs: from it can pass any number of keyword arguments is a dictionary
        """
        if kwargs:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.datetime.strptime(
                        val, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at =datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """str function

        Returns:
            [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()


    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        dich = self.__dict__.copy()
        dich["__class__"] = self.__class__.__name__
        dich["created_at"] = dich["created_at"].isoformat()
        dich["updated_at"] = dich["updated_at"].isoformat()
        return(dich)
