import prob003
import time
start = time.time()
total = 0
prime = 2
while prime < 2000000:
	total += prime
	prime = prob003.next_prime(prime)
runtime = time.time() - start
print total,"runtime: %rs" % runtime