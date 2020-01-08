while True:
	tam = int(raw_input("Tamanho do numero: "))
	if tam == 0:
		print "SAIU!"
		break

	if tam >= 10:
		total = 0
		div = 1

		for i in range(tam):
			if i % 2 != 0:
				total = total - (1.0/div)
			elif i % 2 == 0:
				total = total + (1.0/div)
			div = div+2

		pi = 4*(total)
			
		print "pi = %.6f" % pi