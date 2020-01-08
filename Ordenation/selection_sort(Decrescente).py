l = [3,2,1,4,6,7,10,2,3,5,6,4,7,10,2,1,4,5,8,3]
tam = len(l)

for i in range(tam-1):
	maximo = i
	for j in range(i+1,tam):
		if l[j]> l[maximo]:
			maximo = j

	if l[i] != l[maximo]: #se o maximo não for alterado, o elemento é pra ser igual e já estar no lugar
		l[i],l[maximo] = l[maximo],l[i]

print l