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
    for i in range(len(player)):
        for j in range(len(ranked_dedup)):
            if player[i] < ranked_dedup[len(ranked_dedup)-(j+1)]:
                ranks.append(len(ranked_dedup)-j+1)
                break
            if player[i] == ranked_dedup[len(ranked_dedup)-(j+1)]:
                ranks.append(len(ranked_dedup)-j)
                break
            if player[i] > ranked_dedup[0]:
                ranks.append(1)
                break
    return ranks

if __name__ == '__main__':
    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print('\n'.join(map(str, result)))
    print('\n')