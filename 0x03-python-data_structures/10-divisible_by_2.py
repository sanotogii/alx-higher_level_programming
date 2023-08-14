#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        pass
    t = []
    for i in range(len(my_list)-1):
        if my_list[i] % 2 == 0:
            t.append(True)
        else:
            t.append(False)
    return (t)
