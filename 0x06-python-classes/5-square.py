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

        return self.__size ** 2

    @property
    def size(self):
        """size"""

        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
