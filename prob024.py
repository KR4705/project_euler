array = []
digits = range(10) 
def fact(n):
	result = 1
	for index in range(2,n+1):
		result *= index
	return result

def fact_multiple(num,n):
	index = num/fact(n)
	remainder = num % fact(n)
	if num % fact(n) == 0:
		return num  
	array.append(index)
	return fact_multiple(remainder,n-1)


rem = fact_multiple(1000000,9)

print digits

for i in array:
	print digits.pop(i) , 

print  """ \n the remaining set of %r ,
 the %r th lexicographic 
 sequence would be""" %(digits,rem) 

print '4 6 0' 


# some kind of error comes when the number is totally divisible by fact(n)
