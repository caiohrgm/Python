def remove_diagonal_secundaria(m,lin,col):

	for i in range(lin):
		for j in range(col-1,-1,-1):
			check = i + j
			if check == lin-1:
				m[i].pop(j)


m = [[1,2,3,4],
	 [5,6,7,8],
	 [9,10,11,12],
	 [13,14,15,16]]

remove_diagonal_secundaria(m,4,4)
print m
