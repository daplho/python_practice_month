#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    arrays = [[] for i in range(n)]
    lastAnswer = 0
    result = []

    for query in queries:
        qType = query[0]
        x = query[1]
        y = query[2]
        if qType == 1:
            idx = (x ^ lastAnswer) % n
            arrays[idx].append(y)
        if qType == 2:
            idx = (x ^ lastAnswer) % n
            lastAnswer = arrays[idx][y % len(arrays[idx])]
            result.append(lastAnswer)

    return result

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print('\n'.join(map(str, result)))