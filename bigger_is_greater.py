import  math

# Using algorithm to generate all permutations from this link: https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order

def biggerIsGreater(w):

	k = len(w) - 1

	while k > 0 and w[k] <= w[k - 1]:
		k -= 1

	if k <= 0:
		return 'no answer'

	i = len(w) - 1

	while i > 0 and w[k - 1] <= w[i]:
		i -= 1

	c = list(w)
	
	c[k-1], c[i] = c[i], c[k-1]
	
	c[k:] = c[len(c) - 1 : k-1 : -1]

	return ''.join(c)


