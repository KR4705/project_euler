import time
start = time.time()
# using recurssion
input_string="""
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
string_array = []
temp = input_string.split("\n")
temp.pop(0)
for row in temp:
	string_array.append(row.split(" "))

# converting the string array to number array
array = []
for row in string_array:
	array.append([])
	for num in row:
		array[-1].append(int(num))

# deleting string_array
del string_array

# initializing path_array which stores the path value of each node
path_array = []
for row in array:
	path_array.append([])
	for num in row:
		path_array[-1].append(None)


row_end = len(array) - 1
def path_sum(i,j):
	if i == row_end - 1:
		path = array[i][j] + max(array[i+1][j],array[i+1][j+1])
		path_array[i][j] = path
		return path
	elif path_array[i][j] == None:
		path = array[i][j] + max(path_sum(i+1,j),path_sum(i+1,j+1))
		path_array[i][j] = path
		return path
	else:
		return path_array[i][j]
path_sum(0,0)
runtime = time.time() - start
print path_array[0][0] , "runtime: %rms" % (runtime*1000) 
