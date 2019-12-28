from lxml import html
from lxml.etree import *
import operator
from bokeh.io import show, output_file
from bokeh.plotting import figure

page = open("mtt.html", "r")
doc = html.document_fromstring(page.read())
page.close()

trs = doc.xpath("//tbody/tr")
data = doc.xpath("//tbody/tr/td")
titles = doc.xpath("//tbody/tr/td/h4")

tree = doc.getroottree()

time = {}
for tr in tree.iterfind("//tbody"):
    title = ElementTree(tr).getroot().findall("tr/td/h4")[0].text
    total = ElementTree(tr).getroot().findall('tr[@class="totalrow"]/td')[2].text
    print(title, total)
    time[title] = total 

for k in time:
    time[k] = float(time[k].replace(":", "."))
time = sorted(time.items(), key=operator.itemgetter(1))

output_file("mtt-graph.html")
p = figure(title="Time on web")

p.vbar(x=[n[0] for n in time], top=[e[1] for e in time], width=1,line_color="white", fill_color="blue")

show(p)
