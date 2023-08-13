#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for element in my_string:
        if element not in "cC":
            str += element
    return (str)
