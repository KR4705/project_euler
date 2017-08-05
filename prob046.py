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

def possible(num):
	for i in range(3,num,2):
		x = ((num-i)/2)**0.5
		if int(x) == x and is_prime(i):
			return True
	if is_prime(num):
		return True
	else:
		return False


index = 2
found = False
while not found:
	if not possible(index):
		found = True
		answer = index
	index += 1

print answer


