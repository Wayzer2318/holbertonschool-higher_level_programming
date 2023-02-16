#!/usr/bin/python3
""" square """


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id)
        super().__init__(x)
        super().__init__(y)
        super().__init__(size, size)
        self.size = size

    def __str__(self):
        """ str """
        str = ("[Square] (%s) %s/%s - %s/%s" %
               (self.id, self.x, self.y, self.size, self.size))
        return str
