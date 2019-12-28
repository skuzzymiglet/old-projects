import pickle

words = open("words_formatted.dat", "rb")
wordlist = pickle.load(words)

print(wordlist[239637])
