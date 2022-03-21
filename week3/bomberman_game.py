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

def explode(grid):
    rows = len(grid)
    cols = len(grid[0])

    exploding_positions = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'O':
                exploding_positions.append([row, col])

    grid = ['O' * cols] * rows

    for position in exploding_positions:
        row = position[0]
        col = position[1]
        grid[row] = grid[row][:col] + '.' + grid[row][col+1:]
        if row - 1 >= 0:
            grid[row-1] = grid[row-1][:col] + '.' + grid[row-1][col+1:]
        if row + 1 < rows:
            grid[row+1] = grid[row+1][:col] + '.' + grid[row+1][col+1:]
        if col - 1 >= 0:
            grid[row] = grid[row][:col-1] + '.' + grid[row][col:]
        if col + 1 < cols:
            grid[row] = grid[row][:col+1] + '.' + grid[row][col+2:]
    
    return grid

def bomberMan(n, grid):
    if n < 2:
        return grid
    elif n % 2 == 0:
        return ['O' * len(grid[0])] * len(grid)
    elif (n-1) % 4 != 0:
        return explode(grid)
    else:
        return explode(explode(grid))

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
