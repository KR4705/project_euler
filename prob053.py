limit = 1000000
def fact(num):
	total = 1
	for i in range(num,1,-1):
		total *= i
	return total

def top(n,r):
	total = 1
	for i in range(n-r+1,n+1):
		total *= i
	return total

def ncr(n,r):
	total = top(n,r)/fact(r)
	return total

def no(n):
	total = 0
	if n % 2 == 0:
		if ncr(n,n/2) < limit:
			return total
		else:	
			for i in range(1,n/2+1):
				if ncr(n,i) > limit:
					total = 2*(n/2 - i) + 1
					return total
	else:
		if ncr(n,n/2) < limit:
			return total
		else:
			for i in range(1,n/2+1):
				if ncr(n,i) > limit:
					total = 2*(n/2 - i + 1)
					return total

total = 0
for i in range(23,101):
	total += no(i)
print total
 

