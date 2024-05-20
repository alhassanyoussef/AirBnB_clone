#!/usr/bin/python3
"""
Amenity Module: Defines the Amenity class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity Class: Represents an amenity in the system.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""