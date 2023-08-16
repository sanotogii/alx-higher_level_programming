#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    d_keys = []

    for key, element in a_dictionary.items():
        if element == value:
            d_keys.append(key)

    for k in d_keys:
        del a_dictionary[k]
    return a_dictionary
