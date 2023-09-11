#!/usr/bin/python3
""""add""


def add_attribute(obj, attribute, value):
    """function"""
    if hasattr(obj, '__dict__'):
        etattr(obj, attribute, value)
    else:
       raise TypeError("can't add new attribute") 
