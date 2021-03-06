class Node:
	"""
	Basic node data structure, that can have an arbitrary number of children.
	Each node contains a value, a list of children, knows which player made 
	the move that created the node, and knows the type of move that the node is
	part of. Each node also keeps track of its parents
	"""

	def __init__(self, value, player):
		self.neighbors = []
		self.parent = None
		self.value = value
		self.children = []
		self.player = player
		self.type_of_move = ""

	def add_child(self, child):
		child.parent = self
		child.type_of_move = self.get_type_of_move()
		self.children.append(child)

	def get_value(self):
		return self.value

	def get_parent(self):
		return self.parent

	def get_children(self):
		return self.children

	def get_player(self):
		return self.player

	def get_type_of_move(self):
		return self.type_of_move
