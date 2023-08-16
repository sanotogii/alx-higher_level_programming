#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    d_keys = []

    for key, element in a_dictionary.items():
        if element == value:
            d_keys.append(key)

    for key in d_key:
        del a_dictionary[key]
    return a_dictionary
