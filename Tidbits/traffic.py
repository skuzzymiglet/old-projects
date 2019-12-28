import pygame, random, time
from pygame.locals import *

# Init bit
pygame.init()
surface = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Glorious Traffic!")
pygame.mouse.set_visible(0)

# Constants

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FPS = 20

# Variables

speed = 5

# Functions

def difference(a, b):
	if a > b:
		return a - b
	else:
		return b - a

# Main bit

# Ball class

class Ball(pygame.sprite.Sprite):
	def __init__(self, x=0, y=0, radius=10, color=WHITE):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		pygame.draw.circle(surface, color, (x, y), radius)
		pygame.display.update()
	def goto(self, x, y):
		self.x, self.y = x, y
		surface.fill(BLACK)
		pygame.draw.circle(surface, self.color, (x, y), self.radius)
		pygame.display.update()

running = True
ball = Ball(x=220, y=240, color=RED)
ball2 = Ball(x=220, y=240, color=GREEN)
time.sleep(1)
for x in range(192):
	if difference(ball.x, ball2.x) > 100:
		speed -= 2
	else:
		speed += 1
	ball.goto((x+1)*speed, 240)
	ball2.goto((x+1)*5, 240)
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
