#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    positive = 0
    negative = 0

    r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 100}
    lenght = len(roman_string)
    for i in range(lenght):
        if i+1 < lenght and r[roman_string[i]] < r[roman_string[i+1]]:
            negative -= r[roman_string[i]]
        else:
            positive += r[roman_string[i]]
    result = positive + negative
    return result
