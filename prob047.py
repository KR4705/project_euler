# copied this factor algo 
# my factor algo taking too long 
def factor(n):
    f, factors, prime_gaps = 1, [], [2, 4, 2, 4, 6, 2, 6, 4]
    if n < 1:
        return []
    while True:
        for gap in ([1, 1, 2, 2, 4] if f < 11 else prime_gaps):
            f += gap
            if f * f > n:  # If f > sqrt(n)
                if n == 1:
                    return factors
                else:
                    return factors + [(n, 1)]
            if not n % f:
                e = 1
                n //= f
                while not n % f:
                    n //= f
                    e += 1
                factors.append((f, e))


i = 2*3*5*7
count = 1
while not count == 4 :
	i += 1
	if len(factor(i)) == 4: count += 1
	else: count = 0
print i-3


