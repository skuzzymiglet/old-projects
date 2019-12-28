import random
import math
from PIL import Image

SCALE_FACTOR = 0.5

im = Image.open("twitter.png")
im = im.rotate(0)
im.show()

pre_width = im.width
pre_height = im.height

im.thumbnail((math.floor(pre_width*SCALE_FACTOR), math.floor(pre_width*SCALE_FACTOR)), Image.ANTIALIAS);

WIDTH = im.width
HEIGHT = im.height

yeet = []

for y in range(HEIGHT):
    sub = []
    for x in range(WIDTH):
        px = im.getpixel((x, y))
        if px == (0, 172, 237):
            sub.append(" "*2)
        elif px == (255,255,255):
            sub.append(("\033[0;31;44m"+str(random.randint(0, 1))+"\033[0m")*2)
    yeet.append(sub)

for y in yeet:
    print(''.join(y))
