#!/usr/bin/env python3
def no_c(my_string):
    str = ""
    for element in my_string:
        if element != "c" and element != "C":
            str = str + element
    return (str)
