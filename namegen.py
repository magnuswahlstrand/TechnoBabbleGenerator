import random as rnd
import argparse

def generateWesternishName(markovChains):
	if(rnd.random()<0.8):
		return generateFromMarkovChain(markovChains).capitalize()
	else:
		return generateFromMarkovChain(markovChains).capitalize() + 'son'

def generateJapaneseishName():
	s = ''
	v = 'aeiou'
	c = 'wrtpsdfghklcvbnm' #Some letters are removed because they looked weird.
	l = rnd.randint(2,4)*2
	for i in range(l):
		if(i%2 == 0):
			s += rnd.choice(c)
		else:
			s += rnd.choice(v)
	s = s.capitalize()
	return s

def generateRandomName(markovChains, gadgetType = None):
	buzzwords = ['Quantum', 'Dynamic', 'Static', 'Entangled', 'Nano', 'Relativistic', 'Mega', 'Super', 'Celestial', 'Ridgid', 'Negative', 'Frictionless', 'Superconducting', 'Particle', 'Nuclear', 'Evolutionary', 'Ultra', 'Hyper-G', 'Low-Gravity', 'Interstellar', 'Viscous', 'Inviscous', 'Escalating','Timeless','Hyper', 'Dangerous','Sparkly', 'Boiling', 'Bending', 'Torsion', 'Non-linear', 'Linear', 'Parabolic', 'Hyperbolic', 'Elliptical', 'Conductive', 'Cyclical', 'Sustainable', 'Caffeine-free', 'Deep', 'Improbability', 'Infinite']
	if gadgetType==None or gadgetType == "":
		gadget = ['Gyro', 'Thruster', 'Rocket']
	else:
		gadget = [str(gadgetType)]
	
	names = ['Newton', 'Gauss', 'Euler', 'Kepler', 'Turing', 'Lovelace', 'Hawking','Beeblebrox', 'Izzo', 'Wittig', 'Sapera', 'Baier','Holgersson', 'Selg', 'Wase', 'Brynte', 'Turesson', 'Nystrom']
	nouns = ['Lead', 'Loop', 'Portal', 'Neutron', 'Paper', 'Plasma', 'Solid','Gas','Liquid', 'Fluid', 'Galaxy', 'Star', 'Type-A', 'Type-B', 'Class 1', 'Class 2', 'Candy', 'Sprinkle', 'Hydra', 'Stardust', 'Light', 'Combustion', 'Electron', 'Positron', 'Boson', 'Higgs-Boson', 'Neutrino', 'Tycheon', 'Capacitor', 'Flux', 'Hexa', 'Doca', 'Octa', 'Tetra', 'Yarn', 'Warp', 'Torque', 'Inertia', 'Horizon', 'Laser', 'Core', 'Master', 'Pendulum', 'Chaos']

	inventors = rnd.randint(2,2)
	name = ''
	if(rnd.random()<0.4):
		for inv in range(inventors):
			s = ''
			randtmp = rnd.random()
			if(randtmp <0.1):
				s += names[rnd.randint(0, len(names)-1)]
			elif (randtmp < 0.4):
				s = generateJapaneseishName()
			else:
				s = generateWesternishName(markovChains)
			name += s
			if(inv!=inventors-1):
				name += '-'
		name = rnd.choice(buzzwords) + ' ' + name +' ' + rnd.choice(gadget)
	else:
		name = rnd.choice(buzzwords) + ' ' + rnd.choice(nouns) + ' ' + rnd.choice(gadget)
	return name

