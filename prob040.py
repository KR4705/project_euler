limit = 10**6+1

string = '0'
i = 1
while len(string) < limit:
	string = string + str(i)
	i += 1
answer = 1
for i in range(7):
	answer *= int(string[10**i])

print answer
