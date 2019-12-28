import itertools
from itertools import permutations

words = open("words.txt", "r")
word_list = words.read().split()


def create_possibilities(word):
    return list(permutations(list(word), len(word)))


def solve_anagram(anagram):
    answers = []
    for y in create_possibilities(anagram):
        combin = map(''.join,
                     itertools.product(*((c.upper(), c.lower()) for c in y)))
        for c in combin:
            if c in word_list:
                answers.append(c)
    return answers