def desloca_elementos(lista,index):
	lista.append(None)
	tam = len(lista)
	for i in range(tam-1,index,-1):
		lista[i],lista[i-1] = lista[i-1],lista[i]

l = [1,2,3,4]

desloca_elementos(l,2,6)
print l