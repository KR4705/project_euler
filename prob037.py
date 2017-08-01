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

def series(num):
	array = []
	power = 1
	temp = 10
	while num > temp:
		temp = 10**power
		array.append(num%temp)
		array.append(num/temp)
		power += 1
	array.pop()
	return array
num = 11
array = []
while len(array) < 11:
	tag = True
	for each in series(num):
		if not is_prime(each):
			tag = False
	if tag:
		array.append(num)
	num += 2

	
answer = 0
for each in array:
	answer += each
print answer
