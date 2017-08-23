# brute force
def is_pentagonal(num):
	x = (1+(1+24*num)**0.5)/6
	return x == int(x)

n = 2
found = False
while not found:
	num1 = n*(3*n-1)/2
	for j in reversed(range(1,n)):
		num2 = j*(3*j-1)/2
		add = (num1+num2)
		diff = (num1-num2)
		if is_pentagonal(add) and is_pentagonal(diff):
			print n,j,diff
			found = True
	n += 1		

# since its taking long time to find the second result
# i try the first one.
# and it is the answer.
		
