#!/usr/bin/python3
"""student to json"""


class Student:
    """class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        student_json = {}
        for attr in attrs:
            if hasattr(self, attr):
                student_json[attr] = getattr(self, attr)
        return student_json
