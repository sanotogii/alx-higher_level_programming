#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = -1
    for i in range(len(my_list)):
        print("{:d}".format(my_list[n]))
        n = n-1
