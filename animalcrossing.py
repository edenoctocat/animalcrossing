import random
import shapemodule
import re
import json

class Island:
	def __init__(self):
		pass

class Player:
	def __init__(self, name, location):
		self.name = name
		self.location = location

class Tree:
	def __init__(self, type, probstick, probbell):
		self.type = type
		self.probstick = probstick
		self.probbell = probbell
		self.probnothing = 10 - (probstick + probbell)

	def shake(self):
		itemsintree = ['stick', 'bell', 'nothing']
		itemfromtree = random.choices(itemsintree, weights = [self.probstick, self.probbell, self.probnothing])
		if itemfromtree == ['stick']:
			print('\na stick fell out of the tree')
			stick = Stick()
			stick.draw()
			pickup = input('do you want to pick up the stick? ')
			if re.search('[Yy]', pickup):
				my_pocket.add('stick')
			else: 
				pass
		elif itemfromtree == ['bell']:
			print('\na bell fell out of the tree')
			my_wallet.add(10)
		else:
			print('\nnothing fell out of the tree')

	def chop(self):
		wood = ['softwood', 'wood', 'hardwood']
		c1 = input('\nchopping the tree...')
		woodtype = random.choice(wood)
		my_wood = Wood(woodtype)
		print('\n' + my_wood.type + ' came from the tree')
		my_wood.draw()
		pickup = input('do you want to pick up the piece of ' + my_wood.type + '? ')
		if re.search('[Yy]', pickup):
			my_pocket.add(my_wood.type)
		else: pass 

	def cutdown(self):
		cd1 = input('\ncutting down the tree...')
		cd2 = input('\ntree is cut down')
		self.drawfallen()
		player.location = 'island'
		cd3 = input('')

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
			triangle = shapemodule.Triangle(4, 45, 10, 3)
			triangle.paint(mycanvas, '^ ')
			triangle2 = shapemodule.Triangle(5, 45, 10, 6)
			triangle2.paint(mycanvas, '^ ')
			triangle3 = shapemodule.Triangle(6, 45, 10,  9)
			triangle3.paint(mycanvas, '^ ')
			trunk = shapemodule.Rectangle(9, 15, 3, 4)
			trunk.paint(mycanvas, '| ')
			mycanvas.display()

	def drawfallen(self):
		if self.type == 'maple':
			mycanvas = shapemodule.Canvas(40, 23)
			trunk = shapemodule.Rectangle(11, 11, 7, 3)
			trunk.paint(mycanvas, '– ')
			stump = shapemodule.Rectangle(7, 12, 3, 2)
			stump.paint(mycanvas, '| ')
			leaves = shapemodule.Circle(5, 22, 12)
			leaves.paint(mycanvas, 'O ')
			cover = shapemodule.Rectangle(19, 15, 7, 2)
			cover.paint(mycanvas, '  ')
			mycanvas.display()

		if self.type == 'cedar':
			mycanvas = shapemodule.Canvas(40, 23)
			triangle = shapemodule.RightTri(4, 45, 25, 13, 'RU')
			triangle.paint(mycanvas, '> ')
			triangle2 = shapemodule.RightTri(5, 45, 21, 12, 'RU')
			triangle2.paint(mycanvas, '> ')
			triangle3 = shapemodule.RightTri(6, 45, 16, 11, 'RU')
			triangle3.paint(mycanvas, '> ')
			trunk = shapemodule.Rectangle(13, 14, 3, 3)
			trunk.paint(mycanvas, '- ')
			stump = shapemodule.Rectangle(9, 15, 3, 2)
			stump.paint(mycanvas, '| ')
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

