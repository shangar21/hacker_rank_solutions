import math

def find_min(l,r):
	global table
	k = int(math.log2(r-l+1))
	return min(table[l][k], table[r-(1<<k)+1][k])


def construct_table(arr):
	table = [[-1]*(1<<int(math.log2(len(arr)))) for i in range(len(arr))]
	
	for i in range(len(table)):
		table[i][0] = arr[i]

	for k in range(1, (1<<int(math.log2(len(arr))))):
		i = 0
		while i + (1<<k) - 1 < len(arr):
			table[i][k] = min(table[i][k-1], table[i+(1<<(k-1))][k-1])
			i+=1

	return table 
	


n = int(input())
arr = [int(i) for i in ' '.join([*input()]).split()]
q = int(input())

queries = []

for i in range(q):
    v.append([int(i) for i in ' '.join([input()]).split()])

table = construct_table(arr)


for i in queries:
	l,r = i[0],i[1]
	print(find_min(l,r))
