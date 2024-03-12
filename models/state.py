#!/usr/bin/python3
import uuid
import models
from datetime import datetime
from models.base_model import BaseModel

class State(BaseModel):
    """
        a class that inhereits from BaseModel
        that manages State data
    """
    name = ""  # creating empty string

    def __init__(self, *args, **kwargs):
        """ initializing of the State class """
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


