#!/usr/bin/python3

"""
function that finds a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    if list_of_integers == []:
        return None
    else:
        peak = list_of_integers[0]
        for i in range(1, len(list_of_integers)):
            if (peak < list_of_integers[i]):
                peak = list_of_integers[i]
        return peak
