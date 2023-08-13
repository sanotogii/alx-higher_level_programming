#!/usr/bin/python3
def multiple_returns(sentence):
    lenn = len(sentence)
    if lenn == 0 or sentence is None:
        t = (len, None)
    else:
        t = (lenn, sentence[0])
    return t
