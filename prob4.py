import prob3

def is_palindrome(arg):
	arg = str(arg)
	if len(arg) == 1 or len(arg) == 0: 
		return True
	elif arg[0] == arg[len(arg)-1]:
		return is_palindrome(arg[1:len(arg)-1])
	else:
		return False 

for i in range(999999,100001,-1):
	if is_palindrome(i):
		print i

def length(num):
	return len(str(num))

def max_factor(num):
	factor1 = 1
	factor2 = num
	while(not length(factor1) == 3 && length(
	
	




