import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    rows = len(grid)
    cols = len(grid[0])

    matrix = [[0 for i in range(cols)] for j in range(rows)]

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            c = grid[row][col]
            if c == '.':
                matrix[row][col] = 0
            if c == 'O':
                matrix[row][col] = 3

    time = 1
    while(time <= n):

        # Bombs explode!
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    continue
                matrix[i][j] -= 1
                if matrix[i][j] == 0:
                    if i-1 >= 0:
                        matrix[i-1][j] = 0
                    if i+1 < rows and matrix[i+1][j] > 1: # don't explode mines that are about to explode
                        matrix[i+1][j] = 0
                    if j-1 >= 0:
                        matrix[i][j-1] = 0
                    if j+1 < cols and matrix[i][j+1] > 1: # don't explode mines that are about to explode
                        matrix[i][j+1] = 0
        
        if time % 2 == 0:
        # Bomberman awakes!
            for i in range(rows):
                for j in range(cols):
                    if matrix[i][j] == 0:
                        matrix[i][j] = 3

        time += 1

    return_grid = []
    for i in range(rows):
        cur_row = ""
        for j in range(cols):
            if matrix[i][j] == 0:
                cur_row += '.'
            else:
                cur_row += 'O'
        return_grid.append(cur_row)

    return return_grid

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    print('\n'.join(result))
    print('\n')
