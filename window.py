class Window:
	def __init__(self, width = 400, height = 600, black = (0, 0, 0)):
		self.width = width
		self.height = height
		self.black = black

	def get_width(self):
		return self.width

	def get_height(self):
		return self.height

	def get_color(self):
		return self.black
