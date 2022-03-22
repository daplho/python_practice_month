from curses import meta
import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    frequencies = {}
    for c in s:
        if c not in frequencies:
            frequencies[c] = 1
        else:
            frequencies[c] += 1

    meta_frequencies = {}
    for f in frequencies.values():
        if f not in meta_frequencies:
            meta_frequencies[f] = 1
        else:
            meta_frequencies[f] += 1

    if len(meta_frequencies) == 1:
        return "YES"
    
    if len(meta_frequencies) == 2:
        (k1, v1) = meta_frequencies.popitem()
        (k2, v2) = meta_frequencies.popitem()
        if v1 == 1 or v2 == 1 and abs(k1 - k2) == 1:
            return "YES"

    return "NO"

if __name__ == '__main__':
    s = input()

    result = isValid(s)

    print(result + '\n')