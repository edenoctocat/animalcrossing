import random
import shapemodule
import re
import json
import requests
import pickle

class Island:
	def __init__(self):
		self.weathertemp = None
		self.weatherdescript = None

	def getweather(self):
		jsonweather = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=10002,us&appid=49c7e86bda3a0c8b83bf1efb4cd59041&units=imperial')
		pyweather = json.loads(jsonweather.text)
		mainweather = pyweather['main']
		weathertemp = mainweather['temp']
		self.weathertemp = int(round(weathertemp))
		weather = pyweather['weather']
		my_weather = weather[0]
		self.weatherdescript = my_weather['description']

class Player:
	def __init__(self, name, location):
		self.name = name
		self.location = location

class Forest:
	def __init__(self, maplenum, cedarnum):
		self.maplenum = maplenum
		self.cedarnum = cedarnum
		self.treenum = maplenum + cedarnum
		self.trees = []

	def populate(self):
		for x in range(self.maplenum):
			probstick = random.randint(2, 7)
			probbell = random.randint(0, 3)
			self.trees.append(Tree('maple', probstick, probbell))
		for y in range(self.cedarnum):
			probstick = random.randint(2, 7)
			probbell = random.randint(0, 3)
			self.trees.append(Tree('cedar', probstick, probbell))

	def findtree(self):
		global this_tree
		this_tree = random.choice(my_forest.trees)
		this_tree.tree_actions()

class Tree(Forest):
	def __init__(self, type, probstick, probbell):
		self.type = type
		self.probstick = probstick
		self.probbell = probbell
		self.probnothing = 10 - (probstick + probbell)

	def tree_actions(self):
		if not(player.location == 'tree'):
			c1 = input('\nwalking towards a tree...')
		else: pass
		player.location = 'tree'
		self.draw()
		action = input('\nwhat do you want to do? (shake the tree, chop wood, cut down the tree) ')
		parse_input(action, 'tree')
		print('')

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

		

class Stick(Tree):
	def __init__(self, name):
		self.name = name

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
	def __init__(self, name):
		self.name = name

	def draw(self):
		if self.name == 'softwood':
		        mycanvas = shapemodule.Canvas(40, 22)
        		end = shapemodule.RightTri(3, 45, 8, 8, 'LU')
        		end.paint(mycanvas, '* ')
        		length = shapemodule.Rectangle(9, 8, 5, 3)
        		length.paint(mycanvas, '= ')
        		mycanvas.display()
		elif self.name == 'wood':
		        mycanvas = shapemodule.Canvas(40, 22)
		        end = shapemodule.RightTri(3, 45, 8, 8, 'LU')
		        end.paint(mycanvas, '* ')
        		length = shapemodule.Rectangle(9, 8, 5, 3)
        		length.paint(mycanvas, '- ')
        		mycanvas.display()
		elif self.name == 'hardwood':
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
	def __init__(self):
		self.fishlist = []
		self.population = []
		jsonfish = requests.get('http://acnhapi.com/v1/fish')
		pyfish = json.loads(jsonfish.text)
		self.fishinfo = pyfish
		allfish = pyfish.keys()
		for fish in allfish:
#			myfish = fish.replace('_', ' ')
			self.fishlist.append(fish)

	def populate(self):
		for x in range(10):
			fish = random.choice(self.fishlist)
			thisfishinfo = self.fishinfo[fish]
			thisfishavail = thisfishinfo['availability']
			if thisfishavail['location'] == 'Sea':
				self.population.append(Fish(fish, thisfishinfo))
			else: x += 1

	def fishin(self):
		o1 = input('\nwaiting for a fish to bite...')
		o2 = input('\na fish bit the line!')
		fish = random.choice(self.population)
		print('\n' + fish.catchphrase)
		my_pocket.add(fish.name)

class River(BodyOfWater):
	def __init__(self):
		self.fishlist = []
		self.population = []
		jsonfish = requests.get('http://acnhapi.com/v1/fish')
		pyfish = json.loads(jsonfish.text)
		self.fishinfo = pyfish
		allfish = pyfish.keys()
		for fish in allfish:
			self.fishlist.append(fish)

	def river_actions(self):
		if not(player.location == 'river'):
			e1 = input('\nwalking towards a river...')
		else: pass
		player.location = 'river'
		action = input('\nwhat do you want to do? (go fishing, jump over river) ')
		parse_input(action, 'river')
		a2 = input('')
		print('')

	def populate(self):
		for x in range(10):
			fish = random.choice(self.fishlist)
			thisfishinfo = self.fishinfo[fish]
			thisfishavail = thisfishinfo['availability']
			if thisfishavail['location'] == 'River':
				self.population.append(Fish(fish, thisfishinfo))
			else: x += 1

	def fishin(self):
		r1 = input('\nwaiting for a fish to bite...')
		r2 = input('\na fish bit the line!')
		fish = random.choice(self.population)
		print('\n' + fish.catchphrase)
		my_pocket.add(fish.name)

