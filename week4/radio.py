import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

def hackerlandRadioTransmitters(x, k):
    transmitters = 0
    done = False
    anchor = 0
    x.sort()
    left_border = x[anchor]
    while True:
        # if window can slide:
        if (anchor+1 < len(x)) and (x[anchor+1] - left_border) <= k:
            anchor += 1
        else:
            if anchor + k >= len(x):
                return transmitters
            # create_new_window
            transmitters += 1
            anchor += k
            left_border = x[anchor]

    return transmitters

if __name__ == '__main__':
    fptr = open(sys.stdout.fileno(), 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()