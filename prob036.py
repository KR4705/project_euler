
# returns binary in reverse
	
class Number(object):
	def __init__(self,num):
		self.value = num
		self.binary = None

	def is_pali(self):
		arg = list(str(self.value))
		return list(reversed(arg)) == arg

	def is_binary_pali(self):
		array = []
		num = self.value
		while num > 0:
			array.append(num%2)
			num /= 2
		self.binary = list(reversed(array))
		return array == list(reversed(array))

answer = 0

for i in range(1,1000000,2):
	num = Number(i)
	if num.is_pali() and num.is_binary_pali():
		print num.value,num.binary
		answer += num.value 

print answer






