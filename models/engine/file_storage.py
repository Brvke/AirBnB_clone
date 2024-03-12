#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary __object"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets the value of __objects """
        classname = obj.__class__.__name__
        FileStorage.__objects[f'{classname}.{obj.id}'] = obj

    def path(self):
        """ returns the path of the json file """
        return FileStorage.__file_path

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            towrite = {obj: FileStorage.__objects[obj].to_dict()
                       for obj in FileStorage.__objects.keys()}
            json.dump(towrite, f)
    def reload(self):
        """
            deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists;
            otherwise, do nothing.
            If the file doesnt exist, no exception should be raised)
        """
        if os.path.exists(self.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                try:
                    newdict = json.load(f)
                    for i in newdict.keys():
                        newinstance = \
                         eval(newdict[i]["__class__"])(**newdict[i])
                        self.new(newinstance)
                except json.decoder.JSONDecodeError:
                    pass

