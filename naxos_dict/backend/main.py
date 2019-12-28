from lxml import html
from cssselect import GenericTranslator, SelectorError
import requests

dump_file = open("glossary_dump.txt", "w")

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
            definition = (definition_doc.cssselect('.style6')[0].text_content() + ":\n\n" + definition_doc.cssselect('.style5')[0].text_content() + "\n\n\n")
            dump_file.write(definition)

print("Done")
dump_file.close()            

