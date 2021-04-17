def superReducedString(s):
	ls_s = [i for i in s]

	i = 0

	while i < len(ls_s):
		if i+1 < len(ls_s) and ls_s[i] == ls_s[i+1]::
			ls_s.pop(i)
			ls_s.pop(i)
			if i > 0:
				i -= 1
		else:
			i += 1

	if len(ls_s) < 1:
		return "Empty String"

	return ''.join(ls_s)


print(superReducedString('aa'))