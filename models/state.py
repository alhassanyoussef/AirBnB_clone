#!/usr/bin/python3
"""
Module for the State class.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State Class: Represents a state in the system.

    Attributes:
        name (str): The name of the state.
    """

    name = ""