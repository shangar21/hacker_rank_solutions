import numpy as np

def queensAttack(n, k, r_q, c_q, obstacles):
    attacks = 0

    directions = [[1,0],[0,1],[1,1],[-1,-1], [-1,0],[0,-1],[-1,1],[1,-1]]

    for i in directions:
        row = r_q
        col = c_q
        while True:
            row += i[0]
            col += i[1]
            if ([row,col] in obstacles) or (0 >= row) or (row > n ) or (0 >= col) or (col > n):
                break

            attacks += 1




    return attacks


print(queensAttack(4, 3, 4, 3, [[5,5],[4,2],[2,3]]))
