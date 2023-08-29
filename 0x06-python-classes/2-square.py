#!/usr/bin/python3
"""class square with size"""


class Square:
    """class square defined by it's size"""

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        eif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
