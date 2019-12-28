#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame, time, sys, math, csv, random
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
screen = pygame.display.get_surface()
pygame.display.set_caption('Face the Numbers Training Mode')
pygame.mouse.set_visible(0)
display.fill(BLACK)

# Files

number_font = \
    pygame.font.Font('/media/skuzzymiglet/STORE-11/FTN/fonts/3Dumb.ttf'
                     , 128)
large_number_font = \
    pygame.font.Font('/media/skuzzymiglet/STORE-11/FTN/fonts/3Dumb.ttf'
                     , 256)
score_font = \
    pygame.font.Font('/media/skuzzymiglet/STORE-11/FTN/fonts/3Dumb.ttf'
                     , 64)
results_writer = csv.writer(open("results" + str(time.time()) + ".csv", "wb", buffering=0))


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

def improvement_text(x):
    if x == "--":
        return ""
    elif x < 0:
        return " better "
    elif x > 0:
        return " worse "
    else:
        return " (no change) "
    

def write_target(improvement, last_try, wrong):
    target_obj = score_font.render(str(int(math.floor(last_try)) if not last_try == "--" else last_try) + ' milliseconds '
                                   + str(int(abs(math.floor(improvement))) if not improvement == "--" else improvement)
                                   + (improvement_text(improvement)
                                   + " " + str(wrong) + " wrong" ),
                                   True, WHITE)
    target_rect = target_obj.get_rect()
    target_rect.center = (960, 40)
    display.blit(target_obj, target_rect)
    pygame.display.update()


def write_message(message, color):
    msg_obj = score_font.render(message, True, color)
    msg_rect = msg_obj.get_rect()
    msg_rect.center = (960, 540)
    display.blit(msg_obj, msg_rect)
    pygame.display.update()
    return msg_rect


def show_message(text, duration, color=WHITE):
    msg_rect = write_message(text, color)
    time.sleep(duration)
    display.fill(BLACK)
    pygame.display.update(msg_rect)


def draw_random_square():
    pos_and_size = (random.randint(0, WIDTH), random.randint(0,
                    HEIGHT), random.randint(1, 50), random.randint(1,
                    50))
    color = (random.randint(0, 255), random.randint(0, 255),
             random.randint(0, 255))
    pygame.draw.rect(display, color, pos_and_size)
    pygame.display.update()


def between(n, low, high):
    return not (n < low or n > high)


def results_to_target(results, wrong):
    if len(results) >= 1:
        improvement = results[-1]*1000 - results[len(results)-2]*1000
        last_try = results[-1]*1000
        write_target(improvement, last_try, wrong)
    else:
        write_target('--', '--', wrong)


def main():
    wait = 1
    previous_number = 0  # Impossible
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
    results = []
    wrong = 0
    goes = 0
    correct = False
    #results_writer.writerows([("Go", "Milliseconds", "Number")])
    x = -1
    previous_x = -1
    while True:
        done = False

        # Target code

        results_to_target(results, wrong)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        # for i in range(score):
        #   draw_random_square()

        # Number drawing starts here

        number = random.randint(0, 9)
        while number == previous_number:
            number = random.randint(0, 9)
        while x == previous_x:
            x = random.randint(0, 2)
        if x == 0:
            write_number(number, GREEN)
            t1 = time.time()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == number_to_key[number] :
                            results.append(time.time() - t1)
                            display.fill(BLACK)
                            show_message('CORRECT', 0.75, color=GREEN)
                            done = True
                            correct = True
                        else:
                            wrong += 1
                            display.fill(BLACK)
                            show_message('WRONG', 0.75, color=RED)
                            done = True
                            correct = False
                if done:
                    if correct:
                        goes += 1
                        results_writer.writerows([(goes, results[-1]*1000, number)])
                    break
        else:

            write_number(number, WHITE)
            time.sleep(wait)
            display.fill(BLACK)
        previous_number = number
        previous_x = x


# Main loop

if __name__ == '__main__':
    main()


			
