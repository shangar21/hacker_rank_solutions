#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):

	container_space = []
	ball_count = [0]*len(container[0])

	for i in container:
		container_space.append(sum(i))
		for j in range(len(i)):
			ball_count[j] += i[j]

	if sorted(container_space) == sorted(ball_count):
		return 'Possible'
		
	return 'Impossible'


organizingContainers([[0,2,1], [1,1,1], [2,0,0]])


# if __name__ == '__main__':
#     #fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input())

#     for q_itr in range(q):
#         n = int(input())

#         container = []

#         for _ in range(n):
#             container.append(list(map(int, input().rstrip().split())))

#         print(container)

#         #result = organizingContainers(container)

#         #fptr.write(result + '\n')

#     fptr.close()