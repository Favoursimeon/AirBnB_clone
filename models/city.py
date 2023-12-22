#!/usr/bin/python3
"""This imports some standard modules & modules from the project packages"""
from models.base_model import BaseModel

"""
The python class that models a City class but inherits from the BaseModel
class as Parent Class
"""


class City(BaseModel):
    """
    This is the class modelling the City object for the AirBnB Clone project.
    """
    name = ""
    state_id = ""
