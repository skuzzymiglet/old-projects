import json

term = "ba"

glossary = open("glossary_dump.json", "r")
glossary_dict = json.loads(glossary.read())
glossary.close()
occ = {}

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
            for word in words:
                if "~" in word:
                    print(word)
                    exploded = word.split("~")
                    print(exploded)
                    outer = []
                    for part in exploded:
                        if not part == term:
                            print(part)
                            outer.append(part)
                    print(outer)
                    outer_len = 0
                    for x in outer:
                        print(len(x))

                    print(outer_len)
                occ[i] += 20 - outer_len
                print("hoopie", occ[i])
            # Search def string for word
            # Return word
            # Split by ~
            # Count the total length of the elements that aren't the search term
            # Subtract from 20

    if occ[i] == 0:
        del(occ[i])


print(occ)

# Return: occs, but only title and sentences containing the search term
    
    
