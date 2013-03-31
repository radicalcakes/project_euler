import operator
a = {}

for i in range(999999,500000,-1):
    s = i
    c = 0
    while s > 1:
        if s % 2 == 0:
            s /= 2
            c += 1
        else:
            s = (3 * s) + 1
            c += 1
    a[i] = c

print max(a.iteritems(), key=operator.itemgetter(1))[0]

