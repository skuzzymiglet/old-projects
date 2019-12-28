import pickle, math, csv

words = open("words_formatted.dat", "rb")
wordlist = pickle.load(words)
writer = csv.writer(open("graph.csv", "wb"))

letter_total = 0

writer.writerows([(str("Words"), str("GB"))])

for i in range(len(wordlist)):
	letter_total += len(wordlist[i]) + math.factorial(len(wordlist[i]))
	print(letter_total)
	print([(str(i), str(letter_total))])
	writer.writerows([(str(i), str(float(letter_total)/1000000000))])
		
print(letter_total)
