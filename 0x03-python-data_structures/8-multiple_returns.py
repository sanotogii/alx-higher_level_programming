#!/usr/bin/python3
def multiple_returns(sentence):
    lenn = len(sentence)
    if sentence == []:
        t = (len, None)
    else:
        t = (lenn, sentence[0])
    return t
