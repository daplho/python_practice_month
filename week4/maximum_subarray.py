import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    max_elem = max(arr)
    if max_elem < 0:
        return [max_elem,max_elem]
    subarray_max = 0
    cur_sum = 0
    for i in arr:
        if cur_sum + i > 0:
            cur_sum += i
            if subarray_max < cur_sum:
                subarray_max = cur_sum
        else:
            cur_sum = 0
    
    subsequence_max = 0
    for i in arr:
        if i > 0:
            subsequence_max += i
    
    return [subarray_max,subsequence_max]

if __name__ == '__main__':
    fptr = open(sys.stdout.fileno(), 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()