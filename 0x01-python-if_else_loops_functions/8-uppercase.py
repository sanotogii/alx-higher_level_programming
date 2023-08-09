#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) <= ord('z') and ord(i) >= ord('a'):
            print("{}".format(chr(ord(i)-32)), end="")
        else:
            print("{}".format(i), end="")
    print()
