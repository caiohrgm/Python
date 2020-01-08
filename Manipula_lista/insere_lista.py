def insert(lista,elm,pos):
	if len(lista) == 0:
		lista.append(elm)
		return None
	lista.append(None)
	tam = len(lista)
	for i in range(tam-1,pos,-1):
		if i == pos:
			break
		lista[i],lista[i-1] = lista[i-1],lista[i]

	lista[pos] = elm


lista = [1]
insert(lista,2,0)
print lista

