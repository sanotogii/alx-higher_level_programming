#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    try:
        while c < x:
            print("{}".format(my_list[c]), end="")
            c += 1
    except IndexError:
        pass
    finally:
        print()
    return c
