N = int(input())

seq = []
for i in range(N):
	seq.append(int(input()))

numero_magico = 0
for i in range(N):
	if i % 2 == 0 :
		numero_magico += seq[i]
	else:
		numero_magico -= seq[i]

print numero_magico