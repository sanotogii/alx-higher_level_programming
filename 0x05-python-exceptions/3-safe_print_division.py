#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        key = a / b
        return key
    except ZeroDivisionError:
        key = None
        return key
    finally:
        print("Inside result: {}".format(key))
