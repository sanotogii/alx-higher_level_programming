#!/usr/bin/python3
"""creation of object from a json"""
import json


def load_from_json_file(filename):
    """function"""
    with open(filename, 'r') as file:
        return json.load(file)
