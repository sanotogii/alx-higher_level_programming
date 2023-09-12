#!/usr/bin/python3
"""write a file"""


def write_file(filename="", text=""):
    """write the file function"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    return len(text)

