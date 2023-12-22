#!/usr/bin/python3
"""This imports some of the standard modules and modules from packages"""
from models.base_model import BaseModel

"""
This is the python class that models the Review class but inherits
BaseModel class as the Parent Class
"""


class Review(BaseModel):
    """
    This is the class modelling the Review object for the AirBnB Clone project.
    """
    user_id = ""
    text = ""
    place_id = ""
