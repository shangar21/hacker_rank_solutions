import math
import os
import random
import re
import sys


#My Solutions:

def climbingLeaderboard(ranked, player):
    pscores = []
    
    for i in player:
        ranked = list(dict.fromkeys(sorted(ranked + [i], reverse=True)))
        pscores.append(ranked.index(i) + 1)

    return pscores





def climbingLeaderboard(ranked, player):
    pscores = []

    ranked = list(dict.fromkeys(sorted(ranked, reverse=True)))

    for i in range(len(player)):
    	if (player[i] < ranked[len(ranked) - 1]):
    		pscores.append(len(ranked) + 1)
    		ranked.append(player[i])
    	else:
    		j = 0
    		while j < (len(ranked)):
    			if (player[i] == ranked[j]):
    				pscores.append(j+1)
    				j = len(ranked) + 1
    			elif (player[i] > ranked[j]):
    				ranked.insert(j, player[i])
    				pscores.append(j+1)
    				j = len(ranked) + 1
    			j += 1
    return pscores

#Correct Solution (found at https://livecodestream.dev/challenge/climbing-the-leaderboard/)

def climbingLeaderboard(ranked, player):
    # get the unique ranks sorted descending
    scores = sorted(list(set(ranked)), reverse=True)
    player_ranks = []
    for score in player:
        while scores and score >= scores[-1]:
            scores.pop()
        player_ranks.append(len(scores) + 1)

    return player_ranks



ranked = [100,90,90,80,75,60]
player = [50,65,77,90,102]
print(climbingLeaderboard(ranked, player))

