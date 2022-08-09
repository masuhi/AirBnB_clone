#!/usr/bin/python3
"""`City` class that inherits from `BaseModel`
"""
from models.base_model import BaseModel


class City(BaseModel):
        """Inherits from BaseModel to create a City"""
        state_id = ""
        name = ""
