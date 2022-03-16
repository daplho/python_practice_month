import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGameHelper(n):
    x = 0
    while (pow(2, x) <= n):
        x += 1

    largestRemainder = n - pow(2, x - 1)
    if largestRemainder == 0:
        return x - 1
    else:
        return 1 + counterGameHelper(largestRemainder)

def counterGame(n):
    steps = counterGameHelper(n)
    return "Richard" if steps % 2 == 0 else "Louise"
    

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        print(result + '\n')
