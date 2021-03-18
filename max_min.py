def maxMin(k,arr):
    arr.sort()
    return min( arr[i+k-1]-arr[i] for i in range(0,len(arr)-k+1))

maxMin(4, [1,2,3,4,10,20,30,40,100,200])