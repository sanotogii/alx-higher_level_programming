#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        for i in range(-1, -len(my_list)-1, -1):
            print("{:d}".format(my_list[i]))
