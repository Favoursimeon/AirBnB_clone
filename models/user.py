#!/usr/bin/python3
"""This imports some standard modules and modules fro packages"""
from models.base_model import BaseModel

"""
This is the Python class that models a User class but inherits
BaseModel class as Parent Class
"""


class User(BaseModel):
    """
    This is the class modelling the User object for the AirBnB Clone project.
    """
    first_name = ""
    last_name = ""
    email = ""
    password = ""
