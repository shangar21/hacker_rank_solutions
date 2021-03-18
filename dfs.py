import math

directions = [[1,0], [0,1], [1,1], [-1,0], [0,-1], [-1,-1], [1,-1], [-1,1]]

def count_neighbours(i,j,grid):
	count = 0
	if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
		grid[i][j] = 0
		count += 1
		for dr,dc in directions:
			count += count_neighbours(i+dr, j+dc, grid)
	return count


def maxRegion(grid):
	count = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 1:
				count = max(count, count_neighbours(i,j,grid))
	return count