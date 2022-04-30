import pygame
from .gameobject import GameObjects


class Player(GameObjects):
	class_name = "player"
	desc = "Main Character"
	size = 25

	def __init__(self, name, pos):
		self.name = name
		GameObjects.objects[self.class_name] = self
		self.pos = pos

	
	def render(self, window):
		pygame.draw.rect(window, (0,0,255), (self.pos[0], self.pos[1], 50,50))


	def move(self, event):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP] or keys[pygame.K_w]:
			self.pos[1] -= 0.07
			print("up")
		elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
			self.pos[1] += 0.07
			print("down")
		elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
			self.pos[0] += 0.07
			print("right")
		elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
			self.pos[0] -= 0.07
			print("left")
