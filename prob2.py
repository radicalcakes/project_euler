c,a,b = 0,0,1
while a < 4000001:
    if a % 2 == 0:
    	c+=a
    a,b = b,a+b
print c
