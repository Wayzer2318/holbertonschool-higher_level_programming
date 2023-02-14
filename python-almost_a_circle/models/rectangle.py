#!/usr/bin/python3
""" rectangle """
from models.base import Base


class Rectangle(Base):
    """ Rectangle inherits from base """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ The width property."""
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be greater than 0")

    @property
    def height(self):
        """ The height property."""
        return self.__height

    @height.setter
    def height(self, value):
        self._height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be greater than 0")
