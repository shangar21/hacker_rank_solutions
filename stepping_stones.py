import math


def solve(n):
    t = lambda x : 0.5 * (-1 + math.sqrt((8*x) + 1))
    if int(t(n)) == t(n):
        return "Go On Bob " + str(int(t(n)))
    return "Better Luck Next Time"

print(solve(3))