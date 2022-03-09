import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sLower = s.lower()
    for l in alphabet:
        if l not in sLower:
            return "not pangram"

    return "pangram"

if __name__ == '__main__':
    s = input()

    result = pangrams(s)

    print(result + '\n')