class Wood(Tree):
	def __init__(self, type):
		self.type = type

	def draw(self):
		if self.type == 'softwood':
		        mycanvas = shapemodule.Canvas(40, 22)
        		end = shapemodule.RightTri(3, 45, 8, 8, 'LU')
        		end.paint(mycanvas, '* ')
        		length = shapemodule.Rectangle(9, 8, 5, 3)
        		length.paint(mycanvas, '= ')
        		mycanvas.display()
		elif self.type == 'wood':
		        mycanvas = shapemodule.Canvas(40, 22)
		        end = shapemodule.RightTri(3, 45, 8, 8, 'LU')
		        end.paint(mycanvas, '* ')
        		length = shapemodule.Rectangle(9, 8, 5, 3)
        		length.paint(mycanvas, '- ')
        		mycanvas.display()
		elif self.type == 'hardwood':
        		mycanvas = shapemodule.Canvas(40, 22)
        		end = shapemodule.RightTri(3, 45, 8, 8, 'LU')
        		end.paint(mycanvas, '0 ')
        		length = shapemodule.Rectangle(9, 8, 5, 3)
        		length.paint(mycanvas, '- ')
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
		o1 = input('\nwaiting for a fish to bite...')
		o2 = input('\na fish bit the line!')
		fish = random.choice(self.fishlist)
		print('\nI caught a ' + fish)
		my_pocket.add(fish)

class River(BodyOfWater):
	def __init__(self, fishlist):
		self.fishlist = fishlist

	def fishin(self):
		r1 = input('\nwaiting for a fish to bite...')
		r2 = input('\na fish bit the line!')
		fish = random.choice(self.fishlist)
		print('\nI caught a ' + fish)
		my_pocket.add(fish)

class Beach(Island):
	def __init__(self, findlist):
		self.findlist = findlist

	def comb(self):
		c1 = input('\nwalking along the beach...')
		beachobject = random.choice(self.findlist)
		print('\nI found a ' + beachobject)
		if re.search('shell', beachobject + ' !'):
			this_shell = Shell(beachobject)
			this_shell.draw()
		else:
			pass
		pickup = input('do you want to pick it up? ')
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
		if self.inventory == []:
			print('I have nothing in my pocket')
		else:
			print('my pocket contains:')
			for object in self.inventory: 
				print(object)

class Wallet(Player):
	def __init__(self, bells):
		self.bells = bells

	def add(self, amount):
		int(amount)
		self.bells += amount

	def takeout(self, amount):
		int(amount)
		self.bells -= amount

	def numbells(self):
		mybells = str(self.bells)
		print('I have ' + mybells + ' bells')

# main
this_beach = Beach(['venus comb shell', 'sand dollar', 'cowrie shell', 'message bottle', 'conch shell'])
myocean = Ocean(['dace', 'sea bass', 'horse mackerel', 'red snapper', 'barred knifejaw', 'sea bass', 'sea bass', 'olive flounder', 'dace', 'shark'])
this_tree = Tree('maple', 5, 1)
this_cedar = Tree('cedar', 4, 2)

def parse_input(input, condition):
	actions = {
		'fish':'myocean.fishin()',
		'beachcomb':'this_beach.comb()',
		'shake':'this_tree.shake()',
		'chop wood':'this_tree.chop()',
		'cut down':'this_tree.cutdown()'
	}
	

	def select_action(myaction):
		callaction = actions[myaction]
		eval(callaction)

	search = re.search('([Ff]ish|[Bb]eachcomb|[Ss]hake|[Cc]hop.wood|[Cc]ut.down)', input)
	if not(search == None): 
		action = search.group()
		select_action(action)
	else: print('no match')


f = open('launchscreen.txt', 'r')
print(f.read())
f.close()

a0 = input('')

name = input('name: ')
player = Player(name, 'house')
print('')

try:
	savedgame = open(player.name+'game.txt', 'r')
	x = savedgame.read()
	y = json.loads(x)
	savedgame.close()
	my_pocket = Pocket(y['pocketobjects'], y['pocketspaces'])
	my_wallet = Wallet(y['mybells'])
except:
	f = open(player.name+'game.txt', 'w')
	f.close()
	game = {
		'name':player.name,
		'pocketobjects':[],
		'pocketspaces':10,
		'mybells':0
	}
	my_pocket = Pocket(game['pocketobjects'], game['pocketspaces'])
	my_wallet = Wallet(game['mybells'])

my_pocket.list()
print('')
my_wallet.numbells()
print('')

