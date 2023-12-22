#!/usr/bin/python3
"""This imports some standard modules and modules from the project packages"""
from models.base_model import BaseModel

"""
This is the Python class that models the Amenities class but inherits from
the BaseModel class as the Parent Class
"""


class Amenities(BaseModel):
    """
    This is the class modelling the Amenities object for AirBnB Clone project.
    """
    name = ""
