# gen ab/cd
# gen next of ab

def check(a,b,c):
	# cases 
	values = []
	values.append((a*10.0 + b) /(b*10+c))
	values.append((a*10.0 + b)/(b + 10*c))
	values.append((a + b*10.0)/(b*10+c))
	values.append((a + b*10.0)/(b+ 10*c))

	for each in values:
		if (a*1.0)/c == each:
			return values.index(each)
		else :
			pass
	return None

array = []
for c in range(1,10):
	for a in range(1,10):
		for b in range(1,10):
			temp = check(a,b,c)
			if temp and not a == c:
				array.append([[a,b,c],temp])

denominators = []
numerators = []
answer = 1
for each in array:
	a = each[0][0]
	c = each[0][2]
	denominators.append(a)
	numerators.append(c)


for each in denominators:
	answer *= (each*1.0)

for each in numerators:
	answer /= each

print int(answer)