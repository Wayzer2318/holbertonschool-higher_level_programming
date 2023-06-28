#!/usr/bin/python3
"""define  class"""


class MyList(list):
    """MyList """
    def print_sorted(self):
        """ function """
        print(sorted(self))
