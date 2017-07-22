
def is_palindrome(arg):
	arg = str(arg)
	if len(arg) == 1 or len(arg) == 0: 
		return True
	elif arg[0] == arg[len(arg)-1]:
		return is_palindrome(arg[1:len(arg)-1])
	else:
		return False 


def reverse(num):
	reverse = 0
	while num > 0:
		reverse = 10*reverse + num % 10
		num = num/10
	return reverse

# def is_palindrome(num):
# 	return num == reverse(num)

def is_factorizable(num):
	factor1 = 999
	while not num % factor1 == 0:
		factor1 -= 1
	factor2 = num/factor1
	if factor2 < 1000 and factor2 > 100:
		return True
	else:
		return False
	

	
	
for i in range(999999,100001,-1):
	if is_palindrome(i):
		if is_factorizable(i):
			print i
			break

#my solution is better in terms of cheking for is_palindrome 
# mine has no extra checks and goes from top to low and stops 
# after finding the maximum



