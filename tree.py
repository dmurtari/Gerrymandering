class Node:

	def __init__(self, value):
		self.neighbors = []
		self.parent = None
		self.value = value
		self.children = []

	def add_child(self, child):
		child.parent = self
		self.children.append(child)

	def get_value(self):
		return self.value

	def get_parent(self):
		return self.parent

	def get_children(self):
		return self.children
