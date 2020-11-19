def formingMagicSquare(s):
    list_magic = [[8,1,6,3,5,7,4,9,2], [6,1,8,7,5,3,2,9,4], [4,9,2,3,5,7,8,1,6], [2,9,4,7,5,3,6,1,8], [8,3,4,1,5,9,6,7,2], [4,3,8,9,5,1,2,7,6], [6,7,2,1,5,9,8,3,4], [2,7,6,9,5,1,4,3,8]]  
    
    flat_s = []
    for i in s:
        for j in i:
            flat_s.append(j)

    sums = []
    
    for i in range(len(list_magic)):
        differences = []
        for j in range(len(list_magic[i])):
            differences.append(abs(list_magic[i][j] - flat_s[j]))
        sums.append(sum(differences))
    
    return min(sums)
    