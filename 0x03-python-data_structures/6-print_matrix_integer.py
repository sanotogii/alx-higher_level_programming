#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    for list in matrix:
        for i in list:
            if i == list[len(list)-1]:
                print("{:d}".format(i))
            else:
                print("{:d}".format(i), end=" ") 
