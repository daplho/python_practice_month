#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    frontTries = int(p/2)
    backTries = int(n/2) - int(p/2)

    if frontTries < backTries:
        return frontTries
    else:
        return backTries

if __name__ == '__main__':
    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(str(result) + '\n')
