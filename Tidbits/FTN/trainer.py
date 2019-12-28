#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import time
import sys
import random
from pygame.locals import *

# CONSTANTS

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
FPS = 20
WIDTH = 1920
HEIGHT = 1080

pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Face the Numbers Training Mode')
pygame.mouse.set_visible(0)
display.fill(BLACK)

# Files

number_font = pygame.font.Font('fonts/3Dumb.ttf', 128)
large_number_font = pygame.font.Font('fonts/3Dumb.ttf', 256)
score_font = pygame.font.Font('fonts/3Dumb.ttf', 64)
bomb = pygame.mixer.Sound('audio/bomb.ogg')
running = True


def write_number(number, color):
    if color == RED or color == GREEN:
        number = large_number_font.render(str(number), True, color)
    else:
        number = number_font.render(str(number), True, color)
    # If it's red or green, the font size is 256
    # If it's white, the font size is 128 
    number_rect = number.get_rect()
    number_rect.center = (960, 540)
    display.blit(number, number_rect)
    pygame.display.update()


def write_score(number):
    number_obj = score_font.render('SCORE: ' + str(number), True, WHITE)
    number_rect = number_obj.get_rect()
    number_rect.center = (960, 40)
    display.blit(number_obj, number_rect)
    pygame.display.update()


def draw_random_square():
    pos_and_size = (random.randint(0, WIDTH), random.randint(0, HEIGHT),
                    random.randint(1, 50), random.randint(1, 50))
    color = (random.randint(0, 255), random.randint(0, 255),
             random.randint(0, 255))
    pygame.draw.rect(display, color, pos_and_size)
    pygame.display.update()

def between(n, low, high):
    return not(n < low or n > high)

def train(level):
    number_to_key = {
    0: pygame.K_0,
    1: pygame.K_1,
    2: pygame.K_2,
    3: pygame.K_3,
    4: pygame.K_4,
    5: pygame.K_5,
    6: pygame.K_6,
    7: pygame.K_7,
    8: pygame.K_8,
    9: pygame.K_9,
    }

    
def main():
    while True:

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit(0)
        train(2)

# Main loop

if __name__ == '__main__':
    main()
