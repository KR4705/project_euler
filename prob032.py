# let the form which satisfies be of for x * y = z
# by no loss we can assume x < y < z
# since , sum of all digits in x y z == 9
# consider digits of x = 1 y = 4 and z = 4 
# 1,3,5 not possible
# 2,2,5 not possible  
# if digits of x = 2 y = 3 and z = 4
# consider digits of x = 3 y = 3 and z = 3  impossible by intuition
# so we need to see for two cases 
# 1,4,4 and 2,3,4
# case 1
# digits of x,y,z = 1,4,4

# helping function

def digits_set(num):
	array = []
	while num > 0:
		array.append(num%10)
		num /= 10
	set_array = set(array)
	if len(set_array) == len(array):	
		return set(array)
	else :
		return None


def make_num(*args):
	if len(args) == 2:
		a,b = args
		return a*10 + b
	elif len(args) == 3:
		a,b,c = args
		return a*100 + b*10 + c 
	elif len(args) == 4:
		a,b,c,d = args
		return a*(10**3) + b*(10**2) + c*10 + d
	else:
		a, = args
		return a




def case2():
	answer = []
	digits = (range(1,10))
	for x1 in digits:
		rest_digits1 = list(set(digits) - {x1})
		for x2 in rest_digits1:
			rest_digits2 = list(set(rest_digits1) - {x2})
			for y1 in rest_digits2:
				rest_digits3 = list(set(rest_digits2)- {y1})
				for y2 in rest_digits3:
					rest_digits4 = list(set(rest_digits3) - {y2})
					for y3 in rest_digits4:
						rest_digits_end = list(set(rest_digits4) - {y3})
						# case2
						temp2 = make_num(y1,y2,y3)
						temp1 = make_num(x1,x2)
						lhs =  temp1* temp2
						if digits_set(lhs) == set(rest_digits_end):
							answer.append([temp1,temp2,lhs])
						# case1
						temp1 = make_num(x1)
						temp2 = make_num(x2,y1,y2,y3)
						lhs = temp1*temp2	
						if digits_set(lhs) == set(rest_digits_end):
							answer.append([temp1,temp2,lhs])
	return answer

set_of_solutions = case2()


answer_set = set([])
for item in set_of_solutions:
	print item
 	answer_set.add(item[2])

answer = 0
for item in list(answer_set):
	answer += item

print answer




