#!/usr/bin/python3
"""append to a file """


def append_write(filename="", text=""):
    """append fucntion"""
    with open(filename, "a") as file:
        file.append(text)
    return len(text)
