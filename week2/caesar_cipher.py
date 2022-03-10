#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    result = ''
    
    for char in s:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            result += chr(ord('a') + (ord(char) - ord('a') + k) % 26)
        elif ord(char) >= ord('A') and ord(char) <= ord('Z'):
            result += chr(ord('A') + (ord(char) - ord('A') + k) % 26)
        else:
            result += char

    return result

if __name__ == '__main__':
    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(result)
