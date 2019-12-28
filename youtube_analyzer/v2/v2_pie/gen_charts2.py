import pickle, random, time
import matplotlib.pyplot as plt

# This code is not for the faint-hearted! But it's sure well written. And I'm always here to lead you through this bastard!!

dump = open("dump.dat", "rb")
videos = pickle.load(dump) # Load data already extracted from YouTube history
dump.close()
channels = [] # A list of each video's channel
chcolors = {} # What color each channel's slice of the pie will be (channel: color hex)

# Constants

BATCHSIZE = 25 # The number of videos show in each pie. Larger = faster, less accurate, more dazzling

for video in videos:
    channels.append(video["channel"])

channels_list = list(set(channels)) # A list of all channels watched (i.e. all unique)

get_colors = lambda n: list(map(lambda i: "#" + "%06x" % random.randint(0, 0xFFFFFF), range(n))) # Generates n random colors

def sort_dict(d): # Sort a dictionary by its values
    return sorted(d.items(), key=lambda kv: kv[1], reverse=True)

def gen_chcolors(): # Generate colors for channels
    colors = []
    while len(colors) < len(channels_list): # Generate (unique) colors until there's enough
        colors = list(set(get_colors(len(channels_list))))
    return colors

chcolors = dict(zip(channels_list, gen_chcolors())) # Match each of these colors to channels

def gen_batches(videos): # With our list of every video, generate batches of 25, stepping by 1. Returns a GIGANTIC array
    batches = []
    for batch in range(len(videos) - BATCHSIZE): # For each batch's starting index in the video list
        this_batch = []
        for i in range(BATCHSIZE): # For each of the 25 in the batch
            this_batch.append(videos[batch+i]) # Add the batch's videos
        batches.append(this_batch) # Append this batch to all batches
    return batches

def gen_channel_sizes(channels): # Given the channels, spit out a dict with the frequency of each
    sizes = {}
    for channel in channels:
        if not channel in sizes.keys():
            sizes[channel] = 0
        sizes[channel] += 1
    return sizes

def gen_title(batch): # Given a batch of videos, generate a title for its pie: the range of dates (eg. Jan 2016 - Feb 2016)
    batch_sorted = sorted(batch, key=lambda batch: batch["timestamp"]) # Sort the videos by their Unix timestamps
    start = batch[0]["month"] # The first video's month
    end = batch[-1]["month"] # The last video's month
    if start == end: # If first is in same month as last...
        return start # Return either
    else:
        return start + " - " + end # Else Dec 2018 - Jan 2019 etc WTF

batches = gen_batches(videos) # Generate batches
pies = [] # This is a list of dicts with infos for the pies

start = time.time() # Timer start for whole process
for i, batch in enumerate(batches):
    pie_start = time.time() # Timer start for each pie
    title = gen_title(batch) # Make a title for the pie
    channels = [video["channel"] for video in batch] # Get channel for each video 
    channels = gen_channel_sizes(channels) # Turn this into a dict of frequencies
    channels = sort_dict(channels) # Sort by frequency -> tuple
    labels = [channel[0] for channel in channels] # Get the channel names (slice labels)
    sizes = [channel[1] for channel in channels] # Get channel frequencies (slice sizes)
    colors = [chcolors[channel] for channel in labels] # Get each slice's color according to its channel
    plt.suptitle(title) # Give the chart a title
    plt.pie(sizes, labels=labels, colors=colors, startangle=0.0) # Make the pie chart!
    plt.axis('equal')
    plt.savefig("charts/chart" + "{0:04}".format(i) + ".png") # Save as chart0001.png, chart0002.png, etc
    plt.clf() # Clear the pie for next one
    print(str(i)+"/"+str(len(batches)), str(time.time() - pie_start)+" seconds") # Progress meter

end = time.time()     
print(str(end - start) + " seconds, average " + str(len(batches) / (end - start)) + " seconds per pie")

