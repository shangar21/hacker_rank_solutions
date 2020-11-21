import math
import os
import random
import re
import sys

def climbingLeaderboard(ranked, player):
    pscores = []
    
    for i in player:
        ranked = list(dict.fromkeys(sorted(ranked + [i], reverse=True)))
        pscores.append(ranked.index(i) + 1)

    return pscores




print(climbingLeaderboard([100,100,50,40,40,20,10], [5,25,50,120]))