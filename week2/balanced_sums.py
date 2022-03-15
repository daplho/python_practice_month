import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    sumLeft = 0
    sumRight = sum(arr)
    for i in range(len(arr)):
        if i > 0:
            sumLeft += arr[i-1]
        if i < len(arr):
            sumRight -= arr[i]

        if sumLeft == sumRight:
            return "YES"
    return "NO"

if __name__ == '__main__':
    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        print(result + '\n')
