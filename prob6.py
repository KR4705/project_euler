# using expansion of (a+b+c+...)**2

n = 100
sum_n = n*(n+1)/2
total = 0

for i in range(1,101,1):
	total = total + i*(sum_n - i)

print total 

