import time

start = time.time()
prev1 = 1
prev2 = 2
total = 2
x = 0
while(x < 4000000):
    x = prev1 + prev2
    prev1 , prev2 = prev2,x
    if not x & 1:
        total += x
period = time.time() - start
print total,"in time:%r" % period
