def factorial(n):
    p = 1
    for i in range(1,n+1):
        p = p*i
    return p

def solve(n, m):
    if n ==0 or m == 1:
        return 1
    if m == 0:
        return 0
    total_perm = factorial(n + (m - 1))
    oc_n = factorial(n)
    oc_m = factorial(m-1)
    return int(((total_perm//(oc_n*oc_m)))%(pow(10,9) + 7))





#     if n ==0 or m == 1:
#         return 1
#     if m == 0:
#         return 0
#     total_perm = factorial(n + (m - 1))
#     oc_n = factorial(n)
#     oc_m = factorial(m-1)
#     return (int(total_perm/(oc_m*oc_m)))%(10**9 + 7)

