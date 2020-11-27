import math

def encryption(s):
	ns = list(s)
	ns = list(filter(lambda a: a != " ", ns))
	col = ""
	print(ns)

	for i in range(math.ceil(math.sqrt(len(ns)))):
		j = i
		while j < len(ns):
			col += ns[j]
			j += math.ceil(math.sqrt(len(ns)))
		col += " "

	return col 

print(encryption("if man was meant to stay on the ground god would have given us roots"))