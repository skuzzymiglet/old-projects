import time
from itertools import permutations

print("Anagram Solver Minimal - lighter algorithm than https://repl.it/@skuzzymiglet/Anagram-Solver-V2")

def list_confine(l, anagram):
    # Effectively solves the anagram, no repeated reads needed!
    return_list = []
    for element in l:
        if len(element) == len(anagram):
            if [str(sorted(element)).capitalize(), str(sorted(element)).upper(), str(sorted(element)).lower()] == [str(sorted(anagram)).capitalize(), str(sorted(anagram)).upper(), str(sorted(anagram)).lower()]:
                return_list.append(element)
    return return_list

words = open("words.txt", "r")
anagram = input("Anagram: ")
t1 = time.time() # Start timing

word_list = list_confine(words.read().split(), anagram)
words.close() # Save RAM

def create_possibilities(word):
    return list(permutations(list(word), len(word)))
    
def humanize_time(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    return '%02d:%02d:%02d' % (hours, mins, secs)

def remove_duplicates(l):
    return set(l)

for y in word_list:
    print(y)

t2 = time.time()
print(humanize_time(t2-t1), "seconds")

