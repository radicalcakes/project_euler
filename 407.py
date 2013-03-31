#n = 10000000

"""
If we calculate a2 mod 6 for 0  a  5 we get: 0,1,4,3,4,1.

The largest value of a such that a2  a mod 6 is 4.
Let's call M(n) the largest value of a  n such that a2  a (mod n).
So M(6) = 4.

Find M(n) for 1  n  107.
"""

d = {}

def proc1():
    for i in xrange(1,2500001):
        l = []
        for j in xrange(1,i+1):
            x = (j**2) % i
            if x not in l: l.append(x)
        d[i] = l
    return d



sum = 0
for i in xrange(1,10000000):
    sum += i
    print sum

