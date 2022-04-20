import heapq
import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    iterations = 0
    if len(A) == 0:
        return -1
    
    heapq.heapify(A)

    while True:
        if len(A) == 1 and A[0] < k:
            return -1
        elif A[0] < k:
            iterations += 1
            smallest = heapq.heappop(A)
            second_smallest = heapq.heappop(A)
            mixed = smallest + 2 * second_smallest
            heapq.heappush(A, mixed)
        else:
            return iterations


if __name__ == '__main__':
    fptr = open(sys.stdout.fileno(), 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()