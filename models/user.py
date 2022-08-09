#!/usr/bin/python3
"""
Defines a User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel"""
    def __init__(self):
        """Initialization"""
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
