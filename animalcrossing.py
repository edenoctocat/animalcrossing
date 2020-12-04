import random
import shapemodule
import re
import json

class Island:
	def __init__(self):
		pass

class Player:
	def __init__(self, name):
		self.name = name

class Tree:
	def __init__(self, type, probstick, probbell):
		self.type = type
		self.probstick = probstick
		self.probbell = probbell
		self.probnothing = 10 - (probstick + probbell)

	def shake(self):
		itemsintree = []
		numsticks = self.probstick * 10
		for x in range(numsticks):
			itemsintree.append('stick')
		numbells = self.probbell * 10
		for x in range(numbells):
			itemsintree.append('bell')
		numnothing = self.probnothing * 10
		for x in range(numnothing):
			itemsintree.append('nothing')
		itemfromtree = random.choice(itemsintree)
		if itemfromtree == 'stick':
			print('\na stick fell out of the tree')
			stick = Stick()
			stick.draw()
			pickup = raw_input('do you want to pick up the stick? ')
			if pickup == 'yes':
				my_pocket.add('stick')
			else: 
				pass
		elif itemfromtree == 'bell':
			print('\na bell fell out of the tree')
		else:
			print('\nnothing fell out of the tree')

	def draw(self):
		if self.type == 'maple':
			mycanvas = shapemodule.Canvas(40, 23)
			trunk = shapemodule.Rectangle(9, 11, 3, 7)
			trunk.paint(mycanvas, '| ')
			leaves = shapemodule.Circle(5, 10, 6)
			leaves.paint(mycanvas, 'O ')
			mycanvas.display()

		if self.type == 'cedar':
			mycanvas = shapemodule.Canvas(40, 23)
			box = shapemodule.Rectangle(10, 8, 8, 8)
			box.paint(mycanvas, '* ')
			mycanvas.display()

class Stick:
	def __init__(self):
		pass

	def draw(self):
		mycanvas = shapemodule.Canvas(40, 22)
		stick = shapemodule.Rectangle(6, 10, 8, 3)
		stick.paint(mycanvas, '- ')
		twig1 = shapemodule.Rectangle(11, 8, 1, 2)
		twig1.paint(mycanvas, '/ ')
		twig2 = shapemodule.Rectangle(10, 9, 1, 1)
		twig2.paint(mycanvas, '/ ')
		leaf = shapemodule.Circle(2, 12, 7)
		leaf.paint(mycanvas, '0 ')
		mycanvas.display()

class BodyOfWater:
	def __init__(self):
		pass

	def fishin(self):
		pass

class Ocean(BodyOfWater):
	def __init__(self, fishlist):
		self.fishlist = fishlist

	def fishin(self):
		o1 = raw_input('\nwaiting for a fish to bite...')
		o2 = raw_input('\na fish bit the line!')
		fish = random.choice(self.fishlist)
		print('\nI caught a ' + fish)
		my_pocket.add(fish)

class River(BodyOfWater):
	def __init__(self, fishlist):
		self.fishlist = fishlist

	def fishin(self):
		pass

class Beach(Island):
	def __init__(self, findlist):
		self.findlist = findlist

	def comb(self):
		c1 = raw_input('\nwalking along the beach...')
		beachobject = random.choice(self.findlist)
		print('\nI found a ' + beachobject)
		if re.search('shell', beachobject + ' !'):
			this_shell = Shell(beachobject)
			this_shell.draw()
		else:
			pass
		pickup = raw_input('do you want to pick it up? ')
		if re.search('^[Yy]', pickup):
			my_pocket.add(beachobject)
		else:
			pass 

class Shell(Beach):
	def __init__(self, type):
		self.type = type

	def draw(self):
		my_canvas = shapemodule.Canvas(40, 12)
		circle = shapemodule.Circle(4, 5, 5)
		circle.paint(my_canvas, '| ')
		dot1 = shapemodule.Rectangle(2, 3, 1, 1)
		dot1.paint(my_canvas, '( ')
		dot2 = shapemodule.Rectangle(8, 3, 1, 1)
		dot2.paint(my_canvas, ') ')
		top = shapemodule.Rectangle(3, 2, 5, 1)
		top.paint(my_canvas, 'n ')
		side1 = shapemodule.Rectangle(2, 6, 1, 1)
		side1.paint(my_canvas, '\\ ')
		side2 = shapemodule.Rectangle(8, 6, 1, 1)
		side2.paint(my_canvas, '/ ')
		side3 = shapemodule.Rectangle(3, 7, 1, 1)
		side3.paint(my_canvas, '\\ ')
		side4 = shapemodule.Rectangle(7, 7, 1, 1)
		side4.paint(my_canvas, '/ ')
		side5 = shapemodule.Rectangle(4, 8, 1, 1)
		side5.paint(my_canvas, '/ ')
		side6 = shapemodule.Rectangle(6, 8, 1, 1)
		side6.paint(my_canvas, '\\ ')
		base = shapemodule.Rectangle(3, 9, 5, 1)
		base.paint(my_canvas, '- ')
		my_canvas.display()

class Pocket(Player):
	def __init__(self, inventory, spaces):
		self.inventory = inventory
		self.spaces = spaces

	def add(self, object):
		if self.checkspaces() == False:
			print('\nHuh? My pockets are full.')
		else:
			self.inventory.append(object)
			self.spaces -= 1

	def checkspaces(self):
		if self.spaces == 0:
			return False
		else:
			return True

	def takeout(self, object):
		try:
			self.inventory.remove(object)
			self.spaces += 1
		except:
			print('you do not have that item in your pocket')

	def empty(self):
		for object in self.inventory:
			self.spaces += 1
		del self.inventory[:]

	def list(self):
		for object in self.inventory: 
			print(object)

