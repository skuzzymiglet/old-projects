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
pygame.display.set_caption('Face the Numbers')
pygame.mouse.set_visible(0)
display.fill(BLACK)

# Files

number_font = pygame.font.Font('fonts/3Dumb.ttf', 128)
large_number_font = pygame.font.Font('fonts/3Dumb.ttf', 256)
score_font = pygame.font.Font('fonts/3Dumb.ttf', 64)
bomb = pygame.mixer.Sound('audio/bomb.ogg')


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

def main():
    level = 1
    score = 15
    on_streak = False
    wait = 2 # The time the number is shown
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
    previous_number = 0 # For when game starts
    targets = False
    while True:
        # Quit code

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit(0)
                if event.type == pygame.KEYDOWN:
                        if event.key == "p":
                                pause = True

        if targets:
            pass
        else:
                        
                # Score code
                
                if on_streak:
                        x = 0
                        write_score(str(score) + ' + STREAK   LEVEL ' + str(level))
                        if wait > 0.5:
                                wait -= 0.1
                        else:
                                on_streak = False
                else:
                        wait = 1.5
                        x = random.randint(0, 5)
                        write_score(str(score) + '   LEVEL ' + str(level))

                #for i in range(score):
                #   draw_random_square()
                
                # Number drawing starts here
                
                number = random.randint(0, 9)
                while number == previous_number:
                        number = random.randint(0, 9)
                if x == 0:
                        write_number(number, GREEN)
                        t1 = time.time()
                        while True:
                                if time.time() - t1 > wait:
                                        break
                                else:
                                        for event in pygame.event.get():
                                                if event.type == pygame.KEYDOWN:
                                                        if event.key == number_to_key[number]:
                                                                score += 10
                                                                if random.randint(0, 2) == 1 and level == 2:
                                                                        on_streak = True
                                                                break
                                                        else:
                                                                if on_streak and level == 2:
                                                                        on_streak = False
                                                                elif score > 10:
                                                                        score -= 10
                                                                break
                        display.fill(BLACK)
                elif x == 5:
                        write_number(number, RED)
                        t1 = time.time()
                        while True:
                                if time.time() - t1 > wait:
                                        break
                                else:
                                        for event in pygame.event.get():
                                                if event.type == pygame.KEYDOWN:
                                                        if event.key == number_to_key[number]:
                                                                score -= 10
                                                                break
                                                        if event.key == pygame.K_RETURN:
                                                                score += 1
                                                                break
                                                        else:
                                                                score -= 1
                                                                break

                        display.fill(BLACK)
                else:
                        write_number(number, WHITE)
                        time.sleep(wait)
                        display.fill(BLACK)
                previous_number = number
                if between(score, 0, 50):
                        level = 1
                        wait = 2
                elif between(score, 50, 100):
                        level = 2
                        wait = 1.5
                elif between(score, 100, 150):
                        #level = 3
                        #targets = True
                        level = 2
                        wait = 1.5
    if score <= 0:
        bomb.play()
        time.sleep(2)
        pygame.quit()
        sys.exit(0)
        

# Main loop

if __name__ == '__main__':
    main()