def trainMarkovChain():
	file = open('lastnames.txt','r')
	counter0 = 0
	lettersInAlfabet = 26
	markov0 = [0]*lettersInAlfabet
	markov1 = [None]*lettersInAlfabet
	markov2 = [None]*lettersInAlfabet
	for i in range(lettersInAlfabet):
		markov1[i] = [0]*lettersInAlfabet
		markov2[i] = [None]*lettersInAlfabet
		for j in range(lettersInAlfabet):
			markov2[i][j] = [0]*lettersInAlfabet

	#0:th order Markov Chain
	for line in file:
		listarr = line.split(' ')
		name =  list(listarr[0])
		for letter in name:
			markov0[ord(letter)-65] += 1
			counter0 += 1
	for i in range(len(markov0)):
		markov0[i] /= float(counter0)

	#1:st order Markov Chain
	file = open('lastnames.txt','r')
	#counter1 = 0
	for line in file:
		listarr = line.split(' ')
		name = list(listarr[0])
		for l in range(len(name)):
			if(l!=0):
				#counter1 += 1
				markov1[ord(name[l-1])-65][(ord(name[l])-65)] += 1
	for i in range(len(markov1)):
		counter1 = 0
		for j in range(len(markov1[i])):
			counter1 += markov1[i][j]
		for j in range(len(markov1[i])):
			if(counter1 == 0):
				markov1[i][j] = -1
			else:
				markov1[i][j] /= float(counter1)

	#2:nd order Markov Chain
	file = open('lastnames.txt','r')
	counter2 = 0
	for line in file:
		listarr = line.split(' ')
		name = list(listarr[0])
		for l in range(len(name)):
			if(l!=0 and l!=1):
				counter2 += 1
				markov2[ord(name[l-2])-65][(ord(name[l-1])-65)][(ord(name[l])-65)] += 1


	for i in range(len(markov2)):
		for k in range(len(markov2[i])):
			counter2 = 0
			for j in range(len(markov2[i][k])):
				counter2 += markov2[i][k][j]
			for j in range(len(markov2[i][k])):
				if(counter2 == 0):
					markov2[i][k][j] = -1
				else:
					markov2[i][k][j] /= float(counter2)

	return (markov0, markov1, markov2)

def randIdArr(arr):
	if(arr[0] == -1):
		return -1 #This means that we have no information about this case.
	r = rnd.random()
	s = 0
	for i in range(len(arr)):
		s += arr[i]
		if(r<=s):
			return i
	print s
	assert(0)

#Removes some names that look weird
def isShittyName(name, l):
	cons = list('qwrtuipsdfghjklzxcvbnm')
	voul = list('eyuioa')
	namearr = list(name)
	if(l<3):
		return True
	if((namearr[0] in cons) and namearr[0]==namearr[1]):
		return True #I know that double L is a thing. Sorry Spain.
	if((namearr[0] not in voul) and (namearr[1] not in voul)):
		return True #Yeah, sure your name can be Striker or whatever. But a lot of the weird ones had this problem.
	if(namearr[0] == namearr[1]):
		return True #Sure, your name could be Aaronson, but that still looks weird.

	#Count the consonants in a row
	consInRow = 0
	maxConsInRow = 0
	for letter in namearr:
		if(letter in cons):
			consInRow += 1
			if(consInRow>maxConsInRow):
				maxConsInRow = consInRow
		else:
			consInRow = 0
	if(maxConsInRow>3):
		return True #Once again, yeah there are exceptions. Fuck those people.

	#I feel uneasy even writing this list. But it would be nice if someone added more stuff to it. 
	badWords = ['twat', 'cunt', 'fuck', 'nigger', 'shit', 'cock']
	if(name in badWords):
		return True #But then again, these aaare sort of funny.

	return False

def generateFromMarkovChain(markovChains):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	alphabet = list(alphabet)
	N = len(markovChains)
	hasFoundGoodName = False
	while(hasFoundGoodName == False):
		prev = [-1]*N
		l = rnd.randint(4, 9)
		order = 0 # Start at the lowest order
		name = ''
		idx = -2
		for i in range(l):
			while(True):
				if(order==0):
					idx = randIdArr(markovChains[order])
				elif(order == 1):
					idx = randIdArr(markovChains[order][prev[0]])
					assert(prev[0]>=0)
				elif(order == 2):
					idx = randIdArr(markovChains[order][prev[1]][prev[0]])
					assert(prev[0]>=0)
					assert(prev[1]>=0)

				else:
					assert(0)
				if(idx != -1):
					prev[1] = prev[0]
					prev[0] = idx
					break
				else:
					order -= 1
					assert(order>=0)
			if(order<N-1):
				order += 1
			assert(idx>=0)
			name += alphabet[idx]
		if(isShittyName(name,l) == False):
			hasFoundGoodName = True
	return name

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Generates sci-fi sounding names for made up technoligies. E.g. Relativistic Paper Engine, Nystrom-Euler Gun and Wataki-Lovelace Neutron Rocket")
	parser.add_argument('-n', '--num_names',
								type=int, 
							  	default=15,
							  	help='Number of generated names')

	parser.add_argument('-g', '--gadget_type', 
							  	default="Engine",
							  	help='Type of gadget, e.g. Relativistic Paper >>Engine<<. Use -g "" for random gadget type.')

	args = parser.parse_args()
	m =  trainMarkovChain()
	for i in range(args.num_names):
		print generateRandomName(m, args.gadget_type)
