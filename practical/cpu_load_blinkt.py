#!/usr/bin/python
# -*- coding: utf-8 -*-
# /usr/bin python

from blinkt import set_pixel, show, clear, set_clear_on_exit
import time
import psutil

set_clear_on_exit()


def between(x, low, high):
    return x >= low and x <= high


def find_zone(percent):
    if percent == 0:
        return 0
    elif between(percent, 0.0, 12.5):
        return 1
    elif between(percent, 12.5, 25.0):
        return 2
    elif between(percent, 25.0, 37.5):
        return 3
    elif between(percent, 37.5, 50.0):
        return 4
    elif between(percent, 50.0, 62.5):
        return 5
    elif between(percent, 62.5, 75.0):
        return 6
    elif between(percent, 75.0, 87.5):
        return 7
    elif between(percent, 87.5, 100.0):
        return 8


def find_colour(zone):
    if between(zone, 6, 8):
        return 'red'
    elif between(zone, 4, 6):
        return 'orange'
    else:
        return 'green'


def get_cpu_percent():
    return psutil.cpu_percent(interval=0)


while True:
    zone = find_zone(get_cpu_percent())
    colour = find_colour(zone)
    if colour == 'red':
        r = 255
        g = 0
        b = 0
    if colour == 'orange':
        r = 255
        g = 165
        b = 0
    if colour == 'green':
        r = 0
        g = 255
        b = 0
    for i in range(zone):
        set_pixel(i, r, g, b)
    show()
    time.sleep(0.1)
    clear()
    time.sleep(0.1)


	
