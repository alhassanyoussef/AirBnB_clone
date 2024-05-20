#!/usr/bin/python3
"""
City Module: Defines the City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City Class: Represents a city in the system.

    Attributes:
        state_id (str): The state ID associated with the city.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""