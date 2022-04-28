# Making a horror story based game

# Imports 
import pygame 
import sys
import random 
# INITIALIZE PYGAME
pygame.init()

pygame.font.init()

colors = {
	"none": (30,30,30),
	"red": (255,0,0),

	"green": (0,255,0),
	"h_green": (0,150,0),
	
	"grey": (50,50,50)
}

# ==================================================================
fonts = {
	"title": pygame.font.Font("Ghastly_Panic.ttf", 200),
	"menu": pygame.font.SysFont("Arial", 30)
}

title_text = fonts["title"].render('Hell_0?' , 1, colors["red"])
menu_text = {
	"start": [fonts["menu"].render('Start' , 1, colors["green"]),
	pygame.Rect(297, 287, 100, 40)],		
	
	"option": [fonts["menu"].render('Option' , 1, colors["green"]),
	pygame.Rect(297, 327, 100, 40)],

	"credits": [fonts["menu"].render('Credits' , 1, colors["green"]),
	pygame.Rect(297, 367, 100, 40)],

}
# ==================================================================




HEIGHT, WIDTH = 450, 700 
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hell/0?")


# INITIATE GAME
game_over = False
while True:

	mouse = pygame.mouse.get_pos()
	window.fill(colors["none"])

	# Ingame
	if not game_over:
		pass
	
	for event in pygame.event.get():
		# Quit Game 
		if event.type == pygame.QUIT:
			sys.exit()
		
		if event.type == pygame.MOUSEBUTTONUP:
			for key in menu_text:
				if menu_text[key][1].collidepoint(mouse):
					print(key)
					break
      			
		if event.type == pygame.KEYDOWN:
			
			pass


	
	for key in menu_text:
		collide = menu_text[key][1].collidepoint(mouse)
		color = colors["h_green"] if collide else colors["none"]

		pygame.draw.rect(window, color, menu_text[key][1])
	
	# Menu
	window.blit(title_text, (150, 70))
	
	window.blit(menu_text["start"][0], (300, 290))
	window.blit(menu_text["option"][0], (300, 330))
	window.blit(menu_text["credits"][0], (300, 370))
	
	pygame.display.update()