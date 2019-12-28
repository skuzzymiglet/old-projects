import json

term = "ba"

glossary = open("glossary_dump.json", "r")
glossary_dict = json.loads(glossary.read())
glossary.close()
occ = {}

def calculate_score(word, term):
        word = word.lower().replace(term, "~" + term + "~").split("\n")
	

for i in glossary_dict:
    occ[i] = 0
    term_search = i.lower().replace(term, "~" + term + "~").split("\n")
    for s in term_search:
        if "~" in s:
            occ[i] += 25
            
    def_search = glossary_dict[i].lower().replace(term, "~" + term + "~").split("\n")
    for s in def_search:
        if "~" in s:
            words = s.split()
            occ[i] += 25
            # Search def string for word
            # Return word
            # Split by ~
            # Count the total length of the elements that aren't the search term
            # Subtract from 20

    if occ[i] == 0:
        del(occ[i])


#print(occ)

# Return: occs, but only title and sentences containing the search term
    
    
