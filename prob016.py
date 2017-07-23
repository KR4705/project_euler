import time
n = 2**1000
n_str = str(n)
answer = 0
start = time.time()
while not n == 0:
	answer  += n % 10
	n = n / 10
runtime = time.time() - start
print answer ,"runtime: %r" % runtime

# string functions are much slower 
# compared to the number calculations
