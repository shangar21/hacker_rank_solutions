def gamingArray(arr):
    k = sorted(zip(arr, range(len(arr))), reverse=True) 
    k = [i[1] for i in k]    
      
    min_idx = 1000000000000000000000000000000000
    count = 0 

    for i in k: 
        if i < min_idx:
            count += 1
            min_idx = i 

    return "ANDY" if count %2 == 0 else "BOB"


