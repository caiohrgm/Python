def remove_pares(m,lin,col):
	for i in range(lin):
		for j in range(col-1,-1,-1):
			if m[i][j] % 2 == 0:
				m[i].pop(j)

m = [[1,2,3],
	 [4,5,6],
	 [7,8,9]]

remove_pares(m,3,3)
print m