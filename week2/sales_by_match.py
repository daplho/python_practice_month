import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    socks_dict = {}
    pairs = 0

    for sock in ar:
        if sock in socks_dict:
            socks_dict.pop(sock)
            pairs += 1
        else:
            socks_dict[sock] = []

    return pairs


if __name__ == '__main__':
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(str(result) + '\n')
