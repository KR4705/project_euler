def rem(n):
	array = []
	num = 1
	while num not in array:
		array.append(num)
		num = (num*10 % n)
	return array ,array.index(num)

def no_of_digits(n):
	remainder_list,repeat_index = rem(n)
	if remainder_list[-1] == 0:
		return 0
	else:
		return len(remainder_list) - repeat_index


ans = 1
limit = 0		
for i in range(1,1000):
	number = no_of_digits(i)
	if number > limit:
		limit = number
		ans = i
	else:
		pass	
print ans











