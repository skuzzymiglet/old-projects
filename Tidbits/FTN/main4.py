#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame, sys, random, time
from pygame.locals import *
from decimal import *

# CONSTANTS

# COLORS

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# SCREEN


WIDTH = 1200
HEIGHT = 800

# Pygame initialization

pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Face the Numbers')
#pygame.mouse.set_visible(0)
display.fill(BLACK)

# Files

number_font = pygame.font.Font('fonts/3Dumb.ttf', 128) # For the number
large_number_font = pygame.font.Font('fonts/3Dumb.ttf', 256) # For red and green numbers
score_font = pygame.font.Font('fonts/3Dumb.ttf', 64) # For the score

# Writes number in respective color
def write_number(number, color):
    if color == RED or color == GREEN:
        number = large_number_font.render(str(number), True, color) # If it's red or green, the font size is 256
    else:
        number = number_font.render(str(number), True, color) # If it's white, the font size is 128 
        
    number_rect = number.get_rect()
    number_rect.center = (WIDTH/2, HEIGHT/2) # The center
    display.blit(number, number_rect)
    pygame.display.update() # Show it

# Writes current score, level and streak
def write_score(number, level, on_streak):
    number_obj = score_font.render('SCORE: ' + str(number) + " LEVEL: " + str(level) + (" STREAK"   if on_streak else ""), True, WHITE)
    number_rect = number_obj.get_rect()
    number_rect.center = (WIDTH/2, 40)
    display.blit(number_obj, number_rect)
    pygame.display.update()


# Draws the Pause notice
def draw_pause_screen():
    title = "PAUSED" # The text
    title_obj = number_font.render(title, True, WHITE)
    title_rect = title_obj.get_rect()
    title_rect.center = (WIDTH/2, HEIGHT/2) # The center
    description = "Get mouse into window to resume"
    description_obj = score_font.render(description, True, WHITE)
    description_rect = description_obj.get_rect()
    description_rect.center = (WIDTH/2, 40) # Where the score would be
    display.blit(title_obj, title_rect) # Show title
    display.blit(description_obj, description_rect) # Show description
    pygame.display.update() # Shows:
    # Get mouse into window to resume
    #
    #
    #=============PAUSED=============

# For convenience
def between(n, low, high):
    return not(n < low or n > high) 

def main():
    targets = False
    level = 1 
    score = 15 # The initial score
    on_streak = False # Whether the user is on a streak (level 2+ only)
    wait = 2 # The time the number is shown
    NUMBER_TO_KEY = { # For convenient conversion from an event
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
    previous_x = -1 # X is going to be random.randint(0, 5)
                                    # So -1 is impossible
                                    # The program checks whether the X value is different from last
                                    # So the first number can be anything
    x = 3 # X will be random
              # 0: Green
              # 5: Red
              # 2,3, 4: White
              # The first X has a lesser chance of being white
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Checks if the mouse is inside the window
        if not bool(pygame.mouse.get_focused()):
            # Show the pause screen
            draw_pause_screen()
            while True:
                for event in pygame.event.get():
                    pass
                if bool(pygame.mouse.get_focused()):
                    break # If the mouse is back in, carry on
                else:
                    print(bool(pygame.mouse.get_focused()))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit() # closing the window, end of the game loop

        display.fill(BLACK)
                
        activity = False

        if targets:
            pass
        else:
            # Score code

            if on_streak:
                x = 0
                if wait > Decimal(0.5):
                    wait -= Decimal(0.1)
                else:
                    on_streak = False
            else:
                wait = Decimal(1.5)
                while x == previous_x:
                    x = random.randint(0, 5)
            write_score(score, level, on_streak)
            #for i in range(score):
            #   draw_random_square()
            
            # Number drawing starts here
            
            number = random.randint(0, 9)
            while number == previous_number:
                number = random.randint(0, 9)
            if x == 0:
                write_number(number, GREEN)
                t1 = Decimal(time.time())
                while True:
                    if Decimal(time.time()) - t1 > wait:
                        if not activity:
                            score -= 5
                        break
                    else:
                        for event in pygame.event.get():
                            #HERE!
                            if event.type == pygame.KEYDOWN:
                                activity = True
                                if event.key == NUMBER_TO_KEY[number]:
                                    if number in [1, 0, 2, 9]:
                                        score += 2
                                    elif number in [3, 8]:
                                        score += 5
                                    elif number in [4, 5, 6, 7]:
                                        score += 10
                                    if Decimal(time.time()) - t1 < Decimal(0.8) and level == 2:
                                        on_streak = True
                                    elif Decimal(time.time()) - t1 < Decimal(0.5) and level == 3:
                                        on_streak = True
                                    break
                                else:
                                    if on_streak and level >= 2:
                                        on_streak = False
                                    elif score > 10:
                                        score -= 10
                                    break
                                        
                print(Decimal(time.time()) - t1)
                display.fill(BLACK)
            elif x == 5:
                write_number(number, RED)
                t1 = Decimal(time.time())
                while True:
                    if Decimal(time.time()) - t1 > wait:
                        break
                    else:
                        for event in pygame.event.get():
                            #HERE!
                            if event.type == pygame.KEYDOWN:
                                if event.key == NUMBER_TO_KEY[number]:
                                    score -= 10
                                    break
                                if event.key == pygame.K_RETURN:
                                    score += 1
                                    break
                                else:
                                    score -= 1
                                    break
                display.fill(BLACK)
            # Level Changers
            else:
                write_number(number, WHITE)
                t1 = Decimal(time.time())
                while True:
                    if Decimal(time.time()) - t1 >= wait:
                        break
                    else:
                        #for event in pygame.event.get():
                                #HERE!
                        #print(Decimal(time.time()) - t1)
                        pass
            display.fill(BLACK)
            previous_number = number
            if between(score, 0, 50):
                level = 1
                wait = Decimal(2)
            elif between(score, 50, 100):
                level = 2
                wait = Decimal(1.5)
            elif between(score, 100, 150):
                level = 3
                wait = 1
                    
            previous_x = x
    

# Main loop

if __name__ == '__main__':
    main()
