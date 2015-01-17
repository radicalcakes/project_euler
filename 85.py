from proj import comb_rect

stop = 2000000
l = {}
def euler85(s):
    for n in range(100):
        for m in range(90):
	    if comb_rect(n,m) < s and comb_rect(n,m) > 1900000:
                l[comb_rect(n,m)] = (n,m)

if __name__ == "__main__":
    euler85(stop)
    nbym = l[max(l.keys())]
    ans = nbym[0] * nbym[1] 
    print ans
