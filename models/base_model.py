#!/usr/bin/python3
"""This imports some Standard modules and modules from the project packages"""
from datetime import datetime as dt
import uuid as uid
import models

"""
This is the Python class that will use Base class or Parent class from which
the other classes will inherit.
"""


class BaseModel():
    """
    This is the class modelling BaseModel object for the AirBnB Clone project.
    """
    def __init__(self, *args, **Kwrds) -> None:
        """This is constructor for BaseModel class that makes and instance
        an instances of the BaseModel object when created.
        Args:
            args (any) - the non-keywrded arguments
            Kwrds (any) - the keywrded key and valued paired arguments
        """

        if Kwrds != {} and Kwrds is not None and bool(Kwrds):
            for key in Kwrds:
                if key in ["created_at", "updated_at"]:
                    self.__dictn__[key] = dt.fromisoformat(Kwrds[key])
                else:
                    self.__dictn__[key] = Kwrds[key]
        else:
            self.id = str(uid.uuid4())
            self.created_at = dt.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self) -> str:
        """The Public instance method for the BaseModel that returns a String
        The representation of our BaseModel class"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dictn__)

    def save(self) -> None:
        """The Public instance method that updates the `updated_at` public
         property instance"""
        self.updated_at = dt.now()
        models.storage.save()

    def to_dictn(self) -> dictn:
        """The Public instance method that returns dictionary of key of
        __dictn__ of the BaseModel instance"""
        data = self.__dictn__.copy()
        data["__class__"] = type(self).__name__
        data["created_at"] = data["created_at"].isoformat()
        data["updated_at"] = data["updated_at"].isoformat()
        return data
