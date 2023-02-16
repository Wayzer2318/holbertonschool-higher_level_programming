#!/usr/bin/python3
""" rectangle """
from models.base import Base


class Rectangle(Base):
    """ Rectangle inherits from base """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """ area """
        return self.width * self.height

    def update(self, *args, **kwargs):
        """ update """
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def display(self):
        """ display """
        Rectangle = ""
        if self.y != 0:
            for s in range(self.y):
                print("\n", end='')
        if self.x != 0:
            q = ""
            for t in range(self.x):
                q += " "
            for i in range(0, self.height):
                Rectangle += str(q)
                for y in range(self.width):
                    Rectangle += ("#")
                Rectangle += "\n"
            print(Rectangle, end="")
        else:
            for i in range(0, self.height):
                for y in range(self.width):
                    Rectangle += "#"
                Rectangle += "\n"
            print(Rectangle, end="")

    def to_dictionary(self):
        """ dictionary """
        dictionary = {
            'id': self.id,
            'width': self.width,
            'height': self.height
            'x': self.x,
            'y': self.y}
        return (dictionary)

    def __str__(self):
        """ str """
        str = ("[Rectangle] (%s) %s/%s - %s/%s" %
               (self.id, self.x, self.y, self.width, self.height))
        return str

    @property
    def width(self):
        """ The width property. """

        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ The height property. """

        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ The x property. """

        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ The y property. """

        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
