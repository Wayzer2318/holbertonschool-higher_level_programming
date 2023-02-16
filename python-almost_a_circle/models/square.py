#!/usr/bin/python3
""" square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square """
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """The size property."""
        return self.width

    @size.setter
    def size(self, size):
        self.height = size
        self.width = size

    def __str__(self):
        """ str """
        ident = self.id
        size = self.height
        x = self.x
        y = self.y

        return f"[Square] ({ident}) {x}/{y} - {size}"
