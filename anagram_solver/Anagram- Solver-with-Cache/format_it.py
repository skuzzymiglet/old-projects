import pickle

wordlist = open("words.txt", "r")
words = wordlist.read().split()
words = sorted(words, key=len)
print(words)

myfile = open("words_formatted.dat", "wb")

pickle.dump(words, myfile)

myfile.close()
