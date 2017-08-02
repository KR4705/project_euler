# need to find largest pandigital product 
# pan = num x (1,2,3,....)
# given for num = 9 
# pan = 918273645
# since 918273645 is not answer 
# we have our ans > pan
# so we have our ans starting with 9
# so our num starts with 9
# if num is single digit 9 didnt give us the max answer
# for two digit number
# 91 to 98 ;99 not possible

# cheated
# takes string input and checks if it is pandigital
def is_pandigital(string):
	return len(string) == 9 and not '123456789'.strip(string)

def two_digits():
	array = []
	for i in range(91,99):
		count = i
		string = ''
		while len(string) < 9:
			string = string + str(count)
			count += i
		print string
		if len(string) == 9 and is_pandigital(string):
			array.append(i)
	return array

# we can see that there are no two digit numbers for which a pandigital
# number is formed

# checking three digit numbers:
# possible values for num is 9123 to 9876

def three_digits():
	array = []
	for i in range(912,988):
		count = i
		string = ''
		while len(string) < 9:
			string = string + str(count)
			count += i
		if len(string) == 9 and is_pandigital(string):
			array.append(string)
	return array


def four_digits():
	array = []
	for i in range(9123,9877):
		count = i
		string = ''
		while len(string) < 9:
			string = string + str(count)
			count += i
		if len(string) == 9 and is_pandigital(string):
			array.append(string)
	return array


# 5 digits is not possible for num
array = ['918273645']
array.extend(two_digits())
array.extend(three_digits())
array.extend(four_digits())

maximum = 0
for each in array:
	maximum = max(each,maximum)
print array
print maximum

