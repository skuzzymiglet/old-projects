from lxml import html
from cssselect import GenericTranslator, SelectorError
import random, sys
import matplotlib.pyplot as plt

page = open("watch-history.html", "r")
doc = html.document_fromstring(page.read())
#1, 3
sel = doc.cssselect('div>a')
channels = []
chart_data = []
get_colors = lambda n: list(map(lambda i: "#" + "%06x" % random.randint(0, 0xFFFFFF), range(n)))
BY = 25

print(len(sel))
sys.exit()

def sort_dict(d):
    return sorted(d.items(), key=lambda kv: kv[1], reverse=True)

for i in range(len(sel)):
    if "channel" in sel[i].get("href"):
        channels.append(sel[i].text)


for i in range(len(channels) - BY):
    this_by = []
    for j in range(BY):
        this_by.append(channels[i+j])
    chart_data.append(tuple(this_by))


channels = list(reversed(channels))        
channels_set = list(set(channels))
chcolors = {}
colors = list(set(get_colors(4500)))

for i in range(len(channels_set)):
    chcolors[channels_set[i]] = colors[i]

print(chcolors)

chart_n = 0
for hundred in chart_data:
    channel_videos = {}
    for channel in hundred:
        if not channel in channel_videos.keys():
            channel_videos[channel] = 0
        channel_videos[channel] += 1
    labels = channel_videos.keys()
    sizes = channel_videos.values()
    chart_colors = []
    for channel in labels:
        chart_colors.append(chcolors[channel])
    plt.pie(sizes, labels=labels, colors=chart_colors, autopct='%d%%')
    plt.axis('equal')
    plt.savefig("charts/chart"+str(chart_n)+".png")
    print(str(chart_n) + "/" + str(len(chart_data)))
    plt.clf()
    chart_n += 1
        
    
    

