import pickle, math

words = open("words_formatted.dat", "rb")
wordlist = pickle.load(words)

print(wordlist[-1])

letter_total = 0
omits = 0

for i in range(len(wordlist)):
	if len(wordlist[i]) >= 3 and len(wordlist[i]) <= 9:
		letter_total += len(wordlist[i]) + math.factorial(len(wordlist[i]))
	else:
		omits += 1
	print(wordlist[i])
	if i >= 400000:
		break
		
print(letter_total)
print(omits)
