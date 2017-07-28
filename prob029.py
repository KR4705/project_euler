numbers = set()
for a in range(2,101):
	for b in range(2,101):
		numbers.add(a**b)
array = list(numbers)
array.sort()
print len(array)
