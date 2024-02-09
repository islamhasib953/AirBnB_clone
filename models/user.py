#!/usr/bin/python3
"""
Class User
"""
from .base_model import BaseModel


class User(BaseModel):
    """public instance attributes.

    Attributes:
        email (str):
        password (str):
        first_name (str):
        last_name (str):
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
