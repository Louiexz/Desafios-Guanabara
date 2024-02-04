# desafio 7
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
# Números menores ou maiores que zero
if n1 and n2 < 0:
	s = 0
elif n1 and n2 >= 0:
	s = (n1 + n2) / 2
# Cores
if s < 6:
	print(f'A média é: \033[0;31m{s}\033[m')
elif s == 6:
	print(f'A média é: \033[0;34m{s}\033[m')
else:
	print(f'A média é: \033[0;32m{s}\033[m')