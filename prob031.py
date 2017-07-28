answer = 8
# using one type coin only has 8 cases
for g in range(2):
	for f in range(4):
		for e in range(10):
			for d in range(20):
				for c in range(40):
					for b in range(100):
						value = 2*b + 5*c + 10*d + 20*e + 50*f + 100*g  
						if value <= 200:
							answer += 1
# added all other possible cases but 
# we didnt exclude the case of using only 1p coins
answer -= 1
print answer