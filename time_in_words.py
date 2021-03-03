def wordify_num(x):
	number_words = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'half past'}

	if x > 20:
		return number_words[20] + ' ' + number_words[x%10]
	elif x < 20:
		return number_words[x]

	return 'twenty'

def timeInWords(h, m):
    alias = {0:15, 1:2, 2:2, 3:2, 4:2, 5:2, 6:2, 7:2, 8:2, 9:2, 10:2, 11:2, 12:2, 13:2, 14:2}
    accociated_terms = {0: 'o\' clock', 1: ' minute ', 2: ' minutes ', 15:'quarter ', 30:'half past'}

    if m > 30:
    	return wordify_num(60-m) + accociated_terms[alias[m%15]] + 'to ' + wordify_num(h+1)
    elif m > 1 and m < 30:
    	return wordify_num(m) + accociated_terms[alias[m%15]] + 'past ' + wordify_num(h)
    elif  m == 1:
    	return 'one minute past ' + wordify_num(h)

    return 'half past ' + wordify_num(h) if m == 30 else wordify_num(h) + ' o\' clock'



print(timeInWords(10,57))


