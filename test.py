import re

def fishinocean():
	x = raw_input('fishing for a fish...')
	print('i got a big turtle')

def chopwood():
#	my_tree.chopwood()
	y = raw_input('chopping the tree...')
	print('i got 2 pieces of softwood and 1 piece of hardwood')

myDict = {
    'fish':fishinocean,
    'chop wood':chopwood
}

def myMain(myaction):
    myDict[myaction]()

myoption = raw_input('what do you want to do? ')
search = re.search('([Ff]ish|[Bb]eachcomb|[Ss]hake|[Cc]hop.wood)', myoption)
if not(search == None): 
	match = search.group()
	myMain(match.lower())
else: print('no match')


