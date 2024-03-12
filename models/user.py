#!/usr/bi/python3

from models.base_model import BaseModel
import models
import uuid
from datetime import datetime

class User(BaseModel):
    """a class inherited from basemodel to manage user data"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    def __init__(self, *args, **kwargs):
        """ initializing of the user class """
        if kwargs:
            self.__dict__ = {
                **kwargs,
                "created_at": datetime.fromisoformat(kwargs["created_at"]),
                "updated_at": datetime.fromisoformat(kwargs["updated_at"]),
                "__class__": ""
            }
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)


