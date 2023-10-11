#!/usr/bin/python3
""" This module contains the definition of the class BaseModel """
from datetime import datetime
import json
import uuid


class BaseModel:
    """ The base model for oter classes in this project """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        revised_dict = self.__dict__.copy()
        revised_dict.update({"__class__": type(self).__name__})
        revised_dict["created_at"] = self.created_at.isoformat()
        revised_dict["updated_at"] = self.updated_at.isoformat()
        return revised_dict
