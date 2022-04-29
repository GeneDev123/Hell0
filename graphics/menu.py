import pygame

# Creating a Menu Screen
class Menu:

	# Initial properties of the Menu
	def __init__(self):
		self.colors = {
			"none": (30,30,30),"red": (255,0,0),"green": (0,255,0),
			"h_green": (0,150,0),"grey": (50,50,50)
		}
		# ===========================================================
		self.fonts = {
		"title": pygame.font.Font("graphics/fonts/Ghastly_Panic.ttf", 200),
		"menu": pygame.font.SysFont("Arial", 30)
		}
		# ===========================================================
		self.title_text = self.fonts["title"].render('Hell_0?' , 1, self.colors["red"])
		self.menu_text = {
			"start": [self.fonts["menu"].render('Start' , 1, self.colors["green"]),
			pygame.Rect(297, 287, 100, 40)],		
			
			"option": [self.fonts["menu"].render('Option' , 1, self.colors["green"]),
			pygame.Rect(297, 327, 100, 40)],

			"credits": [self.fonts["menu"].render('Credits' , 1, self.colors["green"]),
			pygame.Rect(297, 367, 100, 40)],
		}
	# =========================================================================
	# Rendering the Menu
	def render_menu(self, mouse, window):

		for key in self.menu_text:
			collide = self.menu_text[key][1].collidepoint(mouse)
			color = self.colors["h_green"] if collide else self.colors["none"]
			pygame.draw.rect(window, color, self.menu_text[key][1])

		# Menu
		window.blit(self.title_text, (150, 70))
		
		window.blit(self.menu_text["start"][0], (300, 290))
		window.blit(self.menu_text["option"][0], (300, 330))
		window.blit(self.menu_text["credits"][0], (300, 370))
	# =========================================================================
	# Detecting Menu Inputs
	def menu_inputs(self, game_state, mouse):
		for key in self.menu_text:
			if self.menu_text[key][1].collidepoint(mouse):
				if key == "start":
					game_state = [0,1,0,0,0]
					print("start")
					break
				elif key == "option":
					game_state = [0,0,0,1,0]
					print("option")
					break
				elif key == "credits":
					game_state = [0,0,0,0,1]
					print("credits")
					break
		return game_state