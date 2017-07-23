import prob003
import time

n = 20
prime = 2
total = 1 
t0 = time.time()
while prime < n:
	power = 0
	while prime**(power+1) < n+1:
		power += 1
	total *= prime**power
	prime = prob003.next_prime(prime)
runtime = time.time() - t0
print total,"in time: %r" % runtime


