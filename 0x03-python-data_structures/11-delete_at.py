#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) == 0:
        pass
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
