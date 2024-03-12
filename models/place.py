#!/usr/bin/python3
""" a module for Place class manage Places place data """
import uuid
import models
from datetime import datetime
from models.base_model import BaseModel


class Place(BaseModel):
    """
        a class that inhereits from BaseModel
        that manages Place data
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """ instansiation of the Place class """
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
