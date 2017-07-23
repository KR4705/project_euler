import time
# for 20x20 lattice
# no of points = 21X21
start = time.time()
n = 21  # sides+1
# initialize the routes array
routes = []
for i in range(n):
	routes.append([])
	for j in range(n):
		routes[i].append(None)
def num_routes(i,j):
	# base case
	if i == n-1 or j == n-1: 
		# making sure no overwriting  
		if routes[i][j] == None:
			routes[i][j] = 1
			routes[j][i] = 1
		return 1
	# recurrsion
	if routes[i][j] == None:
		sum = num_routes(i,j+1) + num_routes(i+1,j)
		routes[i][j] = sum
		routes[j][i] = sum
		return sum
	# from the array
	return routes[i][j]
def print_routes():
	for i in routes:
		print i
answer = num_routes(0,0)
runtime = time.time() - start
print answer , "runtime: %r" % runtime



