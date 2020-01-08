import time
def menor_indice(l,index): # FUnção para achar o menor elemento a cada iteração do for "i";
	tam = len(l)
	menor = l[index]
	menorInd = index

	for i in range(index,tam):
		if l[i] < menor:
			menor = l[i]
			menorInd = i
	return menorInd

def selectionSort(lista):
	tam = len(lista)
	for i in range(tam):
		j = menor_indice(lista,i)
		lista[i],lista[j] = lista[j],lista[i]

l = [3,2,5,8,1,4]

selectionSort(l)
fim = time.time()
print l
