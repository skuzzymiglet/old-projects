import random
import requests
from lxml import html
import webbrowser

url = "https://wiki.archlinux.org/index.php/Table_of_contents"
page = requests.get(url)
doc = html.document_fromstring(page.text)
links = ["https://wiki.archlinux.org"+x.get("href") for x in doc.cssselect("#mw-content-text a")]

webbrowser.open(random.choice(links))



