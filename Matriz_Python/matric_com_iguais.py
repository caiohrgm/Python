def matriz_com_iguais(matriz,lins,cols,k):
	novaMatriz = []

	for i in range(lins):
		nova = []
		novaMatriz.append(nova)

	#preenche:

	for i in range(lins):
		for j in range(cols):
			novaMatriz[i].append(None)
	
	for i in range(lins):
		for j in range(cols):
			if matriz[i][j] == k:
				novaMatriz[i][j] = k

	return novaMatriz

linhas = 3
colunas = 3
matriz = [[1,2,3],
		  [2,4,6],
		  [3,4,2]]
print matriz
print ""
print matriz_com_iguais(matriz,linhas,colunas,2)