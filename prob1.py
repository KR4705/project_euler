i = 0
sum = 0
while 3*i < 1000:
    sum += 3 * i
    i += 1
i = 0
while 5*i < 1000:
    if not 5*i % 3 == 0:
        sum += 5*i
    i += 1

print sum
    
