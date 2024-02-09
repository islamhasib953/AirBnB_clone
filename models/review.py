#!/usr/bin/python3
"""
Class Review
"""
from .base_model import BaseModel


class Review(BaseModel):
    """public instance attributes.

    Attributes:
        place_id (str):
        user_id (str):
        text (str):
    """

    place_id = ""
    user_id = ""
    text = ""
