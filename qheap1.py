import math
# node at index n:

# left_child: 2n + 1
# right_child: 2n + 2
# parent: floor( (n - 1) / 2 )

def delete_item(arr, item):
    if item == arr[-1]:
        arr.pop(-1)
        return arr 
    c_idx = arr.index(item)
    arr[c_idx], arr[-1] = arr[-1], arr[c_idx]
    arr.pop(-1)
    p = (c_idx - 1)//2 
    l =  2*c_idx + 1
    r = 2*c_idx + 2 
    if p >= 0 and arr[p] > arr[c_idx]:
        while c_idx >= 0:
            p = (c_idx - 1)//2
            if p >= 0 and arr[c_idx] < arr[p]:
                arr[p], arr[c_idx] = arr[c_idx], arr[p]
                c_idx = (c_idx - 1)//2
            else:
                break 
        return arr 
      
    
    while c_idx < len(arr):
        l =  2*c_idx + 1
        r = 2*c_idx + 2
        if l < len(arr) and r < len(arr) and (arr[l] < arr[c_idx] or arr[r] < arr[c_idx]):
            idx_min = arr.index(min(arr[l], arr[r]))
            arr[idx_min], arr[c_idx] = arr[c_idx], arr[idx_min]
            c_idx = idx_min
        else:
            break
    return arr  

def insert_item(arr, item):
    arr.append(item)    
    c_idx = len(arr) - 1
    while c_idx > 0:
        p = (c_idx - 1)//2
        if p >= 0 and arr[c_idx] < arr[p]:
            arr[p], arr[c_idx] = arr[c_idx], arr[p]
            c_idx = (c_idx - 1)//2
        else:
            break
    return arr 

q = int(input())
v = []
for i in range(q):
    v.append([int(i) for i in ' '.join([input()]).split()])

heap = []

for i in v:
    if i[0] == 1:
        heap = insert_item(heap, i[1])
    elif i[0] == 2:
        #print("calling delete", i[1], heap)
        heap = delete_item(heap, i[1])
        #print("after calling delete", heap)
    else:
        print(heap[0])