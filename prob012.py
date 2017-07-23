import time

# this no_divisiors is not exactly number of divisors of num
# this is made for this program 
# this omits one 2 from the factors because n*(n+1)/2
# assuming one of n and n+1 is divisible by 2
# cheated on this problem
def no_divisors(num):
	power = 0
	if num % 2 == 0: 
		num = num/2
	divisors = 1
	while not num & 1:
		power += 1
		num /= 2
	divisors = divisors * (power + 1)
	p = 3
	while num != 1:
		power = 0
		while num % p == 0:
			power += 1
			num /= p
		divisors = divisors * (power + 1)
		p += 2
	return divisors

# efficient way of looping though for divisors 
# not by finding next prime but realizing that
# all primes below it are already covered 
# because of the loop from below to top
# 

def find_index(num):
	n = 1
	lnum , rnum = no_divisors(n),no_divisors(n+1)
	while lnum * rnum < num:
		n += 1
		lnum,rnum = rnum,no_divisors(n+1)
	return n
start = time.time()
n = find_index(500)
triangle =  n*(n+1)/2
runtime = time.time() - start
print triangle,"runtime: %rs" % runtime

