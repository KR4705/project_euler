def is_triangle(num):
	n = (0.25+2*num)**0.5 - 0.5
	return n == int(n)

alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
db = dict(zip(alphabets,range(1,27))) 

def value(string):
	total = 0
	for each in string:
		total +=  db.get(each)
	return total


all_the_names = open("prob042_words.txt").read()
names_array = all_the_names.split('","')

names_array[0] = names_array[0][1:]
names_array[-1] = names_array[-1][:-1]



count = 0
for each in names_array:
	if is_triangle(value(each)):
		count += 1

print count