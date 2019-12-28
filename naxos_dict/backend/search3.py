import json
from statistics import mean

search_term = "alto"

glossary = open("glossary_dump.json", "r")
glossary_dict = json.loads(glossary.read())
glossary.close()
scores = {}

def pad_n(word, search_term): # Calculates how many letters are outside search term's occurence within the word/string
    pad = 0
    word = word.replace(search_term, "~%s~" % search_term)
    word_split = word.split("~")
    word_split = delete_values(word_split, search_term)
    for part in word_split:
        pad += len(part)
    return(pad)

def delete_values(x, value):
    new_list = []
    for element in range(len(x)):
        if not x[element] == value:
            new_list.append(x[element])
    return new_list

for term in glossary_dict:
    scores[term] = 0
    # No 1: Term search
    term_lwr = term.lower()
    if search_term in term_lwr:
        score = 100 
        scores[term] += score
    # No 2: Definition search
    definition = glossary_dict[term]
    definition_lwr = definition.lower().split()
    #print(definition_lwr)
    definition_pads = []
    for word in definition_lwr:
        if search_term in word:
            definition_pads.append(pad_n(word, search_term))
    scores[term] += len(definition_pads)

for score in scores:
    if scores[score] > 0:
        #print(score, scores[score])
        pass

print(sorted(scores.items(), key=lambda kv: kv[1]))
