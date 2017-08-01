fact_values = [1]
value = 1
for each in range(1,10):
	value *= each
	fact_values.append(value)

# from fact_values we see that 9! has value 362880 which is 6 digit number
# consider we have six digit number if we add one more digit to it 
# the sum of fact of its digits can be raised to max of 362880 
# which is 6 digits so sum of this can go upto 7 digits 
# if we add one more digit we add max of 362880
# but the sum of fact will not go to a 8 digit number
# so 7 is the limit of the max number of digits
# also a max of 9!*5 is possible

array = []
limit = fact_values[9]*7 + 1
for i in range(3,limit):
	temp = i
	total = 0
	while temp >= 10:
		total += fact_values[temp%10]
		temp /= 10
	total += fact_values[temp]
 	if total == i:
 		array.append(i)

answer = 0
for each in array:
	answer += each

print answer





