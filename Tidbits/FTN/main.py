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

pygame.init()
display = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Face the numbers')
pygame.mouse.set_visible(0)
display.fill(BLACK)

# Files

number_font = pygame.font.Font('fonts/3Dumb.ttf', 128)
score_font = pygame.font.Font('fonts/3Dumb.ttf', 64)
bomb = pygame.mixer.Sound('audio/bomb.ogg')
running = True


def write_number(number, color):
    number = number_font.render(str(number), True, color)
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
    pos_and_size = (random.randint(0, 1920), random.randint(0, 1080),
                    random.randint(1, 50), random.randint(1, 50))
    color = (random.randint(0, 255), random.randint(0, 255),
             random.randint(0, 255))
    pygame.draw.rect(display, color, pos_and_size)
    pygame.display.update()


def main():
    level = 1
    score = 25
    on_streak = False
    wait = 1.5
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
    while True:
        if level == 1:

            # Quit code

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

            # Score code

            if on_streak:
                x = 0
                write_score(str(score) + ' + STREAK   LEVEL 1')
                if wait > 0.5:
                    wait -= 0.1
                else:
                    on_streak = False
            else:
                wait = 1.5
                x = random.randint(0, 5)
                write_score(str(score) + '   LEVEL 1')

            for i in range(score):
                draw_random_square()

            # Number drawing starts here

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
                                    if random.randint(0, 2) == 1:
                                        on_streak = True
                                    break
                                else:
                                    if on_streak:
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

    if score == 0:
        bomb.play()
        time.sleep(2)
        pygame.quit()
        sys.exit(0)

# Main loop

if __name__ == '__main__':
    main()
