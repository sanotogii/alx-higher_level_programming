#!/usr/bin/python3
for harf in range(ord('a'), ord('z')+1):
    if harf != ord('e') and harf != ord('q'):
        print("{}".format(chr(harf)), end='')
