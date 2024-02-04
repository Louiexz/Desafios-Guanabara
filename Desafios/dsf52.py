# Desafio 52
s = 0
n = int(input(' Digite um número: '))
print('\n\033[37m Números verdes = divisíveis\n Números vermelhos = não divisíveis\033[m')
print()
for c in range(1, n+1):
	if n % c == 0:
		print('\033[32m', end=' ')
		s += 1
	else:
		print('\033[31m', end=' ')
	print(f'{c}', end=' ')
if s == 2:
	print('\n\n É um número primo\033[m')
else:
	print('\n\n Não é um número primo\033[m')