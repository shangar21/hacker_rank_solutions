# Complete the gridlandMetro function below.
def gridlandMetro(n,m,k,track):
    #n -> number of rows
    #m -> number of columns
    #k -> number of tracks
    #track -> 2D array [row start, column start, column end]
    ranges = {}
    for i in track:
        if i[0] not in ranges:
            ranges[i[0]] = [(i[1],i[2])]
        else:
            ranges[i[0]].append((i[1],i[2]))
            
    for i in ranges:
        ranges[i].sort()
      
    count = 0
    total = n*m
    
    for i in ranges:
        s = ranges[i][0][0]
        e = ranges[i][0][1]
        for j in ranges[i]:
            if j[0] > e:
                total -= e - s + 1 
                s = j[0]
                e = j[1]
            if j[1] > e:
                e = j[1]
        total -= e - s + 1
    
    return total