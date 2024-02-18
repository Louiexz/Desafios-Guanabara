# Desafio 47
n2 = 0
n3 = 1
for n in range(0, 26):
	print(n2, end=' ')
	n2 += n3
	n2 += n3
print()
# jeito do Guanabara
for n in range(1, 51):
	if n % 2 == 0:
		print(n, end=' ')