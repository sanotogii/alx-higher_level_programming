#!/usr/bin/python3
"""test"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """test class"""
    def setUp(self):
        """method"""
        Base._Base__nb_objects = 0
    def test_base(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

if __name__ == '__main__':
    unittest.main()
