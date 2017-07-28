# there is a pattern for the rhs top most diagnal for every box
# it will be the square of the side of that boxx
# for 5x5 it is 25 and for 3x3 is 9
# so the righttop would be n^2
# left top would be n^2 - n + 1
# and the prev in squence would be 
# getting corners of each box if size n


def corners(n):
	temp = n*n
	rt = temp
	lt = temp - n +1
	lb = lt - n +1
	rb = lb - n + 1
	return rt+lt+lb+rb
answer = 1
# should decrease the n by 2 from pattern itself
for n in range(1001,1,-2):
	answer += corners(n)

print answer 


