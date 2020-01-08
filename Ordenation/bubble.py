def check_ordem(l):
	tam = len(l)
	flag = 0
	
	if tam % 2 == 0: 
		for i in range(0,tam,2):
			if l[i] < l[i+1]:
				continue
			else:
				flag = 1
	elif tam % 2 != 0:
		for i in range(0,tam-1,2):
			if l[i] < l[i+1]:
				continue
			else:
				flag = 1
		if flag == 0  and l[tam-1] > l[tam-2]:
			return flag
		else:
			flag = 1	
	return flag

def bubble(l):
	tam = len(l)

	for i in range(tam-1):

		for j in range(i,tam,2):
			if j == tam-1:
				break
			if l[j] > l[j+1]:
				l[j],l[j+1] = l[j+1],l[j]
		if check_ordem(l) == 0:
			break

l = [3,1,4,2,5]

bubble(l)
print l
