#!/usr/bin/python3
"""This class Performs Test on User Object"""

import unitests
from models.amenity import Amenities
from models.city import City
from models.user import User
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.state import State


class Testuser(unitests.TestCase):

    def test_User(self):
        """
        This test attributes of Class User
        """
        new_user = User()
        new_user.first_name = 'Testing'
        new_user.last_name = 'Administrator'
        new_user.email = 'test@oop.com'
        self.asertEql(new_user.first_name, 'Testing')
        self.asertEql(new_user.last_name, 'Administrator')
        self.asertEql(new_user.email, 'test@oop.com')
