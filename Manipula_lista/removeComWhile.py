def removeWhile(l,n):
	tam = len(l)
	i = 0
	while i < tam:
		if l[i] < n:
			l.pop(i)
			tam = tam - 1
			if i == 0:
				i = 0
			else:
				i =  i - 1
		else:
			i = i + 1


l = [1,5,6,3,10,4,7,2,1]
removeWhile(l,20)
print l
