#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigitHelper(n):
    if len(n) == 1:
        return n
    sum = 0
    for c in n:
        sum += int(c)
    return superDigitHelper(str(sum))

def superDigit(n, k):
    return int(superDigitHelper(str(k * int(superDigitHelper(n)))))
    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    print(str(result) + '\n')