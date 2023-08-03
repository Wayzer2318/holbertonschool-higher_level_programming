#!/usr/bin/python3
"""Contains the class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter Method"""
        return self.__width

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @property
    def x(self):
        """x getter method"""
        return self.__x

    @property
    def y(self):
        """y getter method"""
        return self.__y

    @width.setter
    def width(self, value):
        """width setter method"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter method"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """x setter method"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """y setter method"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of a Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints to the stdout a Rectangle"""
        for nwl in range(self.__y):
            print()
        for nl in range(self.__height):
            for spce in range(self.__x):
                print(" ", end="")
            for htg in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        atttset = ["id", "width", "height", "x", "y"]

        if args:
            for idx, arg in enumerate(args):
                setattr(self, atttset[idx], arg)

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary
        representation of a Rectangle
        """
        return self.__dict__

    def __str__(self):
        """Overrides the str method"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} \
- {self.width}/{self.height}"

    def to_dictionary(self):
        """Returns a dictionary reresentation of a Rectangle"""
        new_dict = {}

        for key, value in self.__dict__.items():
            key = key.split("__")[-1]
            new_dict[key] = value
        return new_dict

