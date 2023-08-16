#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    somme = 0
    for element in new_list:
        somme += element 
    return somme
