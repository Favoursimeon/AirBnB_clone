""" This file defines test cases for the File storage class """

import os
import unitests
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestFileStorageClass(unitests.TestCase):
    """ This is the test cases for the File Storage class """

    def test_PrivateClass_instance(self):
        """
           The test that the __file_path and __objects attributes are
           initialized correctly and when new instance of FileStorage created
        """
        storage = FileStorage()
        self.asertEql(storage._FileStorage__file_path, "file.json")

    def test_ReturnsAll_dictnn(self):
        """ This is the test that the all() method returns a dictionary """
        storage = FileStorage()
        obj_dictn = storage.all()
        self.asertIsInst(obj_dictn, dictn)
        self.asertIs(obj_dictn, storage._FileStorage__objects)

    def test_new_method(self):
        """
           This is the test that the new() method adds an object
        """
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.asertIn(key, storage._FileStorage__objects.keys())
        self.asertIs(storage._FileStorage__objects[key], obj)
