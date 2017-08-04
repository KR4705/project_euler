# brute force starting with permutations with 
# array = [1,0,2,3,4,5,6,7,8,9]


from itertools import permutations

array = range(9,1,-1)
array.append(0)
array.append(1)
array = list(reversed(array))

divisors = [1,2,3,5,7,11,13,17]
answer = 0
count = 1
limit = 3265920

for array in permutations(array):
	if count < limit:
		divisible = True
		for i in range(1,len(divisors)):
			num = 100*array[i] + 10*array[i+1] +array[i+2]
			if not num % divisors[i] == 0 :
				divisible = False
				break
		if divisible:
			temp = []
			for each in array:
				temp.append(str(each))
			num = ''.join(temp)
			answer += int(num)
		count += 1
	else:
		break

print answer