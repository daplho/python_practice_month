import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    done = False
    h1_height = sum(h1)
    h2_height = sum(h2)
    h3_height = sum(h3)

    if h1_height == h2_height and h1_height == h3_height:
        return h1_height
    
    done = False
    while not done:
        cur_max = max(h1_height, h2_height, h3_height)
        if len(h1) > 0 and h1_height == cur_max:
            cur_cylinder = h1.pop(0)
            h1_height -= cur_cylinder
            if h1_height == h2_height and h1_height == h3_height:
                return h1_height
        elif len(h2) > 0 and h2_height == cur_max:
            cur_cylinder = h2.pop(0)
            h2_height -= cur_cylinder
            if h1_height == h2_height and h1_height == h3_height:
                return h1_height
        elif len(h3) > 0 and h3_height == cur_max:
            cur_cylinder = h3.pop(0)
            h3_height -= cur_cylinder
            if h1_height == h2_height and h1_height == h3_height:
                return h1_height
    
    return 0

if __name__ == '__main__':
    fptr = open(sys.stdout.fileno(), 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()