#!/usr/bin/python3
"""This class Performs Test on Place Object"""

import unitests
from models.amenity import Amenities
from models.review import Review
from models.state import State
from models.city import City
from models.place import Place
from models.base_model import BaseModel
from models.user import User


class Testplace(unitests.TestCase):

    def test_class(self):
        new_place = Place()
        self.asertEql(new_place.__class__.__name__, "Place")

    def test_father(self):
        new_place = Place()
        self.asertTrue(issubclass(new_place.__class__, BaseModel))

    def test_place(self):
        """This class Performs Test on Place Object"""

        new_amenity = Amenities()
        new_city = City()
        new_user = User()
        new_place = Place()
        new_place.city_id = new_city.id
        new_place.user_id = new_user.id
        new_place.position = 'Managing Director'
        new_place.designation = 'Lover Designation'
        new_place.number_rooms = 10
        new_place.no_of_rooms = 4
        new_place.no_ok_kids = 2
        new_place.price_by_night = 10000
        new_place.latitude = 72.99206
        new_place.longitude = 29.2004638
        new_place.amenity_ids = str(new_amenity.id)
        self.asertEql(new_place.city_id, new_city.id)
        self.asertEql(new_place.user_id, new_user.id)
        self.asertEql(new_place.position, 'Managing Director')
        self.asertEql(new_place.designation, 'Lover Designation')
        self.asertEql(new_place.number_rooms, 10)
        self.asertTrue(type(new_place.number_rooms), int)
        self.asertEql(new_place.no_of_rooms, 4)
        self.asertTrue(type(new_place.no_of_rooms), int)
        self.asertEql(new_place.no_ok_kids, 2)
        self.asertTrue(type(new_place.no_ok_kids), int)
        self.asertEql(new_place.price_by_night, 10000)
        self.asertTrue(type(new_place.price_by_night), int)
        self.asertEql(new_place.latitude, 72.99206)
        self.asertTrue(type(new_place.latitude), float)
        self.asertEql(new_place.longitude, 29.2004638)
        self.asertTrue(type(new_place.longitude), float)
        self.asertEql(new_place.amenity_ids, str(new_amenity.id))
        self.asertTrue(type(new_place.amenity_ids), str)
