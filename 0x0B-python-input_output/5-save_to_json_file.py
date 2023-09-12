#!/usr/bin/python3
"""save object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """function"""
    with open(filename, w) as file:
        json.dump(my_obj, file)
