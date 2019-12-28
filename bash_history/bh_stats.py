import os, operator, re

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.transform import factor_cmap

home = os.path.expanduser("~")

history_file = open(home+"/.bash_history", "r")
history = history_file.read().split("\n")
history_file.close()
binaries = os.environ['PATH'].split(":")

freq = {}

for c in history:
    p = re.split(r"([|`> ])", c)
    for i in p:
        #print(i, end="-")
        if not i in freq.keys():
            freq[i] = 1
        else:
            freq[i] += 1
    #print()

freq = sorted(freq.items(), key=operator.itemgetter(1))

all_bins = []

for i in binaries:
    for j in os.listdir(i):
        all_bins.append(j)

#print(all_bins)

ofreq = freq
freq = []

for i in ofreq:
    if i[0] in all_bins:
        freq.append(i)
        

# PLOT TWIST!! BOKEH!!

output_file("bh.html")

ofreq = freq
freq = []

for i in ofreq:
    if i[1] >= 10:
        freq.append(i)

x = [i[0] for i in freq]
top = [i[1] for i in freq]

#print(x, top)

#source = ColumnDataSource(data=dict(commands=dict(freq).keys(), runs=dict(freq).values()))

p = figure(title="Most Used Commands", x_range=x, plot_height=1000, plot_width=2560)
p.vbar(x=x, top=top, width=0.75, line_color='white', fill_color="green")

#print(x, top)
p.xaxis.major_label_orientation = 1

show(p)
