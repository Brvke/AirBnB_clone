#!/usr/bin/python3
"""base model for airbnb"""
from datetime import datetime
import uuid
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        """ initialization """
        if kwargs:
            del kwargs["__class__"]
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],"%Y-%m-%dT%H:%M:%S.%f")
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],"%Y-%m-%dT%H:%M:%S.%f")
            self.__dict__ = kwargs
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)


    def __str__(self):
        """print the string representation of instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id , self.__dict__)
    
    def save(self):
        """update the base model date and time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all the
            keys/value pairs of __dict__ of the instance"""
        a = self.__dict__.copy()
        a["__class__"] = self.__class__.__name__
        a["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        a["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return a
    
    def __setattr__(self, key, value):
        """ sets attribute for a class """
        object.__setattr__(self, key, value)
        object.__setattr__(self, 'updated_at', datetime.now())
