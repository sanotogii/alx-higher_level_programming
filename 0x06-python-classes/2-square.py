#!/usr/bin/python3
"""class square with size"""


class Square:
    """class square defined by it's size"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError
            print("size must be an integer")
        elif size < 0:
            raise ValueError
            print("size must be >= 0")
        self.__size = size
