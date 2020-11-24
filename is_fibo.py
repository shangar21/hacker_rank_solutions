def solve(n):
    v1 = 5*n**2 + 4
    v2 = 5*n**2 - 4
    if ((int)(v1**0.5))*((int)(v1**0.5)) == v1 or ((int)(v2**0.5))*((int)(v2**0.5)) == v2:
        return "IsFibo"
    return "IsNotFibo"
