import math

t = int(input())
v = []
for i in range(t):
	v.append([int(i) for i in ' '.join([input()]).split()])


for i in v: 
	num_pieces = math.ceil(i[0]/i[1])
	num_cuts = num_pieces - 1
	total_cuts = math.comb(i[0]-1, i[1]-1) - i[1]*math.comb(i[0]-num_pieces-1, i[1]-1)
	print("{} {}".format(num_pieces%i[2], total_cuts%i[2]))