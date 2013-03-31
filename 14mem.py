def PE14(lim):
    d={}; a=0; b=0;
    def rec(n):
        if n==1: return 1
        if not d.has_key(n):
            d[n] = 1+rec(n/2) if n%2==0 else 1+rec(3*n+1)
        return d[n]
    for n in xrange(1,lim):
        if rec(n)>b: b=rec(n);a=n
    return a

print PE14(10**6)
