#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    _sum, sweight = 0, 0

    for score, weight in my_list:
        sweight += score * weight
        _sum += weight
    avg = sweight / _sum

    return avg
