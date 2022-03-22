import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    ranked_dedup = sorted(list(set(ranked)), reverse=True)

    ranks = []
    i = 0
    j_min = 0
    while i < len(player): 
        j = j_min
        while j < len(ranked_dedup):
            if player[i] < ranked_dedup[len(ranked_dedup)-(j+1)]:
                ranks.append(len(ranked_dedup)-j+1)
                j += 1
                break
            elif player[i] == ranked_dedup[len(ranked_dedup)-(j+1)]:
                ranks.append(len(ranked_dedup)-j)
                j += 1
                break
            elif player[i] < ranked_dedup[0]:
                j_min += 1
            if player[i] >= ranked_dedup[0]:
                ranks.append(1)
                j += 1
                break
            j += 1
        i += 1
    return ranks

if __name__ == '__main__':
    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print('\n'.join(map(str, result)))
    print('\n')