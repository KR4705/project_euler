from itertools import permutations


def is_prime(n):
	if n < 2:
		return False
	if n == 2:
		return True
	if not n & 1:
		return False
	for	x in range(3,int(n**0.5)+1,2):
		if n % x == 0:
			return False
	return True

def make_set(num):
	fourth = num% 10
	num = num/10
	third = num%10
	num /= 10
	second = num%10
	num /= 10
	first = num %10
	return first,second,third,fourth	

def run():
	for start in range(1001,10000,2):
		if is_prime(start):
			for diff in range(2,10000-start,2):
				middle,end = start+diff,start+2*diff
				middle_set,end_set = make_set(middle),make_set(end)
				possible_set  = list(permutations(make_set(start)))
				if middle_set in possible_set and end_set in possible_set:
					if is_prime(middle) and is_prime(end) and end < 10000:
						if not start == 1487: 
							print str(start)+str(middle)+str(end)
							return 

run()