def main():
#	print('options for things to do: \n   shake a tree (st) \n   go fishing (fi) \n   access pocket (ap) \n   walk around the island (wk) \n   chop wood (cw) \n   craft DIY projects (diy) \n   collect shells (cs) \n   catch bugs (cb) \n   go to house/tent (gth) \n   look at nook phone (lnp) \n') 
	whereto = input('\nwhere do you want to go? ')
	if re.search('[Bb]each', whereto) or re.search('[Oo]cean', whereto):
		if not(player.location == 'beach'):
			a1 = input('\nwalking to the beach...')
		else: pass
		player.location = 'beach'
		def beach_actions():
			action = input('\nwhat do you want to do? (go fishing, beachcombing) ')
			parse_input(action, this_beach)
			a2 = input('')
			my_pocket.list()
			print('')

		beach_actions()
		leave = input('do you want to go somewhere else? ')
		if re.search('^[Nn]', leave):
			beach_actions()
		elif re.search('^[Yy]', leave):
			pass

	elif re.search('[Hh]ouse', whereto) or re.search('[Hh]ome', whereto):
		if not(player.location == 'house'):
			b1 = input('\nwalking towards my house...')
		else: pass
		player.location = 'house'

	elif re.search('[Tt]ree', whereto):
		if not(player.location == 'tree'):
			c1 = input('\nwalking towards a tree...')
		else: pass
		player.location = 'tree'
		this_tree.draw()
		def tree_actions():
			action = input('\nwhat do you want to do? (shake the tree, chop wood, cut down the tree) ')
			parse_input(action, this_tree)
			my_pocket.list()
			my_wallet.numbells()
			print('')

		tree_actions()
		leave = input('do you want to go somewhere else? ')
		if re.search('^[Nn]', leave):
			tree_actions()
		elif re.search('^[Yy]', leave):
			pass

	elif re.search('[Aa]irport', whereto) or re.search('[Pp]lane', whereto):
		if not(player.location == 'airport'):
			d1 = input('\nwalking to the airport...')
		else: pass
		player.location = 'airport'

	elif re.search('[Rr]iver', whereto):
		if not(player.location == 'river'):
			e1 = input('\nwalking towards a river...')
		else: pass
		player.location = 'river'

	elif re.search('[Ss]tore', whereto) or re.search('[Nn]ook.*[Cc]ranny', whereto):
		if not(player.location == 'nooks cranny'):
			f1 = input("\nwalking to nook's cranny...")
		else: pass
		player.location = 'nooks cranny'

	elif re.search('[Mm]useum', whereto):
		if not(player.location == 'museum'):
			g1 = input('\nwalking to the museum...')
		else: pass
		player.location = 'museum'

	elif re.search('[Rr]esident.*[Ss]ervices', whereto) or re.search('[Pp]laza', whereto):
		if not(player.location == 'resident services plaza'):
			h1 = input('\nwalking to resident services plaza...')
		else: pass
		player.location = 'resident services plaza'

	elif re.search('[Nn]o', whereto) or re.search('[Ee]xit', whereto) or re.search('[Qq]uit', whereto) or re.search('[Ee]nd', whereto):
		end = input('\ndo you want to quit animalcrossing? ')
		if re.search('^[Yy]', end):
			return 'quit'
		else: pass

	else:
		print("some places you can go are:\n   the beach\n   my house\n   a tree\n   the airport\n   the ocean\n   a river\n   nook's cranny (the store)\n   the museum\n   resident services\n")
	
	if whereto == 'access pocket':
		my_pocket.list()
		print('')
		remove = input('\ndo you want to take anything out of your pocket? ')
		remove_y = re.search('^[yY]', remove)
		remove_o = re.search('^[oO]', remove)
		if remove_y or remove_o:
			removewhat = input('what would you like to take out of your pocket? ')
			if removewhat == 'all' or removewhat == 'everything':
				my_pocket.empty()
			else:
				items = re.split(",\s", removewhat)
				for item in items:
					my_pocket.takeout(item)

			my_pocket.list()
			print('')

for x in range(5):
	if main() == 'quit':
		f = open(name+'game.txt', 'w')
		mygame = {
			'name':name,
			'pocketobjects':my_pocket.inventory,
			'pocketspaces':my_pocket.spaces,
			'mybells':my_wallet.bells
		}
		y = json.dumps(mygame)
		f.write(y)
		f.close()
		exit()
	else: pass

f = open(name+'game.txt', 'w')
mygame = {
	'name':name,
	'pocketobjects':my_pocket.inventory,
	'pocketspaces':my_pocket.spaces,
	'mybells':my_wallet.bells
}
y = json.dumps(mygame)
f.write(y)
f.close()
