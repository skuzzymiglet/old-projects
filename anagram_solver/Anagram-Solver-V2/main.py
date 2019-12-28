import itertools, time
from itertools import permutations

print("Anagram Solver V2 - improved algorithm over https://repl.it/@skuzzymiglet/Anagram-Solver")

words = open("words.txt", "r")
word_list = words.read().split()
anagram = input("Anagram: ")

def create_possibilities(word):
	return list(permutations(list(word), len(word)))
	
def humanize_time(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    return '%02d:%02d:%02d' % (hours, mins, secs)

break_ = False

t1 = time.time()
for y in create_possibilities(anagram):
	combin = map(''.join, itertools.product(*((c.upper(), c.lower()) for c in y)))
	#print(combin)
	for c in combin:
		if c in word_list:
			print(c)
			print(humanize_time(time.time()-t1), " seconds")
t2 = time.time()
print(humanize_time(t2-t1), "seconds")


