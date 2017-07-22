import prob3
total = 0
prime = 2
while prime < 2000000:
	total += prime
	prime = prob3.next_prime(prime)
print total