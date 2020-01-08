# usando POP para alterar a lista original (remover elementos)

valores = [9.1, -1.1, 3.0, 2.1, -3.1]

for i in range(len(l) - 1, -1, -1): # por isso começa do final e vai até -1 (lista vazia), porque pode-se tirar todos os elementos da lista
    if valores[i] < 0:
        valores.pop(i) # ao remover o elemento, ele vai afast os outros da esquerda para direita.

# verificando se o estado da lista é o esperado
assert valores == [9.1, 3.0, 2.1]