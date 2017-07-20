prev1 = 1
prev2 = 2
total = 2
x = 0
while(x < 4000000):
    x = prev1 + prev2
    prev1 = prev2
    prev2 = x
    if x%2 ==0:
        total += x
    print prev1

print total
