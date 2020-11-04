import random
import shapemodule

class Island:
	def __init__(self):
		pass

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
		o1 = raw_input('waiting for a fish to bite...')
		o2 = raw_input('\na fish bit the line!')
		fish = random.choice(self.fishlist)
		print('\nI caught a ' + fish)
		my_pocket.add(fish)

class River(BodyOfWater):
	def __init__(self, fishlist):
		self.fishlist = fishlist

	def fishin(self):
		pass

class Pocket:
	def __init__(self, inventory, spaces):
		self.inventory = inventory
		self.spaces = spaces
		for object in self.inventory: 
			self.spaces -= 1

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
		self.inventory.remove(object)
		self.spaces += 1

	def list(self):
		for object in self.inventory: 
			print(object)


import json

#main

f = open('pocket.txt', 'r')
print(f.read())
if f.read() == '': 
	f = open('pocket.txt', 'w')
	pocket = {
		'name':'eden',
		'objects':[],
		'spaces':5
	}
	y = json.dumps(pocket)
	f.write(y)
	f.close()
f = open('pocket.txt', 'r')
y = json.loads(f.read())
f.close()
print(y['name'])
for object in y['objects']:
	print(object)
print(y['spaces'])


my_pocket = Pocket(y['objects'], y['spaces'])
print('\nmy pocket contains:')
my_pocket.list()
print('')		
a1 = raw_input('\nwalking towards a tree...')

#this_object = raw_input('object to add to pockets: ')
#my_pocket.add(this_object)
#print('')		
#print('my pocket now contains:')
#my_pocket.list()
#print('')

this_tree = Tree('maple', 3, 1)
this_tree.draw()
shaketree = raw_input('do you want to shake this tree? ')
if shaketree == 'yes':
	this_tree.shake()
else:
	pass

print('\nmy pocket contains:')
my_pocket.list()

a3 = raw_input('')

fishing = raw_input('do you want to go fishing? ')
if fishing == 'yes':
	a2 = raw_input('\ngoing to the ocean...')
	myocean = Ocean(['dace', 'sea bass', 'horse mackerel', 'red snapper', 'barred knifejaw', 'sea bass', 'sea bass', 'olive flounder', 'dace', 'shark'])
	myocean.fishin()
	a4 = raw_input('')
	print('my pocket contains: ')
	my_pocket.list()
	print('')
else: pass		

#walk = raw_input('do you want to walk around yor island? ')

f = open('pocket.txt', 'w')
lpocket = {
	'name':'eden',
	'objects':my_pocket.inventory,
	'spaces':my_pocket.spaces
}
y = json.dumps(lpocket)
f.write(y)
f.close()
