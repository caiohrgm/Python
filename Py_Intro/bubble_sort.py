
l = range(100000,0,-1)

for i in range(len(l)-1,0,-1):
	for j in range(0,i):
		if l[j] > l[j+1]:
			aux = l[j]
			l[j] = l[j+1]
			l[j+1] = aux

print l