class Fish:
	def __init__(self, name, info):
		fixname = name.replace('_', ' ')
		self.name = fixname
		self.info = info
		infoavail = self.info['availability']
		self.location = infoavail['location']
		self.rarity = infoavail['rarity']
		self.catchphrase = self.info['catch-phrase']
		self.museumphrase = self.info['museum-phrase']
		self.price = self.info['price']

	def draw(self):
		mycanvas = shapemodule.Canvas(5, 5)
		block = shapemodule.Rectangle(0, 0, 5, 5)
		block.paint(mycanvas, '* ')

class Beach(Island):
	def __init__(self):
		self.findlist = []

	def populate(self):
		self.findlist = [Shell('venus comb shell'), Shell('cowrie shell'), Shell('giant clam shell'), Shell('conch shell'), MessageBottle('message bottle', 'to whoever finds this, \n	i just found this diy project the other day and wanted to share it with someone. happy crafting! \n	best wishes, june')]

	def beach_actions(self):
		if not(player.location == 'beach'):
			a1 = input('\nwalking to the beach...')
		else: pass
		player.location = 'beach'
		action = input('\nwhat do you want to do? (go fishing, beachcombing) ')
		parse_input(action, 'beach')
		a2 = input('')
		
	def comb(self):
		c1 = input('\nwalking along the beach...')
		beachobject = random.choice(self.findlist)
		print('\nI found a ' + beachobject.name + '!')
		if re.search('shell', beachobject.name):
			beachobject.draw()
		else:
			pass
		pickup = input('do you want to pick it up? ')
		if re.search('^[Yy]', pickup):
			my_pocket.add(beachobject)
			if beachobject = 'message bottle':
				open = input('do you want to open the message bottle? ')
				if re.search('[Yy]', open):
					this_message.open()
		else:
			pass 

class Shell(Beach):
	def __init__(self, name):
		self.name = name

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

class MessageBottle(Beach):
	def __init__(self, name, message):
		self.name = name
		self.message = message

	def open(self):
		m0 = input('opening message bottle...')
		print(self.message)

class House(Player):
	def __init__(self, type, furniture, inventory):
		self.type = type
		self.furniture = furniture
		self.inventory = inventory

	def house_actions(self):
		if not(player.location == 'house'):
			b1 = input('\nwalking towards my house...')
		else: pass
		player.location = 'house'

class Museum(Island):
	def __init__(self, fish, insects, fossils):
		self.fish = fish
		self.insects = insects
		self.fossils = fossils

	def museum_actions(self):
		if not(player.location == 'museum'):
			g1 = input('\nwalking to the museum...')
		else: pass
		player.location = 'museum'

class Airport(Island):
	def __init__(self):
		pass

	def airport_actions(self):
		if not(player.location == 'airport'):
			d1 = input('\nwalking to the airport...')
		else: pass
		player.location = 'airport'

class Store(Island):
	def __init__(self, objects):
		self.objects = objects

	def store_actions(self):
		if not(player.location == 'nooks cranny'):
			f1 = input("\nwalking to nook's cranny...")
		else: pass
		player.location = 'nooks cranny'

class ResidentServices(Island):
	def __init__(self):
		pass

	def residentservices_actions(self):
		if not(player.location == 'resident services'):
			h1 = input('\nwalking to resident services...')
		else: pass
		player.location = 'resident services'

