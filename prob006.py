# using expansion of (a+b+c+...)**2
import time

n = 100
sum_n = n*(n+1)/2
total = 0
t0 = time.time()
for i in range(1,101,1):
	total = total + i*(sum_n - i)
runtime = time.time() - t0
print total,"in time: %r" % runtime

