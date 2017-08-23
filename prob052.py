# cannot start num with 0
def permute(u,v):
	digits = [0]*10
	while u > 0:
		digits[u%10] += 1
		u /= 10
	while v > 0:
		digits[v%10] -= 1
		v /= 10
	for each in digits:
		if not each == 0:
			return False
	return True

num = 0
x = 0
found = False
while not found:
	num += 1
	for i in range(2,7):
		if permute(num,num*i):
			x = i
		else:
			break
	if x == 6 :
		answer = num 
		break		

for i in range(1,7):
	print answer*i






