#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
# def solve(s):
#     names = s.split(' ')
#     rename = []
#     for item in names:
#         rename.append(chr(ord(item[0])-32) + item[1:])
#     return ' '.join(rename)


def solve(s):
    for i in s.split():
        s = s.replace(i, i.capitalize())
    return s


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    # fptr.write(result + '\n')
    #
    # fptr.close()
