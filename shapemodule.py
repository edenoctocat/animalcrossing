class Canvas:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.data = [['  '] * width for i in range(height)]

	def setpixel(self, brush, row, col):
		self.data[int(row)][int(col)] = brush

	def getpixel(self, row, col):
		return self.data[row][col]

	def display(self):
		print('\n'.join([''.join(row) for row in self.data]))

	def clear(self):
		self.data = [['  '] * self.width for i in range(self.height)]

class Shape:
	def paint(self, canvas): pass

class Rectangle(Shape):
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h

	def paint(self, canvas, brush):
		for y in range(self.h):
			for x in range(self.w):
				canvas.setpixel(brush, (self.y + y), (self.x + x))

class Circle(Shape):
	def __init__(self, radius, x, y):
		self.radius = radius
		self.x = x
		self.y = y
		self.diameter = (self.radius * 2) - 1
		if (self.radius % 2) == 1:
			self.startwidth = self.radius
		else:
			self.startwidth = (self.radius - 1)
		self.edgex = self.x - (self.radius - 1)
		self.edgey = self.y - (self.radius - 1)

	def paint(self, canvas, brush):
		for y in range(int((self.diameter - self.startwidth) / 2)):
			numpixels = self.startwidth + (y * 2)
			for x in range(numpixels):
				canvas.setpixel(brush, (self.edgey + y), (self.edgex + ((self.diameter - self.startwidth) / 2) - y + x))

		for y in range(self.startwidth):
			for x in range(self.diameter):
				canvas.setpixel(brush, (self.edgey + ((self.diameter - self.startwidth) / 2) + y), (self.edgex + x))

		for y in range(int((self.diameter - self.startwidth) / 2)):
			if y == 0: numpixels -= 0
			else: numpixels -= 2
			for x in range(numpixels):
				canvas.setpixel(brush, (self.edgey + self.diameter - ((self.diameter - self.startwidth) / 2) + y), ((self.edgex + (y + 1)) + x))

class Triangle(Shape):
	def __init__(self, height, angle, x, y):
		self.height = height
		self.angle = angle
		self.x = x
		self.y = y

	def paint(self, canvas, brush):
		if self.angle == 45:
			w = 1
			for y in range(self.height):
				for x in range(w):
					canvas.setpixel(brush, (self.y + y), ((self.x - y) + x))
				w += 2

		elif self.angle == 60:
			w = 1
			for y in range(self.height):
				for x in range(w):
					canvas.setpixel(brush, (self.y + y), ((self.x - (w // 2)) + x))
				if (y % 2) == 1: w += 2
				else: pass

		elif self.angle == 75:
			w = 1
			for y in range(self.height):
				for x in range(w):
					canvas.setpixel(brush, (self.y + y), ((self.x - (w // 2)) + x))
				if (y % 3) == 2: w += 2
				else: pass
	
class RightTri(Triangle):
	def __init__(self, height, angle, x, y, orient):
		self.height = height
		self.angle = angle
		self.x = x
		self.y = y
		self.orient = orient

	def paint(self, canvas, brush):
		if self.orient == 'RU':
			w = 1
			for y in range(self.height):
				for x in range(w):
					canvas.setpixel(brush, (self.y + y), (self.x + x))
				if self.angle == 45:
					w += 1
				elif self.angle == 60:
					if (y % 2) == 1: w += 1
					else: pass
				elif self.angle == 75:
					if (y % 3) == 2: w += 1
					else: pass

		if self.orient == 'LU':
			w = 1
			for y in range(self.height):
				for x in range(w):
					canvas.setpixel(brush, (self.y + y), ((self.x - y) + x))
				if self.angle == 45:
					w += 1
				elif self.angle == 60:
					if (y % 2) == 1: w += 1
					else: pass
				elif self.angle == 75:
					if (y % 3) == 2: w += 1
					else: pass

		if self.orient == 'RD':
			if self.angle == 45:
				w = this_triangle.height
			elif self.angle == 60:
				w = (this_triangle.height // 2) + 1
			elif self.angle == 75:
				pass
			for y in range(self.height):
				for x in range(w):
					canvas.setpixel(brush, (self.y + y), (self.x + x))
				if self.angle == 45:
					w += 1
				elif self.angle == 60:
					if (y % 2) == 1: w += 1
					else: pass
				elif self.angle == 75:
					if (y % 3) == 2: w += 1
					else: pass

		if self.orient == 'LD':
			w = 1
			for y in range(self.height):
				for x in range(w):
					canvas.setpixel(brush, (self.y + y), (self.x + x))
				if self.angle == 45:
					w += 1
				elif self.angle == 60:
					if (y % 2) == 1: w += 1
					else: pass
				elif self.angle == 75:
					if (y % 3) == 2: w += 1
					else: pass


def hi():
	print('hi turtles')

