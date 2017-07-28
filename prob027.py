# b must be a prime for n == 0 
# possible values of b must be from set of primes

primes = []

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
for n in range(1,1000):
	if is_prime(n):
		primes.append(n)

# for a value of n the quadratic to be prime 
# n**2 + n*a + b should be prime

# using lambda function i have defined it
def func(a,b):
	return lambda n : n**2 + n*a + b

def prime_till(a,b):
	quad = func(a,b)
	n = 0
	value = b
	while is_prime(value):
		n += 1
		value = quad(n)
	return n - 1
limit = 0
ans = 1
for b in primes:
	for a in range(-999,1000,1):
		number  = prime_till(a,b)
		if number > limit :
			ans = a*b
			limit = number

print ans



