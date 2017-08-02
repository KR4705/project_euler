import time
start = time.time()

squares = []
for a in range(0,1000):
	squares.append(a*a)

def triads(perimeter):
	count = 0
	for a in range(1,perimeter-2):
		for b in range(a,perimeter-a-1):
			c = perimeter-a-b
			if squares[a] + squares[b] == squares[c]:
				count += 1
	return count

answer = 0
maximum = 0
for perimeter in range(1,1001):
	num = triads(perimeter)
	if num > maximum:
		maximum = num
		answer = perimeter

runtime = time.time() - start
print answer,runtime