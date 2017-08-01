def digits(num):
	array = []
	while num > 0:
		array.append(num%10)
		num /= 10
	return list(reversed(array))

def make_num(array):
	rev_array = list(reversed(array))
	power = 0
	value = 0
	for each in rev_array:
		value += each*(10**power)
		power += 1
	return value

def cycle(array):
	cycle_list = []
	# cycle 1
	for i in range(len(array)):
		x = array.pop(0)
		array.append(x)
		cycle_list.append(make_num(array))
	return cycle_list

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

# the algo runs repetitive 
# not very efficient

array_of_primes = [2]
for num in range(3,1000000,2):
	if is_prime(num):
		is_cycle = True
		prime_cycle = cycle(digits(num))
		for each in prime_cycle:
			if is_prime(each):
				pass
			else:
				is_cycle = False
		if is_cycle:
			print num
			array_of_primes.append(num)

print array_of_primes,len(array_of_primes)



