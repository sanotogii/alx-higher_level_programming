#!/usr/bin/python3
def multiple_returns(sentence):
    lenn = len(sentence)
    if len(sentence) == 0:
        t = (lenn, None)
    else:
        t = (lenn, sentence[0])
    return t
