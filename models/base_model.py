#!/usr/bin/env python3
"""
contain the BaseModel class
"""
import uuid
from datetime import datetime
import models
T_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """This is the parent class that defines all common attributes
    /methods for other classes."""

    def __init__(self, *args, **kwargs):
        """The constructor."""
        if kwargs:  # Initialize with kwargs
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    # Convert string datetime to datetime objects
                    kwargs[key] = datetime.strptime(value, T_format)
                # Skip the '__class__' attribute
                if key != "__class__":
                    setattr(self, key, value)
        else:
            # Default Initialization
            self.id = str(uuid.uuid4())
            now = datetime.utcnow()
            self.created_at = now
            self.updated_at = now

    def __str__(self):
        """Returns a string representation of the instance,
        including class name, id, and attributes."""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """Updates the attribute 'updated_at' with the current datetime."""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        data = self.__dict__.copy()
        data["__class__"] = self.__class__.__name__
        for key, value in data.items():
            if isinstance(value, datetime):
                data[key] = value.isoformat()
        return data
