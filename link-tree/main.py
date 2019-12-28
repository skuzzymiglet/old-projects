from lxml import html
import requests

url = "https://devrant.com/feed"
base = "https://devrant.com"
page = requests.get(url).text
doc = html.document_fromstring(page)

def absolute(link):
    return base+link 

def links(url):
    urls = [a.get("href") for a in doc.cssselect("a")]
    new_urls = []
    for i in urls:
        #print(i)
        if i == None or i == "#":
            pass
        elif i[0] == "/":
            new_urls.append(absolute(i))
        else:
            new_urls.append(i)
    return new_urls

tree = {}

def tree(url, depth=2):
    tmp = {}
    if depth == 0 :
        pass
    for i in links(url):
        t

print(tree)
