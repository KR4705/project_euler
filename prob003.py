
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

def next_prime(prime):
	next = prime + 1
	while not is_prime(next):
		next = next + 1
	return next


def max_prime_factor(num,p):
	ans = p
	if num == 1:
		return 1
	while (not num == 1):
		is_div = num % p == 0
		while(num % p == 0):
			ans = p	
			num = num / p
		p = next_prime(p)
	return ans
		

# print max_prime_factor(int(number),2)



