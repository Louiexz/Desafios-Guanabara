matrix = [[],[],[]]
for c in range(0, 3):
	for indice in range(0, 3):
		matrix[c].append(float(input(f'\033[37m Digite um número para [{c}, {indice}]: ')))
for a in range(0, 3):
	print()
	for pos in range(0, 3):
		print(f'[{matrix[a][pos]:^8}]\033[m', end='')