import prob3


# too many iterations 
# needs better method
def no_divisors(num,prime):
	if num < prime:
		return 1
	if num == prime:
		# print prime,1
		return 2
	power = 0
	while num % prime == 0:
		power += 1
		num = num/prime
	# print prime,power
	return (power + 1)*no_divisors(num,prob3.next_prime(prime))


i = 9000
divisors = 1
while(divisors < 500):
	number = i * (i+1) / 2
	divisors = no_divisors(number,2)
	i += 1
	print i,divisors 
print number

# print no_divisors(10000,2)
