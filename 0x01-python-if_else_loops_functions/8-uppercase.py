#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str))
        if ord(str[i]) <= ord('z') and ord(str[i]) >= ord('a'):
            print("{}".format(chr(ord(str[i])-32)))
        else:
            print("{}".format(str[i]))
