import prob003
import time
start = time.time()
n = 0
answer = 1
while(n < 10001):
	n = n+1
	answer = prob003.next_prime(answer)
runtime = time.time() - start
print answer,"runtime: %rms" % (runtime*1000)