#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    k = 0
    while c < x:
        try:
            print("{:d}".format(my_list[c]), end="")
            c += 1
        except (ValueError, TypeError):
            c += 1
            k += 1
    print()
    return c - k
