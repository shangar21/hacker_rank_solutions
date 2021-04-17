import collections

def pairs(k,arr):
	count = 0
	arr_vals = collections.Counter(arr)

	for i in range(len(arr)):
		if arr[i] + k in arr_vals:
			count += 1

	return count 