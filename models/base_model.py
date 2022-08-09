#!/usr/bin/python3
"""
The `BaseModel class` that defines all common attributes/methods
for other classes
"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """Defines the common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel class

        Args:
            *args (any type): A variable number of arguments
            **kwargs (dict): Key/value pairs of attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    t_format = "%Y-%m-%dT%H:%M:%S.%f"
                    self.__dict__[key] = datetime.strptime(value, t_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Updates the public instance attribute `updated_at`
        with the current datetime
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def __str__(self):
        """Returns the string representation of an instance of BaseModel
        """
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of `__dict__` of the instance.
        """
        converted = self.__dict__.copy()
        converted["created_at"] = self.created_at.isoformat()
        converted["updated_at"] = self.updated_at.isoformat()
        converted["__class__"] = self.__class__.__name__
        return (converted)
