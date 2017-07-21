import prob3

n = 20
prime = 2
total = 1 

while prime < n:
	power = 0
	while prime**(power+1) < n+1:
		power += 1
	total *= prime**power
	prime = prob3.next_prime(prime)
print total


