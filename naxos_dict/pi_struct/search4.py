import json, re, itertools, time
from statistics import mean

search_term = "der"

glossary = open("glossary_dump.json", "r")
glossary_dict = json.loads(glossary.read())
glossary.close()

def replace_ignore_case(x, y, z): # x: string, y: what to replace, z: with what
    pattern = re.compile(re.escape(y), re.IGNORECASE)
    return pattern.sub(z, x)

def pad_n(word, search_term): # Calculates how many letters are outside search term's occurence within the word/string
    pad = 0
    word = replace_ignore_case(word, search_term, "~%s~" % search_term) #word.replace(search_term, "~%s~" % search_term)
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

def create_scores(search_term):
    scores = {}
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
    return scores

def sort_scores(scores):
    return sorted(scores.items(), key=lambda kv: kv[1])

def get_val(x, tup):
    for i in tup:
        if i[0] == x:
            return i[1]

def format_text(x, search_term):
    search_term_possibilities = list(map(''.join, itertools.product(*zip(search_term.upper(), search_term.lower()))))
    for i in search_term_possibilities:
        x = x.replace(i, "<b>%s</b>" % i)
    return x
   
start = time.time()

scores = create_scores(search_term)
scores = sort_scores(scores)
        
response = {}

response["verif"] = search_term
response["terms"] = []
terms = []

for score in range(len(scores)):
    if scores[score][1] <= 1: 
        continue
    fterm = format_text(scores[score][0], search_term)
    fdef = format_text(glossary_dict[scores[score][0]], search_term)
    rank = len(scores) - score
    terms.append({"fterm": fterm, "fdef": fdef, "rank": rank})

response["terms"] = terms

end = time.time()

response["time"] = end - start

print(response)
