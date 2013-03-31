i = 1
for j in range(1,21):
    if i % j > 0:
        for x in range(1,21):
	    if(i * x) % j == 0:
	        i*=x
		break
print i
