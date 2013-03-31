def newton_sqrt(n):
    x = n
    g = 1.0
    eps = 0.0001
    if n == 1:
        return 1
    while abs(x**2 - n) >= eps:
        g = (n/g)
   	x = (x+g) / 2
	print x
        g = x
    return x


def newt_cube(n):
    x = n
    g = 1.0
    eps = 0.0001
    if n == 1:
        return 1
    while abs(x**3 - n) >= eps:
        x = ((2*g))
	g = (x+(n/g**2))/3.0
	x = g
    return x

print newt_cube(1232342)
        
     
