
import time
def len_chain(num):
	count = 0
	while not num == 1:
		if not num & 1:
			num = num/2
		else :
			num = 3*num +1
		count += 1
	return count


start = time.time()
n = 1000000
max_chain = 0
while n > 2**19: # this limit i understood from parity view 
	length = len_chain(n)
	if length > max_chain:
		max_chain = length
		answer = n
	n -= 1
runtime = time.time() - start
print answer,"with chain length: %r  and in time: %rs" %(max_chain,runtime)	

