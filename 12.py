from proj import factors

def PE12():
    s = 0
    for i in range(250000,100000000):
        s += i
        if len(factors(s)) >= 500:
            return s

print PE12()
