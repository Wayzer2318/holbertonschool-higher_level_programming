#!/usr/bin/python3
"""Co"Contains Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overrides the inherited str method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """size getter method"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter method"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        atttset = ["id", "size", "x", "y"]

        if args:
            for idx, arg in enumerate(args):
                setattr(self, atttset[idx], arg)

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary reresentation of Square"""
        new_dict = super().to_dictionary()
        new_dict["size"] = new_dict["height"]
        del new_dict["width"], new_dict["height"]
        return new_dict
