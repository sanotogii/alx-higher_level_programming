#!/usr/bin/python3
"""write a file"""


def write_file(filename="", text=""):
    """write the file function"""
    with open(filename, "x") as file:
        file.write(text, end="")
    return len(text)

