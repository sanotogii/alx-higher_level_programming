#!/usr/bin/python3
"""write a file"""


def write_file(filename="", text=""):
    with open(filename, "x") as file:
        file.write(text)

