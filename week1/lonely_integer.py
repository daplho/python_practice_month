import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    counts = {}
    
    for n in a:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1

    for n, count in counts.items():
        if count == 1:
            return n

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    print(str(result) + '\n')
