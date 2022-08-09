#!/usr/bin/python3
"""`Amenity` class that inherits from `BaseModel`
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Inherits from `BaseModel to create Amenity

    Attributes:
        name (str): to hold name
    """
    name = ""
