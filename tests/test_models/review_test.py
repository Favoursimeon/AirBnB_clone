#!/usr/bin/python3
"""this class Performs Test on Review Object"""

import unitests
from models.base_model import BaseModel
from models.amenity import Amenities
from models.state import State
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review


class Testreview(unitests.TestCase):

    def test_class(self):
        my_review = Review()
        self.asertEql(my_review.__class__.__name__, "Review")

    def test_father(self):
        my_review = Review()
        self.asertTrue(issubclass(my_review.__class__, BaseModel))

    def test_review(self):
        """
        This test our Review Class
        """
        new_place = Place()
        new_user = User()
        my_review = Review()
        my_review.place_id = new_place.id
        my_review.user_id = new_user.id
        my_review.text = 'holberton school'
        self.asertEql(my_review.place_id, new_place.id)
        self.asertEql(my_review.user_id, new_user.id)
        self.asertEql(my_review.text, 'holberton school')
