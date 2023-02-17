#!/usr/bin/python3
""" unittest """
import unittest
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """ unittest """

    def test_init(self):

        r = Rectangle(8, 6, 4, 2, 10)

        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.area(), 48)

        r = Rectangle(8, 6)

        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 6)
