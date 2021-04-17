#!/bin/python3

import math
import os
import random
import re
import sys

def fw(grid):
    for k in range(len(grid)):
        for i in range(len(grid)):
            for j in range(len(grid)):
                if i != j:
                    grid[i][j] = min(grid[i][j], grid[i][k]+grid[k][j])


if __name__ == '__main__':
    road_nodes, road_edges = map(int, input().split())

    grid = [[float('inf')]*road_nodes for i in range(road_nodes)]

    for i in range(road_edges):
        a,b,k = map(int, input().split())
        grid[a-1][b-1] = k
    
    fw(grid)
    q = int(input())

    for q_itr in range(q):
        xy = input().split()

        x = int(xy[0])

        y = int(xy[1])
        
        if x == y:
            print(0)
        elif grid[x-1][y-1] == float('inf'):
            print(-1)
        else:
            print(grid[x-1][y-1])
    

