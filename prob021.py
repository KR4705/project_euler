import time
end = 10000
start = time.time()
# init the sum_of_factors array
sum_factors = []
for i in range(10001):
	sum_factors.append(None)
sum_factors[0] = 0
sum_factors[1] = 0 
sum_factors[2] = 1

def sum_of_factors(n):	
	total = 1
	for factor in range(2,n):
		if n % factor == 0: 
			total += factor 
	sum_factors[n] = total
	return total
# filling up the array 
for index in range(3,10001):
	sum_of_factors(index)

answer = 0 
for i in range(len(sum_factors)):
	sum_fact_i = sum_factors[i]
	if sum_fact_i > 9999 :
		continue 
	else :
		# if a and b are amicable
		# not a == b
		# b == f(a)
		# and f(b) = a 
		if (not sum_fact_i == i) and sum_factors[sum_fact_i] == i:
			answer += i


runtime = time.time() - start
print answer , runtime




