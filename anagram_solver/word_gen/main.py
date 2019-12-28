import random
import time

t1 = time.time()
words = open("words.txt", "r")
word_list = words.read().split()
chosen = ""
length = int(input("Length?: "))

while not len(chosen) == length:
        chosen = (word_list[random.randint(0, len(word_list))])

t2 = time.time()

print("Your lucky word is:", chosen ,"\n", str(t2-t1), "seconds")

words.close()
