#!/usr/bin/python3
"""This imports some of the standard modules and modules from packages"""
from models.base_model import BaseModel

"""
This is the Python class that models a Place class but inherits
BaseModel class as the Parent Class
"""


class Place(BaseModel):
    """
    This is the class modelling that Places object for the AirBnB Clone project.
    """
    amenity_ids = []
    city_id = ""
    description = ""
    name = ""
    number_bathrooms = 0
    number_rooms = 0
    latitude = 0.0
    longitude = 0.0
    max_guest = 0
    price_by_night = 0
    user_id = ""
