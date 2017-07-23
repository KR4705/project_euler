import time

start = time.time()
n = 1000
for a in range(1,n,1):
	for b in range(a+1,n-a-1,1):
		c = n-a-b
		if c**2 == a**2 + b**2:
			print a,b,c
			runtime = time.time() - start
			answer = a*b*c
			print "product:",answer,"runtime: %rms" % (runtime*1000)

