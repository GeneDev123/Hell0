# Making a horror story based game

# Imports 
import pygame 
import sys
import random 
from graphics import Menu
# INITIALIZE PYGAME
pygame.init()

# Screen
HEIGHT, WIDTH = 450, 700 
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hell/0?")


colors = {
	"none": (30,30,30),"red": (255,0,0),"green": (0,255,0),
	"h_green": (0,150,0),"grey": (50,50,50)
}

# INITIATE GAME
game_state = [1,0,0,0,0] # game_state  = [menu, playing, pause, option, credits]

while True:
	mouse = pygame.mouse.get_pos()
	window.fill(colors["none"])

	# Games States
	if game_state == [1,0,0,0,0]:
		menu = Menu()
		menu.render_menu(mouse, window)
	#======================================================== 
	# EVENTS
	for event in pygame.event.get():
		# Quit Game 
		if event.type == pygame.QUIT:
			sys.exit()
		
		# Mouse Clicks 
		if event.type == pygame.MOUSEBUTTONUP:

			game_state = menu.menu_inputs(game_state, mouse)
      		 		

		# Keyboard Inputs 
		if event.type == pygame.KEYDOWN:
			
			# Chracter Movements inputs 
			if game_state == [0,1,0,0,0]:
				if event.key == pygame.K_UP or event.key == pygame.K_w:
					print("up")
				elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
					print("down")
				elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
					print("left")
				elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					print("right")
				# Pause input  

				elif event.key == pygame.K_p:
					print("pause")
					game_state = [0,0,1,0,0]
	
	
	pygame.display.update()