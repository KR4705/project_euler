import time
start = time.time()
names_str = open("prob022_names.txt").read()
names_list = names_str.split("\",\"")
names_list[0] = names_list[0][1:]
names_list[-1] = names_list[-1][0:-1] 
names_list.sort()
letters_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
letter_value = dict(zip(letters_list,range(1,27)))


def value(name):
	value = 0
	for letter in name:
		value += letter_value[letter]
	return value 
total = 0
for each in names_list:
	total += (names_list.index(each) + 1)*value(each)
runtime = time.time() - start

print total , "runtime: %r" % runtime
