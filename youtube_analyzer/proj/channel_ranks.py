from lxml import html
from cssselect import GenericTranslator, SelectorError

page = open("watch-history.html", "r")
ranks = open("ranks", "w")
doc = html.document_fromstring(page.read())
#1, 3
sel = doc.cssselect('div>a')
channels = []
chdict = {}

def sort_dict(d):
    return sorted(d.items(), key=lambda kv: kv[1], reverse=True)

for i in range(len(sel)):
    if "channel" in sel[i].get("href"):
        channels.append(sel[i].text)

for channel in channels:
    if not channel in chdict.keys():
        chdict[channel] = 0
    chdict[channel] += 1
    
chdict_sorted = sort_dict(chdict)

for ch in range(len(chdict_sorted)):
    print(str(ch+1) + "\t" + chdict_sorted[ch][0] + ": " + str(chdict_sorted[ch][1]), file=ranks)


