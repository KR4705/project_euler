def is_triangle(num):
	n = (0.25+2*num)**0.5 - 0.5
	return n == int(n)
def is_pentagonal(num):
	x = (1+(1+24*num)**0.5)/6
	return x == int(x)

count = 0
i = 1
answer = 0
while count <= 2: #because 1 is also an answer
	x = i*(2*i-1) #generating a hexagonal number with index i
	if is_pentagonal(x) and is_triangle(x):
		count += 1
		answer = x
	i += 1

print answer