name = raw_input('name: ')

try:
	f = open(name+'pocket.txt', 'r')
	x = f.read()
	y = json.loads(x)
	f.close()
	print(y['name'])
	for object in y['objects']:
		print(object)
	print(y['spaces'])
	my_pocket = Pocket(y['objects'], y['spaces'])
except:
	f = open(name+'pocket.txt', 'w')
	f.close()
	pocket = {
		'name':name,
		'objects':[],
		'spaces':5
	}
	my_pocket = Pocket(pocket['objects'], pocket['spaces'])

print('\nmy pocket contains:')
my_pocket.list()
print('')		

def main():
#	print('options for things to do: \n   shake a tree (st) \n   go fishing (fi) \n   access pocket (ap) \n   walk around the island (wk) \n   chop wood (cw) \n   craft DIY projects (diy) \n   collect shells (cs) \n   catch bugs (cb) \n   go to house/tent (gth) \n   look at nook phone (lnp) \n') 
	whereto = raw_input('\nwhere do you want to go? ')
	if re.search('[Bb]each', whereto) or re.search('[Oo]cean', whereto):
		a1 = raw_input('\nwalking to the beach...')
		def beach_actions():
			action = raw_input('\nwhat do you want to do? (go fishing, beachcombing) ')
			if re.search('[Ff]ish', action):
				myocean = Ocean(['dace', 'sea bass', 'horse mackerel', 'red snapper', 'barred knifejaw', 'sea bass', 'sea bass', 'olive flounder', 'dace', 'shark'])
				myocean.fishin()
				a2 = raw_input('')
				print('my pocket contains: ')
				my_pocket.list()
				print('')
			elif re.search('[Bb]eachcomb', action) or re.search('[Ss]hell', action):
				this_beach = Beach(['venus comb shell', 'sand dollar', 'cowrie shell', 'message bottle', 'conch shell'])
				this_beach.comb()
				a3 = raw_input('')
				print('my pocket contains: ')
				my_pocket.list()
				print('')
			else: pass

		beach_actions()
		leave = raw_input('do you want to go somewhere else? ')
		if re.search('^[Nn]', leave):
			beach_actions()
		elif re.search('^[Yy]', leave):
			pass

	elif re.search('[Hh]ouse', whereto) or re.search('[Hh]ome', whereto):
		b1 = raw_input('\nwalking towards my house...')

	elif re.search('[Tt]ree', whereto):
		c1 = raw_input('\nwalking towards a tree...')
		this_tree = Tree('maple', 5, 1)
		this_tree.draw()
		def tree_actions():
			action = raw_input('\nwhat do you want to do? (shake the tree, chop wood, cut down the tree) ')
			if re.search('[Ss]hake', action):
				this_tree.shake()
				print('\nmy pocket contains:')
				my_pocket.list()
			elif re.search('[Cc]hop.*[Ww]ood', action):
				pass
			elif re.search('[Dd]own.*[Tt]ree', action):
				pass
			else: pass

		tree_actions()
		leave = raw_input('do you want to go somewhere else? ')
		if re.search('^[Nn]', leave):
			tree_actions()
		elif re.search('^[Yy]', leave):
			pass

	elif re.search('[Aa]irport', whereto) or re.search('[Pp]lane', whereto):
		d1 = raw_input('\nwalking to the airport...')

	elif re.search('[Rr]iver', whereto):
		e1 = raw_input('\nwalking towards a river...')

	elif re.search('[Ss]tore', whereto) or re.search('[Nn]ook.*[Cc]ranny', whereto):
		f1 = raw_input("\nwalking to nook's cranny...")

	elif re.search('[Mm]useum', whereto):
		g1 = raw_input('\nwalking to the museum...')

	elif re.search('[Rr]esident.*[Ss]ervices', whereto):
		h1 = raw_input('\nwalking to resident services...')

	elif re.search('[Nn]o', whereto) or re.search('[Ee]xit', whereto) or re.search('[Qq]uit', whereto) or re.search('[Ee]nd', whereto):
		end = raw_input('\ndo you want to quit animalcrossing? ')
		if re.search('^[Yy]', end):
			return 'quit'
		else: pass

	else:
		print("some places you can go are:\n   the beach\n   my house\n   a tree\n   the airport\n   the ocean\n   a river\n   nook's cranny (the store)\n   the museum\n   resident services\n")
	
	action = 'hi'

	if action == 'access pocket' or action == 'ap':
		print('my pocket contains: ')
		my_pocket.list()
		print('')
		remove = raw_input('\ndo you want to take anything out of your pocket? ')
		remove_y = re.search('^[yY]', remove)
		remove_o = re.search('^[oO]', remove)
		if remove_y or remove_o:
			removewhat = raw_input('what would you like to take out of your pocket? ')
			if removewhat == 'all' or removewhat == 'everything':
				my_pocket.empty()
			else:
				items = re.split(",\s", removewhat)
				for item in items:
					my_pocket.takeout(item)

			print('\nmy pocket contains:')
			my_pocket.list()
			print('')

for x in range(5):
	if main() == 'quit':
		f = open(name+'pocket.txt', 'w')
		lpocket = {
			'name':name,
			'objects':my_pocket.inventory,
			'spaces':my_pocket.spaces
		}
		y = json.dumps(lpocket)
		f.write(y)
		f.close()
		exit()
	else: pass

f = open(name+'pocket.txt', 'w')
lpocket = {
	'name':name,
	'objects':my_pocket.inventory,
	'spaces':my_pocket.spaces
}
y = json.dumps(lpocket)
f.write(y)
f.close()
