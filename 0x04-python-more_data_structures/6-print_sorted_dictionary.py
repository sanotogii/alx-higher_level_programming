#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_d = sorted(a_dictionary.items())
    for key, value in new_d:
        print("{}: {}".format(key, value))
