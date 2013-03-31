def palindrome():
    for i in range(100,1000):
        for j in range(100,1000):
	    if str(i * j) == str(i * j)[::-1]:
	        print str(i*j)[::-1], i, j

print palindrome()


