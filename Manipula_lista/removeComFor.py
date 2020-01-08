def remove(lista,num):
	count = 0
	for i in range(len(lista)-1,-1,-1):
		if lista[i] == num:
			lista.pop(i)
			count = count + 1

	return count




lista = [1,3,3,3]
x = remove(lista,3)
print x
print lista