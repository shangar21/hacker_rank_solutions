def maximum_subarray(arr):
	
	if min(arr) < 0:
		arr = [i + -1*min(arr) for i in arr]

	cs = 0
	start=end=0

	for i in range(len(arr)):
		if cs >= cs + arr[i]:
			cs = 0
			start = i
			end = i
		else:
			cs = cs + arr[i]
			end += 1

	print(start, end)


maximum_subarray([-1,2,3,-4,5,10])