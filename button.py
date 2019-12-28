import pygame, time
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((440, 480))
pygame.display.set_caption("A single button")

# Variables

running = True

# Constants

WHITE = (255, 255, 255)

def main():
	screen.fill(WHITE)
	print("What")
	
if __name__ == "__main__":
	main()
	while running:
	  for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  running = False

