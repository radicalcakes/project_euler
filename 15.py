#(m + n)!/(m! * n!) 20 X 20

from math import factorial
def PE15(m,n):
    x = (factorial(m+n))/(factorial(m) * factorial(n))
    return x


print PE15(20,20)
