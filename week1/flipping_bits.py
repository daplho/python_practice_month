import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    numAsStr =  "{:032b}".format(n)
    flippedBitsStr = ''
    for bit in numAsStr:
        if bit == '0':
            flippedBitsStr += '1'
        else:
            flippedBitsStr += '0'

    return int(flippedBitsStr, 2)

if __name__ == '__main__':
    q = int(input().strip())

    resultString = ''
    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)
        resultString += '{0}\n'.format(result)
        
print(str(resultString) + '\n')
