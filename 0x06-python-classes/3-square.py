#!/usr/bin/python3
"""class square with size"""


class Square:
    """class square defined by it's size"""

    def __init__(self, size=0):
        """Size validation"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Area of a square method"""

        return self.__size * self.__size
