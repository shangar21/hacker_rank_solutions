import math
from collections import deque

class Graph():
    edges = {}
    n = 0

    def __init__(self, n):
        self.n = n
        for i in range(n):
            self.edges[i] = [] 


    def connect(self, x, y):
        self.edges[x].append(y)
        self.edges[y].append(x)

    def find_all_distances(self, s):
        visited = [False]*self.n
        queue = []
        queue.append((s,0))
        distances = [-1]*(self.n)
        distances[s] = 0
        visited[s] = True 

        while queue:
            s = queue.pop(0)
            if s[0] in self.edges:
                for i in self.edges[s[0]]:
                    if visited[i] == False:
                        queue.append((i, s[1]+1))
                        distances[i]=(6*(s[1]+1))
                        visited[i] = True
        distances.remove(0)
        return distances




t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    g = [str(x) for x in graph.find_all_distances(s-1)]
    print(" ".join(g))
