import time
start = time.time()

len_digits = [0,3,3,5,4,4,3,5,5,4] # 0-9
len_10_19 = [3,6,6,8,8,7,7,9,8,8] #10-19
len_10x = [0,3,6,6,5,5,5,7,6,6] # 10*[0-9]

array1 = []
array1.extend(len_digits)
array1.extend(len_10_19)
for i in range(2,len(len_10x)):
	for j in len_digits:
		array1.append(len_10x[i] + j)
array = []
array.extend(array1)
for i in range(1,10):
	for j in array1:
		if j == 0:
			array.append(len_digits[i] + 7)
		else :
			array.append(len_digits[i] + 7 + 3 + j)

answer = 0
for i in array:
	answer += i
runtime = time.time() - start
answer += 11
print answer  ,  "runtime: %r" % runtime











# although the below version works its much slower 

# def length(num):
# 	if num == 1000:
# 		return 11
# 	elif num >= 100:
# 		if num % 100 == 0:
# 			return len_digits[num/100] + 7
# 		else: 
# 			return len_digits[num/100] + 10 + length(num%100)
# 	elif num >= 20:
# 		return len_10x[num/10] + len_digits[num%10]
# 	elif num >= 10:
# 		return len_10_19[num%10]
# 	else:
# 		return len_digits[num]


# start = time.time()
# answer = 0
# for i in range(1,1001):
# 	answer += length(i)
# 	runtime = time.time() - start
# print answer ,  "runtime: %r" % runtime





# the below is reverse loop of above slower than below

 # 	if num < 10:
	# 	return len_digits[num]
	# elif num < 20:
	# 	return len_10_19[num%10]
	# elif num < 100:
	# 	return len_10x[num/10] + len_digits[num%10]
	# elif num < 1000:
	# 	if num % 100 == 0:
	# 		return len_digits[num/100] + 7
	# 	else: 
	# 		return len_digits[num/100] + 10 + length(num%100)
	# else:
	# 	return 11 
