import time

def fact(n):
	result = 1
	for index in range(2,n+1,1):
		result *= index
	return result

start = time.time()
num = fact(100)	

answer = 0
while num > 10:
	answer,num = answer+num%10,num/10
answer += num
runtime = time.time() - start
print answer,"runtime: %rms" % (runtime*1000)

