#!/usr/bin/python3
"""rectangle"""
from models.base import Base


class Rectangle(Base):
    """init"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    """this section of the code is about Validate attributes"""
    def intvalid(self, attribute, value):
        """check if the value is int"""
        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")

    def valid_signe(self, attribute, value):
        """checks if the value is absolute"""
        if value <= 0:
            raise ValueError(f"{attribute} must be > 0")

    def valid_value(self, attribute, value):
        """checks if the value is positive"""
        if value < 0:
            raise ValueError(f"{attribute} must be >= 0")

    def validation(self, width, height, x, y):
        """checks the validation of the values with the help of the funcs above"""
        self.intvalid("height", height)
        self.intvalid("width", width)
        self.intvalid("x", x)
        self.intvalid("y", y)
        self.valid_signe("height", height)
        self.valid_signe("width", width)
        self.valid_value("x", x)
        self.valid_value("y", y)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.intvalid("width", value)
        self.valid_signe("width", value)
        self.__width = value

    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        self.intvalid("height", value)
        self.valid_signe("height", value)
        self.__height = value

    @property
    def x(self):
        """x"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.intvalid("x", value)
        self.valid_value("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.intvalid("y", value)
        self.valid_value("y", value)
        self.__y= value
