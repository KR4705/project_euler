# recreated
def is_pandigital(num):
	string = str(num)
	n = len(string)
	return  not '123456789'[:n].strip(string)

def is_prime(num):
	if num == 1:
		return False
	elif num == 2:
		return True
	elif num % 2 == 0 :
		return False
	else :
		for factor in range(3,int(num**0.5)+1,2):
			if num % factor == 0 :
				return False
		return True 

def max_n_digit(n):
	array = []
	lower,upper = '',''
	for i in range(1,n+1):
		lower = lower + str(i)
	for i in reversed(lower):
		upper = upper + i
	upper = int(upper)
	lower = int(lower)
	for each in range(upper,lower,-2):
		if is_pandigital(each) and is_prime(each):
			return each



# Note: Nine numbers cannot be done (1+2+3+4+5+6+7+8+9=45 => always dividable by 3)
# Note: Eight numbers cannot be done (1+2+3+4+5+6+7+8=36 => always dividable by 3)
for n in range(7,2,-1):
	test = max_n_digit(n)
	if test:
		print test
		break
