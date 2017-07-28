powers = []
for i in range(10):
	powers.append(i**5)

def sum_of(num):
	total = 0
	while num > 0:
		rem = num%10
		total += powers[rem]
		num /= 10
	return total

answers = []
# found that the converging point of 10**n and (9**5)*n is between 6 and 7
# we get this limit of 6
max_range = 10**6
for i in range(1,max_range):
	if sum_of(i) == i:
		answers.append(i)

answer = -1
for i in answers:
	answer += i
print answer
