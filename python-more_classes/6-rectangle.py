#!/usr/bin/python3
""" rectangle """


class Rectangle():
    """ rectangle """
    number_of_instance = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instance += 1
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')

        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        else:
            Rectangle = ""
            for k in range(0, self.height):
                for i in range(self.width):
                    rectangle += "#"
                rectangle += "\n"
            return rectangle[:-1]

    def __repr__(self):
        return "Rectangle(2, 4)"
    def __del__(self):
        Rectangle.number_of_instance -= 1
        print("Bye rectangle...")
