from lxml import html
from cssselect import GenericTranslator, SelectorError
import requests, json

dump_file = open("glossary_dump.json", "w")
as_dict = {}

def make_absolute(link): # Turn an absolute link relative
    return "https://www.naxos.com" + link

print("Extracting text data from glossary to glossary_dump.txt")

page = requests.get("https://www.naxos.com/education/glossary.asp?char=A-C#").text
pages = []

pages.append("https://www.naxos.com/education/glossary.asp?char=A-C#") # Also scan this page!

doc = html.document_fromstring(page)
for a in doc.cssselect("td > b > a"):
    pages.append(make_absolute(a.get("href")))

for page in pages:
    text = requests.get(page).text
    doc = html.document_fromstring(text)
    for a in doc.cssselect('br ~ a'):
        if not a.get("onclick") == None:
            link = a.get("onclick").split("'")[1]
            link = make_absolute(link)
            definition_text = requests.get(link).text
            definition_doc = html.document_fromstring(definition_text)
            term = (definition_doc.cssselect('.style6')[0].text_content())
            definition = (definition_doc.cssselect('.style5')[0].text_content())
            as_dict[term] = definition

dump_file.write(json.dumps(as_dict))
print("Done")
dump_file.close()            

