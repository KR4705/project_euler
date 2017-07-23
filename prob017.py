import time

len_digits = [0,3,3,5,4,4,3,5,5,4] # 0-9
len_10_19 = [3,6,6,8,8,7,7,9,9,8] #10-19
len_10x = [0,3,6,6,5,5,5,7,7,6] # 10*[1-9]

def length(num):
	if num == 1000:
		return 11 
	elif num > 100:
		if num%100 == 0:
			return len_digits[num/100] + 7
		else:
			return len_digits[num/100] + 10 + length(num%100)
		# x_hds and x_ties or digits
	elif num == 100:
		return 10
	elif num >= 20:
		return len_10x[num/10] + len_digits[num%10]
	elif num >= 10: 
		return len_10_19[num%10] 
	else:
		return len_digits[num]

# start = time.time()
# answer = 0
# for i in range(1,1001):
# 	answer += length(i)
# runtime = time.time() - start
# print answer ,  "runtime: %r" % runtime


print length(1000)



