#!/usr/bin/python3
"""`Review` class that inherits from `BaseModel`
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Inherits from `BaseModel to create a Review

    Attributes:
        place_id (str): to hold the place.id
        user_id (str): to hold the user.id
        text (str): to hold the text
    """
    place_id = ""
    user_id = ""
    text = ""
