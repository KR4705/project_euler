all_pairs = open("prob054_poker.txt").read()
single_pairs = all_pairs.splitlines()

value_card = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']


def is_flush(array):
	temp = array[0][1]
	for each in array:
		if not each[1] == temp:
			return False
	return True 

def is_3kind(array):
	temp = []
	for each in array:
		temp.append(each[0])
	for each in set(temp):
		if temp.count(each) == 3:
			return True
	return False

def is_2pair(array):
	count = 0
	temp = []
	for each in array:
		temp.append(each[0])
	for each in set(temp):
		if temp.count(each) == 2 and temp.count(each) < 3:
			count += 1
		else:
			return False
	if count == 2 :
		return True
	else: 
		return False

def is_pair(array):
	count = 0
	temp = []
	for each in array:
		temp.append(each[0])
	if len(set(temp)) == 4:
		return True
	else:
		return False

def is_4kind(array):
	temp = []
	for each in array:
		temp.append(each[0])
	for each in temp[:1]:
		if temp.count(each) == 4:
			return True
	return False

def is_fhouse(array):
	temp = []
	for each in array:
		temp.append(each[0])
	for each in set(temp):
		if not temp.count(each) in [2,3]:
			return False
	return True


class Pair(object):

	def __init__(self,string):
		array = string.split(' ')
		self.player1 = array[:5]
		self.player2 = array[5:]

	def winner(self):
		pass

	def __str__(self):
		return 'player1: '+ str(self.player1) + '\n' + 'player2: '+str(self.player2)



for each in single_pairs:
	x = Pair(each)
	if is_flush(x.player2) :
		print x.player2
