# Making a horror story based game
# Imports 
import pygame 
import sys
import random 
from mechanics import Menu
from mechanics import Player
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
		if 'menu' in locals():
			menu.render_menu(mouse, window)
		else:
			menu = Menu()
	else: 
		if 'menu' in locals():
			del menu
	# ======================================
	if game_state == [0,1,0,0,0]:
		if 'player' in locals():
			player.render(window)
		else:
			player = Player("Eugene", [50,200])
			print(player.name)
	else: 
		if 'player' in locals():
			del player


	#======================================================== 
	# EVENTS
	# Player Movement
	if game_state == [0,1,0,0,0]:
		player.move(event)
		# Pause Input
		
	
	for event in pygame.event.get():
		# Quit Game 
		if event.type == pygame.QUIT:
			sys.exit()
		
		if game_state == [0,1,0,0,0] and event.type == pygame.KEYDOWN and event.key == pygame.K_p:
			print("pause")
			game_state = [0,0,1,0,0]

		# Mouse Clicks 
		if event.type == pygame.MOUSEBUTTONUP:		
			# Menu inputs
			if game_state == [1,0,0,0,0]:
				game_state = menu.menu_inputs(game_state, mouse)

			
	pygame.display.update()