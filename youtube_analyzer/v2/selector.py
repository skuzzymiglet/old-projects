from lxml import html
from cssselect import GenericTranslator, SelectorError

page = open("watch-history.html", "r")
doc = html.document_fromstring(page.read())
sel = doc.xpath("//div/a[contains(@href, 'watch')]")
csel = doc.xpath("//div/a")
selection = []

for i in sel:
    # if not "Watched" in str(i):
    print(str(i.text))
    selection.append(str(i.text))

print(selection)
print(len(selection), len(csel)/2)


