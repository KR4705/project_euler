def fib(num1,num2):
	while True:
		total = num1 + num2
		yield num2,total
		num1,num2 = num2,total

def no_digits(num):
	ans = 0
	while num > 0:
		ans,num = ans + 1,num / 10
	return ans

a = 1
b = 1
index = 2
while no_digits(b) < 1000:
	a,b = fib(a,b).next()
	index += 1
ans = index

print ans


