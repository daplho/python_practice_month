import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    sortedGrid = []
    for row in grid:
        sortedGrid.append(sorted(row.replace(' ', '')))

    colNum = len(sortedGrid[0])
    for colIndex in range(colNum):
        c = 'a'
        for row in sortedGrid:
            if ord(c) > ord(row[colIndex]):
                return "NO"
            c = row[colIndex]

    return "YES"

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        print(result + '\n')
