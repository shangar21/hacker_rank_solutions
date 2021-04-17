def kangaroo(x1, v1, x2, v2):
        
    if v2 == v1 and x1 != x2:
        return "NO"
    elif divmod((x1-x2), (v2-v1))[0] > 0 and divmod((x1-x2), (v2-v1))[1] == 0:
        return "YES"
    
    return "NO"