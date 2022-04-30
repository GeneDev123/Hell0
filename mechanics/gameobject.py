class GameObjects: 
	obj_type = ""
	desc = ""
	objects = {}

	# def __init__(self, name):
	# 	self.name = name
	# 	GameObjects.objects[self.class_name].append(self)

	def get_desc(self):
		return self.class_name + "\n" + self.desc


# class Player(GameObjects):
# 	class_name = "player"
# 	desc = "Main Character"

# class NPC(GameObjects):
# 	class_name = "player"
# 	desc = "Non-Playable Character"

# class Interactable(GameObjects):
# 	class_name = "player"
# 	desc = "Interactables"


# class NonInteractable(GameObjects):
# 	class_name = "player"
# 	desc = "Non-interactablesr"


# class Collision(GameObjects):
# 	class_name = "player"
# 	desc = "Collision"



