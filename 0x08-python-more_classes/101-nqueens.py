#!/usr/bin/python3
"""initializing the board"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)





def solve():
    col = set
    positive_diagonal = set()
    negative_diagonal = set()
    result = []
    backtrack(0)
    return result
