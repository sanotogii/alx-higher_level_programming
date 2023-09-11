#!/usr/bin/python3
"""print sorted list"""


class Mylist(list):
    """sort"""

    def print_sorted(self):
        print(sorted(self))
