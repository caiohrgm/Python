#ex:l = [1,6,7,5,6,3,1,4,2,1,9,8,9,5,2,4,3]

tam = len(l)

for i in range(tam-1):
	minimo = i
	for j in range(i+1,tam):
		if l[j] < l[minimo]:
			minimo = j

	if l[i] != l[minimo]:
		l[i],l[minimo] = l[minimo],l[i]

print l