import prob3
n = 0
answer = 1
while(n < 10001):
	n = n+1
	answer = prob3.next_prime(answer)
print answer