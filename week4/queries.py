import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#

def solve(arr, queries):
    results = []

    for d in queries:
        local_max_arr = []
        for i in range(len(arr)-d+1):
            if i == 0:
                cur_arr = arr[i:i+d]
                cur_max = max(cur_arr)
            else:
                to_remove = arr[i-1]
                to_add = arr[i+d-1]
                if to_remove == cur_max:
                    cur_arr = arr[i:i+d]
                    cur_max = max(cur_arr)
                else:
                    if cur_max < to_add:
                        cur_max = to_add
            local_max_arr.append(cur_max)
        results.append(min(local_max_arr))

    return results

if __name__ == '__main__':
    fptr = open(sys.stdout.fileno(), 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = solve(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()