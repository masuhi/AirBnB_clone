#!/usr/bin/python3
"""
Defines a FileStorage Class
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Representation of a FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file path `__file_path`
        """
        a_copy = FileStorage.__objects
        obj_dict = {obj: a_copy[obj].to_dict() for obj in a_copy.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                objs = json.load(f)
                for obj in objs.values():
                    name = obj['__class__']
                    del obj['__class__']
                    self.new(eval(name)(**obj))
        except FileNotFoundError:
            return