class Pocket(Player):
	def __init__(self, inventory, spaces):
		self.inventory = inventory
		self.spaces = spaces

	def access(self):
		print('')
		self.list()
		action = input('\nwhat do you want to do? (drop something, hold somthing, empty pocket) ') 
		if re.search('[Dd]rop', action):
			dropobjects = action[5:]
			dropobjects = dropobjects.split(', ')
			for object in self.inventory:
				if object.name in dropobjects:
					self.takeout(object)
					dropobjects.remove(object.name)
		elif re.search('[Hh]old', action):
			holdobject = action[5:]
			for object in self.inventory:
				if object.name == holdobject:
					object.draw()
		elif re.search('[Ee]mpty', action):
			self.empty()

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
			print('i have nothing in my pocket')
		else:
			print('my pocket contains:')
			for object in self.inventory: 
				print(object.name)

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
def parse_input(input, condition):
	actions = {
		'fish':{
			'beach':'my_ocean.fishin()', 
			'river':'my_river.fishin()'
		},
		'beachcomb':{
			'beach':'this_beach.comb()'
		},
		'shake':{
			'tree':'this_tree.shake()'
		},
		'chop wood':{
			'tree':'this_tree.chop()'
		},
		'cut down':{
			'tree':'this_tree.cutdown()'
		},
		'beach':'this_beach.beach_actions()',
		'ocean':'this_beach.beach_actions()',
		'river':'my_river.river_actions()',
		'tree':'my_forest.findtree()',
		'house':'my_house.house_actions()',
		'airport':'airport.airport_actions()',
		'nooks cranny':'nookscranny.store_actions()',
		'store':'nookscranny.store_actions()',
		'museum':'museum.museum_actions()',
		'resident services':'residentservices.residentservices_actions()',
		'pocket':'my_pocket.access()',
		'nook phone':'nookphone.access()',
		'diy':'diy project'
	}
	

	def select_action(myaction, condition):
		callaction = actions[myaction]
		if type(callaction) == dict: 
			try: 
				eval(callaction[condition])
			except: 
				global thisreturn
				thisreturn = 'incorrect place:' + myaction + ':' + condition
		else: 
			eval(callaction)			

	actionsearch = re.search('(fish|beachcomb|shake|chop.wood|cut.down)', input)
	placesearch = re.search('(beach|ocean|river|tree|house|airport|nook.*cranny|store|museum|resident.*services)', input)
	quitsearch = re.search('([Ee]nd|[Qq]uit|[Ee]xit)', input)
	personalactionsearch = re.search('(pocket|nook.phone|diy|stop)', input)
	ynsearch = re.search('(^[Yy]|^[Nn])', input)
	global thisreturn
	thisreturn = ''
	if actionsearch: 
		action = actionsearch.group()
		select_action(action, condition)
	elif placesearch: 
		place = placesearch.group()
		select_action(place, condition)
	elif quitsearch:
		thisreturn = 'quit'
	elif personalactionsearch:
		action = personalactionsearch.group()
		select_action(action, condition)
	elif ynsearch:
		thisreturn = ynsearch.group()
	else: thisreturn = 'no match'

f = open('launchscreen.txt', 'r')
print(f.read())
f.close()

a0 = input('')

name = input('name: ')
player = Player(name, 'house')
print('')

try:
	savedgame = open(player.name+'game.txt', 'rb')
	x = savedgame.read()
	game = pickle.load(x)
	savedgame.close()
	my_pocket = game['pocket']
	my_wallet = game['wallet']
	my_house = game['house']

except:
	f = open(player.name+'game.txt', 'x')
	f.close()
	my_pocket = Pocket([], 10)
	my_wallet = Wallet(0)
	my_house = House('tent', ['cot', 'lamp', 'radio'], [])
	game = {
		'name': player.name,
		'pocket':my_pocket,
		'wallet':my_wallet,
		'house':my_house
	}

my_island = Island()
this_beach = Beach()
this_beach.populate()
my_ocean = Ocean()
my_ocean.populate()
my_river = River()
my_river.populate()
my_forest = Forest(10, 10)
my_forest.populate()
#my_house = House('tent', ['cot', 'lamp', 'radio'], [])
museum = Museum([], [], [])
nookscranny = Store(['fishing rod', 'net', 'shovel', 'alarm clock', 'teapot and teacup', 'electric fan'])
airport = Airport()
residentservices = ResidentServices()
this_maple = Tree('maple', 5, 1)
this_cedar = Tree('cedar', 4, 2)
my_island.getweather()
print('it is ' + str(my_island.weathertemp) + ' degrees farenheit with ' + my_island.weatherdescript)
q1 = input('') 

my_pocket.list()
print('')
my_wallet.numbells()
print('')

def main():
#	print('options for things to do: \n   shake a tree (st) \n   go fishing (fi) \n   access pocket (ap) \n   walk around the island (wk) \n   chop wood (cw) \n   craft DIY projects (diy) \n   collect shells (cs) \n   catch bugs (cb) \n   go to house/tent (gth) \n   look at nook phone (lnp) \n') 
	whereto = input('\nwhere do you want to go/what do you want to do? ')
	parse_input(whereto, player.location)
	if thisreturn == 'quit':
		end = input('\ndo you want to quit animalcrossing? (y/n) ')
		if re.search('^[Yy]', end):
			return 'quit'
		else: pass

	elif re.search('incorrect.place', thisreturn):
		returns = thisreturn.split(':')
		print('\nyou cannot ' + returns[1] + ' at the ' + returns[2])

	elif thisreturn == 'no match':
		print("some places you can go are:\n   the beach\n   my house\n   a tree\n   the airport\n   the ocean\n   a river\n   nook's cranny (the store)\n   the museum\n   resident services\n")

while main() != 'quit':
	print('ok')

f = open(name+'game.txt', 'wb')
mygame = {
	'name':player.name,
	'pocket':my_pocket,
	'wallet':my_wallet,
	'house':my_house
}
pickle.dump(mygame, f)
f.close()
