import math

# def next_permutation(list_num):

# 	k = len(list_num) - 1

# 	while k > 0 and list_num[k] <= list_num[k-1]:
# 		k -= 1

# 	if k <= 0:
# 		return list_num

# 	i = len(list_num) - 1

# 	while i > 0 and list_num[i] < list_num[k-1]:
# 		i -= 1

# 	list_num[k-1], list_num[i] = list_num[i], list_num[k-1]

# 	list_num[k:] = list_num[len(list_num) - 1 : k-1 : -1]

# 	return list_num

def absolutePermutation(n,k):
	if k == 0:
		return [i+1 for i in range(n)]
	
	if (n/k)%2 != 0:
		return [-1]

	list_num = []

	for i in range(0,n,k*2):
		tmp = [i+1 for i in range(i,i+k*2)]
		list_num += tmp[k:] + tmp[:k]

	return list_num


print(absolutePermutation(3,2))
	


