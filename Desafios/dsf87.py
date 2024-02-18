matrix = [[],[],[]]
num = 0; soma = 0; somaTwo = 0
for c in range(0, 3):
	for indice in range(0, 3):
		matrix[c].append(float(input(f'\033[37m Digite um número para [{c}, {indice}]: ')))
for a in range(0, 3):
	print()
	for pos in range(0, 3):
		print(f'[{matrix[a][pos]:^8}]\033[m', end='')
while num != 3:
	for b, posTwo in enumerate(matrix[num]):
		if posTwo % 2 == 0:
			soma += posTwo
		if b == 2:
			somaTwo += posTwo
	num += 1
print(f'\n\n Soma dos números pares {soma}\n Soma da terceira coluna {somaTwo}\n O maior valor da segunda linha é {max(matrix[1])}\033[m')