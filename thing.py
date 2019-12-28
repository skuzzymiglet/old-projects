import pygame
from pygame.locals import *

pygame.init()

# Colors

WHITE = (255, 255, 255)

surface = pygame.display.set_mode((480, 500))
pygame.display.set_caption("Bwyd")
pygame.display.update()
burger = pygame.image.load("img/burger.jpg")
surface.fill(WHITE)

running = True
while running:
	surface.blit(burger, (240, 250))
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

