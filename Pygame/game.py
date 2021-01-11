#current spot in tutorial: 27.18
import pygame
import os
import time
import random

pygame.font.init()

#set pygame window dimensions
WIDTH, HEIGHT = 750, 750
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Shooter')

#links image with assets folder and name of pic in order to load ships
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png")) 
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png")) 
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png")) 

#load in player ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png")) 

#load in lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

#load in background image
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

#starting main loop to handle all events
def main():
 	run = True
 	FPS = 60 #rn, program will check for events 60 times per second
 	level = 1
 	lives = 5
 	clock = pygame.time.Clock() #time tracking object
 	main_font = pygame.font.SysFont('comicsans', 50)

 	#only can call redraw_winddow function inside main function b/c it is nested
 	def redraw_window():
 		"""
 		Blit - renders object in the pygame screen
		(0, 0) - refers to top left corner, in order to increase x - values, move object to the right, in order
		to increase y -vvalues, move object down (opposite of normal)
 		"""
 		WINDOW.blit(BACKGROUND_IMAGE, (0, 0)) 

 		#drawing text onto screen

 		pygame.display.update()

 	while run:
 		clock.tick(FPS) #keeps game constant on any computer, updates clock
 		redraw_window()
 		#checking if any event has occured
 		for event in pygame.event.get():
 			if event.type == pygame.QUIT:
 				run = False

main()