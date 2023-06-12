#!/usr/bin/python3
"""
Define a class Square
"""


class Square:
    """
    square class
    """
    def __init__(self, size=0):
        """
        init square with size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        return area of square
        """
        return self.__size * self.__size
    
    def size(self, value):
        """
        size of square
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        self.__size = value

