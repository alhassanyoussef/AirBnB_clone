#!/usr/bin/env python3

"""Contains the User class."""

from models.base_model import BaseModel
import models


class User(BaseModel):
    """Class that inherits from BaseModel."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
