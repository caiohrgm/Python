import time
def bubbleSort(lista): # Joga o maior para o final, comparando dois a dois e repetindo;
	tam = len(lista)

	for i in range(tam):
		for j in range(tam-1):
			if l[j] > l[j+1]:
				l[j],l[j+1] = l[j+1],l[j]

l = [3,2,5,8,1,4]

bubbleSort(l)
print l
