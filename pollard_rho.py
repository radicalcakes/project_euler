import random, math
from fractions import gcd

def pollard_rho(n):
    if n % 2 ==0:
        return 2
    x  = random.randint(1, n-1)
    y = x
    c = random.randint(1, n-1)
    g = 1
    while g == 1:
        x = ((x*x)%n+c)%n
	y = ((y*y)%n+c)%n
	y = ((y*y)%n+c)%n
	g = gcd(abs(x-y),n)
	return g

print pollard_rho(13195)
