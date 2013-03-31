#bruted
def greatest_prime(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    #c STarts after 1
    i = 2
    while i <= n**0.5:
        if n % i == 0:
	    n /= i
	   # print i 
	else:
	    #i is supposed to increment to highest? check
	    i += 1
    return n
    # by this point, n will be the greatest prime facctor, hence the return

x = int(raw_input("Enter int to find greatest prime factor: "))

print greatest_prime(x)


