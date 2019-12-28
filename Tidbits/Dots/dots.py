import pygame, time
from pygame.locals import *
from xml.dom.minidom import parse, parseString # For text-info

# Constants

WHITE = (255, 255, 255)

# Variables

running = True
level = 1
score = 0
splashscreen_button_areas = []


# Init

pygame.init()
pygame.mixer.init()
surface = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Dots")
surface.fill(WHITE)
pygame.display.update()

# Files

text_info = parse("xml/text-info.xml")
background = pygame.mixer.Sound("audio/background.ogg")

# Functions

def write_text(words, text_style, x, y, background_color=(255, 255, 255)):
	
    # Step 1: Get the text element we want
    
	text_types = text_info.toxml().splitlines() # Split it up
	del text_types[0]; del text_types[len(text_types)-1] # Delete junk, such as </text-info> at the end
	for text_type in text_types: # Iterate over the list
		if ('type="{0}"').format(text_style) in text_type: # If that type contains "text-type='the...one...we..want'" ...
			text_style_xml = text_type
			break # And we're done!
			
	# Step 2: Extract color, font and size
	
	text_type_attributes = text_style_xml.split(" ") # Split the attributes up
	del text_type_attributes[0]; del text_type_attributes[len(text_type_attributes)-1] # Remove junk, such as "<text-info"
	
	loop_num = 0
	for attribute in text_type_attributes:
		attribute = attribute.split('"')
		text_type_attributes[loop_num] = attribute[1]
		loop_num += 1	
	color = text_type_attributes[0].split(",")
	
	for i in range(len(color)):
		color[i] = int(color[i])
		
	color = tuple(color)	
	font = "fonts/" + text_type_attributes[1] + ".ttf"
	size = int(text_type_attributes[2])
	font = pygame.font.Font(font, size)

	# Step 3: Write!
	
	text_surface = font.render(words, True, color, background_color)
	text_rect = text_surface.get_rect()
	text_rect.center = (x, y)
	surface.blit(text_surface, text_rect)
	 

# Main

def main():
	
	background.play(loops=-1)
	write_text("Rafik Harrington Presents...", "splashscreen-heading-1", 960, 150)
	write_text("Dots", "splashscreen-title", 960, 270)
	write_text("Quit", "plain", 1800, 540)
	
	pass
	
if __name__ == "__main__":
	main()
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		pygame.display.update()
		time.sleep(1/20)

	
