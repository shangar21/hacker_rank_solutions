def rmam(grid, i,j):
    directions = [[1,0], [0,1], [1,1], [-1, 0], [0, -1], [-1,-1], [-1, 1], [1, -1]]
    grid[i][j] = 'X'
    for d in directions:
        if 0<= i+d[0] <len(grid) and 0<= j+d[1] < len(grid[0]) and grid[i+d[0]][j+d[1]] == '#':
            rmam(grid, i+d[0], j+d[1])

def find_loops(grid):
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == '#':
                rmam(grid, x, y)
                count += 1
    return count

n, m = map(int, input().split())
grid = [[*input()] for _ in range(n)]


print(find_loops(grid))