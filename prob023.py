def sum_of_factors(n):	
	total = 1
	for factor in range(2,int(n**(0.5))+1):
		if n % factor == 0: 
			total += factor
			factor_alt = n / factor
			if not factor_alt == factor:
				total += factor_alt  
	return total

limit = 28123
def abun_num_next(num):
	num += 1
	while True:
		if sum_of_factors(num) > num:
			yield num
		else :
			num += 1

def abun_num_prev(num):
	num -= 1
	while True:
		if sum_of_factors(num) > num:
			yield num
		else :
			num -= 1 
num = 1
array = []
while num < 28123 - 11:
	temp = abun_num_next(num).next()
	array.append(temp)
	num = temp

 # used sets difference 
 # tried using iteration had some errors
can_list = set([i+j for i in array for j in array if i <= j and i+j <= limit])
cannot_list = set(range(1,limit)) - can_list
answer = 0
for i in cannot_list:
	answer += i

print answer





