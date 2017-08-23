limit = 1000000

def binary(array,num):
	n = len(array)/2
	temp = array[n]
	if temp == num:
		return True
	elif n == 0 :
		return False
	elif temp > num:
		return binary(array[n:],num)
	else:
		return binary(array[:n],num)

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


primes_sum = [0,2]
for i in xrange(3,limit,2):
	# need to find why this is the limit
	# if not for this limit need more computations
	if primes_sum[-1] > limit:break 
	if is_prime(i): primes_sum.append(primes_sum[-1] + i)
c = len(primes_sum)
no_primes = 0

for i in xrange(c): 
	for j in xrange(c-1,i+no_primes,-1):
		temp = primes_sum[j] - primes_sum[i]
		if temp > limit: 
			continue
		elif j-i > no_primes and is_prime(temp): 
			no_primes = j-i
			answer = temp
			break

print no_primes,answer




