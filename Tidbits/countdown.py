#!/usr/bin/python

import thread
import time

def count_down():
    seconds = 0
    while seconds > 0:
        seconds -= 1
        print(seconds)

try:
   thread.start_new_thread(count_down)
except:
   print("Error: unable to start thread")

while 1:
   pass
