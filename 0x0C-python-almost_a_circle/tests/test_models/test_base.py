#!/usr/bin/python3
"""test"""
import unittest
import os
from models.rectangle import Rectangle
from models.base import Base


class TestBase(unittest.TestCase):
    """test class"""
    def setUp(self):
        """method"""
        Base._Base__nb_objects = 0
    def test_base(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

if __name__ == '__main__':
    unittest.main()
