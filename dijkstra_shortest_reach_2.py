#!/bin/python3

import math
import os
import random
import re
import sys

  

def edge_to_matrix(n, edges):
    graph = [[-1 for i in range(n)] for j in range(len(edges))]
    for j in edges:
        graph[j[0]-1][j[1]-1] = j[2]
    return graph       

def min_distance(n, distances, visited):
    u = float('inf')
    u_idx = -1
    for i in range(n):
        if not visited[n] and u > distances[i]:
            u = distances[i]
            u_idx = i 
    return u_idx 
# Complete the shortestReach function below.
def shortestReach(n, edges, s):
    distances = [float('inf')]*n
    visited = [False]*(n+1)
    distances[s] = -1
    visited[s] = True
    matrix = edge_to_matrix(n, edges)
    
    for i in range(n):
        u = min_distance(n, distances, visited)
        visited[u] = True 
        for j in range(n): 
            if  matrix[u][j] != -1 and not visited[j]:
                distances[j] = min(distances[j], distances[i] + matrix[i][j]) 
    
    return distances 
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()