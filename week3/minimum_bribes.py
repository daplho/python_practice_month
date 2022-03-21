import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def bribe(position, desired, new_q):
    if position + 1 < len(new_q) and desired == new_q[position + 1]:
        new_q[position], new_q[position+1] = new_q[position+1], new_q[position]
        return 1
    if position + 2 < len(new_q) and desired == new_q[position + 2]:
        new_q[position+1], new_q[position+2] = new_q[position+2], new_q[position+1]
        new_q[position], new_q[position+1] = new_q[position+1], new_q[position]
        return 2

    return 3


def minimumBribes(q):
    # Write your code here
    new_q = list(range(1, len(q)+1))
    
    total_bribes = 0
    for i in range(len(q)):
        if q[i] != new_q[i]:
            n = bribe(i, q[i], new_q)
            if n <= 2:
                total_bribes += n
            else:
                print("Too chaotic")
                return
    
    print(total_bribes)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)