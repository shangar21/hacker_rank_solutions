import re

x = [[1,2,3,4,5,6,7,8,9,0],[0,9,8,7,6,5,4,3,2,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2,2,2]]

flat_x = [item for sublist in x for item in sublist]

pattern = [[8,7,6,5,4], [1,1,1,1,1], [1,1,1,1,1]]

# def gridSearch(G, P):

# 	for row in range(len(G) - len(P)):

# 		if ''.join(str(i) for i in P[0]) in ''.join(str(j) for j in G[row]):
			
# 			pattern = True
# 			pattern_index = 1

# 			while pattern_index < len(P):
# 				if ''.join(str(i) for i in P[pattern_index]) not in ''.join(str(j) for j in G[row + pattern_index]) or ''.join(str(j) for j in G[row + pattern_index]).find(''.join(str(i) for i in P[pattern_index])) != ''.join(str(j) for j in G[row]).find(''.join(str(i) for i in P[0])):
# 					pattern = False
# 					pattern_index = len(P) + 1
# 				pattern_index += 1

# 			if pattern:
# 				return 'YES'

# 	return 'NO'

def gridSearch(G,P):

	for rowg in range(len(G) - len(P) + 1):

		for bounds in re.finditer(''.join(str(i) for i in P[0]), ''.join(str(j) for j in G[rowg])):

			grid_index = rowg
			pattern = True

			while grid_index - rowg < len(P):

				if ''.join(str(i) for i in G[grid_index][bounds.start():bounds.end()]) != ''.join(str(i) for i in P[grid_index - rowg]):
					pattern = False

				grid_index += 1

			if pattern:
				return 'YES'

	return 'NO'

print(gridSearch(x, pattern))