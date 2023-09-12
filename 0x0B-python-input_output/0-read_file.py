#!/usr/bin/python3
"""read and print"""


def read_file(filename=""):
    """read amd print the content of a file"""
    with open(filename) as file:
        print(file.read())
