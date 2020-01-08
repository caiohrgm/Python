lista = [1,2,3,4,5]

lista.append(None)
tam2 = len(lista)


for i in range(tam2-1,3,-1):
	lista[i],lista[i-1] = lista[i-1],lista[i]

print lista
