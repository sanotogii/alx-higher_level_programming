#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return my_list
    c = len(my_list)
    for i in range(idx, c-1):
        my_list[i] = my_list[i+1]
        c -= 1
    return my_list
